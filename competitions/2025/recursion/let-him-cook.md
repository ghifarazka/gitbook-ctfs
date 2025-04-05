# let him cook

Kita diberikan sebuah website yang akan menampilkan page resep makanan berdasarkan jenis makanan yang diklik. Untuk mengakses page, URL-nya kira-kira berbentuk seperti berikut.

```
/?page=recipes/coto
```

Sekedar untuk mencoba, jika "coto" kita ganti dengan nama file yang tidak ada, maka akan terjadi error pada kode PHP-nya.

<figure><img src="../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

Sementara itu, error (atau tepatnya blokir) akan terjadi jika kita tidak menggunakan `recipes/`  atau menggunakan titik "." untuk melakukan directory traversal.

Jadi, bisa disimpulkan bahwa aturan URL-nya adalah:

* file yang dirujuk harus benar-benar ada
* harus diawali dengan `recipes/`
* tidak boleh ada titik "."

Sebagai patokan, kita akan mencoba membaca file `etc/passwd`.  Kita bisa membiarkan awalan `recipes/` , lalu menambahkan directory traversal di mana karakter titik "." di-encode URL sebanyak dua kali (%252e).  Terakhir, jangan lupa tambahkan `#` untuk mengabaikan karakter setelah payload (jika ada penambahan karakter seperti ekstensi oleh kode PHP). Maka dari itu, payloadnya adalah sebagai berikut.

```
/?page=recipes/%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd#
```

<figure><img src="../../../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

Nah sekarang, coba saja akses `flag.txt`  yang (kemungkinan) terletak di root.

```
/?page=recipes/%252e%252e/%252e%252e/%252e%252e/%252e%252e/flag%252etxt#
```

<figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

Flag: `RECURSION{t3s_omb4k}`

### Footnote

* Menambahkan `#`  di akhir payload saya pelajari dari [artikel ini](https://www.vaadata.com/blog/exploiting-an-lfi-local-file-inclusion-vulnerability-and-security-tips/).
* Dalam CTF yang mengangkat topik LFI, biasanya patokannya adalah membaca file `etc/passwd` terlebih dahulu, lalu cari flagnya. Letak flag biasanya di root `/` , home `~` , atau directory yang sama dengan file index. Nama file dari flag bisa `flag.txt`, `secret.txt`, atau bahkan yang lainnya.
