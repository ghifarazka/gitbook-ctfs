# Siap Tempur!!

### Description

> WAH INI DIAAAAAA SISTEM ALAT ENKRIPSI MUTAKHIR DARI ISEKAI YANG DAPAT MEMPORAK-PORANDAKAN KETAHANAN KRIPTOGRAFI REPUBLIK INDONESIA!!!!
>
> Author: AnYujin
>
> nc 103.185.53.181 4255

Kita diberikan 2 file source code yakni `Paillier.py` dan `soal.py` serta sebuah service. Berikut adalah file source dari soal.

```python
from Crypto.Util.number import *
from math import lcm
import random

class Paillier :
    def __init__(self):
        self.cnt=1
        while True:
            p, q = getPrime(512), getPrime(512)
            if GCD(p*q, (p-1)*(q-1)) == 1:
                break
        self.phi=lcm(p-1,q-1)
        self.n = p * q
        self.r= { r+1 : random.randint(2, self.n-1) for r in range(128) }

    def encrypt(self,msg,r):
        msg_len=len(msg)
        msg=bytes_to_long(msg.encode())
        gm=pow(self.n+1,msg,self.n**2)
        if r==0:
            rn=pow(self.r[msg_len],self.n+self.cnt,self.n**2)
        else:
            rn=pow(r,self.n+self.cnt,self.n**2)
        ct=(gm*rn)%(self.n**2)
        self.cnt+=1
        return ct
```

```python
from Paillier import Paillier
from secret import flag
from Crypto.Util.number import *

cipher=Paillier()

while True:
    print("What you want to do?")
    print("1. Encrypt a message")
    print("2. Encrypt the flag")
    print("3. exit")
    inp=int(input("> "))
    if(inp==1):
        print("Enter message")
        msg=input("> ")
        print("Enter r")
        r=int(input("> "))
        ct=cipher.encrypt(msg,r)
        print(f"encrypted : {ct}")
    elif(inp==2):
        ct=cipher.encrypt(flag,0)
        print(f"encrypted flag : {ct}")
    else:
        exit()
```

Soal ini menerapkan [Paillier cryptosystem](https://en.wikipedia.org/wiki/Paillier\_cryptosystem). Untuk mendapatkan ciphertext `ct`, kita perlu menghitung `ct = (g^m * r^n) mod n^2`. Di soal ini, `g^m` dilambangkan dengan `gm`, sedangkan `r^n` dilambangkan dengan `rn`.  Setelah menganalisis kode di atas untuk memeriksa adanya cacat implementasi yang menimbulkan kerentanan, ada beberapa hal yang ditemukan.

Di sini `g` di-set sebagai `n+1`. Dengan menggunakan teorema binomial:

```
gm = (g^m) mod n^2
gm = ((n+1)^m) mod n^2
gm = (1^m + n*m + mC2*n^2 + ...) mod n^2        # teorema binomial
gm = m*n + 1
```

Jika kita mendapatkan gm, maka kita bisa mendapatkan `n`. Di soal, kita bisa mengenkripsi pesan (misalnya 'A', nilai decimal = 65) dan memasukkan `r` secara custom. Kita bisa saja memasukkan `r = 1` supaya `ct == gm`. Setelah itu, tinggal hitung n dengan `n = (gm-1)//65`.

Kerentanan berikutnya adalah `n` yang digunakan secara konstan. Di sini ada sistem untuk membedakan setiap enkripsi, yaitu menggunakan "count". Akan tetapi, sistem ini justru bisa kita manfaatkan. Misalnya saat ini `count == 2`, lalu kita encrypt flag sebanyak dua kali. Maka perhitungannya menjadi seperti berikut.

```
ct1 = gm*r^(n+2) % n^2
ct2 = gm*r^(n+3) % n^2
ct2 * ct1^-1 = r % n^2
# karena r pasti < n (aturan di Paillier), maka
ct2 * ct1^-1 = r
```

Nah, `r` sudah kita dapatkan. Berikutnya, kita bisa mendapatkan nilai `gm` dari flag.

```
gm = ( ct1 * r^(-(n+2)) ) % n**2
```

Jika gm sudah didapatkan, maka kita dapat menghitung nilai `m` dengan mudah, seperti berikut.

```
m = (gm-1)//n
```

Berikut adalah kode solver lengkapnya. Soal ini menggunakan service oracle, jadi nilai-nilai parameternya dapat berubah di setiap sesi.

```python
from Crypto.Util.number import *

# Encrypt "A" (65 di decimal), dengan r = 1
# ct = gm
# gm = mn + 1; menggunakan teorema binomial
enc = 6276893213329167752128078564524048240849285055140453373047594965125809791555037998747079798841393543778930472616349381967164203034215086686735731569351040662962905680142589121570682267751062965110316378766857233231823737625177119068132482158735759725280167444770265925240695695090330576829133017323152505129816

# Hitung n
n = (enc-1)//65

# Encrypt flag; count = 2
ct1 = 2151001259599988641998687482514825897918853117427527508753809657678824521381422459080301076718220769920035886555508086414081804040166035319637893798225331941854353760922278861537398363948778726588084383060262022107783216975919757570739654080764839964098775953448354987642067340461419224033868176640116485910487147580198959174218206464320672276722564825402189709409812201239296474905048739507699102472221753449784211133814248833331498857609237219113254377786480322160204018358978337562409200694575619616187417223534388644070155013606463048348670479147544550868890764060911555244467495373340356511149366099153768656322

# Encrypt flag; count = 3
ct2 = 8606364435051217187722030150691256140186872568340894681580942425342565909071273472744444522307517631327206700058262478597222493931623793204619638784029937740513557377713105872776476601777504386459940448926403558044354753549548162949026905399197031667525702426260789925971085492578959021928767040320971517639011128905937272353581479523169238124490335284981318923405897387550637036278415141527211342090337416635263922548694959035055295794496995351114151320925811488048152141865905824268137940437829656899982376710649539807041707733957927859954017780664650309381744813500190916820763241894187567680487803371278947515324

# Ambil nilai r dari flag
r = (ct2 * inverse(ct1, n**2)) % n**2

# Hitung nilai gm dari flag
gm = (ct1 * inverse(pow(r, n+2, n**2), n**2)) % n**2

# Hitung m
m = (gm-1)//n
print(long_to_bytes(m))
```

Flag: `TechnoFair11{R415ha_M4r5h4_M1ch13_Fl0R4_91T4}`
