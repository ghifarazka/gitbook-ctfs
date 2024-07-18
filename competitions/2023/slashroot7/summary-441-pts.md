# Summary (441 pts)

### Deskripsi

> sum it up baby
>
> nc 103.152.242.228 1011
>
> Author : MockingJay

Pada soal ini kita diberikan sebuah service dan source code-nya yakni `chall.py`.

```python
#! /usr/bin/python3

import hashlib
import subprocess
from binascii import hexlify

wl_cmd = b'echo lol'
wl_hash = hashlib.sha1(wl_cmd).digest()[:3]

def main():
    while True:
        print('\nWelcome to my secret service, have fun!\n')
        input_cmd = input('> ').encode('latin1')
        
        if input_cmd == b'exit':
            print('Bye-Bye 👋👋👋')
            exit()
        
        if hashlib.sha1(input_cmd).digest()[:3] != wl_hash:
            print(f'Unknown command, try this command instead : {wl_cmd.decode("latin1")}')
            continue

        if b'flag.txt' in input_cmd:
            print(f'bruh use another method h3h3h3h3')

        try:
            res = subprocess.check_output(['/bin/bash', '-c', input_cmd])
            print(res.decode())            
        except subprocess.CalledProcessError as e:
            print(f'Command returned non-zero exit status {e.returncode}')

if __name__ == '__main__':
    main()
```

Jadi intinya begini: Kita bisa memasukkan command bash melalui input pada service Syaratnya, 3 byte pertama dari hasil hash input kita harus sama dengan 3 byte pertama dari hasil hash b”echo lol” Selain itu, input kita tidak boleh mengandung “flag.txt” Hash yang digunakan adalah sha1 (ini tidak terlalu relevan dengan penyelesaian dari soal)

Di sini vuln-nya adalah pengecekan hasil hash yang hanya pada 3 byte pertama. Apabila kita mencoba memasukkan input berbeda sebanyak lebih dari 256^3 maka kemungkinan terjadi collision akan sangat tinggi (adapun karena di sini kita hanya bisa menggunakan karakter printable, jadi saya menggunakan 4 byte untuk slot karakter random, sehingga ada 100^4 kemungkinan). Maka dari itu, kita buat saja versi input yang berbeda-beda, tapi tujuan command-nya sama, yaitu membaca `flag.txt`.

Oh iya, karena command yang kita inputkan tidak boleh ada “flag.txt”-nya, maka diperlukan workaround. Setelah beberapa trial and error, saya akhirnya menggunakan `cat *; echo “{hal random}”`.

Untuk mencoba segala kemungkinan tersebut dengan “hal random”, saya menggunakan script berikut.

```python
import hashlib
from string import printable

test = hashlib.sha1(b"echo lol").digest()[:3]

base_cmd = 'cat *; echo "'


for i in printable:
	for j in printable:
		for k in printable:
			for l in printable:
				check = hashlib.sha1((base_cmd + i + j + k + l + '"').encode()).digest()[:3]
				print(base_cmd + i + j + k + l + '"')
				if check == test:
					print("FOUND!")
					print(check)
					exit(0)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfkRSTmtYrJZOE3kS1mA5g6Jx4GS26EfBhrbAXPIFag-9J9w_jhSzDbJsIxeDMK7QHStANzgE8KBKKpEIlnAIMo24_y7PgbC6ervkeVBtB96BczfDvPyWQvH1BkFNXj7LFx_fKEsp5X6yHWoJ6MvjTeNLI?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Didapat `cat *; echo “8R=0”`. Memasukkannya ke service, kita mendapat isi dari semua file yang ada di directory server, termasuk `flag.txt`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcKTl4Ucm5TdUmlKeH08Qity0Gigp6Zx6nLVYoVFy8SCUQ0zRaxQA1JZ8OAJhq1iihxqFPXelmESzo2DtNfd8m-TtZwyjKdxEjO4jzcapI-cz9zDCMAGziulij8_X1DwL7zkiJjmhU3xG70AlM80o_p_QLH?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcLRg0KlDaamK7Pchtx3-MqZxsSnb1VXQIAaHx72PeL3tOZGKYaU5WSXaUT9Pf1NyR8mF0o8q5b6Z2_8ZPhYhhfL9FXe6F-LYq82sUREJBpRvQ12jaFTTaAQvL8smtr95lDGBQUekkIMEXDWHzMwyF3uEKj?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Flag: `slashroot7{easy_crypt0_chall_f0r_ez_first_chall}`
