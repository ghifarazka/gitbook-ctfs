# daruma

> Software audit is so cringe bro, why don't we do paper audit instead
>
> nc 178.128.102.145 50001

Kita diberikan file challenge.py sebagai berikut.

```python
import random
from Crypto.Util.number import *


class AECF:
    def __init__(self, p=None, q=None, g=2):

        p = p or getPrime(512)
        q = q or getPrime(512)
        n = p * q
        self.g = g
        self.n2 = n**2
        self.totient = n * (p - 1) * (q - 1)

        while True:
            self.k = random.randrange(2, self.n2 - 1)
            if GCD(self.k, self.n2) == 1:
                break

        while True:
            self.e = random.randrange(2, self.totient - 1)
            if GCD(self.e, self.totient) == 1:
                break

        self.d = inverse(self.e, self.totient)

        self.l = random.randrange(1, self.n2 - 1)
        self.beta = pow(self.g, self.l, self.n2)

    def public_key(self):
        return (self.n2, self.e, self.beta)
    
    def private_key(self):
        return (self.d, self.l)

    def encrypt_and_sign(self, plaintext, public):
        n2, e, beta = public
        m = bytes_to_long(plaintext)
        r = pow(self.k, e, n2) % n2
        s = m * self.k * pow(beta, self.l, n2) % n2
        return r, s

    def decrypt_and_verify(self, r, s, beta):
        m = s * inverse(pow(r, self.d, self.n2), self.n2) * inverse(pow(beta, self.l, self.n2), self.n2) % self.n2
        return long_to_bytes(m)

FLAG = open('flag.txt', 'rb').read()
bob = AECF()

enc_flag = bob.encrypt_and_sign(FLAG, bob.public_key())
assert bob.decrypt_and_verify(*enc_flag, bob.beta) == FLAG

print("Encrypted flag:", enc_flag)
print("Bob public key:", bob.public_key())

for _ in range(2):
    print()
    print("="*40)
    try:
        n = int(input("Your public modulus: "))
        if n.bit_length() < 2000 or n.bit_length() > 10000 or isPrime(n):
            print("Insecure modulus")
            break

        e = int(input("Your public e: "))
        beta = int(input("Your public beta: "))
        message = input("Message you want to encrypt and sign: ")

        c = bob.encrypt_and_sign(message.encode(), (n, e, beta))
        print("Your ciphertext:", c)

    except Exception as e:
        print(e)
        break
```

Kode yang diberikan ini merupakan implementasi dari algoritma yang ada pada paper yang diberikan. Di sini, kita diminta untuk mencari kelemahan yang terdapat pada implementasinya.

Jika kita mencoba menjalankan `challenge.py` atau connect ke service, kita akan diberikan encrypted flag serta public key yang digunakan untuk meng-encrypt flag tersebut. Berikutnya, kita bisa meng-encrypt sesuka kita dengan menginputkan parameter-parameter public key kita sendiri.

Kalau menelusuri source code nya, ada dua hal menarik di sini. Pertama-tama, ada dua value yang seharusnya rahasia, yakni `k` dan `l`. Tapi jika dilihat, walaupun kedua value ini telah digunakan untuk meng-encrypt flag,  value-nya akan selalu tetap. Kalau begitu, kita bisa saja me-leak kedua nilai tersebut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc8uPFDq_MNPna7wWTEkMDyhLBmlhmkQDjsENPh_WD-rlEAaaEwucq-_xEo2TkOWSEtR2iXpRbxga-BmBMdxzNM7DNJl-WDdtqVDY5a19LwvEM6hSvGqZXpwCKY7taOYgaWUyULQeGda98uQ0hClA1f2egz?key=ClRRTIJ-4B22vL4Wwq497Q" alt=""><figcaption></figcaption></figure>

