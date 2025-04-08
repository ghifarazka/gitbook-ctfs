# 🇮🇩 Hology 6

{% hint style="info" %}
Participated as **teori ganti nama tim**
{% endhint %}

## Crypto

### xor

> Author: Hazbiy
>
> Today i visit a museum. It was an animal museum While it was fun, i see some gold bug with strange name displayed It says "3‡0†2?3", what does that even mean?

Kita diberikan file `encrypted` yang isinya telah terenkripsi. Berdasarkan soal, enkripsi yang digunakan adalah XOR. Namun, untuk key-nya agak membingungkan. Berdasarkan deskripsi, tampak bahwa mungkin “gold bug” itu ada hubungannya. Karena itu, saya mencoba beberapa kombinasi dari “gold bug” seperti “goldbug”, “Goldbug”, “GoldBug”, dan akhirnya menemukan bahwa key yang benar adalah “GOLDBUG”.

```python
from pwn import *

enc = open("encrypted", "rb").read()

print(xor(enc, b"GOLDBUG"))
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeJdUp-t28z6ITI4P6Pi3Odx5gvHE2mtvzuJoe1mjICYB0Uo3CJKW6zwS68MTQfKc_H3sybT9-jtkiq-mvfqstF5tWAo2qmTFVVveKiM1DiGkNIP9cwBMmJGG4v0Qwpe4b4E-uAC9MB7F_sO7SAU4jPNGla?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Flag: `Hology6{yOu_d3crypt_m3_Huh}`

## Forensics

### Beep Boop

> Author: Hazbiy
>
> Why someone hold this poster so dearly, it's 23th year of this century already!
>
> (btw gak salah kah ini desc nya xD)

Pada soal ini kita diberikan file audio `beep_boop.wav`. Setelah mendengarkan isi audio tersebut yang tidak jelas, seketika saya langsung terpikir bahwa flagnya ada di spectrogram. Oleh karena itu, saya membuka `sonic-visualizer`, lalu memilih opsi “add spectrogram”. Berikut adalah hasilnya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcxR08EYpW4r96iP1t4cwaZTKvU4j-GS8wkMBjUSwRMgw7aqyQ1Y0yC369f9bs7NRYpMF9F2HzObFVJGRjz3vC5y_L81q0D06OIFJljSPbj-BySEsCosOy8-IA1EguwqhQSFXSKg6rzjNs65QvtjD3UU4j5?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Flag: `Hology6{W3_c4N_rE4D_s0uNd_1T_Se3mS}`

### His Idol

> Author: Hazbiy
>
> Why someone hold this poster so dearly, it's 23th year of this century already!

Kita diberikan file gambar `poster.jpg`. Melakukan `exiftool` pada file, kita mendapat string berikut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfQh105mK1ZMOnYtC-qGzmQrtBzEfG-pEzMrTgzQDejRhay6IE8M4JTnbiiwcdJtLxH4TYXZ9HJF31uaHqG9R_9fWyDkqCjdMUwiOV1dPJRk9D9bu5aCdP4zQRnS1eS7YoEu0C6gMCrBVgr_FEgRWfu2W2L?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Sesuai clue pada deskripsi, string ini menggunakan caesar cipher dengan shift sebanyak 23, sehingga hasilnya adalah sebuah link.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdxe_vDfNf5ridISV8UgqCNL77S_jfEWXCayrAvY9Tor60iFIpiKF3KC8m3vdyPa8UqcqIgYG2DbvWVNqlso4e2fYbhLeo42F-MBcnFqDSlvl4AQloNCQm6_U5QNUDpR2HNLbw4Fx3FZQaMZ9VQr4CWS2qQ?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Pada link tersebut, kita diarahkan pada sebuah google drive berisi gambar `original_logo.jpg` yang tampaknya sama persis dengan `poster.jpg`.

| poster.jpg                                                                                                                                                                                                                                 | original\_logo.jpg                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcjGZKNZ33G8eC5IgEL_2vV2UitxPd5bVTA9P7FFmnvauvjeoLdaknnmv0qS1YdGzgoxRGb2VB07H_WlR-BL7sKbjNk5-2slTTboDNIYs_XOpSem3ZoyG0G8Cc4cC0wypF6qYzsh3WZahpATxud135r5Ho?key=j25-8FRNm3AiBoMACfBbTw) | ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcjGZKNZ33G8eC5IgEL_2vV2UitxPd5bVTA9P7FFmnvauvjeoLdaknnmv0qS1YdGzgoxRGb2VB07H_WlR-BL7sKbjNk5-2slTTboDNIYs_XOpSem3ZoyG0G8Cc4cC0wypF6qYzsh3WZahpATxud135r5Ho?key=j25-8FRNm3AiBoMACfBbTw) |

Saat mencari-cari di mana letak perbedaan kedua gambar, saya mencoba membandingkan value hex dari kedua gambar, dan akhirnya menemukan perbedaan. Terlihat di bawah ini bahwa pada salah satu byte, yang aslinya `00` malah menjadi `48`.\


<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdiVkHwOO8zjyuWsrZku4AFhKXWYqr_cNztkixnhs6s8fG40pd6HAkm2H5QYSDvc5cLwDUgY96l94xqPn-VqDK6BywXxRqyG9aZrdVqHLO9ar0zTWFtjSDpCJ52LjYnMMGkRlYBp9cBlUqX2M1Vbhr_tcGU?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc_wbGUXqaYxa7VU5lj235WmOUjTAv_FS4CUG1tcBVbjHkAAwHr9s8BgS9y45HDWU2mm7wLlYnbcuxAZM8M6_4ejXZVheCbRW-6iw89xDq1sWhrcNmzh0Moiqfq2e079EYbuSvWxDDyXwJ7nWDaKW_DPs52?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Menariknya, karakter hex 48 dalam ascii adalah “H”, yang juga merupakan karakter pertama dari flag. Oleh karena itu, saya menduga bahwa flagnya merupakan semua byte pada `poster.jpg` yang berbeda dari gambar aslinya. Untuk itu, saya menggunakan kode berikut.

```python
poster = open("poster.jpg", "rb").read()
ori = open("original_logo.jpg", "rb").read()

answer = ""
for x, y in zip(poster, ori):
	if x != y:
		answer += chr(x)

print(answer)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfgwuK_5yQzNv4jy3KB2NPpracSFyKq1QdbdEtFVe-cAnYvHhQJ4ukbegEnhLzb4ily-TqeWGUyMBrtGbHcYA9dsWRHJGD5K2Bn9Na46sy2HmvSX_3Zd-q0ZqnN0ITE6KJiZ1Hw4GKaK43TlAmFalTWVEM?key=j25-8FRNm3AiBoMACfBbTw" alt=""><figcaption></figcaption></figure>

Flag: `Hology6{Y0u_goT_M3}`
