# Xorban

### Description

> Basic XOR
>
> format flag : TechnoFair11{..}
>
> Author: macaril

Diberikan `chall.py` dan `output.txt`.

```python
import random
from secret import flag

key = [random.randint(1, 256) for _ in range(len(flag))]

xorban = []
enc = []
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    xorban.append(k)
    enc.append(flag[i] ^ v)

with open("output.txt", "w") as f:
    f.write(f"{xorban=}\n")
    f.write(f"{enc=}\n")
```

```
xorban=[1, 243, 128, 75, 251, 28, 249, 9, 231, 152, 154, 2, 237, 223, 175, 17, 5, 150, 118, 14, 173, 151, 242, 240, 176, 10, 209, 29, 236, 208, 222, 177, 183, 91, 162, 8, 12, 103, 221, 30, 119, 184]
enc=[105, 151, 16, 163, 222, 136, 163, 145, 135, 13, 51, 169, 148, 6, 30, 199, 97, 249, 137, 22, 252, 105, 81, 107, 36, 229, 175, 164, 192, 79, 81, 6, 117, 179, 186, 198, 48, 24, 201, 170, 10, 178]
```

Pada soal ini, basicnya adalah xor. Kita hanya perlu memahami hubungan antara xorban dengan plaintext. Setelah melakukan eksplorasi, saya menemukan fakta berikut (angka di bawah tidak ada hubungannya dengan soal, karena saya mencoba menjalankan chall.py sendiri).

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeBWzuk3UAbmyk3OBaHKF_PQVgZ7RvJ3evrH89MLJFCgXRyXE4bpPnZSE5WOY4f0z5tTnX21nxMll8PCywWJwq_ovw2u_dk8WqfuacMo_GcKShWKHM6tEoQb-hs-ANMHxnwmsd2DhBGKLv6EFMJ4LL1N_eX?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Untuk elemen kedua dan seterusnya dari xorban, berlaku bahwa key xor yang digunakan pada index i adalah: `xorban[i] ^ xorban [i-1]`. Langsung saja, berikut adalah kode solver yang saya gunakan.

```python
xorban=[1, 243, 128, 75, 251, 28, 249, 9, 231, 152, 154, 2, 237, 223, 175, 17, 5, 150, 118, 14, 173, 151, 242, 240, 176, 10, 209, 29, 236, 208, 222, 177, 183, 91, 162, 8, 12, 103, 221, 30, 119, 184]
enc=[105, 151, 16, 163, 222, 136, 163, 145, 135, 13, 51, 169, 148, 6, 30, 199, 97, 249, 137, 22, 252, 105, 81, 107, 36, 229, 175, 164, 192, 79, 81, 6, 117, 179, 186, 198, 48, 24, 201, 170, 10, 178]

res = ""
for i, c in enumerate(enc):
	if i == 0:
		continue
	k = xorban[i] ^ xorban[i-1]
	res += chr(c ^ k)

print(res)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeBqib7FqbEcnA_xZwb4gLvpBjWAmtpSxezrgngs-RDAE9PyrNNJPFG2skt2ylL34toD4epN5SZ0D_pzHvfK5svgm04IYzSjH-6q426dAQzfDUpxMqPh_412B3e7s0XYTvHlgtIiUI7Uep6Whsmn1LOGkqg?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{4nyujin_S4id_th1s_is_Cl4ssic}`
