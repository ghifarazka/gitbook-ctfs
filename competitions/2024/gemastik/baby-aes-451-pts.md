# Baby AES (451 pts)

> I recently learned about AES encryption, and now I'm offering an AES encryption service to anyone. Please provide a message that you would like encrypted.
>
> Author: Chovid99
>
> nc ctf.gemastik.id 10004

Pada soal ini, kita diberikan source code serta sebuah service oracle.

```python
#!/usr/local/bin/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt(key, pt):
	cipher = AES.new(key, AES.MODE_CBC)
	ct = cipher.decrypt(pad(pt, 16))
	return cipher.iv + ct

print(f'Welcome to the AES CBC Machine')
print(f'Give me some input, and I will encrypt it for you')

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
assert len(flag) == 67

key = os.urandom(16)
out = encrypt(key, flag)
print(f'This is the example of the encryption result: {out.hex()}')
while True:
    msg = bytes.fromhex(input('Give me your message: '))
    print(f'Encryption result: {encrypt(key, msg).hex()}')
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf1aY-xwSDaaNIOjc42chkVk3TrUrcyBlGEfDpVuoKZjyEr_f58ZLCPnk8JwWKajEZP0f4OW5RLpf8NAr8HJvYXqYCTypBLguyxbB9QDAQobGeeqloRcRFbXURwenduT5zRVxh9b9Dj_-s5UH8iOAsnsjQ?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Ada beberapa hal yang bisa dicatat sejauh ini:&#x20;

* Mode AES yang digunakan adalah CBC.&#x20;
* Pada fungsi “`encrypt(key, pt)`”, method yang digunakan adalah decrypt(), bukan encrypt().&#x20;
* Panjang flag persis 67, artinya ada 4 block + block kelima yang berisi 2 karakter tertentu, karakter ‘}’, dan sisanya padding.&#x20;
* Pada oracle, key yang sama dengan key untuk meng-encrypt flag digunakan berulang kali.

Karena menggunakan fungsi decrypt untuk meng-encrypt, maka alurnya menjadi seperti berikut.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfkL8aI_R5UnpV55YR5XzHqlBYc2ieOlk2dsXTguJNGO1B_GTjbWpSihgwPjgzQ-hte2S5J678jfvDqe637QPEQE_SIKoSnRJqoF6OJFM4OJjVZQABH-4ggnfon9rXCIYLU__0EmW-1hEE50N8epBlC86qf?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Jika kita bisa mengetahui nilai `dk5`, kita akan mendapatkan nilai `pt4`. Jika kita tahu nilai `pt4`, kita bisa menghitung `dk4` dan mendapatkan `pt3`, begitu seterusnya.

Kita bisa mendapatkan `dk5` dengan memanfaatkan oracle yang diberikan. Kita akan mencoba semua kemungkinan kombinasi 2 karakter dari flag aslinya lalu memasukkannya ke oracle. Katakanlah hasilnya `et5`, nah kita bisa mendapatkan `dk5` dengan melakukan xor antara `et5` dengan `iv` yang digunakan oracle pada saat itu. Cara kita memastikan bahwa kombinasinya benar adalah dengan mencoba decode hasil `pt4`-nya dan memastikan bahwa string `pt4` tersebut terdiri dari 100% karakter printable.

Berikut adalah kode untuk mendapatkan dua karakter flag tersebut.

```python
from pwn import *
import string
from Crypto.Util.number import *

def hex_xor(hex_a, hex_b):
	a = bytes.fromhex(hex_a)
	b = bytes.fromhex(hex_b)
	result = ""
	for a,b in zip(a,b):
		result += format(a^b, "02x")
	return result

r = remote('ctf.gemastik.id', 10004)

# dapatkan encrypted flag
r.recvuntil(b'result: ')
ct = r.readline().decode()
iv = ct[:32]
ct1 = ct[32:64]
ct2 = ct[64:96]
ct3 = ct[96:128]
ct4 = ct[128:160]
ct5 = ct[160:-1]	# -1 untuk menghilangkan \n

# dapatkan pt5
chars = string.printable 	# list char yang dicoba
for a in chars:
	break_status = False
	for b in chars:
		try_string = (a + b + '}').encode()
		r.recvuntil(b'message: ')
		r.sendline(try_string.hex())
		r.recvuntil(b'result: ')
		result = r.recvline()
		iv = result[:32].decode()
		et5 = result[-33:-1].decode()
		print(iv)
		dk5 = hex_xor(iv, et5)

		# xor dk5 dengan ct5
		pt4 = hex_xor(dk5, ct5)
		print(try_string)
		print(pt4)
		try:	
			if bytes.fromhex(pt4).decode().isprintable():
				print("YESSS!!")
				print(try_string)
				print(bytes.fromhex(pt4).decode())
				break_status = True   # untuk nge-skip double for loop
				break
			else:
				assert 1 == 0 # jika pt4 tidak printable, maka ke ’except’
		except:
			continue
	if break_status:
		break
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMUYR1-tuSt6ycVaUYV1krJGxXnUciPNH03CjDF9JoQGzYF_D8mUjRGKmW5Xoj8mLREWNuf88AXnOaDoNrkAOiEdEu_3qTEqEo5xvWs2Pdi0woVgS-64WskCbI3JTEtRuNKu26rHSvbMfcK1wrVwd4D_ni?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Karena `pt5` dan `pt4` sudah didapatkan, berikutnya tinggal melanjutkan alur penyelesaian yang sudah saya sebutkan sebelumnya. Berikut adalah kode solver full-nya.

```python
from pwn import *
import string
from Crypto.Util.number import *

def hex_xor(hex_a, hex_b):
	a = bytes.fromhex(hex_a)
	b = bytes.fromhex(hex_b)
	result = ""
	for a,b in zip(a,b):
		result += format(a^b, "02x")
	return result

r = remote('ctf.gemastik.id', 10004)

# dapatkan encrypted flag
r.recvuntil(b'result: ')
ct = r.readline().decode()
iv = ct[:32]
ct1 = ct[32:64]
ct2 = ct[64:96]
ct3 = ct[96:128]
ct4 = ct[128:160]
ct5 = ct[160:-1]	# -1 untuk menghilangkan \n


# pt5 telah didapatkan sebelumnya
pt = 'Zz}'
ct = [ct5, ct4, ct3, ct2, ct1]

flag = pt

# dapatkan pt4, pt3, pt2, pt1
for i in range(4):
	r.recvuntil(b'message: ')
	r.sendline(pt.encode().hex().encode())
	r.recvuntil(b'result: ')
	result = r.recvline()
	iv = result[:32].decode()
	et = result[32:-1].decode() # xor dengan iv
	dk = hex_xor(iv, et)
	pt = bytes.fromhex(hex_xor(dk, ct[i])).decode()
	flag = pt + flag

print(flag)

```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXev045BPTD4ygjxtlE4cWm0PXJu612Js239a9j-7IoWkW7HBZE70Plp1z2_jbyL638bX5bhbGoTR0c6WnqZfwU5uJBYhsT9F7aDlIZBgSSc9-SZWc0AwsBSyJvLioud8C2g6hT_I3_tzL7S2kgER8hWrxkm?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Flag: `gemastik{i_am_so_sorry_coz_it_should_be_encrypt_not_decrypt_bZzZ Zz}`
