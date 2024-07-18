# not simply corrupted (316 pts)

### Deskripsi

> My friend loves to send me memes that has cats in it! One day, he sent me another cat meme from his 4-bit computer, this time with “a secret”, he said. Unfortunately, he didn’t know sending the meme from his 4-bit computer sorta altered the image. Can you help me repair the image and find the secret?
>
> Author: notnot

Diberikan `cat.png` yang apabila dibuka isinya adalah sebagai berikut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdccTpASLkcIPv1jukZdPmgQ8NMSX8BUt1354M6jGGvwjAXBzLeYQ6TW_oAD3t2POK3u0unHn9-qtrLBpC0zwH9sbX-U8ZOrBDaAmyHGjLvR1yTBPQMmP_O8AQFCrDwc-qbJESyVL9Qqpb8ONQZ5uvDj7t1?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Saya curiga bahwa ini merupakan gambar yang dikonversi ke dalam encoding binary. Untuk, memastikan, saya coba decode beberapa bytes pertama dan benar, didapat sebuah header file PNG.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcHAVZNw2p-vR16UoRHOwg2mjqqFByd5OG6xvYBcfK5F637c105Ug25kD2DWkEwUh4itQj-Im10opmbFPGIfvj3Eb4qz2r919KoBA7z-W5IT4H0pKAEUl2i9-luQTFD8Pa5ugxX3KJVrnaLSE0_aikPCfc?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Dengan begitu, file tadi kita konversikan saja dari masing-masing 8-bit binary ke dalam bytes. Saya menggunakan solver berikut.

```python
img = open("cat.png","rb").read()

binstring = ""

for byte in img:
    if byte == 0:
        binstring += "00"
    elif byte == 1:
        binstring += "01"
    elif byte == 16:
        binstring += "10"
    elif byte == 17:
        binstring += "11"

res = bytes.fromhex(hex(int(binstring, 2))[2:])

result = open("flag.png", "wb")
result.write(res)
print("Process complete.")
```

Hasilnya adalah sebagai berikut. Karena masih belum ada flag, saya mencoba menggunakan tool `aperisolve.com`. Flag terdapat pada red plane dari gambar.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXetR6T93-ELfkp4CN_NOSW4k-bTKEoCScdQmCsJcj0P8nJMrcvGGdvx5u-8lQgpWfooDyJBSbOu0SyCTXBX-POpOXoKlyfzqhjKNhQuuNZQCUr4lGMhb8QedYLRjo1b9AhrqojQ3v9i_ZA8nZQj6DcL6kaU?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdcHZ-HEddvzMEtEYEPaCPF8CsI69nWpNBhHDRYf5S3D6Xqd95IbDWhk15DgghrsPMzgZoNl3dklmO41M40JeQKxLVStejn1pEh5Skcr_NFurz-pQTlKQtVFB1ekkxOgSj2Yu8ywfP7HsJh5Dj_mDXazS5m?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Flag: `COMPFEST15{n0t_X4ctlY_s0m3th1n9_4_b1t_1nn1t_f08486274d}`
