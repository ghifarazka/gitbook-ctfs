# Marsha

### Description

> Seseorang berhasil melakukan serangan terhadap ruang chat antara marsha dan pacarnya!!!
>
> Author: AnYujin
>
> nc 103.185.53.181 4254

Kita diberikan sebuah service dan `soal.py` yang berisikan source code dari service tersebut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXck4H5wTSznM9jyM2ygXVK3nF6zvcuMlKR5yqH62jBDca2COIZTaMCl0iLmGC9ueUu5jfHwWNtDLHUzJFy9GB2VSKnFUFca0eWcfc8ETBM4Vm3SkZCogwTgXdZ_L42gXW_QtTsnDzLP3kIL4GE6pOcYsRcb?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Berikut adalah `soal.py` yang sudah saya annotate untuk menjelaskan alurnya.

```python
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secret import flag
import hashlib
import os
import random
import string

charset=string.printable


class dh():
    def __init__(self,p,g):
        self.p=p
        self.g=g
        self.privatekey=random.randrange(2,p-1)
        self.pubkey=pow(g,self.privatekey,p)
        self.BLOCK_SIZE=16

    def get_pubkey(self):
        return self.pubkey

    def bytes_to_bin(self,val):
        return "{:08b}".format(bytes_to_long(val))

    def mult_mat(self,a,b,m):
        assert len(a[0]) == len(b)
        return [[sum([int(a[k][i]) * int(b[i][j]) for i in range(len(b))]) % m for j in range(len(a))] for k in range(len(a))]

    def add_mat(self,a,b,m):
        assert len(a[0]) == len(b[0]) and len(a) == len(b)
        return [[(int(a[i][j]) + int(b[i][j])) % m for j in range(len(a[0]))] for i in range(len(a))]

    def hex_to_bytes(self,msg):
        return long_to_bytes(int(msg,16))
    
    def bits_to_matrix(self,val):
        temp=[list(val[i:i+16]) for i in range(0, 256, 16)]
        return temp
    
    def matrix_to_bits(self,val):
        return ''.join(str(i) for j in val for i in j)

    def bytes_to_hex(self,msg):
        return "{0:x}".format(bytes_to_long(msg))


    def generate_secret(self,pub):
        self.sharedsecret=pow(pub,self.privatekey,self.p)
        temp=("{0:b}".format(self.sharedsecret)).rjust(768,'0')
        self.A,self.B,self.C=[temp[i:i+256] for i in range(0,768,256)]
        self.A=self.bits_to_matrix(self.A)
        self.B=self.bits_to_matrix(self.B)
        self.C=self.bits_to_matrix(self.C)

    
    def encrypt(self,msg):
        msg=pad(msg,self.BLOCK_SIZE)
        iv=os.urandom(self.BLOCK_SIZE)
        cipher=AES.new(hashlib.sha256(long_to_bytes(self.sharedsecret)).digest(),AES.MODE_CBC,iv=iv)
        ct=cipher.encrypt(msg)
        return self.bytes_to_hex(ct),self.bytes_to_hex(iv)

    def decrypt(self,enc,iv,sig):
        cipher=AES.new(hashlib.sha256(long_to_bytes(self.sharedsecret)).digest(),AES.MODE_CBC,iv=self.hex_to_bytes(iv))
        try:
            pt=unpad(cipher.decrypt(self.hex_to_bytes(enc)),self.BLOCK_SIZE)
            verif=(self.hash(pt)==sig)
            return verif,pt.decode()
        except:
            return False,''

    def hash(self,msg):
        len_msg=len(msg)
        msg=self.bytes_to_bin(msg)
        if(msg[0]=='0'):
            val=self.mult_mat(self.A,self.C,2)
        else:
            val=self.mult_mat(self.B,self.C,2)
        msg=msg[1:]
        for i in msg:
            if int(i)==0:
                val=self.mult_mat(self.mult_mat(val,self.A,2),self.C,2)
            else:
                val=self.mult_mat(self.mult_mat(val,self.B,2),self.C,2)
        val=self.add_mat(val,self.C,2)
        sig=self.matrix_to_bits(val)
        return "{:x}".format(int(sig))

    def kirim(self,msg):
        sig=self.hash(msg)
        enc,iv=self.encrypt(msg)
        return enc,iv,sig
        
if __name__=='__main__':
    p=getPrime(768)
    g=8
    print('Yujin sending modulo and base')
    print(f'Modulo  : {p}')
    print(f'g       : {g}')
    print('Able to change modulo')
    try:
        inp=input("> ")
        temp=len("{:08b}".format(int(p)))
        if(temp>=512 and temp<=768):
            pass
        else:
            print('Invalid value sending as it is')
        p=int(inp)
    except:
        pass

    # DH setup for Marsha
    B=dh(p,g)
    print("Marsha sending public key...")
    print(f"Sucessfully intercepted Marsha's public key")
    print(f"Marsha's public key : {B.get_pubkey()}")

    # DH setup for Yujin
    A=dh(p,g)

    # Yujin generate pubkey
    A.generate_secret(B.get_pubkey())
    print("Yujin sending public key...")
    print(f"Sucessfully intercepted Yujin's public key")
    print(f"Yujin's public key : {A.get_pubkey()}")

    # Marsha generate pubkey
    B.generate_secret(A.get_pubkey())

    # [ == shared secret is calculated == ]

    # Marsha send message
    enc,iv,sig=B.kirim(b"Halo, kamu apa kabar?")

    # WE intercept the message
    print(f"Successfully intercepted Marsha's message")
    print(f'enc          : {enc}')
    print(f'iv           : {iv}')
    print(f'signature    : {sig}')

    # WE tamper message, system check that the message is 
    # ...valid hex (already encrypted)
    try:
        print("Able to change Marsha's encrypted message")
        inp1=input("> ")
        enc=int(inp1,16)
        enc="{:x}".format(enc)
    except:
        print('Invalid value sending as it is')
        pass
    
    # Yujin will verify the message
    verif,pt=A.decrypt(enc,iv,sig)

    # Yujin must receive valid message
    try:
        assert all(i in charset for i in list(pt))
    except:
        print('Yujin left the chat...')
        exit()

    # to get flag, try to send something other than 
    # ..."halo kamu apa kabar"
    if(not verif):
        print('Yujin left the chat...')
    elif pt!="Halo, kamu apa kabar?":
        if verif:
            enc,iv,sig=A.kirim(flag)
            print(f"Successfully intercepted Yujin's message")
            print(f'enc          : {enc}')
            print(f'iv           : {iv}')
            print(f'signature    : {sig}')
        else:
            print('Yujin left the chat...')

    # if you just forward Marsha's message, Yujin will not give flag
    else:
        enc,iv,sig=A.kirim(b"Aku baik, bentar ya aku tidur dulu...")
        print(f"Successfully intercepted Yujin's message")
        print(f'enc          : {enc}')
        print(f'iv           : {iv}')
        print(f'signature    : {sig}')
        print(f"Yujin left the chat...")
```

