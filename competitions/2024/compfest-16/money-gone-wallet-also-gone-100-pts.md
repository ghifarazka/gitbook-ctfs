# money gone, wallet also gone (100 pts)

> help me find my wallet please :c
>
> Author: tipsen

Diberikan file `chall.py` dan `encrypted_memory.txt`. Isi file `chall.py` adalah sebagai berikut.

```python
import hashlib
import random

methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224']

def random_encrypt(x) :
    method = random.choice(methods)
    hash_obj = hashlib.new(method)
    hash_obj.update(x.encode())
    return hash_obj.hexdigest()

def main() :
    message = open("tipsen_memory.txt", "r").read()
    enc = []

    for char in message :
        x = (ord(char) + 20) % 130
        x = hashlib.sha512(str(x).encode()).hexdigest()
        x = random_encrypt(x)
        enc.append(x)

    with open('encrypted_memory.txt', 'w') as f :
        f.write(str(enc))

if __name__ == "__main__" :
    main()
```

Pada kode di atas, intinya adalah setiap karakter pesan pada file asli (`tipsen_memory.txt`) di-hash dengan salah satu algoritma hash random.

Maka dari itu, kita bisa pertama-tama membuat sebuah database berisi semua kemungkinan hash dari semua karakter printable yang ada di ascii. Bentuk database tersebut adalah sebuah dictionary yang terdiri dari 1 karakter sebagai key, dan valuenya adalah sebuah list berisi hash dari karakter tersebut dalam berbagai algoritma yang ada di list “methods”. Kira-kira akan seperti ini:

```
{ ‘0’: [hash1, hash2, hash3, ...],
  ‘1’: [hash1, hash2, hash3, ...],
  ‘2’: [hash1, hash2, hash3, ...],
  ‘3’: [hash1, hash2, hash3, ...],
  ...
  ‘\n’: [hash1, hash2, hash3, ...] }
```

Setelah itu, kita akan baca masing-masing hash yang ada di `encrypted_memory.txt`. Untuk setiap hash, kita akan cari ke dalam list-list yang ada di dictionary. Jika ketemu, kita akan mencatat key (char aslinya) dan menambahkannya ke sebuah string baru. String tersebut kemudian kita print. Berikut adalah kode lengkapnya.

```python
from string import printable
import hashlib
import random
import ast

methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224'][::-1]

# build a hash database for all printable chars

hashed = {key: [] for key in printable}

def encrypt(x, method) :
    hash_obj = hashlib.new(method)
    hash_obj.update(x.encode())
    return hash_obj.hexdigest()

for char in printable :
    for method in methods:
    	print(f"encrypting {char} with {method}...")
    	x = (ord(char) + 20) % 130
    	x = hashlib.sha512(str(x).encode()).hexdigest()
    	x = encrypt(x, method)
    	hashed[char].append(x)

print(hashed)

# read encrypted message

enc = open('encrypted_memory.txt', 'r').read()
enc_list = ast.literal_eval(enc)

msg = ""

for c in enc_list:
	for key, val in hashed.items():
		if c in val:
			msg += key

print(msg)
```

Berikut adalah hasilnya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd_pOFM4teci0wSkSXDthhCM-qIuly_VUIx6AB4Mr79y7iJvn9zbQUuuv0wu2K8ihAVUWv6nMrk7UsEm1qEkv_OiwfUeqRv0EvymRmIgScyub7dWq4r3qBNZ8rUgF5wvjpSD8CWpEcdA8ESqgSnkl9jTrRU?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

```python
# tipsen and PapaChicken met at the library at 10 PM to delve into the intricacies of CTF challenges over cups of steaming coffee. As they wrapped up their discussion, ready to head home, PapaChicken realized his wallet was nowhere to be found. Panic turned into curiosity as they examined the scene like seasoned cryptographers. The missing wallet wasn't just an inconvenience but a cryptic puzzle waiting to be decrypted, challenging them to apply their CTF skills to unravel the mystery of its disappearance in the late-night library labyrinth. Solve this to help PapaChicken find his wallet :c

from Crypto.Util.number import getPrime, bytes_to_long

while True:
    try:
        p = getPrime(512)
        q = getPrime(512)
        n = []

        for i in range(16):
            q = p
            p = getPrime(512)
            n.append(p * q)

        m = bytes_to_long(b'COMPFEST16{SECRET}')
        e = 65537
        c = pow(m, e, n[0])

        for i in range(1, 16):
            assert c < n[i], i
            c = pow(c, e, n[i])

        with open('chall2_mem.txt', 'w') as f:
            f.write(f"n = {n}\n")
            f.write(f"e = {e}\n")
            f.write(f"c = {c}\n")

        break
    
    except AssertionError as e:
        print(f"Assertion error: {e}. Retrying...")

#n = [8057419996346381409..., ...36754743087981]
#e = 65537
#c = 1310681505162667824975...
```

Ternyata ada chall lanjutan :D. Di sini, jika kita lihat pada kodenya, kita akan menyadari bahwa ada flag di-encrypt sebanyak 16 kali menggunakan 16 `n` yang berbeda. Masalahnya, cara pembangkitan `n` tersebut tidak aman, karena bilangan prima yang digunakan untuk suatu nilai `n`, digunakan lagi pada `n` setelahnya. Jadi, kita tinggal ambil GCD dari dua nilai `n` terakhir, dan kita dapatkan bilangan prima `q`.

Nilai `q` ini bisa kita gunakan untuk membagi nilai `n` sebelumnya dan kita akan mendapatkan `p`. Lalu nilai `p` ini kita gunakan lagi untuk membagi nilai `n` sebelumnya, begitu seterusnya. Pada akhirnya kita bisa mendapatkan private key `d` untuk semua round enkripsi dari flag. Berikut adalah solver lengkapnya.

```python
from Crypto.Util.number import *

n = [8057419996346..., ...754743087981]
e = 65537
c = 13106815051626678249752...

pq = []

n = n[::-1]	# reverse the list

for i in range(1,16):
	if i == 1:
		q = GCD(n[i-1], n[i])
		p = n[i]//q
		pq.append((n[i-1]//q, q))
		pq.append((q,p))
	else:
		q = p
		p = n[i]//q
		pq.append((q,p))

ds = []
for i in range(16):
	phi = (pq[i][0]-1) * (pq[i][1]-1)
	d = pow(e,-1,phi)
	ds.append(d)

for i in range(16):
	c = pow(c,ds[i],n[i])

print(long_to_bytes(c))
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXewBiPcFH3kS0KnGdvfJKfHtqShCCTmxX77i3gZdG06lT1_Xk4H4E3PCNKPLIXtMeXJcda8eLFgyYDJF7LcTHp4THcIybVND92aNur2xVsh6Cg77jgmM5hGw7Jm1Lof64uKQQ21d_QlenZDqJfyYZBwGl5W?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Flag: `COMPFEST16{d0nt_F0rg3t_ur_w4ll3T_4g4in_0r_3lse_ur_m0n3y_1s_G0ne_47dcdc753c}`
