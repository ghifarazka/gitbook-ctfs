# Malicious

### Description

> Hi hacker..can you assemble me?
>
> Author: Fanshh
>
> Hint 1: Tidak ada data sensitif apapun yang dpt disembunyikan, atau mungkin ada?&#x20;
>
> Hint2: Hidden text on PDF

Diberikan file zip yang berisi 3 file: `file1.jpg`, `file2.png`, dan `file3.pdf`. Pada `file1.jpg`, tidak ada  hal menarik yang kita dapatkan dari membuka, mencari string, atau sebagainya.&#x20;

<figure><img src="../../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

Akan tetapi, ada kemungkinan bahwa file ini memiliki pesan yang disembunyikan menggunakan `steghide`.

<figure><img src="../../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

Sekarang, untuk `file3.pdf`, karena ada hint "hidden text", mungkin saja file pdf ini berasal dari docx lalu diubah ke pdf. Jika kita buka di Word atau software semacamnya, kita bisa memindahkan text maupun shape yang membentuk dokumen (jika ada). Karena saya menggunakan Linux, saya membukanya menggunakan LibreOffice.

<figure><img src="../../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (9) (1) (1).png" alt=""><figcaption></figcaption></figure>

Flag part 1 pun didapatkan. Nah, setelah kompetisi selesai, saya mendapatkan info bahwa jika dibuka di Ms Word, akan ada alert yang menunjukkan string yang merupakan password untuk `file1.jpg`. Karena saya membuka file pdf ini menggunakan Libre Office, alert tersebut tidak muncul. Akan tetapi, string tersebut masih bisa didapatkan dengan menggunakan `strings -n 10 file3.pdf`.

<figure><img src="../../../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>

Langsung saja saya gunakan untuk `file1.jpg`.  Flag part 3 pun didapatkan.

<figure><img src="../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

Terakhir, untuk `file2.png`. Di file png ini, ada beberapa header chunk yang tidak benar, karena itu kita perlu memperbaikinya.

<figure><img src="../../../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

Jika kita buka filenya sekarang, masih terdapat error "bad adaptive filter value". Salah satu penyebab error ini adalah dimensi PNG yang tidak sesuai. Sepertinya, dimensi asli gambar telah diganti. Oleh karena itu, kita perlu mencari dimensi yang benar, yakni yang jika dimasukkan ke chunk IHDR gambar, CRC32 nya akan sesuai dengan yang sudah ada di gambar yakni `0x6c20113a`.  Saya mengambil referensi dari [writeup ini](https://ctftime.org/writeup/23809) dan membuat kode solver berikut.

```python
from zlib import crc32

data = open("fixed2.png","rb").read()

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
		if hex(crc32(ihdr)) == "0x6c20113a":
			print(f"FOUND!!")
			print(f"width: {w}, height: {h}")
			print(f"width: {width.hex()}, height: {height.hex()}")
```

<figure><img src="../../../.gitbook/assets/image (13) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

Dengan ini, semua part dari flag telah didapatkan.

Flag: `TechnoFair11{Welc0m3_4_Gr3at_Hack3rrr_00}`
