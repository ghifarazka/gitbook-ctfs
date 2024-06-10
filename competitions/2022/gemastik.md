---
description: participated as 0xinsidious
---

# Gemastik

## Forensics

### Traffic Enjoyer (500 pts)

Di sini kita diberikan file traffic.pcap. Pertama-tama, kita coba analisa menggunakan Wireshark. Ketika mengamati stream-nya, terlihat bahwa ada banyak text dengan encoding base64.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXejHMREIvnSOkForuuwKc9sjAhP4QyG3iVcG2dVAeC9Q2WS3TDYBvAni12zw9NSvIEEj324iCpVvEziaTVwLI7IfExgiiVlc7R9bJKZiFUtI31n6erWaRtCRZ1xRSx7ykIETZOGclXJ6SdaZT4Kv84nO_9l1Q8hOCgvfNKtgnG9_RB1YQaJXGg?key=ix06C2_XFVksU1GYnJ5hOQ" alt=""><figcaption></figcaption></figure>

Saya mencoba memasukkan text” tersebut ke dalam CyberChef. Rupanya, text” base64 tersebut merupakan representasi base64 dari banyak gambar.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcww-20QCjrMxaqd6cBpyEAy2dyeD_QktX9Ez-Yu8EJsXPqkOjGNlP22WfifmlUPHyImKYryTv7-GWUI614ETXY20xpKX2blJCyT8v6Bp2yazaJ2wyeqsbAnvnMfKx_RYI34watQXBQJHJRfKV3QYyP8aghcLzVbL1-_WHR2irwRKp1fxLPhA?key=ix06C2_XFVksU1GYnJ5hOQ" alt=""><figcaption></figcaption></figure>

Maka dari itu, mula-mula kita download terlebih dahulu masing” text. Didapati bahwa nama-nama file memiliki pola “%3findex={angka dari 0 sampai 49}”. Untuk men-decode masing-masing file ini secara berurutan, saya membuat script sebagai berikut.

```python
import os
import natsort
import base64

files = os.listdir('.')
list_files = natsort.natsorted(files)

for f in list_files:
    file = open(f, 'rb')
    encoded_data = file.read()
    file.close()
    
    decoded_data=base64.b64decode((encoded_data))

    img_file = open(f, 'wb')
    img_file.write(decoded_data)
    img_file.close()
```

Dan hasilnya adalah gambar-gambar yang mengeja flag-nya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcQcCK3q_sZwMFFUTfhfKRfsOhrimelie-QM5IrMjJgj9G97g6wb_3uD4rOri9tUSlrP2WAZTNAv52_4eTrXXiLC1AWFpeA8WAPhd0bLW8G3jx8oyKZ6YXTcKNBbu0y0FQjlBGCpO8vV7iogyDnZStgeSNTTcrlxhoc5YFYRh6azou5tDkzKzY?key=ix06C2_XFVksU1GYnJ5hOQ" alt=""><figcaption></figcaption></figure>

Flag: Gemastik2022{balapan\_f1rst\_bl00d\_is\_real\_f580c176}

\
