# Not Too Random

Diberikan ciphertext serta program yang menghasilkan ciphertext tersebut. Program ditulis dalam bahasa C, dan kita hanya diberikan fungsi `main()` nya serta executable-nya saja. Executable-nya itu sendiri merupakan program utuh dari kode yang diberikan andaikan lengkap (tidak cuma fungsi `main()` saja). Oke, pertama-tama kita lihat kode `main()` yang diberikan.

```python
int main() {
    char flag[] = "REDACTED";
    int len = sizeof(flag) - 1;
    shuffle(flag, len);

    if (len % 8 == 0) {
        char A[(len / 4) + 1], B[(len / 4) + 1], C[(len / 4) + 1], D[(len / 4) + 1];
        separate(flag, A, B, C, D, len);

        int lenA = sizeof(A) - 1;
        int lenB = sizeof(B) - 1;
        int lenC = sizeof(C) - 1;
        int lenD = sizeof(D) - 1;

        shift(A, lenA, 2);
        shift(B, lenB, 1);
        shift(C, lenC, -2);
        shift(D, lenD, 3);

        int finallen = lenA + lenB + lenC + lenD;

        char finalflag[finallen + 1];
        merging(A, B, C, D, lenA, lenB, lenC, lenD, finalflag, finallen);

        printf("\nfinal flagnya: ");
        for (int i = 0; i < finallen; i++) {
            printf("%c", finalflag[i]);
        }
    } else {
        printf("Masukan kelipatan kalimat dengan jumlah kelipatan 8");
    }
    return 0;
}
```

Intinya, algoritma-nya adalah sebagai berikut. Sebuah input/flag dimasukkan ke dalam fungsi `shuffle()`, lalu dipisah ke substring A, B, C, D dengan fungsi `separate()`, kemudian masing2 substring di-`shift()` dengan panjang shift tertentu, dan akhirnya A, B, C, D kembali disatukan dengan fungsi `merge()`.

Karena kita tidak tahu definisi dari fungsi `shuffle()`, `separate()`, dan `shift()`, kita cari tahu dulu cara kerjanya dengan melakukan reverse engineering pada executable yang diberikan.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeDdqNoIF_RdjozPL-cJG8KLw6oMt4yVNjVWOc4TgDpn-iv2p0cLYCeg1L4vWxIEvyWtrL4EJvyaM89x2QNefR_ORvD0ax6Np7t--Bi9KVhzytg90JpUwKv2vaREF3cpWJhwkMhon_DJn7pTm1CC3SUNlk6dANlvgmmnj2MY6PzzgrwN9shZZU?key=EjfUZ-OPjpKiC6ETtcwPSQ" alt=""><figcaption></figcaption></figure>

Rupanya, cara kerja masing-masing fungsi adalah sebagai berikut.

| shuffle()  | Membalik urutan karakter pada string                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| separate() | Kunjungi setiap substring A-D secara bolak-balik, ambil satu karakter pertama, lalu di iterasi berikutnya ambil karakter kedua, dst \[sulit dijelaskan, sebaiknya lihat contoh] |
| shift()    | Intinya menggeser value ASCII dari setiap karakter pada substring sebanyak key ditambah angka tertentu tergantung ada di substring apa.                                         |

Sebagai contoh, ini yang akan terjadi jika flagnya adalah “REDACTED”.

| Normal     | REDACTED                  |
| ---------- | ------------------------- |
| shuffle()  | DETCADER                  |
| separate() | \['DR', 'EE', 'TD', 'CA'] |
| shift()    | \['BO', 'DC', 'VE', '@='] |

Kode pada shift (encode):

```python
def shift(s, key):

	i = 0
	j = 1
	k = 2
	z = 3

	while (i < len(s)):
		s = s[:i] + chr(ord(s[i]) - key) + s[i+1:]
		i += 4
	while (j < len(s)):
		s = s[:j] + chr(ord(s[j]) - key - 1) + s[j+1:]
		j += 4
	while (k < len(s)):
		s = s[:k] + chr(ord(s[k]) - key + 1) + s[k+1:]
		k += 4
	while (z < len(s)):
		s = s[:z] + chr(ord(s[z]) - key + 2) + s[z+1:]
		z += 4

	return s
```

Untuk meng-decode flag, maka algoritmanya tinggal kita balik saja. Termasuk pada fungsi shift(), algoritmanya juga kita balik (dari pengurangan jadi penjumlahan, begitu pula sebaliknya). Berikut ini adalah kode solvernya.

```python
def shift_decode(s, key):

	i = 0
	j = 1
	k = 2
	z = 3

	while (i < len(s)):
		s = s[:i] + chr(ord(s[i]) + key) + s[i+1:]
		i += 4
	while (j < len(s)):
		s = s[:j] + chr(ord(s[j]) + key + 1) + s[j+1:]
		j += 4
	while (k < len(s)):
		s = s[:k] + chr(ord(s[k]) + key - 1) + s[k+1:]
		# s += chr(ord(s[k]) - key + 1)
		k += 4
	while (z < len(s)):
		s = s[:z] + chr(ord(s[z]) + key - 2) + s[z+1:]
		# s += chr(ord(s[z]) - key + 2)
		z += 4

	return s

cipher = "{-mC]x2Jcr_slK2Dt`3}w43X1dro.`0E"

length = len(cipher)//4
cipher = [cipher[i:i+length] for i in range(0, len(cipher), length)]

plain = [] 

plain.append(shift_decode(cipher[0], 2))
plain.append(shift_decode(cipher[1], 1))
plain.append(shift_decode(cipher[2], -2))
plain.append(shift_decode(cipher[3], 3))

print(plain)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXe3OOZOEPuxZYTr8ylP6eaWGCvkadEsl7aEi52BdI_E43pD9u4NTXTStU2ov_zYTa9fdZrZ3rP57yjY8ah2G_q_ptfiy-_H6Oyy9ataM3hj3d0rhAByLSiM9H3Cqz5fy6rNmpneS0zPmxHQes7qiURMiCe2D8qtuaaaiUpyaj3okJ32HC5o_BE?key=EjfUZ-OPjpKiC6ETtcwPSQ" alt=""><figcaption></figcaption></figure>

Karena tadi waktunya tidak cukup, saya tidak sempat membuat kode untuk me-reverse algoritma fungsi `separate()` dan `shuffle()`. Tapi itu bisa dilakukan secara manual dengan membaca karakter terakhir dari substring pertama (J), lalu karakter terakhir dari substring kedua (C) dan seterusnya, seperti yang telah saya jelaskan sebelumnya.&#x20;

Flag: `JCTF2023{M3d1um_Crypt0_n0t_h4rd}`

\
