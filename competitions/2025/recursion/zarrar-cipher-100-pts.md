# Zarrar Cipher (100 pts)

> **by Pablu**
>
> Untuk berkomunikasi secara rahasia dengan sahabatnya, Oejang. Oelyl menciptakan sebuah cipher baru yakni zarrar cipher. Bisakah anda mengungkap pesan rahasia yang dikirim
>
> nc 103.87.66.171 13339

Pada soal ini, kita diberikan `message.txt` berisikan pesan yang terenkripsi.

```
zaaaaarraaaarrrrraaaarrraaaaarrrrraaaaarraaaaarrraaaarrrrrrrrraaaarrrrrrrrrrrrrrraaaarrrrrrrrrrrrrraaaaaaarrrrrrrrrrraaaraaaaaarrrrrrrrrrrrrraaaaaarrrrrraaa_aaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrrrraaa_aaaaaarrrrrrraaaaaarrrrrrrrraaaaaarrrrrrrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaaarraaaaaaraaaaaarrrrrrrrrrrrrraaaaaarrrrrrrrrrraaaaaarrrrraaaaaarrrraaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrraaaaaaraaaaaarrrrrrrrrrrrraaa_aaarrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrrrrraaaaaaraaaaaarrrrrrrrrrrraaarrrraaaaaarrrrrrrrrrrrraaraaraaraaaaaaarrrrrrrrrraaarrrraaaaaaarraaaaaaarraaarrrraaaaaaarraaaaarrrrrrrrrrrrrrraaaaaarrraaaraaaaaaa_aaaaaarrrrrrrraaarrraaaaaaarraaaaarrrrrrrrrrrrrrraaaraaaaaaarrrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaaarraaaaaarrrrraaaaaaraaaaaarrrrrrrrrrrraaaaaaarrrrrrrrrrrrr
```

Karena kita diberikan sebuah oracle yang memungkinkan kita mengenkripsi pesan sesuka kita, maka saya melakukan beberapa percobaan.

| Input | Output             | Kode ASCII |
| ----- | ------------------ | ---------- |
| !     | zaar               | 33         |
| “     | zaarr              | 34         |
| /     | zaarrrrrrrrrrrrrrr | 47         |
| 0     | zaaa\_             | 48         |
| 1     | zaaar              | 49         |
| !!    | zaaraar            | 33 + 33    |

Dari percobaan di atas, saya tarik polanya dan berikut yang dapat saya simpulkan tentang aturan pada cipher ini.

* `z` selalu ada di awal ciphertext, tapi sebenarnya tidak punya fungsi apa-apa
* `a` bernilai 16
* `r` bernilai 1
* Untuk mengembalikan dari ciphertext ke karakter semula, hitung `(jumlah a)*16 + (jumlah r)*1`

Bagian yang agak tricky adalah bagaimana memisahkan ciphertext yang kita miliki menjadi bagian-bagian yang sesuai per karakter. Di sini, saya menggunakan regex. Ketika bagian-bagiannya sudah didapatkan, saya menghitung masing-masing jumlah karakter a dan r lalu melakukan perhitungan.

#### solve.py

```python
import re
from collections import Counter

# Remove the leading 'z'
ciphertext = "aaaaarraaaarrrrraaaarrraaaaarrrrraaaaarraaaaarrraaaarrrrrrrrraaaarrrrrrrrrrrrrrraaaarrrrrrrrrrrrrraaaaaaarrrrrrrrrrraaaraaaaaarrrrrrrrrrrrrraaaaaarrrrrraaa_aaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrrrraaa_aaaaaarrrrrrraaaaaarrrrrrrrraaaaaarrrrrrrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaaarraaaaaaraaaaaarrrrrrrrrrrrrraaaaaarrrrrrrrrrraaaaaarrrrraaaaaarrrraaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrraaaaaaraaaaaarrrrrrrrrrrrraaa_aaarrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaarrrrrrrrrrrrraaaaaaraaaaaarrrrrrrrrrrraaarrrraaaaaarrrrrrrrrrrrraaraaraaraaaaaaarrrrrrrrrraaarrrraaaaaaarraaaaaaarraaarrrraaaaaaarraaaaarrrrrrrrrrrrrrraaaaaarrraaaraaaaaaa_aaaaaarrrrrrrraaarrraaaaaaarraaaaarrrrrrrrrrrrrrraaaraaaaaaarrrrrrrrrraaaaarrrrrrrrrrrrrrraaaaaaarraaaaaarrrrraaaaaaraaaaaarrrrrrrrrrrraaaaaaarrrrrrrrrrrrr"

# Use re.split with two delimiters:
# 1. "_" splits the string wherever an underscore is found.
# 2. (?<=r)(?=a) is a zero‐width assertion that splits whenever an "r" is followed by an "a".
parts = re.split(r'(?<=r)(?=a)|_', ciphertext)

print(parts)
print(len(parts))

# Decode each part to a character
res = []
for part in parts:
	total = 0
	char_count = Counter(part)
	total += 16*char_count['a']
	total += 1*char_count['r']
	res.append(total)

print(len(res))
print(res)

# Decode decimal to text
FLAG = ""
for n in res:
	FLAG += chr(n)

print(FLAG)
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSJeKKxOfDdTK_zS2UrfZQPYqbf2B_iqkOIKzf9is8_MZJPMY8hN2bPB-hhfOE9n5YZ3urOeHBP_7HLKz8Taf-mMLIkGG3LR_TvEljzagBykHtXMO4eB9AY-KpScdhguGR3Tgz?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Flag: `RECURSION{1nf0_l0gin_ranked_jam09_mal4m!!!z4rr4r_c1ph3r_1z_real}`
