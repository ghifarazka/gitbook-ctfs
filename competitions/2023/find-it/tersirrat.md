# Tersirrat

### Deskripsi

> Findy has an annoying girlfriend. His girlfriend didn't like to be to the point and often gave Findy "codes" to him. One day, Findy received messages and pictures from his girlfriend which made him confused because he couldn't figure out the meaning of the messages, moreover the pictures couldn't be opened!. Help Findy find out what his girlfriend means!
>
> Attachments&#x20;
>
> Author - AODreamer#6160

Pada attachment kita diberikan `chall.png` dan `msg.txt`. File chall.png tidak bisa dibuka, sedangkan msg.txt berisi beberapa clue sebagai berikut.

```
Halo Findy sayang <3! maaf ya kalau aku ganggu kamu terus, maaf aku suka KOMEN hidupmu terus.
Aku sadar kok aku belum bisa jadi pasangan yang baik buat kamu. Sebagai permintaan maafku, nih aku belikan CHUNKy bar buat kamu, semoga kamu suka ya! di dalamnya ada sesuatu yang harus kamu lihat dengan TELITI :D. Btw, kamu gak lupa kan 2 hari lagi aku ulang tahun? ajak aku WALKING-WALKING ya! hehehe
```

Oke, pertama-tama sebaiknya kita perbaiki dulu file png-nya. Ada clue yakni CHUNK, berarti kita mesti memperhatikan chunk yang ada di chall.png (PNG, IHDR, IDAT, IEND) dan menggantinya dengan nilai yang benar. Tidak lupa untuk menyesuaikan value CRC-nya dengan tool [https://www.nayuki.io/page/png-file-chunk-inspector](https://www.nayuki.io/page/png-file-chunk-inspector).&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXefGlE1l90c1DtxK7ZTM9RGoiPgMX5stMPurw9NOsn49-e8Xr2NElQUC6FGwoghkrsK9CB-pJUaS267svEhU_3mWBIQ_rF52yWR5bfEyRsPxyJEfmMv24xYWkQrZTB6WnCUukeSaQWTtn3NtudYxtF6TFvPsFTM4UIzR3R_hnoHqoLOoChHRts?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfuSslz5wVaLQbi8lQUXexPOT0ZDM3TpEHMWm3nqyoRWvBJ3cw0LUKMwHHZir_JQt0CNKmJRRJW_upqf8DJuFIXzIWs0IhSzv5FOosuy3Oic0bFDspauV3KE34RDbsGEh_S5y4yAuPE-hzYf4tfrgne6kUbLIjOypYkiNrUeJpB2ndFa5IbH9g?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Berikutnya, file gambar pun bisa dibuka. Karena ada clue tentang KOMEN, maka kita coba `exiftool` pada gambar. Didapat string hex yang apabila di-decode, akan didapatkan bagian pertama flag. `flag1 : FindITCTF{`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXe5m9QFRhlCohe7LDyDIQYHFohnjRMU9I02kCm_OCv3bhMAzX9ETtwqUFeRQGQRbqcbx1ZAmtv2MP0O_vVd2CkLNKSkVJ7I9Bhg5P7DBA1PDAVxPH1P5keoltW6CKK4EH7qdO8G1LWAQItkwgLxJWP4B_grXpkHs_FsTZD3mTGlYeA8JKqbkbQ?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Lalu gambar kita buka. Karena ada clue untuk TELITI, di bagian atas kubus terlihat angka “740”. Awalnya saya tidak tahu apa artinya, tapi setelah melihat angka “720” pada width dan height gambar pada exiftool, saya jadi sadar bahwa 740 merujuk pada ukuran gambar.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdCLtM3Hi0lMlJltS5c__NhY6n5MDjHRJWSTHYhS0I7RmY7S0n_Si0hfVK4FAue1WaxmYHxQh8k-mCkY25TF-c-nRmb_mGDpPL8vsLfekAWBxPLaNMzCLw3rk5y1kbLTyqS3K7uGRir0gTVXmwbMW9zgAbs6HbkuxwjcwacOHErG5UCCPb8bw?key=mXIWbPaL7LDkP4mqEjVsLw" alt="" width="188"><figcaption></figcaption></figure>

Maka dari itu kita ubah saja ukuran gambar dari 720x720 menjadi 720x740. Didapat bagian kedua flag (dalam base64) dan sebuah password.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXd5btkwldl0uemrZE0ZANWGQWHQe3E6lEHjXXMl6tIC6qc6_FzJQjvCeVhL7-_jsXgAQoZklalJUMUjowe_pI4ux4EeE7TK9MRU8R-LdT4H7-n2pf53dyUqh7TwLi30jujDimoOZYh3k3mEqlQALi3C4r88GwLXd6Bydd53QweuuV0va-iXm2k?key=mXIWbPaL7LDkP4mqEjVsLw" alt="" width="188"><figcaption></figcaption></figure>

Berikutnya ada lagi clue untuk WALKING, yang merujuk pada binwalk. Namun, saya menggunakan `foremost` untuk meng-extract gambar dan mendapatkan sebuah file zip yang dienkripsi. Dengan password yang diberikan, enkripsinya adalah sebagai berikut: `7z x -pdidufindit 00000132.zip`. Didapat bagian ketiga dari flag yang di-cipher dengan caesar.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcg9l9InlE56f5UH266lneh7fApUEtTwxw28STaPERwe9a_aNsGdLzGcILI3bFOBTChGX1FStQUxMAnBVpUvTpFxQDxPQ48a2tnJGA4yfaoxPAjW51ACHdR0X3Ppg7a2IDu4Wopnx8d7ykGGGnIcLqM88kfix7NMn7xr96n1Q18CxHknyO-R68?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Setelah di-decipher, maka keseluruhan flag telah didapatkan.

Flag: `FindITCTF{1_L0v3_y0u_3K_F1nDy}`
