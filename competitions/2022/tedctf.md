---
description: participated as insidious_hex, got into the final stage
---

# 🇮🇩 TEDCTF

## Cryptography

### RSAPonent (356 pts)

Diberikan file source code rsaponentmod.py dan outputnya yakni output.txt. Apabila kita lihat pada source code, terdapat fungsi sebagai berikut. Apabila kita coba pahami, fungsi ini sebenarnya hanya mengalikan inputnya md dengan sebuah nilai konstan yang sangat besar yakni 4\*\*(4\*\*(4\*\*2)). Ini juga berarti bahwa apapun nilai exp, itu tidak berpengaruh.

```python
# dari rsaponentmod.py

def GCZ_x(md, exp):
return md * ((((1 << exp) - (1 << (exp - 1))) // ((1 << (exp - 2)) - (1 << (exp - 3)))) ** ( ((((1 << exp) - (1 << (exp - 1))) // ((1 << (exp - 2)) - (1 << (exp - 3)))) ** (((1 << exp) - (1 << (exp - 1))) // ((1 << (exp - 2)) - (1 << (exp - 3))))) ** ((((1 << exp) - (1 << (exp - 1))) // ((1 << (exp - 2)) - (1 << (exp - 3)))) >> 1)))
```

Karena pmod dan qmod berasal dari fungsi yang sama, maka mereka memiliki common divisor yakni nilai konstan 4\*\*(4\*\*(4\*\*2)) yang sudah disebutkan sebelumnya. Apabila kita membagi masing-masing pmod dan qmod dengan nilai tersebut, kita akan mendapatkan nilai p dan q aslinya. Berikut adalah kode solvernya.

```python
from math import gcd
from Crypto.Util.number import *

# c, pmod, qmod ambil dari output.txt. Google docs gakuat load angkanya :v

common = gcd(pmod,qmod)

def GCZ_reverse(md, com):
return md // com

p = GCZ_reverse(pmod,common)
q = GCZ_reverse(qmod,common)
n = p*q
e = 65537
phi = (p-1) * (q-1)
d = pow(e,-1,phi)
m = pow(c,d,n)

print(long_to_bytes(m))
```

Flag: CTFTED2022{3xponent\_50\_big\_but\_it\_is\_just\_4\_math\_olymp\_questions\_to\_rec0ver\_pq:p}

### wrth (400 pts)

Diberikan file source code chall.py dan outputnya out.txt. Ketika melihat source code, yang saya sadari adalah banyaknya nilai variabel yang di print-out untuk output-nya. Dari situ, kita bisa mencari mana saja yang bisa dimanfaatkan. Di sini, diketahui variabel q dihasilkan menggunakan nilai hasil dari w \* h. Padahal, diketahui n = w \* r \* t \* h dan nilai n, r, t merupakan salah tiga nilai yang di-print-out. Memanfaatkan ini, berikut adalah kode solvernya.

```python
from Crypto.Util.number import *

def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n

ct = 177024696876919136608801697870895309017511060008360843393168803091459108871081310687261495021280102809400672912669937418838413166284567379658516253300239346337924594495232478180364459634771085602051226475802179347980798365381215424
mod = 189221587086097332636329343305756499362857851186076787250069910515117168681235480811027829453952949101336969994487798651037022217096158597474386328262860440135780602095962544279103321094268887216509347681698819767258378399584105849

n = 8217388685287506548535468018765805063994971720300385361558695755131638364935786830537956922584660077190031593380891890817478632579664343292346640516832909
r = 266660807362275947517652129109350110673
t = 331928392204793675799570771702846815101

wh = n // (r*t)

q = nextPrime(wh)
p = mod // q
e = 65537

phi = (p-1)*(q-1)
d = pow(e,-1,phi)

m = pow(ct, d, mod)
print(long_to_bytes(m))
```

Flag: CTFTED22{simpl3\_m0dul4r\_4r1thm3ticc\_d9e60e76db}
