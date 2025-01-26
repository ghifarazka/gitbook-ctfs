# Fun Walk

### Description

> Fun walk I am a handyman. I was looking around the city. Looking for something interesting and a place to have lunch.
>
> The hint can be placed everywhere!!
>
> https://tinyurl.com/25jwd57t https://tinyurl.com/28x7dys6 Start from Broome St. and turn left to Wooster St. lang: en
>
> Author : Nando\_0

Kita diberikan dua file: citymap.jpg dan HINT.zip. HINT.zip apabila di-unzip akan menjadi HINT.rar yang dilindungi password.

Pada peta citymap di bawah ini, ada dua detail: Broome St. yang akan menjadi starting point, dan sebuah URL yang akan memberikan koordinat referensi pada google maps (didapatkan bahwa tempat ini ada di Manhattan, US).

| ![](https://lh7-us.googleusercontent.com/DcfXoZSk8XXX3615Nf7oSsJDrgvJ-EUjwAA29qNjb7gxTPxRLqWPvdXFzQHOOQJnBzTGey8XYtAJKGaWavyCa7p4vkYf6Gk-gnVCFyUgsiLaxuQp7QXu476v_DtPoG4_MPRmVk3o-bS6H2I9jJ9xqQk) | <img src="../../../.gitbook/assets/image (6) (1) (1) (1).png" alt="" data-size="original"> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |

Selama challenge ini, perlu diingat bahwa cara paling gamblang untuk menyimpan informasi di dalam gambar adalah metadata (exiftool) dan file (binwalk). Maka dari itu, setiap kali mendapat gambar, akan kita lakukan binwalk. Mulai dari citymap.jpg. Hasilnya, didapatkan arrow.jpeg. \


<figure><img src="https://lh7-us.googleusercontent.com/qMQyF4M8QrleGcT42oUsL--yV4B5BEdlGE5oWg0ItCCfffa0oYZy_FhVcv95Qel1d7nxYxetj8kW-K9_UvO-C692uJv7LmYoQLNL4LDTlWSwjNEwlIDdEgVRhH-hCSlp2DpW6X9DesCYMUomD91V7Xk" alt="" width="375"><figcaption></figcaption></figure>

Ini merupakan urutan belokan yang akan kita ambil ketika menelusuri peta, mulai dari starting point yang tertera pada peta. Pokoknya, pada akhirnya akan berhenti di sini:

<table data-header-hidden><thead><tr><th width="290"></th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/image (5) (1) (1) (1).png" alt="" data-size="original"></td><td><img src="https://lh7-us.googleusercontent.com/cmxe4c190pNITahOigf992Ev64oC7_RBjxXKHE8x4s_vMoUWyM85CAs661LsEHH9Q_Iqtfwe3tWy6Blmw2DcAoTuLj6NVRjbot-Ltk7PEEexOx4w_j1JS2YnI2q_ufIQyQKhPG5lRt88eNWoZXGUhqc" alt=""></td></tr></tbody></table>

Deskripsi menyebutkan “lunch”, sehingga kita hendak mencari tempat makan di perempatan tersebut. Jika kita melakukan binwalk pada Arrow.jpg, kita akan mendapatkan file “password.jpg” berisikan bendera Belanda yang menegaskan nama dari restoran yang kita cari. Tentunya, nama restoran ini menjadi password untuk file HINT.rar yang tadi kita miliki.

HINT.rar berisikan Hint.jpg yang isinya adalah sebagai berikut. Berdasarkan petunjuk dari author, ini maksudnya adalah “79 Pine Street”.

| ![](https://lh7-us.googleusercontent.com/swnluSOoA_SjoNTNHgOXhdTygx2AorE5YwP4a7ySZ7OZ2aZhHnufuv40tpI1pFx950Aht_TJxUJ6MTxIPc28e-kIYN-Zse0xEK8n_4n5OJ_9BVQnr4W23o4TRkkvikjQKOaiLI77FsiZyxV1OdMerNo) | <img src="../../../.gitbook/assets/image (7) (1) (1) (1).png" alt="" data-size="original"> | <img src="../../../.gitbook/assets/image (8) (1) (1) (1).png" alt="" data-size="original"> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |

Berikutnya, lagi-lagi kita lakukan binwalk terhadap Hint.jpg, dan didapatkan Flag.jpg berikut.

<figure><img src="https://lh7-us.googleusercontent.com/Y2omnwHpC03ji0XD6DxShet0gDu4oVVqk09HO-wAMnduS6ajHvenaVveZvnYyHi1TPHNaTy8WwAQUzsdXmlYfFELP4eUbmp4aoB7g36yFKAhW6fyMMas3qweMTSlaobTpOOzMYKwt4f_8MUgu705a2I" alt="" width="188"><figcaption></figcaption></figure>

Link yang diberikan akan mengarahkan kita ke google street view, tapi belum selesai sampai di situ. Kita harus mencari 79 Pine Street lewat street view tersebut. Sampailah kita pada tujuan akhir.

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Gambar pada Flag.jpg (dan petunjuk dari author) memberikan informasi bahwa flag dibagi menjadi 3 bagian sesuai emoji pada gambar (tele, star, dan locksmiths).

Flag: `GKSK#8{Tele_Star_Locksmiths}`
