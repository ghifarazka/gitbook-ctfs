# Downloader (244 pts)

Di sini kita diberikan file Quarantined.zip dan diminta menjawab beberapa pertanyaan yang bisa diverifikasi lewat service nc 103.167.136.75 1112.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXf3DzsxDNJwBuMgeVJdVPgH0w11AhYfzcL5IOjjW8CepcugchJij75JKCEwIbUD28qAh50VMHxHKLdEWtrVarg5vrWE-80TCOscEmpSe1pEoQKP2ZnYkmK19ZS8q2mpEQvj0n9xygAD6OOwpq8f7A6y8eOxj_iGxDaTH-2c4sqXeieGiCG44Kw?key=4MW_RSVrGpPtImkfMQF2Yw" alt=""><figcaption></figcaption></figure>

Ketika di unzip, isi dari file .zip tersebut adalah sebuah file shortcut MS Windows. Saya mencoba menjalankan command cat terhadap file tersebut untuk melihat isinya. Di dalamnya, tampak ada command Powershell untuk men-download sebuah file .exe dan menjalankannya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeI2uly-6DarQRpwdJKqmQBCSRl__2IkW6n2PnFGRfor5PVr-5AhD78XMgkecwxROHBEU0PkTQf8IVcUb6yprX9D5JYZGt82ELOBqhrDFGOa3Oji2CCMo3I-f-lM0cvl8MgsDvqfPLO1MxoLsAt5Jf3KB9KYPEabcIrzt9aDAfv4H89HK1Biw?key=4MW_RSVrGpPtImkfMQF2Yw" alt=""><figcaption></figcaption></figure>

Di sini kita dapat melihat ada baris yang menyebutkan ‘http://2filmes.com/svchost.exe’. Dari sini berarti kita telah mendapat jawaban untuk pertanyaan nomor 1 dan 2 yakni 2filmes dan svchost.exe. Untuk pertanyaan-pertanyaan berikutnya, saya mencoba memanfaatkan URL yang sudah diketahui untuk mencari jawabannya.&#x20;

Setelah beberapa lama mencari jawaban dan menggunakan berbagai tools, saya menemukan sebuah write-up yang cukup berguna: [https://ctftime.org/writeup/19137](https://ctftime.org/writeup/19137). Write-up ini mengarahkan pada tool [https://www.virustotal.com/](https://www.virustotal.com/).&#x20;

Memasukkan URL yang diketahui pada situs tersebut, saya berhasil mendapatkan IP-nya, yakni 104.37.35.127. Setelah itu saya menggunakan tool pada [https://www.iplocation.net/ip-lookup](https://www.iplocation.net/ip-lookup) untuk menemukan negara yang meluncurkan domain-nya, yaitu Denmark.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeo5nYNiPkUs5oMds2mw7eElCskz_RcVZjIf2yVvMfevNZIVfaX9Gz-6BYAWQ4prfImVnBNYjygLzGNUjpzeM8NoceKeDKTMzp1rFaWqit7Mws74PY82QOisI7K0D92Tq_gbrADsItzisKMwBQTA16tsxKMouY1fFGsXiAccDM1VahHDGiHhKY?key=4MW_RSVrGpPtImkfMQF2Yw" alt="" width="375"><figcaption></figcaption></figure>

Flag: NCW22{2filmes\_svchost.exe\_104.37.35.127\_Denmark}
