# sabeb64 (331 pts)

Diberikan service pada `nc 103.167.136.75 9988` dan source code dari servernya. Tapi pada source code tersebut, kode untuk fungsi encodenya tidak ada, jadi kita perlu menganalisis langsung dengan mencoba input-output pada service yang diberikan lalu membandingkannya dengan hasil dari base64 asli. Di sini saya mencoba memeriksa apa outputnya apabila diberikan 1 karakter, 2 karakter, dst.

| sabeb                                                                                                                                                                                                               | base64 aseli                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>00 -> AA=</p><p>0000 -> AAA</p><p>000000 -> AAAAA=</p><p>00000000 -> AAAAAA</p><p>0000000000 -> AAAAAAAA=</p><p><br></p><p>Jumlah karakter:</p><p>1 -> 3</p><p>2 -> 3</p><p>3 -> 6</p><p>4 -> 6</p><p>5 -> 9</p> | <p>00 -> AA==</p><p>0000 -> AAA=</p><p>000000 -> AAAA</p><p>00000000 -> AAAAAA==</p><p>0000000000 -> AAAAAAA=</p><p><br></p><p>Jumlah karakter:</p><p>1 -> 4</p><p>2 -> 4</p><p>3 -> 4</p><p>4 -> 8</p><p>5 -> 8</p> |

Dari sini terlihat bahwa pada sabeb, outputnya berupa chunk berisi 3 karakter dan bukannya 4. Pada base64 asli, angka 4 tersebut didapatkan dari rangkaian algoritma berikut, dengan contoh plaintext memiliki 2 karakter.

| Tahapan                                                                                                                                                        | Jumlah karakter |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| plaintext                                                                                                                                                      | 2               |
| padding supaya len(plaintext) menjadi kelipatan 3                                                                                                              | 3               |
| masing-masing karakter diubah menjadi binary 8-bit dan dikumpulkan dalam satu string panjang                                                                   | 3\*8 = 24       |
| string tersebut dipotong dengan setiap bagian masing-masing terdiri dari binary 6 digit, dan setiap bagian tersebut merepresentasikan 1 dari 64 jenis karakter | 24/6 = 4        |
| encoded                                                                                                                                                        | 4               |

Sementara itu untuk men-decode sabeb, kita bisa membuat tabel yang sama, dengan diketahui encoded text memiliki 3 karakter dan plaintext memiliki 2 karakter.

| Tahapan                                                                                                                                                                            | Jumlah karakter |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| encoded                                                                                                                                                                            | 3               |
| masing-masing karakter diubah kembali menjadi binary 6 digit dan dikumpulkan dalam satu string panjang                                                                             | 3\*6 = 18       |
| string tersebut kini dipotong bukan menjadi bagian berisikan 8 karakter, melainkan 9 karakter. masing-masing bagian tersebut kemudian merepresentasikan karakter dari plaintext    | 18/9 = 2        |
| apabila pada input/encoded text ada karakter “=” atau padding maka kita kurangi dengan banyaknya “=” pada input. Tapi pada kasus soal ini tidak ada, jadi langsung ke plaintextnya | 2               |
| plaintext                                                                                                                                                                          | 2               |

Jadi untuk men-decode sabeb kita hanya perlu mengubah panjang chunknya saja dari 8-bit menjadi 9-bit. Untuk solver saya memodifikasi kode dari [https://gist.github.com/trondhumbor/ce57c0c2816bb45a8fbb](https://gist.github.com/trondhumbor/ce57c0c2816bb45a8fbb).&#x20;

```python
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
secret = 'IZPJpSLBILJDKhCJJWJZZIxNIhMJxCKZDJ5MKRPJpVJBD'

def chunk(data, length):
    return [data[i:i+length] for i in range(0, len(data), length)]

def decode(data):
    override = data.count("=")
    data = data.replace("=", "A")
        
    binstring = ""
    for char in data:
        binstring += "{:0>6b}".format(charset.index(char))

    ninechunks = chunk(binstring, 9)

    outbytes = b""
    for chnk in ninechunks:
        outbytes += bytes([int(chnk, 2)])

    return outbytes # karena tidak ada padding, tidak perlu dipotong

msg = decode(secret)
print(msg)
```

Untuk mendapatkan flag, kita tinggal submit hasilnya ke server.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdtFcvuK-5b-pv289ar9hhZNGzaIwyxZZUji9M6Urzqsj_RYRxXzTDfQoulvLIUSRJORfcTC0B7cHKiYXciguf9yIteSb8NL-N2zbETAOwt7y0JRUx1uuLpnV6nUSJgyypmhqgVVslnEAdBZjQ3CV4PbwwlfePIKjA3niku4fFt16u6j8J_eQ?key=4MW_RSVrGpPtImkfMQF2Yw" alt=""><figcaption></figcaption></figure>

Flag: NCW22{jusT\_a\_littl3\_d1ff3r3nt\_C0ncept\_0f\_base\_6nam\_emp4t\_x1x1x1\_1be1ec3c3ea96b983a75e17dd3d44e8b}
