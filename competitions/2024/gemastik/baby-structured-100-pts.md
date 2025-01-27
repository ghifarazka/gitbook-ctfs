# Baby Structured (100 pts)

> my friend sent me a picture, but she say its got 'cropped'. can you recover it?
>
> Author: blacosuru

Kita diberikan sebuah file PNG yang bernama `zhezhi_______`. File ini tidak bisa dibuka karena ada ‘CRC error’.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc8Hv_MHKNP3jy1bntw17aJ4F3COaRerX1sBTY2hR8L2wdw-U9byVsOmySVD2zvXRTYXhvOOCSkOMGXelPVrvB3NC5rEoh2KZQdNwUaRHbxBiYO-j6yhBpmMpe-j1i-h_w6KMypJbgRvwIZfzH3_bOWn0c?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Kita bisa menggunakan tool seperti [nayuki.io](https://www.nayuki.io/page/png-file-chunk-inspector) untuk memeriksa apa yang terjadi di file PNG ini. Rupanya memang benar, pada chunk IHDR CRC32-nya salah.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRW1FSckbIOCsPwftID9dc5811jhWNbj4lWKJg_rVht7Ho8OFNwTbZo7a7JACHZd5xHENx_MUlE9-4FLlo-cV34vuNd3zB4y1K_8ntMolHHRBpLa7WTqb1AdunP1o9pEeK1W1iKpR7ltZcumQZG8zHI0s?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Di sini ada dua kemungkinan, yakni memang CRC32-nya yang corrupt dan harus dibenarkan, atau ada metadata yang diubah (misalnya dimensi gambar) sehingga CRC32 yang ada menjadi tidak sesuai. Karena di deskripsi soal ada clue bahwa gambarnya di-’crop’, maka kemungkinan terbesarnya adalah dimensi gambar ini telah diubah.

Maka dari itu, tugas kita adalah mencari dimensi yang benar. Kode di bawah ini akan mem-brute force semua kemungkinan dimensi dan menghitung nilai CRC32-nya. Jika sama dengan yang ada pada file gambar, maka itulah dimensi yang benar.

```python
from zlib import crc32

data = open("zhezhi_______","rb").read()

ihdr_index = 12
ihdr_size = int.from_bytes(bytearray(data[ihdr_index-4:ihdr_index]), byteorder="big")

ihdr = bytearray(data[ihdr_index:ihdr_index+ihdr_size+4]) 	

# IHDR: 4 bytes for size, 4 bytes 'IHDR', 13 bytes content, 4 bytes CRC32
# CRC32 calculates 4 bytes of 'IHDR' + 13 bytes of content

# offset with respect to IHDR chunk
w_offset = 4
h_offset = 8

for w in range(1,2000):
	width = bytearray(w.to_bytes(4,"big"))
	for h in range(1,2000):
		height = bytearray(h.to_bytes(4,"big"))
		ihdr[w_offset:w_offset+4] = width
		ihdr[h_offset:h_offset+4] = height
		if hex(crc32(ihdr)) == "0xa5ae0f88":
			print(f"FOUND!!")
			print(f"width: {w}, height: {h}")
			print(f"width: {width.hex()}, height: {height.hex()}")
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdZMbFapTTshqGuhPsjGBb1Cgyc6Gjav0WRnCgcVBWHryBhTGtrnvjTITr2B0tD20VdAAfU15oLzPtlMo8ap5V6dPEfcybp_QMRF6HAoBN8p6v-LSh1_8DjIP5tuybj3klKV0s4E8fO71AQmH4ygtq6LfA?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Karena sudah didapatkan, kita bisa langsung menggantinya menggunakan [hex editor](https://hexed.it/).

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKxPWql9K6afgUP3Z3LP-3p79pAfpKDHQd8Froz6l3NwsT5S2XPNjO66_zJzEultVRI10vDlDaI6APaU_633RlQzBc1W7AHeQcGlGHR1IvSLn8gaeGs61TU48VI8EcJ93npV8BfAqTY5V6BCiHOedX5_g?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Setelahnya, gambar pun bisa dibuka.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdkLOWtrCsF6xyGen8-xI7VaDv4K6g_5M4C7J_SDtF-55OCIccUNM_msSM9sr0V749e5iH-NQ7W10ahsTaEe6bARbNTJ4lhTZ3mr5EDFzIaRmN7uOQ0UctWOH2BZhWwV0fBsPcF_ZIoF6dR3kyZR3yvJFPO?key=tJbezAN_j6YxD_OtpLAq3g" alt=""><figcaption></figcaption></figure>

Flag: `gemastik{g0t_cr0pped_by_structur3}`
