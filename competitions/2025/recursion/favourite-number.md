# Favourite Number

Kita diberikan sebuah file yang _katanya_ file gambar.

Melihat file tersebut menggunakan hex editor, tampak bahwa strukturnya sangat mirip dengan PNG.&#x20;

<figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

Jika dipikir-pikir, kemungkinan yang terjadi adalah masing-masing byte pada file PNG ini telah di-XOR dengan suatu byte (merujuk pada judul soal, favourite number). Untuk mengujinya, coba kita XOR-kan `PNG` dengan `YGN`.

<figure><img src="../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

Tampak bahwa ketiga byte `YGN` sama-sama telah di-XOR dengan byte yang sama, yakni `\x09`. Maka dari itu, tinggal kita balikkan saja. Berikut adalah kode solvernya.

```python
file = open("ciro", "rb").read()
new = b""
key = 9

for b in file:
	new += (key ^ b).to_bytes()

fixed = open("flag.png", "wb")
fixed.write(new)
print("DONE")
```

Berikut adalah file yang dihasilkan.

<figure><img src="../../../.gitbook/assets/flag.png" alt="" width="250"><figcaption></figcaption></figure>

Masih belum menampilkan flag, tetapi, saya curigai bahwa flag disembunyikan di salah satu plane warna. Untuk memeriksanya, kita bisa gunakan `stegsolve`.

<figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

Nah, barulah flag dapat dibaca.

Flag: `RECURSION{09_1s_my_f4v0ur1t3_numb3r}`
