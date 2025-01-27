# head’s up! (493 pts)

> Oh no! My mischievous cat decided to play with my laptop and now all my important files are missing! The only thing left is this single, mysterious file. Can you help me retrieve all my important files?
>
> Author: ultradiyow

Diberikan file `heads_up.zip`. Jika di-`unzip` ada beberapa file yang muncul.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2t6CFDplCoB48Q9ow_uq0RBxVJFJbiGp3l5jXFFlbM-deqgp2QoBBlGbyA1meM6Wo2_BWxHXCeIANyBhq4i5QzCJrdex1H-zZooFDXBJ95-G9NZk_jqiVCuG8amcT-Tdz9FpXt0DDLkegsX02XFZLXDQ?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Directory `__MACOSX/` itu tidak relevan untuk soal ini (mungkin hanya semacam cache). Intinya, kita mendapatkan file `flag.txt` dan `meong.txt`. File pertama berisi part pertama dari flag. File kedua berisi gibberish.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfkhXs4EiOa9PYvyr02ZrJK9GYORaEnT8JclQYIZEzQUx4gCR-CkGzGL2I4MHYPnWwLIPKR4M-3LIKNEnHq0JmboeIMvRUm_uGCiRuGX_tkeKeL3-FPMolEZs5UqLXWiMFgE4T432_k_3m0SJyd_jVfi9MX?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Berikutnya, ada yang menarik apabila kita melihat ke dalam file menggunakan hex editor.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcKG2tZMlgGw2xEZrvsw1sdnEM335UDt-8w7FjarWI6Qtue4TuFAOLkVFKxXBZJ3UwSdGivb3yRIAM59N9-eXtgxUJMNKSk5EQ6zenn3hHQLTXa8nvId5krobsd3qwOYvstSX9e0m4HiTVzsTVCoNxHlTEV?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Tepat setelah segmen untuk `meong.txt` pada zipfile, ada beberapa header yang tampak seperti header dari PNG. Sepertinya, file PNG tidak ke-detect pada zip (ataupun binwalk, jika dicoba) karena header awal PNG-nya telah berganti menjadi MMEONG. Oleh karena itu, header tersebut saya perbaiki dan kemudian seluruh byte dari PNG ini saya ekstrak ke file baru. Berikut adalah hasilnya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXt2Wj49NhGuDnXLmcrSx7_IuJzL9cV18_1KBYZRt2pJWAYq9O0YtOOALrFzmzqB7mmiLqWYHIUTA0ZapvdAvLahg0este3Cf2AuNZbYqoin7HSl55_3_I_LfNIS3fawc4hLZjwCUWP0KnGXjGDXjRqW0?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Terakhir, jika kita scroll kebawah pada hex editor, kita akan menemukan bahwa setelah header IEND, ada header berupa DSIG, yang biasa ditemukan pada file TTF (TrueType Font). Akan tetapi, signature awalnya lagi-lagi tidak tepat. Kita perlu mengubah 5 byte di bawah menjadi `00 01 00 00 00`. Lalu bytes nya kita ekstrak ke file baru.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeKOdFCvtVB58FExmAy2gRXhBdih8fXLpqIsmXs6yQwPX_effTt43lh-sNdSaMQ8nTlNLG0FyB73wKb12OtG0aulZYu8CUlYBNn7cfkfekUqX9bEeqeSY8BHd4OtCPRs18kQevH8TVqGQB09JMuXca07-mX?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Untuk membuka file TTF, kita bisa menggunakan website berikut: [https://fontdrop.info/](https://fontdrop.info/).

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeDrsRmJyE0mWPYR5VSEzaaKdwdOcUK9V8xFyQ_ESTTYdPlzMEsGSr0kH5y7TpRuD2vorrftDx1iCi3xxd3AX4zqBpg1LgR0VTD3FhUcqdqlRS-Ekeyo38UhGV0_zITLPShsrDXP4GAWrEp6jwKsCiYGWn3?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Berikutnya, kita bisa ke tab “Type Yourself” dan kita copas saja text yang ada pada `meong.txt`. Flag part 3 pun kita dapatkan.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfgt4pQ-VT-xVgsfCE5zTYvvrlb2cnYHHWDo05BlGvtUV4rh-A9LhDyyoydXvzVs96haovrddNipXxbTHWs7ef-rqaJZ23aJolP_j6k4MGdYhFoUhZ55dErVTEHvvU5oVceBKHuBy4tdYqUsWqWUQqEL6Ih?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Flag: `COMPFEST16{lO0kS_l1k3_u_k3Pt_Ur_hE4D_uP!_22a4b9bdf7}`
