# eftipi

### Description

> Jangan sebar rahasiaku!!!
>
> Author : millkywaay

Diberikan file capture `chall.pcapng`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdHI-vT8dFeB1NOR81kvpbXOEkPNJWTwL3rfQH5B-tGLPZBRqNiWdctik81WRvBUAfPQzz2Fxg8D-bZ2rqachbtOG9mMt42ZAfijByXWEj04CuDFFumR_JjD6kcJYl_dIC2KUpp3T_zD9zcDcy3Z2MEmNx5?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Judul soal ini merujuk pada salah satu protokol yaitu FTP atau File Transfer Protocol. Oleh karena itu, saya langsung memfilter paket-paket yang memiliki protokol FTP.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcr-3IlP5BO-PdER4sfs1LHSJsiR1RMWdeTUWJjWm48lxEtuJN2sNI5sUukEWTOahF-lvKhlCK0ShIF20ndRLObGbLVVPKd7W4acLkwFQvWTUNSFMk6dVlMXJ_oBSwDZatMP7-auMzukVNk8vp5EiAJ6Mqu?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Setelah membaca-baca paket yang ada, diketahui bahwa seseorang telah melakukan pengiriman 3 file menggunakan FTP, yakni `secret.txt.lst`, `secret2.png`, dan `secret3.zip`. Jika paket dengan protokol FTP berisi log dari pengiriman file menggunakan FTP, data dari file-nya sendiri ada pada FTP-DATA.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXflt2bLEYdcB3N9UfZBly7zFGoTAq5cBDh2n5mGqd54bffMaxjs6r3IzhG61-hQQjQCApyaXcSTqdIEsDDFL9nL09Hnr2FhXduwCVSbw8IABw304UVhHjcfIuSJl0-twpRBr3fANaEkAPZtWiyyJAkEopl6?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Berdasarkan petunjuk dari [artikel ini](https://adrinanthony.wordpress.com/2019/07/19/how-to-extract-http-and-ftp-files-from-wireshark-pcap-file/), cara menyimpan file FTP dari wireshark adalah dengan follow stream, ubah ke raw, lalu “save as”.

File pertama merupakan file text yang berisikan [wordlist ini](https://github.com/geovedi/indonesian-wordlist/blob/master/00-indonesian-wordlist.lst), namun dengan kelebihan satu kata. Kata tersebut saya temukan dengan membandingkan wordlist asli dengan `secret.txt.lst` menggunakan kode dibawah. Satu kata lebih tersebut adalah “hilirasi”.

```python
file1 = open("secret.txt.lst","r").readlines()
file2 = open("geovedi.txt","r").readlines()

for l1, l2 in zip(file1, file2):
	if l1 == l2:
		continue
	else:
		print(l1)
		print(l2)
		break
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdHJQMLhfl8A7kOFwA59TktBX_VSt2gg6VCroXbP6_AzeGJxWDOvWSpFBnSGKXSkBpHi7Vt_pRgaGAiee4vBR9L_eYgxf5bgqeSvrmvliNFsvhwNkOAcGSYME0s3RhYqj_ZrzpPTAH5bo0KxkCDR4F4XGSz?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

File kedua hanya berisikan clue.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXd5LfRuXEKqiegCrD57QvYr_CKfp_OSNu8jWXErR4BjWSR9rx3KkFs3x9JiFBFfoJM4aeysII65c3Dms2lfZLDVe3euhBbIOSF4-Ln6j4zdGcN478-6DMWPb1ncN9Z1sez_xcyW4JMTpfGdfGBW5eUxOJJK?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

File ketiga merupakan file zip yang dienkripsi. Kita bisa asumsikan kata “hilirasi” tadi sebagai password dari file zip ini.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXePeE8i4UoD2ed8BWNkIcW-zUP7NnQ17TmfrfbTAO8qX72b7Q4AEsz3dqdFFWbcuCQWuoJnkl9XpcJEKAxpJoYXmBbU6yfsbkdryzj0NmfaQKoIbLsh8EH9WqlEVj5iJ7iHXtqDW8iJRToxS3vetX80zr9W?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Sayang sekali, kita tidak bisa melakukan `unzip` pada file ini.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcS7HNyTelvdv3mYykWYsUxe0dSQ9W4bmpt0lkM72weI9z_6W_pZ6AmFn3eTbnqpkSSRSpdKfFp0QUhEQOP_b6_ZM2PTC-iqYKYZwKL3pNO5ILYU7GlRDcnoe11ghnUn-9Rxlt3o1GJtnvRqhPtGx5IIjJk?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Alternatif lainnya adalah menggunakan GUI Linux lalu memasukkan passwordnya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdZCfFoeCv0CLZLJ50qYLvKVcZyymgtOndGeu8-h3GGXMdqwMOdG0sGkK8BKzk2bhYz7yBX3_JHgrS81TfWYPFAEwPLmV1MjaErPlEvO9wuxpHUVEdPAEXLVRr0zP3i4SYznoLVtNF82IPhEmLaIOvYs_6l?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Di dalam file zip ini, ada file “`flag`” yang jika dibuka menggunakan hex editor tampak seperti berikut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcJgiEYZqJLcvn5vvX5PA7xyMiQ4SxpAdvD1KjMPvZVXIVwm1oDIUj1LWGKYuF6IK-R9ek29nQLVEjtDkIqlUVuDrVPNwC_4aHgRfwy16kD43AWVubLpxaFeLSiCenFWJE5uqnVs4iLCZ60Tat4jCRNdUq0?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Di sini ada “DNEI” yang mungkin saja berasal dari “IEND”, header chunk yang ada di akhir file PNG. Oleh karena itu, dapat diasumsikan bahwa file ini merupukan file PNG yang memiliki urutan bytes terbalik. Berikut adalah kode yang saya gunakan untuk membalik bytes dari file ini.

```python
with open("flag", 'rb') as file:
	file_bytes = bytearray(file.read())

file_bytes = file_bytes[::-1]

with open("result.png", 'wb') as file:
	file.write(file_bytes)
```

File PNG pun berhasil di-recover.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc9XZqIpBE48FwVboSXj2s3QZOdlVfaHoyESWKl-Skt4STpttftxCD7LTOJdHMET96zbdD10yFrc_6Y4jcCx8sgKAD_7oFYPe8coWe6zB2RV6DqAj4iKMHMPBecKCrhybD1V2N072UrT6bwWnbaqE5C-_Id?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{B3_c4R3FuLL_w1tH_sN1ff3r}`
