# wangsaf (320 pts)

### Deskripsi

> biarkan dia memasak
>
> nc 103.145.226.206 1965 Mirror: nc 103.145.226.209 1965
>
> Author: kisanakkkkk

Pada soal ini kita diberikan file yang cukup banyak, tapi intinya, ada source code dari sisi client, server, dan attacker. Inti dari soal ini sendiri adalah `Man in the Middle` attack terhadap `Diffie-Hellman`.

Pada service yang diberikan, ada percakapan antara client dan server yang bisa kita _tamper_ sebelum dikirim ke tujuannya. Untuk keseluruhan prosesnya, kira-kira urutannya sebagai berikut.

* client dan server meng-establish connection dengan sama2 mengirimkan “hello!”
* client melakukan key generation
* client mengirimkan parameter DH
* server meng-ACC parameter DH
* client mengirimkan public key
* server meng-ACC public key
* server mengirimkan public key
* client meng-ACC public key
* client dan server bertukar pesan yang terenkripsi

Kita perlu melakukan tampering pada parameter DH dan public key client supaya shared secret yang dimiliki server adalah yang di-share dengan kita. Di samping itu, kita perlu melakukan tampering pada public key server supaya mendapat ACC dari client (jadi, parameter yang datang dari client asli juga harus disimpan). Untuk meng-generate parameter2 tersebut, kita bisa menggunakan kode yang ada pada `server.py` dan `client.py`.

Langsung saja ke kode solvernya. Maaf berantakan, bikinnya buru-buru soalnya :)

```python
import socket, threading
from Crypto.Util.number import *
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, dh
from cryptography.hazmat.primitives import serialization, hashes, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import time
import os
import random
from server_messages import server_messages
from client_messages import client_messages
from pwn import *


# generate key
parameters = dh.generate_parameters(generator=2, key_size=512)
private_key = parameters.generate_private_key()
public_key = private_key.public_key()

# sendparam()
serialized_parameters = parameters.parameter_bytes(serialization.Encoding.PEM, serialization.ParameterFormat.PKCS3)
sent_param = b"PARM||" + serialized_parameters.hex().encode()
print(sent_param)

# sendpubkey
serialized_public_key = public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
sent_pkey = b"PUBK||" + serialized_public_key.hex().encode()
print(sent_pkey)

# "SERVER" --> maksudnya di sini kita berpura-pura sebagai server
# terima parameter asli dari client
def a(SERVER_responseparam):
	global SERVER_parameters
	global SERVER_private_key
	global SERVER_public_key
	SERVER_parameters = serialization.load_pem_parameters(bytes.fromhex(SERVER_responseparam[6:].decode()))
	# generate key
	SERVER_private_key = SERVER_parameters.generate_private_key()
	SERVER_public_key = SERVER_private_key.public_key()

# terima pubkey asli dari client
# kita dapat pubkey yang akan di-ACC
def b(SERVER_responsepubkey):
	global SERVER_holder_public_key
	global SERVER_shared_key
	global SERVER_serialized_public_key
	SERVER_holder_public_key = serialization.load_pem_public_key(
		bytes.fromhex(SERVER_responsepubkey[6:].decode()),
		backend=default_backend(),
	)
	SERVER_shared_key = SERVER_private_key.exchange(SERVER_holder_public_key)
	# send pub key
	SERVER_serialized_public_key = SERVER_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
	SERVER_sent_pkey = b"PUBK||" + SERVER_serialized_public_key.hex().encode()
	return SERVER_sent_pkey

# terima pubkey dari server
# ini akan menghitung shared secret yang...
# ...akan digunakan utk encrypt decrypt
def c(responsepkey):
	global holder_public_key
	global backend
	global shared_key
	global derived_key
	holder_public_key = serialization.load_pem_public_key(
		bytes.fromhex(responsepkey[6:].decode()),
		backend=default_backend(),
	)
	shared_key = private_key.exchange(holder_public_key)
	# keyderiv
	derived_key = HKDF(
		algorithm=hashes.SHA256(),
		length=32,
		salt=None,
		info=b'handshake data',
	).derive(shared_key)

# encrypt data
def encrypt(message):
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
	encryptor = cipher.encryptor()
	padder = padding.PKCS7(algorithms.AES.block_size).padder()
	padded_message = padder.update(message.encode()) + padder.finalize()
	ciphertext = iv + encryptor.update(padded_message) + encryptor.finalize()
	return base64.b64encode(ciphertext)

# decrypt data
def decrypt(message):
	message = base64.b64decode(message)
	iv = message[:16]
	message = message[16:]
	cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
	decryptor = cipher.decryptor()
	plaintext = decryptor.update(message) + decryptor.finalize()
	unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
	unpadded_message = unpadder.update(plaintext) + unpadder.finalize()
	return unpadded_message


# koneksi ke server
r = remote(b"103.145.226.206", 1965)

# hello, establish connection
r.recvuntil(b'): ')
r.sendline(b'hello!')
r.recvuntil(b'): ')
r.sendline(b'hello!')

# get PARM
r.recvuntil(b't: ')
client_parm = r.recvline()[:-1]
a(client_parm)
print(client_parm)

# tamper PARM
r.recvuntil(b'): ')
r.sendline(sent_param)
r.recvuntil(b'): ')
r.sendline(b'PARM_ACC')

# get client PUBKEY
r.recvuntil(b't: ')
client_pubkey = r.recvline()[:-1]
SERVER_sent_pkey = b(client_pubkey)
print(SERVER_sent_pkey)

# tamper client PUBKEY
r.recvuntil(b'): ')
r.sendline(sent_pkey)
r.recvuntil(b'): ')
r.sendline(b'PUBK_ACC')

# get server PUBKEY
r.recvuntil(b'r: ')
server_pubkey = r.recvline()[:-1]
c(server_pubkey)

# tamper server PUBKEY
r.recvuntil(b'): ')
r.sendline(SERVER_sent_pkey)
r.recvuntil(b'): ')
r.sendline(b'PUBK_ACC')

# tamper message (get FLAG)
r.recvuntil(b'): ')
r.sendline(encrypt("giv me the flag you damn donut"))

# decrypt flag
r.recvuntil(b'r: ')
enc = r.recvline()[:-1]
print(decrypt(enc))
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeN2mbA9LAKpIaFaCtUtJVxPdpwQqkV0VNY86OrZRuRrkfRmmbScPWidbjNsGuBg1__RJHuau5XXJox4G354i4OLvGn_YWlb4CB4i_2mguaVTj10ZyJXNvyUffhV5-PYULO0YoklmnugUR7ccZxIkScBahv?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Flag: `NCW23{bro_pikir_dia_sesungguhnya_adalah_whitfield_diffie_dan_martin_hellman}`\
