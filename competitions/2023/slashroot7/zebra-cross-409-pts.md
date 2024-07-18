# Zebra Cross (409 pts)

### Deskripsi

> Ini mirip QR code tapi panjang kaya zebra cross, jadi cara scannya gimana yaah ?
>
> Author : bukan\_littlekrisna

Pada soal ini kita diberikan sebuah file gambar yaitu `qr?.png`.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfvgAuosR7Uix2x-sLr0-W04EyCGRDbPw0S0Rx_qi6TWWqHf9vI28fJ9grpHt9dDSd2HaKDU4ZOFySFEv7QYkE8IL5dVMWEFbePZlsyKiiU0BL0hm91XI1ESbu4wKJASvE9KOKdCccxUMcnRIQrANcewQ2d?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Di sini terlihat bahwa kemungkinannya adalah sebuah gambar qr code dipotong-potong menjadi bagian lalu disusun secara horizontal (dan kemungkinan posisinya acak). Pertama-tama saya mencoba mencari tahu ada berapa bagian. Saya mencoba membagi width gambar dengan beberapa angka, dan didapat bahwa width habis dibagi 9. **Berarti ada 9 bagian**.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc7XCQQLcQ5kGAe1jPtLXWJDBUhuAkCmVgoTdd4Il72Pp0m9y4qLm32z1XSR9kDtwOARWyW15Is_ljeVEe4MH2Yvq1yTDdGYZM_KB4CiA6sEYsx3_LpOg6wKmlf9nBT_G92b6iXBJfMSrNlaOn-xKlPDFsM?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Berikutnya adalah kita harus “split” gambar tadi menjadi 9 bagian. Saya menggunakan script berikut.

```python
from PIL import Image

img = Image.open("qr.png")

split_width = img.width // 9
split_height = img.height

for i in range(9):

    left = i * split_width
    upper = 0
    right = (i + 1) * split_width
    lower = split_height

    split_image = img.crop((left, upper, right, lower))

    split_image.save(f"hasil{i + 1}.png")

img.close()
```

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcwO0IoreoVqnB_M-hFILDi9Qrw8KGkB8A9SMIf1koLOjllvGipAA2g-x4PsNAiLywAK4ivzrJC44JQjsC6rHYYxZBSz0QfoYc3n927NCR2gD4MEd7XkdwPBHNTh7wsLmHMlOZiLU5WNCPT-UVrczyRzLQf?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Sisanya adalah seperti bermain puzzle. Saya mencocokkan ke-9 bagian gambar tadi secara manual (menggunakan `Canva`). Saya mulai dari bagian yang memuat kotak besar QR (yang letaknya ada di atas dan bawah) lalu melanjutkan dengan mencocokkan pola hitam-putihnya untuk bagian-bagian yang lain. Terakhir, tinggal scan saja qr code nya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXexwqP3TrOhmgzrQVUJlB-h5-eO_XTzslKC3x3JGrztEVL-cVe7Nh3RUYZ_LrOWUJZO72br8IQigC04XRvCljUnzwLfDmVGTULB5llyzR-EC_Yfx83vhXcKVHIj9JMYYY6LDvWqVV2S80ap0rGGd07RUcvZ?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdx7cHGWcYrPfXgAR7AYwW0PHLHHFhoo7u1YP-nqkEclCIhCtEN_Ny6McK_jlwFe2aSicLV7iliJLOroG-oblMpjkCbZh9wwoBVtms9bb1BAH4svgSSAu4kLkfGIWhlsGXF-ntJV_WNoRE4Swn2bTiyROca?key=UHUbZEdePaoFI73ooJngNw" alt=""><figcaption></figcaption></figure>

Flag: `slashroot7{jUst_pL4y1N6_WiTh_QqRr_c0D33}`\
