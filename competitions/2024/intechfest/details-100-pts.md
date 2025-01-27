# Details (100 pts)

> Author: aimardcr
>
> You were just enjoying watching your favorite VTubers, while suddenly the FBI breached into your room because they have found out that you have an outstanding still in Open Source Intelligence. They need your help to recover an image that is taken by a threat actor who recently hacked their National Data Center, one of the FBI's intel managed to get a picture of the hacker by hacking into his/her phone but that's all they can get. Unfortunately the picture really didn't give much information as they thought. Can you analyze the image further? The intel said that the picture could be a clue where the hacker hides. Some might say it's full of paradise.
>
> Notes - Enter the name of the place (without space) you have found based on the image wrapped with INTECHFEST{}

Kita diberikan gambar berikut dan diminta untuk mencari lokasinya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe52Wrx4JUyuxUYT8O7SkCCTfO6VuD6PYgKHXARYyPc68OXu5rdFsJGnMQP_b94oGseI-pp_WF1kv2M9G9ykFLOrp1V1HlA6oxFXYryvjHYRr1yrySCJPSoEdg3EtZOOtPHKFtZdI3atOZ_O-eGsknR8SL7?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Melihat metadata gambar menggunakan `exiftool`, ditemukan koordinat pengambilan gambar berikut.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc7e_SWUsQyv_S6jb-B9Emxf4fxUDsfTCD8FCEfQx6BtlkMVCH27_WVhU3MqnnzPyaRlsMDwoN31T9ar7CWPLQFWWFvoTVl5BD_rzcLGkQcvMmT91UpGrm5N9XrAfKMfSkl8UGw1ZyIeP_aqMhdRFUxapw?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Jika dibuka di google maps, hasilnya adalah sebagai berikut. Berikutnya tinggal memasukkan nama tempat ke format flag.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe56JzGIt4RV5kzGmfoSw7_LqqHMAoqZsj-CgNs3zUppWIDM4uPTHxdyvd5jsqbw_mredKBWYKpodR0HcV9mbKX1U0z8nfnQgdFyW_UyXVfIrGTuX65Mjiw9YcFRURoxhZ93B1QzU0ZnfC8eQyJPeTqTd6_?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Flag: `INTECHFEST{JimbaranBayBeachResort&Spa}`
