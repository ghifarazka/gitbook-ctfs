# Let's Help John! (100 pts)

> Oh no! My ex-cellmate got jailed again! Help me leave a key for him!
>
> Author: Ultramy
>
> http://challenges.ctf.compfest.id:9016

Tema dari soal ini adalah kita perlu memodifikasi header request HTTP sesuai ketentuan-ketentuan yang diberikan soal. Untuk connect ke service dari soal, saya menggunakan `curl`. Berikut adalah tampilan pertama dari service.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXenUBRAJxtV_MemYDJ_jj6l_2Vtf9377Nh4eN4t-wHujDqQCLR934cWw7puYQdHnTSC7Jnc05QVTtiu444jA20K6vg-ZvOhHveCPQWtbh_tlWE2qBULEVUVDntHYnHCEe-fypFy5FthbO7mgcx2AnM1pF5g?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeoH6Ki_fHWqlqwO-vVa6TKHrqhxIkxtLCvuQfKWF2tREAMxvZ6XV_7PdWn_DYWvNYtptPdnHMPxcGCvZdoXL6kjaj14A88ztugu96Cib8yEPW7-b3Ofc4U75yqVu9qFehbOnQ08uZuZZgNms_62DX_oYuG?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Di sini, “referred” merujuk pada header “Referer”.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZu-dfH-G8knLQStahttGEkkRHk23vmRCVHpj1N4uvzQFEeY3fIYqcrc3ujWEWi-SHlYaSSNGszQ2mCo3PD2CFuJdzQkFloKEFiQG16VCo-06R5AQRZauzXv0ocqub9BhG85mJy4c2EKgXuxRznGn1yZ0?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Di sini ada value Set-Cookie yang bernilai “quantity=Limited”. Kita perlu menggantinya menjadi “quantity=Unlimited”.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeEOYAaKqxn_atPLvcsSpKzuPjIr_knVmoB2VGLT32J-gAKpRnn7S-tJeWzwSVbbjcKY1S9dvjCUvLH1iKWG1dvvccfhym8L9P2tcMde1bBB7rgXynXJ8_Z7qR5KiJGwXyDOEwmdAHrjkcKZShFleyNBwZN?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Berikutnya ganti User-Agent.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXefgYgkAAuvd8ovmfo-WOAyUiaKWtB6a9cti_SQEQtCMond2YuuBfExZcDusOSJyymOP-cAIvj2fvmi5pLNaf3oLq-IutcqaTMprvAg5URYGuG4i5JcWf2XhQ4WpDX5NBGAoIXhQ-rRD9rsu1yZgc1lpauC?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Berikutnya, kita tambahkan header yang bernama “From”. Isi header tersebut biasanya adalah email pengirim request.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXem2xzAjWaHuAzT6fOwf9taLrVTJUwtCbtR12-pMVQbuxNLl_Y1BpJIyB_dNI12T8-f4s2dzQwiJYfu2oiFBaIpBK-xSu6JuYLPnQrbHCnC93A3T5-84XLlbIsH8AIycA9tJOv9FcXRTENOzR4sUFFzZxff?key=ndfxH1b3fpmazlbRgIkT3Q" alt=""><figcaption></figcaption></figure>

Flag pun didapatkan.

Flag: `COMPFEST16{nOW_h3Lp_H1m_1n_john-O-jail-misc_8506972ce3}`