Kedua, pada saat kita dibolehkan meng-input pesan serta parameter public key, parameter public key yang dicek hanyalah modulusnya saja. Ini berarti kita bisa saja memasukkan nilai “1” untuk `e`, `beta`, dan pesan yang ingin dienkripsi.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeyAsTrED4rUz943PiHvz8uXIiBciDtf0_egSsSHstGr4lw5TaANb-AN3ZSE1hNwoNrdN9gjBzC5zSm80EqGf1LDLY8ZTWq7_6fiJF5uz1AAAguac1bNwBPBWITYoB_BDiW2-hPCVec6kCYKMrKn3CUOFrR?key=ClRRTIJ-4B22vL4Wwq497Q" alt=""><figcaption></figcaption></figure>

Baiklah, sekarang tinggal memanfaatkan fakta-fakta yang ada. Berdasarkan fungsi encrypt di bawah, jika kita memasukkan nilai `e == 1`, maka r yang dihasilkan akan sama dengan `k`. Oh iya, ini memungkinkan karena by definition, `k < n2`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfidP-F3LwVDy587HfvNbBexh4thAWjQApMpIimbVxXdrRQ0_uqGMVczn5DAI3l1_58LQtAyLnfKaU14kjbdY1zNTEj2Ud8kPCzDWrA6W-6uvtVcgBijsEM1m2fz0Si64M6uHH9cklLBr0-MWVQcaj5wv0Z?key=ClRRTIJ-4B22vL4Wwq497Q" alt=""><figcaption></figcaption></figure>

Nah kalau sudah dapat `k`, berikutnya kita ingin me-leak nilai `l`. Tapi, saya merasa kalau itu akan sulit. Sehingga, saya mencoba mengakalinya. Kira-kira penjabaran mod-arithmeticnya seperti di bawah ini.

Kalau kita ingin mendapatkan nilai `m`, maka nilai `s` harus dikalikan dengan inverse dari `k` dalam modulo `n2`, serta dikalikan lagi dengan inverse dari `beta^l` dalam modulo `n2`.&#x20;

```
s = m*k*(b^l) mod n2
s*k^(-1)*(b^l)^(-1) mod n2 = m*k^(-1)*(b^l)^(-1) mod n2 
```

Tapi karena nilai `k` kita ketahui, ambil saja inverse dari `k*beta^l` dalam modulo `n2`. Oh iya, untuk mendapatkan nilai `beta^l mod n2` nya, kita bisa connect ke service dan untuk parameternya dimasukkan nilai beta yang sama yang digunakan untuk meng-encrypt flag serta message yang nilainya mudah diketahui.

```
s*(k*(b^l))^(-1) mod n2 = m*(k*(b^l))^(-1) mod n2 
```

Full solvernya adalah sebagai berikut.

```python
from Crypto.Util.number import *

# ciphertext
r = 114317210878076873409523...
s = 649156775068941224032463...

# public key
n2 = 124272585341670616060844540...
e = 11739771616354359829825784056...
beta = 912579443257101021490467...

# get k
m_usr = bytes_to_long(b'1')
k = 7998334566914373029...

# get inv_mk
s_usr = 66733792196253686...
inv_mk = inverse(m_usr*k, n2)

# get b^l mod n2
s_beta = 85036343138956...
bl = (s_beta*inv_mk) % n2

# decrypt
inv_k = inverse(k,n2)
inv_bl = inverse(bl,n2)
m = (s*inv_k*inv_bl) % n2
print(long_to_bytes(m))
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfWw2eL4xZerZmtYLnI2yGV67_uq2uIa5-nhxiLDeg-RZumsou8SJr2Wg-JqlAeEE8hXAa0UhrV8j0eID83VejQfpgleoO1EwrNtquS9hTaq5VGWe4muKEJDJK410NJH8yBBak2d0r8BHQtlnAQJdTFPaeN?key=ClRRTIJ-4B22vL4Wwq497Q" alt=""><figcaption></figcaption></figure>

Flag: `CJ2023{dont_roll_your_own_crypto_part_xxxxx_idk}`
