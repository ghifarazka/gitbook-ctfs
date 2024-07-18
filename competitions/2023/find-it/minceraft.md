# MINCERAFT

### Deskripsi

> Alex adalah seorang pencari kerja. Dia aktif bermedia sosial. Hingga saat ini dia belum mendapatkan pekerjaan. Akhirnya dia menjadi pengangguran.
>
> Ternyata Alex dan keluarga manusia 4 dimensi!
>
> Attachments&#x20;
>
> Author - hanz0x17#5746
>
> Hints: game kok kubus. ohh sama kaya temanya tema findit ternyata 4d gist

Pada attachment kita diberikan gambar karakter Alex dari Minecraft. Namun, setelah mengonfirmasi pada probset, objektif dari soal ini adalah mencari nama lengkap (dan dari situ, sosmed) dari seseorang yang bernama Alex dan memenuhi kriteria pada deskripsi soal. Oleh karena itu, gambar tadi tidak perlu ditelusuri.

Melihat pada deskripsi, clue pertama adalah “_Ternyata Alex dan keluarga manusia 4 dimensi!_”. Di sini, keluarga berarti family name alias last name. Oleh karena itu, nama lengkap alex memiliki format sebagai berikut:

`Alex + [last name yang berhubungan dengan 4 dimensi]`

Saya bingung bagaimana menebaknya, tapi setelah muncul hint “tema findit ternyata 4d”, kita mengetahui dari IG findIT bahwa tema findIT tahun ini adalah “Tesseracts”. Oleh karena itu, dapat disimpulkan bahwa nama lengkap Alex adalah `Alex Tesseracts`.

Berikutnya, saya ingin mencari sosmed milik Alex. Saya menggunakan tool `sherlock` untuk mencari username yang digunakan pada berbagai website. Saya mencoba berbagai variasi dari nama Alex Tesseracts.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdnp8bh70i3zT5_ythgnTue0CzerinFClzF4vSKAOEGnvepFY0Le9jsBIhYCPUfSpNqLvKYTGN0AvCMNIJN9vgJRtLHs517rFdIZ0z8B4fOyb5jcusZcQBvDlBfdNv7onaCAMihOKg2SNOh5KUoyeepy-oLKnDFX1T3GAdYAmFpGUzpLx-oARs?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Website yang paling stand-out di sini adalah github. Akhirnya kita dapatkan bahwa sosmed Alex yang dimaksud adalah [https://github.com/alextesseracts](https://github.com/alextesseracts). Sebagai konfirmasi, tampak pada profilnya bahwa ia sedang mencari pekerjaan, sesuai dengan clue pada deskripsi.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdY0C2UpIWsadc2WrjmnDL3VQtOEwLcY3pbcxFGa694OMybxIXAYIbSZ2KCk134PR2x6fPz19WR6mNX4aMrMIfiEyr9Fq6Z1YK7gjLPt2DCGCu5DQmaVSGmYjPAxMi5WhC8PBrqySA6K0GqcJR7tx3kUWx5SejfINKT6-bPcWZkGZheNfbCjw?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Di sini juga terdapat secret berupa kode hex 16-byte. Saya juga tidak tahu ini apa sampai muncul hint terakhir, yakni “gist”. Saya pun langsung mengunjungi [https://gist.github.com/alextesseracts](https://gist.github.com/alextesseracts). Di sini kita melihat data berupa gambar yang di-encode dalam base64. Saya membuka gambarnya menggunakan `CyberChef`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcUBypf1vUfWl2PmrOGJYz07Nkd5N4re4FP3jme35SBgqsptLkxVss8fkuqzlzlKq6cvTe0HNwrw9lddST6xDP1nr8gP-jqVnb9ZvJq0BnLoE73t9dxI-vDTq0IIUCRIp8AtiOogcZihXngpT6ZdHyOzh5VCnqfavWe5A_M3dSSliKeBHP-bt4?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdxH_iVltWat38wWFTockOEIzHmllfWE8F6EM8_UqyxHMfi5eKG4hqnfynQAv10FqevIEE1NTx9jvJ-joS-8Zkc8IuUZsMtgBYIgNEvO-lsZ53B3uETOy4cL5f_aJkRvTzmS-l_wYT_htHsUlNmxeNw5OjYRU3aYC1YD2AMYPJmawWbv8734eU?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Di dalam gambar ada sebuah monumen yang apabila kita cari di Google adalah “_Tugu Fakultas Teknik UGM_”. Ketika mengunjungi kolom review tempat tersebut, kita mendapatkan flag-nya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcw2XlY66gKTdYWb4C0dEUYVYqPnFjtQooi88kruzpEK0IbHehApiYerIhOnFBzkuQKwW8A5oiJLg1I-X6wTZ87SnapHv5Oqvd1lN_OiHqHk-UPaEdMIJhqLqe1n3kZS2Bif1Cgqrl1dWnJbQuQb1BoLHOKaK7l6DnUd0ZlMoqAZq8DEYtIrwc?key=mXIWbPaL7LDkP4mqEjVsLw" alt=""><figcaption></figcaption></figure>

Flag: `FindITCTF{0h_t3Rk3N4L_8U4N63t_m45_Alex}`\
