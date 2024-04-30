# I am Late

### Description

> Today is Tuesday. I had an important meeting, and ...... I was late!!! Even worse, I forgot where I put my car keys. Can you help me to find them?
>
> Last memory: I got home at 6 P.M, yesterday and had dinner in the living room. After that, I took a bath. Then I played games, changed clothes, and checked the car in the garage. I forgot about the arrangement.
>
> https://tinyurl.com/48r3ewf9
>
> Author: Nando\_0

Karena authornya masih sama dengan Fun Walk maka kira-kira strateginya penyelesaiannya sama: jika ada gambar, langsung di-binwalk. Kebetulan pada soal ini kita diberikan 1 file gambar. Oleh karena itu, langsung saja menggunakan opsi rekursi pada binwalk untuk meng-ekstrak juga file-file hasil ekstraksi: `binwalk -M -e HousePlan.jpg`&#x20;

Berikut hasilnya. Wow, banyak juga.

<table data-header-hidden><thead><tr><th width="210"></th><th></th><th></th></tr></thead><tbody><tr><td><img src="https://lh7-us.googleusercontent.com/tnaurfjbxLHM5w-rmoHtXvzMoBCr4plDPsd4LDoNJ5USp6mltB1NdLcGtQvwzE287s1Y6FY6_ubFaaVHnaMXOQxj4t_INQUfaS0AWSVty3IvMHOh_2U2d5zJQfn1f760-GgdIuiwxFIrjY0snyUk6WI" alt=""></td><td><img src="https://lh7-us.googleusercontent.com/DvcGuxucFadMcE-u09-xuLnvZt0TY8pckrayaGFmfSWy45EV3pZqzFIFQaxxYiJ6jmp--i-0e_OR18xKC-i_sFbJQCz-BrJoQEhqIcEXc2KMaoZcD5AFzMv7yvNHVCVKObVAr6Xno_X1iBY_wHXq8us" alt=""></td><td><img src="https://lh7-us.googleusercontent.com/mhk87GUve09I7F3ekQHVQLyzsVUHO-XPStLKLGr7TwTvvuLThJEk3EH1jV4cO3C3r4quWIRCzJUDJ0-2ojMmc2tJvTVF8niHVkLibM457HBSLDakCCntZR8MxcnGt_j6kuv3bDDUUvQ8C_SUAN5ImTM" alt=""></td></tr></tbody></table>

Di antara file-file di atas ada yang namanya Flag.png, yang ada di “dalam” Laundry. Berikut adalah isinya.

<figure><img src="https://lh7-us.googleusercontent.com/GGyho6VGCGmus_afvcEQPnBb9ehjmwEKTfPpypD7Fs_aJY4VBmWjm7Vb8LEAwdQKVfzfsCLt9UqKVvuw9E5H8z4rA9wtJEGx2gLDiAupx1rmsw1ussrn1XyGLWjlcZLQ0KwyCS1TePxx6fTpRbPFYpE" alt=""><figcaption></figcaption></figure>

Flag: `GKSK#8{I_AM_LATE}`

\
