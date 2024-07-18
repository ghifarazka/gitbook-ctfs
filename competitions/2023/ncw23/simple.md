# Simple

### Deskripsi

> Cuma maen AES doang. Simple Kan?
>
> nc 103.145.226.206 1945
>
> Mirror: nc 103.145.226.209 1945
>
> Author: Lawson Schwantz

Kita diberikan source code dari soal yakni sebagai berikut.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import *
import string
import random
import os
from Crypto.Util.number import *
from secrets import FLAG, enc
 
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
 
def encrypt(msg,key,iv):
###############################################################################
#                                                                             #
#                    Haduh kena prank opo iki rek jadi ilang                  #
#                   Seinget gw ini AES jg deh cm entah apa ini                #
#                              Gudlak All!! :)                                #
#                                                                             #
###############################################################################
    return enc.hex()
 
key = os.urandom(16)
iv1 = os.urandom(16)
iv2 = os.urandom(16)
plainkey = os.urandom(16)
 
enckey = encrypt(plainkey + os.urandom(16), key, iv1)
 
code = ("Very simple, " + generate_random_string(random.randint(50,60))).encode()
 
cipher = AES.new(plainkey + (os.urandom(2)*8),AES.MODE_CBC, iv2)
 
enccode = cipher.encrypt(pad(code,16))
 
print(f'enckey = {enckey}')
print(f'enccode = {enccode}')
print(f'iv2 = {iv2}')
 
while True:
    print("""      ========================================
        1. Tes Enkripsi
        2. Tebak kode
        3. Exit
        ============================================""")
 
    choose = input(">> ")
    if choose == "1":
        plaintext = input("Masukan pesan: ")
        try:
            plaintext = bytes.fromhex(plaintext)
            ciphertext = encrypt(plaintext, key, iv1)
            print(f'Ciphertext = {ciphertext}')
        except:
            print("woila...")
 
    elif choose == "2":
        cobaan = input("Masukkan kode: ").encode()
        if cobaan == code:
            print(f'dahlah, {FLAG}')
            exit(1)
        else:
            print("salah :(")
            exit(0)
 
    elif choose == "3":
        print("Bye!")
        exit(1)
 
    else:
        print("woi!")
        exit(0)
```

Intinya begini:

* kita dimintai `code`, tapi hanya dikasih `enccode` (code yang dienkripsi)
* enkripsi `code` menggunakan kunci `plainkey` + random byte (tapi cuma 2 byte jadi bisa di-bruteforce)
* `plainkey` tidak diberikan, tapi kita diberikan `enckey` yang 16 byte pertamanya merupakan hasil enkripsi dari plainkey
* algoritma enkripsi yang sama yang meng-encrypt `plainkey` diberikan, dan bebas untuk kita gunakan

Pertama-tama, saya berusaha untuk mendapatkan `plainkey`. Saya mencoba-coba algoritma “Tes Enkripsi” yang diberikan. Rupanya, penambahan byte di akhir plaintext tidak mengubah hasil enkripsi di byte awalnya. Selain itu, hasil enkripsi masing-masing byte dapat berbeda tergantung posisinya di mana. Misalnya:

| plain  | aa | bb | aabb | aabb1212 |
| ------ | -- | -- | ---- | -------- |
| cipher | 00 | 11 | 0033 | 003378fe |

Maka dari itu, saya mencoba untuk melakukan brute-force di mana untuk setiap byte pada `enckey`, saya berusaha mencari sebuah byte yang apabila diencrypt, hasilnya adalah byte pada `enckey` tersebut.

```python
# brute the plainkey
inp = b''
target = b''
for i in range(0,32,2):
	targetbyte = enckey[i:i+2]
	target += targetbyte

	for b in range(256):
		byte = '{:02x}'.format(b).encode()

		r.recvuntil(b'>> ')
		r.sendline(b'1')
		r.recvuntil(b': ')
		r.sendline(inp+byte)
		r.recvuntil(b'= ')
		ct = r.recvline()[:-1]

		if ct == target:
			# print(inp+byte, "translates to", ct)
			print("FOUND!", inp+byte)
			inp += byte
			break

plainkey = bytes.fromhex(inp.decode())
```

Nah kalau plainkeynya sudah ketemu, sekarang kita perlu menghitung nilai berikut.

```python
cipher = AES.new(plainkey + (os.urandom(2)*8), AES.MODE_CBC, iv2)
```

Di sini yang belum kita ketahui adalah hasil dari `os.urandom(2)` nya. Karena hanya 2 byte, berarti masih bisa kita brute force. Kalau sudah ketemu kode aslinya, kita bisa submit ke server dan mendapatkan flag. Langsung saja berikut ini saya berikan full kode solvernya.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import *
from pwn import *

r = remote(b"103.145.226.206", 1945)

# get enckey
r.recvuntil(b'= ')
enckey = r.recvline()[:-1]
print(enckey)

# get enccode
r.recvuntil(b'= ')
enccode = r.recvline()[2:-2].decode().encode('latin-1').decode('unicode-escape').encode('latin-1')
print(enccode)
print(len(enccode))

# get iv2
r.recvuntil(b'= ')
iv2 = r.recvline()[2:-2].decode().encode('latin-1').decode('unicode-escape').encode('latin-1')
print(iv2)
print(len(iv2))

# brute the plainkey
inp = b''
target = b''
for i in range(0,32,2):
	targetbyte = enckey[i:i+2]
	target += targetbyte

	for b in range(256):
		byte = '{:02x}'.format(b).encode()

		r.recvuntil(b'>> ')
		r.sendline(b'1')
		r.recvuntil(b': ')
		r.sendline(inp+byte)
		r.recvuntil(b'= ')
		ct = r.recvline()[:-1]

		if ct == target:
			# print(inp+byte, "translates to", ct)
			print("FOUND!", inp+byte)
			inp += byte
			break

plainkey = bytes.fromhex(inp.decode())

# brute the cipher
breakout = False
for i in range(256):
	for j in range(256):
		trying = i.to_bytes(1,'little') + j.to_bytes(1,'little')

		cipher = AES.new(plainkey + (trying*8), AES.MODE_CBC, iv2)
		plaincode = cipher.decrypt(enccode)
		print(plaincode)

		if b"Very simple" in plaincode:
			plaincode = unpad(plaincode,16)
			print(plaincode)
			breakout = True
			break
	if breakout:
		break

r.recvuntil(b'>> ')
r.sendline(b'2')
r.recvuntil(b': ')
r.sendline(plaincode)
print(r.recvline())
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjMDpyxQPnCAWkOXsZf0QGSX3-_VPbGfHyQ8LaOx-Wq8W37--JB56DFFf3GBaoehdUUVcYAWXAt7rGSTyX5qNqz7H8F9fu8D60_LX3IhelPhvG0MqRQm8Zk0zh5zUECYmw8uap8jYN9z0yc4ZHj1KoD-g?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Flag: `NCW23{kenapa_bocor_lagi_yak_keynya?_yang_penting_soalnya_simple_dah}`
