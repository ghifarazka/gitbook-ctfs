# Marsah

### Deskripsi

> Kamu suka matrix? sama, aku juga suka Marsha
>
> Format Flag: TechnoFairCTF{}
>
> Author : AnYujin

Diberikan source code beserta outputnya.

```python
from sage.all import *
from Crypto.Util.number import *
import random

flag="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
flag=[ord(i) for i in flag]
flag=[flag[i:i+6] for i in range(0,len(flag),6)]

def gen_key():
	a=[random.getrandbits(16) for _ in range(6)]
	key=[[0]*_+[a[_]]+[0]*(5-_) for _ in range(6)]
	key=Matrix(key)
	return key

flag=Matrix(flag)
key = gen_key()
key=Matrix(key)

enc=flag*key
ev=key.eigenvectors_right()
enc=list(enc)

print(f"key_hint :{ev}")
print(f"enc : {enc}")
```

```
key_hint :[(65382, [(0, 0, 0, 1, 0, 0)], 1),
(62011, [(0, 0, 0, 0, 1, 0)], 1),
(60874, [(1, 0, 0, 0, 0, 0)], 1),
(46110, [(0, 0, 1, 0, 0, 0)], 1),
(43844, [(0, 1, 0, 0, 0, 0)], 1),
(27708, [(0, 0, 0, 0, 0, 1)], 1)]
enc : [(6270022, 2279888, 4611000, 6865110, 7131265, 2632260), (6513518, 2104512, 4979880, 6603582, 7069254, 2909340), (7000510, 4165180, 5579310, 3399864, 6821210, 1579356), (5783030, 2323732, 5394870, 4903650, 3224572, 2632260), (5965652, 4428244, 5256540, 6865110, 6759199, 1440816), (6452644, 3200612, 5072100, 3399864, 7131265, 1357692)]
```

Pertama-tama, saya mengutak-atik terlebih dahulu program yang ada untuk memahami cara kerja kodenya. Saya menemukan bahwa ternyata key itu adalah matriks diagonal, jadi perkalian `flag*key` itu mirip dengan perkalian skalar tapi berbeda-beda untuk setiap kolom.

Kira-kira seperti ini contohnya untuk flag yang karakternya sama semua.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXd4d0sOLvmE25hVUrQKyrjBaWoA954lf_H6oibpNJVrf6P1E5t6PpYIFax785fitoOVhdZSTCBp_5EjQzcONmU6_1S0M6W9244wpLOa87FKZ0PqXF0Gw65SNyhtMeiHBHVeRXRyPGSBUoH1tVye7mKNOlA?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Selain itu, rupanya `key_hint` menunjukkan pada kita, “_untuk kolom tertentu pada matrix diagonal, value-nya apa?_”. Dengan pengetahuan ini, berikut adalah solver lengkapnya.

```python
# key_hint :[(65382, [(0, 0, 0, 1, 0, 0)], 1),
# (62011, [(0, 0, 0, 0, 1, 0)], 1),
# (60874, [(1, 0, 0, 0, 0, 0)], 1),
# (46110, [(0, 0, 1, 0, 0, 0)], 1),
# (43844, [(0, 1, 0, 0, 0, 0)], 1),
# (27708, [(0, 0, 0, 0, 0, 1)], 1)]

key_diagonal = [60874, 43844, 46110, 65382, 62011, 27708]
enc = [(6270022, 2279888, 4611000, 6865110, 7131265, 2632260), (6513518, 2104512, 4979880, 6603582, 7069254, 2909340), (7000510, 4165180, 5579310, 3399864, 6821210, 1579356), (5783030, 2323732, 5394870, 4903650, 3224572, 2632260), (5965652, 4428244, 5256540, 6865110, 6759199, 1440816), (6452644, 3200612, 5072100, 3399864, 7131265, 1357692)]

result = []

for t in enc:
	for i in range(len(t)):
		result.append(t[i] // key_diagonal[i])

flag = ""
for i in result:
	flag += chr(i)

print("TechnoFairCTF{"+flag+"}")
```

Flag: `TechnoFairCTF{g4dis_k0leris_y4n9_5uK4_berim4jIn4s1}`
