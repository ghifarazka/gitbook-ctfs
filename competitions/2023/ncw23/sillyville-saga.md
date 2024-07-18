# Sillyville Saga

### Deskripsi

> Chopi is a famous short story writer in Teruland. One day, Chopi wanted to innovate by writing a short story but printed using a custom font that he created himself. However, his font accidentally got scrambled with another language's font...
>
> Wrap the flag with NCW23{.\*}
>
> Author: cipichop

Di sini kita diberikan file `SillyvilleSaga.xps`. Tampilannya adalah sebagai berikut. Ada sebuah teks yang menggunakan suatu font style Jepang yang terdiri dari huruf Jepang dan huruf latin.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfNdRo3wci5VvsZ2VCl8nhPLesCHxsxvUmfFmgFVGocATvjNqKMshOq0WcoicnQbHI4uVcqDGYMDAgg9OAKO4jcMmcF9XQJLDHLsOKBI6CPvNLD5j_4zNliE2SKIzn7g07EJcMvNldBm-lKskYwcjI5i4c?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

`xps` sendiri merupakan file dokumen, dan karena biasanya document file == `.zip` file, jadi file xps tadi bisa kita unzip. Di dalam file ini, apabila kita menelusuri ke “`/Documents/1/Pages`” kita akan menemukan file yang berisi konten dari halaman, dalam format XML.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXJiyMcnoGOs9hUmeRl97qztvI4XslkMin9PQ30-AsH9t5MPthFdYZDAJ6Ibs9N7Pct8gllK4bOiBBLLQcwfYdaliPcm8EegFQtnwN5wahYuqhoy0PKKf1AkC_AbRs1spM5Hzv0T45y_5ILyoI1OUIMms?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdSTs0uY_xcsYKEbNPPdt5-8yy8yk793YY3IP7fhHoFZj4dB1AoIAHo0RCMQyYhqm838SzhZoeDgzSqGZnJ0B-I7bIkYdse3c5oLch2qGF9GvzKWWEubc2BQb7hVSCA140giSouH75QcvJ8gs645H-wN05G?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Menariknya, pada XML tersebut, terdapat atribut “`UnicodeString`”. Artinya, bisa saja kita menuliskan apapun di situ, dan hasilnya akan muncul pada dokumen, tentunya dengan font aneh yang dipakai dalam dokumen ini.

Merujuk kembali pada isi dari dokumen `.xps` tadi, kita diminta untuk menuliskan A-Z menggunakan font tersebut.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdPaFMrZct3jYLndyJHPYYa7HqIWMX4K9Er57mkgSR90GSSPSzgDg2DK5wGSfOGA0ADxLwlxp8TKqRCzsMFjMlKE4zNnkl_7h7ezkYH-Z3JUrFbxh9-k9eLKXWTznAbh1gK4nbqvlKRDYz4Jpmn60iltO8-?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Maka dari itu saya pertama-tama mencoba secara naif untuk menuliskan A-Z pada atribut “`UnicodeString`”. Selain itu juga saya warnai untuk membedakan dari yang lain hehe.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc8UG8U-iWcTNODgLwSzXpQ2XyEgR7gtQfVR7cq_0Udq738W6E-IqzbXyTpFoUnroHYgYlIiOPHaqXCLFC0zgOgsLyx2dBzb55nCu1GIMihmepA3p7TGcPYjFsoSCzZRNgjfHpR7xtH4rjgef2drUZkMMD3?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Hasilnya adalah sebagai berikut. Rupanya, suatu karakter tidak direpresentasikan sebagai karakter yang sama pada font ini. Misalnya A menjadi Y, begitu seterusnya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHB1WptJ-dzBt26k7C01MWlgYuK3EJO69qU3suKUX-WYiTwIr_RQmnjSfuoRbSh955bS42N9e9wuINY19Mazg6LtBTKiRp_EJemkreQxsuIdeIFo5BZ6eZVVXtQsJxeF8_QWf2UhP_OQP_hKt5-7iTD2mt?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Oleh karena itu, kemudian saya mencoba bagaimana hasilnya untuk karakter-karakter lainnya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAfkjQdJKjjtiH137GOuhDNIfXeRlrgmHyrUJ79a9_mr_9WyGJWxaCMtuqfMbcTUbe4_sE8Y1x6934KYtQYSPDKepcG1k77I0yWUVAdTw-m64m4GMM5QKYdOlLKV6MVWXAnkqoBQcjYVXDWudLWUMZHMrP?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAO_-4Jm1wS_yr7NN9Dx4Kz6F3cxzz4t16ciFwdX3lQLXGApuqfrxv8t0uEc0c7uH5-VJe9fQkOTTN4eMA516W6pu5JD6nK-sXUzLMsze0JUd9Ri7uU8lGgpGQzel62Wrkb6u8s32vurXTbcFgWPYf8Jc?key=BAXu6xjRjwtQCs9M05USOQ" alt=""><figcaption></figcaption></figure>

Ketika dirasa sudah cukup, saya mencoba menuliskan karakter-karakter yang menghasilkan A-Z secara berurutan. Berikut adalah hasil lengkapnya.

| <p>A F</p><p>B 0</p><p>C n</p><p>D T</p><p>E -</p><p>F s</p> | <p>G t</p><p>H y</p><p>I L</p><p>J e</p><p>K _</p><p><br></p> | <p>L N</p><p>M o</p><p>N =</p><p>O p</p><p>P r</p><p><br></p> | <p>Q O</p><p>R b</p><p>S l</p><p>T 3</p><p>U m</p><p><br></p> | <p>V ~</p><p>W Y</p><p>X a</p><p>Y A</p><p>Z !</p><p><br></p> |
| ------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |

Flag: `NCW23{F0nT-styLe_No=prObl3m~YaA!}`