Intinya adalah sebagai berikut:

* Di awal, kita bisa mengubah parameter “modulo” atau `p` dari protokol Diffie-Hellman pada komunikasi ini
* Kedua pihak (Marsha dan Yujin) akan saling mengirimkan public key, dan menghitung shared secret
* Dengan shared secret, Marsha mengirim pesan “Halo, kamu apa kabar?”. Pesan ini bisa kita ganti.
* Yujin akan membalas pesan berdasarkan pesan yang dikirimkan. Jika seperti yang di atas (tidak diubah), Yujin akan membalas dengan “Aku baik, bentar ya aku tidur dulu...”. Selain pesan di atas (kita ubah) maka Yujin akan membalas dengan flag.
* Awalnya saya mengira bahwa signature-nya juga perlu diatur supaya pesannya verified. Rupanya, di sini kita tidak perlu memperhatikan signature karena pesan akan selalu verified, jadi cukup pesannya saja.

Jadi sudah cukup jelas bahwa tujuan kita adalah mengetahui shared secret mereka berdua supaya bisa mengganti pesan Marsha dengan pesan lain yang bisa didekripsi oleh Yujin.

Celah utama dari protokol Diffie-Hellman adalah serangan discrete log, yang disebabkan oleh pemilihan modulo atau `p` yang tidak kuat. Pada soal ini, `p` bisa kita ubah, dan saya memasukkan `p` yang smooth, artinya `p-1` memiliki banyak faktor. Nilai `p` seperti ini rentan akan serangan discrete log. Berikut adalah kode solver yang saya gunakan.

```python
from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *
import hashlib
from pwn import *

r = remote('103.185.53.181', 4254)

def encrypt(msg, shared_secret, iv):
	key = hashlib.sha256(long_to_bytes(shared_secret)).digest()
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = cipher.encrypt(pad(msg,16))
	return ciphertext

def decrypt(msg, shared_secret, iv):
	key = hashlib.sha256(long_to_bytes(shared_secret)).digest()
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(msg)
	plaintext = unpad(plaintext,16)
	return plaintext

# get g
r.recvuntil(b'g       : ')
g = int(r.readline()[:-1])	# g = 8

# generate smooth p
p = 2
k = 3
while (p < 2**512) or not isPrime(2*int(p) + 1):
	p *= k
	k = next_prime(k)
p = 2*p + 1

# send smooth p
r.recvuntil(b'> ')
r.sendline(str(p).encode())

# get A (Yujin's PK) and B (Marsha's PK) from service
r.recvuntil(b"Marsha's public key : ")
A = int(r.recvline()[:-1])
r.recvuntil(b"Yujin's public key : ")
B = int(r.recvline()[:-1])

# calculate shared secret
F = IntegerModRing(p)
a = discrete_log(F(A), F(g))
s = int(pow(B,a,p))

# get Marsha's message
r.recvuntil(b"enc          : ")
enc = bytes.fromhex(r.readline()[:-1].decode())
r.recvuntil(b"iv           : ")
iv = bytes.fromhex(r.readline()[:-1].decode())
marsha_msg = decrypt(enc,s,iv).decode()
print("Marsha's original message:", marsha_msg)

# send tampered message
tampered_msg = marsha_msg + 'a'		# 'a' can be replaced with anything
tampered_msg = encrypt(tampered_msg.encode(),s,iv).hex().encode()
r.recvuntil(b'> ')
r.sendline(tampered_msg)

# get Yujin's reply
r.recvuntil(b"enc          : ")
enc = bytes.fromhex(r.readline()[:-1].decode())
r.recvuntil(b"iv           : ")
iv = bytes.fromhex(r.readline()[:-1].decode())
yujin_msg = decrypt(enc,s,iv).decode()
print("Yujin's message:", yujin_msg)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXf4Ph1OsYcmqgyJ28P8EXxVSbnfBxZQrebEGZxPOjQ_WTTYPMBQD1dCQukImLi0kEKfRawraytcrRlQaHY7scIWH79cRs03VXB4As_ONsMnKC1b9KbHCbFJsYgz1IHgcQ7meyCeKmFR1rtxNz9v1Z-dpIug?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{4Ku_4d4lAH_R4J4_M3ks1Ko_El_M4r5hal3}`
