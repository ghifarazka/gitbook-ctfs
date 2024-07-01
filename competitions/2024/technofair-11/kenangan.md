# Kenangan

### Description

> Yoriichi mengencrypt sebuah file gambarnya tetapi dia lupa cara membukanya. Bisakah kamu membantu Yoriichi untuk membuka filenya?
>
> Author : macaril

Diberikan `chall.py` dan hasil enkripsinya yaitu `flag.enc`. Berikut adalah kode dari `chall.py`.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

with open("flag.png", "rb") as f:
    flag = f.read()

key = os.urandom(1) * 16 
iv = os.urandom(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

ciphertext = cipher.encrypt(pad(flag, AES.block_size))

with open("flag.enc", "wb") as f:
    f.write(iv + ciphertext)
```

Sesuai deskripsi soal, ini adalah gambar yang dienkripsi dengan AES CBC biasa, dengan key-nya adalah 1 byte random di antara 0-255 yang diulang sebanyak 16 kali. Untuk mendapatkan 1 byte tersebut, saya melakukan bruteforcing dengan kode berikut.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

file = open("flag.enc", "rb").read()
iv = file[:16]
ciphertext = file[16:]

for i in range(256):
	key = int.to_bytes(i,1,'big') * 16
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext)
	if b"PNG" in plaintext[:4]:
		print("FOUND!!!")
		print("key byte:", i)
		with open("flag.png", "wb") as f:
			f.write(plaintext)
		break
```

Berikut adalah hasilnya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeyV8aM-2Pm6McO-g4eQZ_kuTBJx_LZKBPM5aUlk_EY-6sLT99iw8fih23MP8C2QY7RcRkgmKyK6EbqtRg19mGd-6SnFgXqCu3BwzxvDOWW6dT8gDPNJE5q-xAEUEaqjrQmARbhVuq0i6lJbiXT9tBDVJE?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{Cek_Khodamnya_kakak}`
