# space mono

### Deskripsi

> If i could fall into the space, do you think .. .. .. .. would pass me by
>
> Chall: GLHF!!
>
> Format Flag: TechnoFairCTF{random\_string}
>
> Author: jsbach#7151

Diberikan file `chall` yang apabila kita buka menggunakan hex editor, merupakan sebuah file PNG yang bytes-nya dibalik.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXelsmW-eX1NrcKoBx3JsGm9Qr_6QRS_byr0OLrsyM2-WjgShVlRAPf5OpIqXI0dnfk1SnjxkB8q_Osq63i6mFhJANM2yrGBjPOGLdmHOlync_EvTZSwIc1kMt6peePV1uZwTIj5WlG2m5wSozaoD7p9y-BE?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Dengan scripting dikit menggunakan Python, saya berhasil membalik bytes-nya. Namun ternyata masih ada yang kurang. Kita perlu menambahkan header chunk IHDR dan IEND secara manual. Selain itu, ada 36 header IDAT yang terbalik menjadi TADI. Oleh karena itu, semuanya perlu kita perbaiki.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeIvZrvoOVY4QBJHZchzv4XmxKL4vM_ZAVd3ikuvSz8Lydh1DMrnktYy79O0R3u2gMfucmCTLVwLlID3T5I-6Ew95A1ZXWz_uVvsYDTyqb50uOMjCFZYGKmCu7ZwGCMIQwq4BFQj4YQAwiNF8uUp4W8N1Hs?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Setelah memperbaiki semua yang disebutkan di atas, masih ada yang perlu kita perbaiki, yakni ukuran gambar. Pada file awal kita diberikan ukuran gambar sebesar `13 x 37`, namun dengan ukuran ini, CRC nya tidak sesuai. Oleh karena itu, kita perlu mencari ukuran gambar yang sesuai dengan CRC yang diberikan. Untuk itu, saya merujuk pada write-up ini: [https://ctftime.org/writeup/23809](https://ctftime.org/writeup/23809).&#x20;

Berikut adalah kode solver beserta hasilnya.

```python
from zlib import crc32

data = open("haha.png",'rb').read()
index = 12

ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11

for x in range(1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for i in range(len(height)):
            ihdr[height_index - i] = height[-i -1]
        for i in range(len(width)):
            ihdr[width_index - i] = width[-i -1]
        if hex(crc32(ihdr)) == '0x83d03504':
            print("width: {} height: {}".format(width.hex(),height.hex()))
    for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfW1MCcHyQYYdD4MgukKlxuWNHRtik1qE2w4gSfZXfEy-jYoUb1je7Nyk_rSFXlGf-BrQcjdNHWqmOxB0OyxqSThe9FHg9kzZYlfbXOEswa2hbKTlDbn8YVMUfSmoh2xbpZbh-B_i9js0nHXcZj0O1L4MyO?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXemwNKYZ9TBD8G02zoOzYj94tHBX7meZguSG0yTYjIZQDKEbpE1R0UaeOj3AzTW6tj6FzCtw6-Qz2e0TvsNK5i3jqH8-UpH1f_AFdRqfw-LW-XZolVdlyV66nv9C0EoyVBQo6Z68GCOvvdY4brUbUCAGalk?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Dan berikut ini adalah hasil gambarnya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfi0e1YNWf50KUi88E12tBIHD7Nk1FUqwK92Sh6jgb_2SS7EqcbsdROUzawqmEPfPZ7MfaDlsox71LSOQTnhAGLoMeBzUooD2sPv_Y9HBgE3LNjKWreFy_cqiexxSNlaXrWIP07YXQg8WJIDXZJGOqRpcg?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFairCTF{th3r3_1s_n0th1N9_3L53_0nLy_5p4c3_h3r3_d81d0481f0}`
