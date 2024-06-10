---
description: participated as insidious_hex
---

# ARA

## Forensics

### corrupted (10 pts)

Diberikan file bernama rahasia. Dengan membukanya lewat hexed.it, terlihat bahwa ini adalah file .png yang corrupt. Oleh karena itu yang saya lakukan adalah mencocokkan data hex file ini agar sama dengan file .png normal yang dapat dibuka.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdFV47xM6joyX938CpMUaESrPvyzsjRxjeaN2OXdYMiC2W15lBn_ZR86ZOMqWBvCrC3hJJcKJJLGw9zFgsiuXHGIybPMOvE3fRGRX-tP_S96yWZsZ1UQMYNCTttH_NY_h6UHtJ5ENzZ565I6NIKNp0_7BArBA2nMRJfPnrYk8ceHLeIYxd502Q?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc8F38VxBWv-c9dZUbXszc0hQvwZN6jFY6W-mB7D29Od4mE1-lQL-NhTnvz-7Qzhgs5rwXu3Av8j1PeUeo2ouSqoAFCfiaKjqEhPESBEQl9F-VNs2wFDgBTx7gGcRX9b9q5THlByFcgfD_zng4e8cmaVqcBvsCjYSxbitlr8U-fJs-bfcQxXjo?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

Hasilnya, sebuah gambar dengan flag.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcZLxUCfevc_DPeZl_x6yMWG0vuBpv-jpJKhps6gANTYE7qDjABoPfFVDAHsMQxGzshpu9PMyHhZGbAcx6v7fdmdp8AZXXRiRiNfaPeK6nlOrlvQhnLxjY-afgoaIS-HgIg7R_6rViJ4Cl_FAGbFUIV44_zUHNpk5IDycnc5U4hgb_A2UlDVg?key=smVvNwC0TJMlqHL-kwJjng" alt="" width="188"><figcaption></figcaption></figure>

Flag: ara2022{r35t0r3\_c0rrupt\_f1l3}

### Perpustakaan ITS (10 pts)

Diberikan file bernama perpus.jpeg.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfC-nyBZw5xQBP5NNzn7INCBY0sJ1ha60ROr3KjYgtuVzGWoynFs4RMJiPFVZB1tPJ5OqZU9zWM5Rl2WagZed8E4EZ78Np7jDVSllNcx5P4zYqnGgWFz53bo3Rkn-lw50uFlBwrHTiTI134nxfdBo2RMHRGvZy5ceN9TEaWRvIsZaI5TNsojEI?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

Setelah melakukan pengecekan lewat exiftool ternyata ada XP comment yang apabila di-decode menjadi:

Kulit manggis kini ada extractnya! mastiin pass

Kebetulan karena ini adalah file .jpeg, salah satu tool steganography yang dapat digunakan adalah Steghide, dan Steghide memerlukan password. Oleh karena itu, dengan menggunakan pass ‘mastiin’ untuk Steghide, didapat file flag dan flag ditemukan.

Flag: ara2022{53l4m4t\_k4m03\_d4p4t\_fl4g}

### senja (10 pts)

Diberikan file bernama ini\_foto\_davin.jpg.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfOX0lGallxZGLWV7L_3BIMM-sz8qTLfD4SShU8OFEE6ta1Jv2Ydkdykc0P_n0MvWgLnYyJh_lm1BGc67Q6IQzt_hhYhAI2iDKLnw8gdnlZB5kAzMmx7PsS3eL21dBLTc2T-b7vetbv09td8ehLAPT5RCUwNPwK__1hpInXS_qjwoLXx4aBLrQ?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

Setelah melakukan exiftool pada file, ditemukan adanya sebuah link Google Drive.&#x20;

https://drive.google.com/drive/folders/1f-xtexUNxI0cieXt15PLZEEYCUz7npom?usp=sharing

Link Google Drive tersebut berisi beberapa file .wav, salah satunya adalah flag.wav. Melihat file tersebut melalui Sonic-visualizer, terlihat adanya link video YouTube.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcRaHDJqHil7BI5FSmCPmkMXLqUPJxKUMW93E0ar5w5DyDsZiVDT6AGX8k-FeVgjEoXJVG0BI92Q20H4zv_pwwPb_lMJwnt-PCjce5PDbh9tqM898NNmALo-e1T8QXheM4j-BmurxKSxa613VbX40jQZKrkLkGKbs9_H5ZHMjpTcaRV5F8iVw?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

Dalam video YouTube tersebut, terdapat flag yang dibacakan.

Flag: ara2022{1ni\_9amp4n9}

## Misc

### Song of Number (94 pts)&#x20;

Diberikan sebuah file ctf.zip yang berisi dua file: pic.jpg dan file.zip. file.zip terkunci, dan pada pic.jpg terlihat ada susunan angka-angka. Apabila dicek lewat exiftool, terdapat comment yang mengatakan bahwa:&#x20;

recamansaysthesequencehasbeenmodifiedfindthemistakeandtheywilllendyouthepassword

Searching di Google dikit, ternyata ada pola urutan angka yang bernama Recamán's Sequence. Melihat lagi ke gambar, ada beberapa angka yang tidak masuk ke dalam pola urutan tersebut. Apabila angka-angka tersebut dikumpulkan dan di-decode ke ASCII, akan didapat string ‘g0n3xt5t3p’ yang dapat digunakan untuk membuka file.zip. Di dalam file.zip ada file song.mp3. Awalnya saya bingung ini file mau diapakan, tetapi setelah mendengar beberapa suara distorted dari audionya saya mencoba untuk mengamati file ini melalui Sonic-visualizer, dan ternyata ketemu flagnya.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcxCp7vIfqaeUdic510ksuYnBtKTnb6rNFb4jWygb0MU2iTMTFwmZM4Z-wXpe83wdtP4rCXe6cXx4TYpQgjOTiKDNCvGMT3Wk1q7ZN0ThhbqeXlJtu0ob0VNieaozxWuE3P5POhjE5C_fepq8XTPvQj7sQqjU-mCqwrKNr9m_5J6mP8zROMKMc?key=smVvNwC0TJMlqHL-kwJjng" alt=""><figcaption></figcaption></figure>

Pada waktu saya mengerjakan, huruf ‘G’ nya harus diubah menjadi ‘g’ terlebih dahulu agar dapat diterima.

Flag: ara2022{fl4g\_1s\_n0t\_s0\_h1dd3n}

### isi form doang kok (100 pts)&#x20;

Di sini hanya perlu mengisi form feedback, lalu flag didapatkan.

Flag: ara2022{t3RIM4\_k4S1h}

\
\
