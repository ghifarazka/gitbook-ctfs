# DUMPling

### Description

> hufttt, saya lupa dimana menyimpan folder flag nya :(
>
> chall
>
> Author: millkywaay

Kita diberikan file memory dump bernama `chall.raw`. Untuk menganalisis file memory dump, kita bisa menggunakan tool `Volatility`. Di waktu kompetisi, saya tidak berhasil melakukan dumpfiles sebagaimana pada soal [tahun lalu](../../2023/technofair-10/bantu-aku.md) menggunakan volatility 2, untuk alasan yang tidak saya ketahui.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Setelah kompetisi selesai, saya mendapatkan info cara solve yang menggunakan volatility 3. Jadi pertama-tama, kita menggunakan command berikut: `vol -f chall.raw windows.filescan | grep -Fi "flag"`.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Jika membuka`clue.txt` menggunakan dumpfiles, kita akan diarahkan untuk membuka `flag1.png` dan `flag2.png` (kita telah menemukan kedua file tersebut di atas).

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Dumpfiles bisa kita lakukan dengan command berikut: `vol -f chall.raw windows.dumpfiles --virtaddr 0xa80953ebc870`

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{You_fiNd_THe_fLaG}`

### Kesimpulan

* `vol -f chall.raw windows.filescan | grep -Fi "flag"`
* `vol -f chall.raw windows.dumpfiles --virtaddr 0xa80953ebc870`
* Sebaiknya, gunakan kedua versi dari Volatility
