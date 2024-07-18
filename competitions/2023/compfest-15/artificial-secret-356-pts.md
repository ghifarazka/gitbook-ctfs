# Artificial secret (356 pts)

### Deskripsi

> I'm developing an AI Waifu chatbot startup but i'm too lazy to host my own LLMs, So i just use chatGPT API, but first i need to hide my prompt since it's my only moat, can you help me pentesting this?
>
> the bot is online as lemond #8498 on the Discord server, but only talking in DMs. (Note: this challenge requires no automation. Please do not automate your Discord account as that is a violation of Discord's Terms of Service and may lead to the termination of your account)
>
> format flag : COMPFEST15{flag\_sha256(flag)\[:10]}
>
> Author: fahrul

Pada soal ini, diberikan `main.py` yang berisi sebagian source code dari bot.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXf0Fu8VCUhv15G202WRRsx1uL_yuODA05kXqhsIid_Xnb6pJpN1Wx66D2uGyhQ_OxhbVImDkQ1g3DKVfjmFvtpEgV7xT6eN12NJYj775Ti3CPwGnjak3Hp-Bsr-42P4wtKM43V84K4GEJ6OOoElYt9jkK7l?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfeUnRR_wUTxjBGrpXfgieXcBrIHQpsCWGCI3y1djEducYIgF2lXWtJIxzfW-_9zfhL86GQaqewA2zY9gW6VSL_pphFc_REuC5gMj7N38QghDSdePldQ275whG0vvrtQgDZ4N70hU0FSgOKlU01ciIuuHiH?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Yang saya coba lakukan pertama-tama adalah berpura-pura sebagai pemberi prompt, tapi tidak berhasil. Bot akhirnya mau memberikan flag ketika saya minta dalam encoding lain, seperti base64.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeu5ys9FqhCC0qoAXu7tVwIAeus7Pp5aGpBgEDIstNm8J2kxOi9AG0LZbz4opYf_nZbPtdUzGnwuKL9ByUfATIUlMcxYfvwitr6cgwJx8ITVe1fN5N-xfhWO0Nvrz9FKkDnNHYh5_eUsDCjnLSeT6lCsIw?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeAPZCrJVlLYWKLcD0HRV0eFiSRpB0wPA8couwE6TzKiuiB63Z9S9oyXKIixVf_6bLTeE8wkupDnyp8wPH6R7_MrXM0Q2m1-01ANoV4NsC_gaIq33meDn3zw55ElUWcwuNVbIg4rKGHfQdZ17hFlOL1O5cQ?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Berikut adalah flag-nya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcLX9NOecEpNO9q1GN7eWLqwId1Mg5ePgLJ24MB6xe2CPpshsCKAk6iN2DoZtNqbeA4KEuBuizUHdUnSgMA4nux44K8DjS9VUDVKH-cLBqxXZQeoa-oY1VnNmixury_X5eWii4sUEMKjAouzhAA2gzNrx9p?key=NvqXZ32fxcgC5n7TP8Sd3w" alt=""><figcaption></figcaption></figure>

Flag: `COMPFEST15{d0nT_STOR3_S3CrET_On_Pr0MP7_874131ddff}`
