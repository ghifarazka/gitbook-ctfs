# eeee (480 pts)

### Deskripsi

> eeee?
>
> nc 103.152.242.228 1021
>
> Author : MockingJay

Pada soal ini kita diberikan sebuah service tapi tidak diberikan source code nya. Tampilannya adalah sebagai berikut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdbD7MVyeh5v-F6VxU3XQReKZQMQxwM3OWMfOsadgaDJDxPD6Uu3s3blhRIU-4REIcHlc3b2lqDdlvD0S2NOiPyHTY-W7TsQgcQ6-vGFg8r_SkmeGh49G_OGz5jzbXieEWrhYBnLFijE6Q4GFsWIrmde-mK?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Di awal kita diberikan nilai `n` dan `e`. Berikutnya, kita dibolehkan menginput sebuah nilai `e`. Server akan meng-output sebuah bilangan. Setelah menanyakan pada probset, rupanya ini adalah hasil dari `inverse(e_user, phi)`. Dengan kata lain, ini adalah `d` dari `e_user`. Lalu setelah itu kita juga diberikan sebuah `c` untuk di-decrypt menjadi `m`. Jika salah, maka kita dibolehkan untuk menginput `e` lagi, begitu seterusnya. Btw walaupun boleh input `e` lagi, `n` dan `e` awal tetap sama.

Sekarang, katakanlah `e` awal itu `e1`, dan private key nya `d1`. Sementara itu, `e` user adalah `e2` dan private key nya `d2`. Berdasarkan definisi dari `e` dan `d` dalam RSA, didapat:

```
e1*d1 ≡ 1 mod phi
e2*d2 ≡ 1 mod phi
```

Berikutnya, berdasarkan sifat-sifat modular arithmetic, didapat:

```
e1*d1*e2*d2 ≡ 1*1 mod phi
d1*(e1*e2*d2) ≡ 1 mod phi
```

Di sini nilai `e1`, `e2`, dan `d2` diketahui. Nilai yang ingin kita cari adalah `d1`. Dengan begitu, untuk mendapatkan `d1`, kita tinggal perlu mengambil:

```
inverse(e1*e2*d2, phi)
```

Yang mana `inverse([sesuatu], phi)` itu telah disediakan oleh service. Oleh karena itu tinggal kita kalikan saja nilai `e1`, `e2`, dan `d2` lalu masukkan ke service. Hasilnya adalah `d1`. Berikutnya, kita gunakan `d1` untuk men-decrypt `c` yang diberikan server. Flag pun kita dapatkan.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcMgI9Q9qlz1eunb0oHbypZ9Zv1dvV5pJXVDFCme8AyddpJVIZrKOvkwrKSglaCnG_J3wKJrwOJ31IruhCOcWNGJIscywjwCWZC4ddKaE85TG0r6F6joVn0l9RrGjQ_VGbOo9CIl2f5DBOBnGvz5OphOPho?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeCIiHNKDXJAkQNoJYYlsTLAmmY01BeeojnUKTMOT_2mdqr0cmYC0LTlE9yhdkycPk8ly_uz1JIQpKImvqOS6Du6kwwuV1vGCNU6w3-uwr-nGJIYq3s_S-W1w5RcBip5JFjnEoB4lj6DcMZwOEPjA8beOVl?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfwd_VjEYIacivaI1gyjOx_K_uknI-UAwsWKB_N9ro-xUAjVtNVr4E5sTrmE7iEMfQvkhkv-wVocU39tU83GoJrXtsiUec0iPQy6fCU0j6nWQCCQ-bpwFr5CK1vwpqfsDM9u8IQSKF0yeBCXgbMQnhLA3eY?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdhI1A6CsCekHEZSCrJT6NlLdNHfEdQwwrZIT-85u4H_Jh843k6HpSGx-Lfp7_ve2XNhZZ01IJ1BYd3Scsl9UmPRTWnjlyTU96VXjRCnf4SsegOTtCQRVcg-9ct2JXT0e3i0urUk7CODOanjywml90I0m3o?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Flag: `slashroot7{meh_this_is_just_an_ez_crypto_wahahaha_welcome}`
