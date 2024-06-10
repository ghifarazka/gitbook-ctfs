# cakemath (451 pts)

Diberikan source code dessert.py dan file output.txt. Untuk menyelesaikan soal ini, pertama-tama saya mencoba memahami apa yang dilakukan kodenya. Setelah beberapa waktu mengotak-atik kodenya, saya menemukan beberapa hal yang menarik.

```python
import random,math,os
from Crypto.Util.number import *

flag = os.getenv("NCW_FLAG")
c_n1 = random.getrandbits(512)
c_n2 = random.getrandbits(512)

assert c_n1 != c_n2
encrypted = []
bittersweet = [int(r) for r in "{:b}".format(bytes_to_long(flag))]

for sugar in bittersweet:
    while True:
        gc_c = random.randint(65536, c_n1)
        if math.gcd(gc_c, c_n1) == 1:
            encrypted.append((pow(c_n2,sugar)*pow(gc_c,2)) % c_n1)
        break


print("c_n1 =",str(c_n1))
print("c_n2 =",str(c_n2))
print("encrypted = ", end='')
print(encrypted)
```

Pertama-tama, baris kode berikut ini akan memberikan sebuah list berisi angka 0 atau 1 yang merupakan representasi binary dari flag. Oleh karena itu, untuk mendapatkan flag, dapat kita asumsikan bahwa kita perlu mencari string binary tersebut.

```python
bittersweet = [int(r) for r in "{:b}".format(bytes_to_long(flag))]
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfsuD0pLXWZyMOxlqGPRRRU54Do_YBVkXoKPLpYGqijO4lwrajYIB59_Ah1Od8DWwKgzvbtSqmAnc29eDM0cs9_8Y4xxDNQZsg_rAlXpPBAi3AA5ny5zp64is4iW-GLmZ211b8Hc2zzU715WOJqQ1exILGIWJQ34PVwgqmWghg7xW5iwRQT9Pg?key=4MW_RSVrGpPtImkfMQF2Yw" alt=""><figcaption><p>Contoh output untuk flag asal</p></figcaption></figure>

Kedua, hasil dari bittersweet tersebut digunakan untuk baris kode berikut ini. Karena nilai dari sugar itu hanya bisa berupa 0 atau 1, maka keluaran yang mungkin dari baris kode ini hanyalah (c\_n2\*(gc\_c^2)) mod c\_n1 atau (gc\_c^2) mod c\_n1 saja.

```python
encrypted.append((pow(c_n2,sugar)*pow(gc_c,2)) % c_n1)

Atau:
(cn2sugargcc2) mod cn1 
```

Ketiga, baris kode if math.gcd(gc\_c, c\_n1) == 1: memberitahu kita bahwa gc\_c dan c\_n1 adalah koprima. Di samping itu, apabila kita mencoba mengambil gcd(c\_n1, c\_n2), kita akan mendapatkan hasil angka 29. Sekarang, apabila kita mencoba mengambil dua kemungkinan untuk encrypted yang sebelumnya disebutkan, kemudian kita gcd()-kan dengan c\_n1, kita akan mendapatkan 29 untuk text yang di-encrypt dengan (c\_n2\*(gc\_c^2)) mod c\_n1 dan 1 untuk text yang di-encrypt dengan (gc\_c^2) mod c\_n1.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeGUV67TN7-dFLTC41wD488HfEJJa0UiOQcCbILnR2JGaXdfpVuHJWYgHaEYyRb0B4L8FPwd4nwEkSMMXHD8KMK44yokYvmBCEOm60fXERP6KvcbP6hkBrwi6Cbo2ch_A6O9A0oLYlOWAlWj7HlPX9-CTYOT6Pezc8ZpIDk-d92elgKZp3futE?key=4MW_RSVrGpPtImkfMQF2Yw" alt="" width="188"><figcaption></figcaption></figure>

Nah sekarang kita tinggal memprogram saja sesuai dengan nilai sugar awalnya. Untuk elemen di encrypted yang menghasilkan 29 akan kita return angka 1, dan untuk elemen yang menghasilkan 1 akan kita return angka 0.

```python
from math import gcd
from Crypto.Util.number import *

c_n1 = 3855144799899048327534121215306941141185997589420691125094911911082597963257300429096794014315805279596530735439263764994759442420373314885435640329972555
c_n2 = 5299396373535953706628077154342198627748435935987447573061077335778202151741165833985790411265547771371574434052556785516415658261684773030001154912306733
encrypted = [507104000732472450402938437721529021378564745838604181711052463510983043412099070337891206768987338263502149153936534933899109822282227342709312445026628, ..., ...]

m = ''
for c in encrypted:
    val = gcd(c_n1, c)
    if val == 29:
        m += '1'
    elif val == 1:
        m += '0'

print(long_to_bytes(int(m,2)))
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeh2mZ_T6RTiuvICdvrCatphYH_5_YJl_6-HeluMEK6zD3evgzwXlx4aNgTrnFH8bmXNLtPIaVkd6CG4QB-XxX2FkGBrySSYdfmLrrINjuhvAQkHKcBGXbnf1BiceHeF07MmPwVDbm0mF2Pp1PQt1JOtkoupiXFxFxVOnJAONScVAI3YEwTksk?key=4MW_RSVrGpPtImkfMQF2Yw" alt=""><figcaption></figcaption></figure>

Flag: NCW22{j4c0bi\_symb0ls\_101\_w!th\_c0mposit3\_numbers}
