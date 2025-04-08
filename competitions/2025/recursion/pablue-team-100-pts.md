# paBlue Team (100 pts)

> by Pablu
>
> Loh…
>
> nc 103.87.66.171 32128

Pada soal ini, kita diberikan sebuah file Windows Event Logs bernama [Security.evtx](https://drive.google.com/file/d/1pWF6dvD8YmvhF0IK_g2m6bfsOd_jPIi3/view?usp=drive_link). Kita diminta untuk menganalisis file log tersebut dan menjawab beberapa pertanyaan pada service yang diberikan.

Saya membuka file dengan Event Viewer bawaan Windows, lalu memilih “Save All Events as...” untuk menyimpan file ini dalam format XML dan TXT. Kenapa? Karena di app Event Viewer, fitur ‘find’ nya sangat lemot, tidak seperti file text yang bisa langsung ctrl+f. Kenapa XML dan TXT? Karena isinya beda. Tau dari mana kalau isinya beda? Karena saya mencoba menggunakan keduanya ketika mencoba menjawab pertanyaan pada server.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2-EtQpDVii2bhkUUrq-r0i2NjZ3qRsrM4NvN1XLj-IWek1pk7x7q-1TK5xLPDkU_5BDTlL-pcGr1NnZZcOgtiHxaKAdrdoaFHdZRcMYbXxSaNZeZ2yivWPdwKbXdTx-ZryHUliA?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdSTEF19b6Muz-NYCChAedbJYhJpsuy2BiJxFapRb3sWpaahgzyJZLmVubWVdteFxa5mOFu4SzINgt2vx6Taxl0Mh1I7VAEPzRfgW_y3t5IDMuxQqEk2BPB8LbXQ8i0pN06QIARow?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfCp_I_hc0ir6TKLk4McJSF09bJ4Rr60_El7VuTJQJy_4-5YZXozdO0CeLyYPSSahtJSsF_BIg2bHRSmT0sMUKszicI7bbE1A5LOOsEOrM2HHRjSp4oyQbGjOAbVN9Y4xcbYNJFAA?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

\
Dari sini, saya dapatkan [events.xml](https://drive.google.com/file/d/15h-xGiVoIul1nNAzreFhHw1W2WEwXpba/view?usp=drive_link) dan [events.txt](https://drive.google.com/file/d/1Z8O4i2bdUeE94psutbfDlInq1iGQJ8ut/view?usp=drive_link). Approach saya adalah melakukan ctrl+f pada kedua file dengan keyword penting seperti “powershell”. Dari situ, saya bisa melihat penjelasan event yang ada di sekitar keyword. Berikut adalah salah satu contoh.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNOv0EOMQ5Xj-YQpo5yiDdiH2wjC7aEteKjS8J5mn7YMP8_9BQI4LuiEZiuNmjglaOoTH8rnwzUokTG2SvXBGILqmGoGcS22lqhuEa-k0cbim-M-9kIQJ6DQ5jP5R6QTRcjnRsLw?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Dari sini saja, kita mendapatkan informasi bahwa terjadi eksekusi command malicious pada `Powershell` yang disebabkan oleh malware executable bernama `payload.exe`. Malware tersebut menjalankan command yang di-encode menggunakan `base64`. Eksekusi oleh Powershell ini memiliki Event ID `4104`, dan menjalankan sebuah tool credential-stealing bernama “`Mimikatz`”.

Nah, lakukan saja hal yang sama untuk setiap pertanyaan dari server.

```
$ nc 103.87.66.171 32128
Welcome, analyst. Please answer the following questions:

Question 1: What is the Event ID for malicious PowerShell execution?
Format: number
Answer: 4104
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeR-ymuAumweWEVU-Tx7UwuCtKLckhOK3jHkcg88TWHXmP_WIgI2OT7WoFp53aldmF6dA514f1jD2qSC3Gn3x8eBqrMuhOJRPKdXKjBv0aa8bMXRMsq68jCJjNejMFJ5wkd42sohg?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 2: What is the name of the malware executable that was dropped?
Format: name.exe
Answer: payload.exe
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe6o63wCI87D_-eYwezM0lkIMKhvmWuY8x0dVaOBASrCxzAaOvOTNzwgswCrxs_pX3ZRVjJlleLbea7w3dvwnj8pAvnqNxw-cRS_mrkohmohSAoPY3QiHIUTIR0sDolChZm5CRT_Q?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 3: What encoding was used in the PowerShell command?
Format: lowercase
Answer: base64
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRw9Unyqd2x033PDVR_7xjgocio7poeUnktY1lqx_MgM5VjuYLkuq5rfXtZazxqgEsGfeOFjRQD715JmplhfkubFDxlod4vyNXK7ggf9HrXxAeG2f5qtUvwPdqHxDvht3J5C7S6w?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 4: What credential-stealing tool was executed?
Format: lowercase
Answer: mimikatz
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdF2DO8iOXpR18ONG_Lm8EHnQTbTSWy5k9Ht5Jf9Y4COxbqxMK0t7lHsearosU3ZOEUMhP8a36zIJHoj9SLzszWVMsAbJ4rs1yc7ocoX0t-Bn2s41HBCXz7fsNzRBqdd2Bjq5si?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 5: What registry key was modified to maintain persistence?
Format: this\is\example\path
Answer: HKLM\Software\Microsoft\Windows\CurrentVersion\Run\Malware
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXci_1kQtX1spi7KKFEjJfyEl3ZFr2bFDq9zNHk5jbCtJpgLksY2ggMvjyXR7edgQhisAItEZD0aggqVErbFYzDIcUak6B-lkQ8BaI1pXtCR6scewARC_3fZT1_q9gimZ5lKtrUM?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 6: What is the name of the backdoor service installed?
Format: NameSvc
Answer: BackdoorSvc
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf8fsoGOiqJwQjcx8nOtT5I4WtFg4Zz-grzt24kiumLXGzIG8TMgefFzY5IbQjyrDp8C16F2ytylOokW9b_AGs3kSSfz3t0geGV18Ebu82gPSKDha4LPxCI0Be2BP29dnTzrozJUg?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 7: Which LOLBin was used for process injection?
Format: binary.exe
Answer: rundll32.exe
Correct
```

Awalnya saya mencari dulu LOLbin itu apa. Lalu saya mencoba membandingkan apa yang ada di Google dengan binary yang digunakan pada file.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdOSsC1QfIuODAJ9fiQc8ot1GOZAdhetHXtB8ipWZjSSF5YzFYha7KFgqR5el6RSus5kv0vwYO9gjXfMP7DRbcFi6HHbA1mxTqiMFZYF5KTp-eMch8dq2QEMLSLwXQ_xz9QKaIRdA?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcLqXTwmyhm-e2sDntTysH3mmzJdhLrNxslXKiYQqXwlzthtTyMkWqHTGOD-GkkJU3PQkhgDGBVwfJDjriqMSkjD6WEO_dZTPmyFhULNW1Y4U2gp8dqc_ZsSg8PIwQhmN6pe8dtxg?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 8: What is the IP address used by the attacker to access RDP?
Format: xxx.xxx.x.xxx
Answer: 192.168.1.100
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcR9wEpxbKDYT6I_GRmrj6lcLwZHy0xzl8Pir5r65rS3EOXTeVmsGdh_HiMQvC0sE_i7j_ayeose1avHFmOcHL2Ax7YTAgREu8eZOoXgrSNU-S2BV4qwvRLqRui0JVt0awl81Chzg?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 9: What file was accessed in the C:\Finance directory?
Format: filename.ext
Answer: secret.docx
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfZnmEwapmvzU0P3faFlezMtyj8mnjcj4hIsWE3ZkrON-lU8QwwsOKqE8jh80EXxJ8VdO96W7bK9L6YtPYDmNui6LfyzvoMTAJin9I7Q9MrVl2K3Xzl2fHcFrMeIJwtKKzxIfBu0A?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Question 10: What protocol was used for data exfiltration?
Format: lowercase
Answer: ftp
Correct
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd47pAhisN_vbi3mRd0M3cREgjJM2jhfxDPjAf4EhxNnYSW4zg8EtIMJFHoltQiIKFK5zmq5OCSnJNpRIGKCbkenLvil-eApQwDEdv8RCDAWS8MNhxeQvzZyI1VIg8ACFw3HWQaiw?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

```
Congratulations! Flag: RECURSION{y0u_4r3_4_r3l14bl3_blu3_t34m_4n4lys7_09_URRRAAAHHH}
```

Flag: `RECURSION{y0u_4r3_4_r3l14bl3_blu3_t34m_4n4lys7_09_URRRAAAHHH}`
