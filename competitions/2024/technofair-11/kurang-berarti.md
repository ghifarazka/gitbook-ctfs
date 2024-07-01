# kurang berarti

### Description

> help me to find the hidden message in this photo
>
> Author: H4NN

Diberikan `chall.jpg` dan `enc.py`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdibwLlOnuJsi17otKaXX1YFs76l2fv3jiF2fJ8RhBf9QTtoOYA-L6RWCHW0-eK6TT5ucf_-tN9a_i8K0J5Ktf2bwalyObn1Tj9OccQb-13zMOUEiKufNb6lC73uOtQTYn0OMRLXK2FZLu-jeM1Sqw8N1Q?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Berikut adalah `enc.py` yang sudah saya annotate.

```python
def insert_plaintext_into_image(input_file, output_file, plaintext, offset):
    
    #  read file
    with open(input_file, 'rb') as file:
        file_bytes = bytearray(file.read())
    
    # change plaintext to binary
    plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext)
    
    plaintext_index = 0
    plaintext_length = len(plaintext_binary)

    # start from an offset
    for i in range(offset, len(file_bytes)):
        if plaintext_index < plaintext_length:
            original_byte = file_bytes[i]
            plaintext_bit = int(plaintext_binary[plaintext_index])

            # update the file byte with these
            new_byte = (original_byte & 0xFE) | plaintext_bit
            file_bytes[i] = new_byte
            plaintext_index += 1
        else:
            break
    
    with open(output_file, 'wb') as file:
        file.write(file_bytes)
    
    print(f"{output_file}")

input_file = ''
output_file = 'chall.jpg'
plaintext = "flag"
offset = 0x00000D00
insert_plaintext_into_image(input_file, output_file, plaintext, offset)
```

Pada `chall.jpg`, telah ditaruh plaintext berupa binary string ke dalam data bytes dari gambar. Saya mencoba melakukan eksplorasi untuk memahami cara penaruhan plaintext tersebut.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcNE6tuMyuPXh9nLP85iyPEM8Qc8z6VmYkgLPIeVunQH193LdLCQc89fXeQHfWtmxKFUbFL-IpuhIHvX4EYpJGdbJpWa2K6aifB1alU1XPwm8eSq7EmE8WmZhs7Oa_toqXDCo60msZ4Fq0hdDim__xJYlM?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Di sini, `& 0xFE` akan membulatkan suatu bilangan ke bilangan genap sebelumnya. Setelah itu, melakukan `| 1` pada hasilnya sama seperti menambahkan nilai hasilnya dengan 1 (atau 0 jika `| 0`). Intinya, dapat ditarik kesimpulan bahwa jika suatu byte gambar ganjil, maka bit binary dari plaintext nya adalah ‘1’, sedangkan jika byte-nya genap maka ‘0’.

Karena panjang flag tidak diketahui, saya asumsikan saja panjang binary stringnya terdiri dari 800 bit.

```python
with open("chall.jpg", 'rb') as file:
	file_bytes = bytearray(file.read())

offset = 0x00000D00

result_bin = ""

print("skjhagd")
# start from an offset
for i in range(offset, len(file_bytes)):
	if i == 800:
		break
	if (file_bytes[i] % 2) == 0:
		result_bin += '0'
	else:
		result_bin += '1'

print(result_bin)
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcwjYffPaYNLaNtBzF9hJysdyv53fkchKABVuWEDSXWx8OTeZ3H652w0UEk4ibqt1XMZJCWDOm6gh3ivwVADbGBb2s_S8ppSsfX1M-yzMbZaO6aW7DIKd_yliI5UaQChBe5Jaql9MaeMq0iUmzcph3tDBU?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Hasil binarynya kita tinggal decode saja menggunakan `Cyberchef`.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcWBMaX52rESLU3q5Hhk6yDpStzL4pUXoLKCxh1J_GMFWC3LUhggpQlJez5Iq0g0mOh86pUQbSrsADyxBVmY9zIz5MG1FOB_JBnUSaQ6dFiXLi-nwaFXUHOZSkzJ02DCLUi9rmMnzXXgTekDQLA_mbS0nKd?key=bKZVH89yO64ULuuh4491eA" alt=""><figcaption></figcaption></figure>

Flag: `TechnoFair11{patenkalikaubang}`
