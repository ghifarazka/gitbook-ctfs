# Small House (200 pts)

> by ztz
>
> So me and my friend are building a small house in Minecraft with two beds and a chest, but the house is too small to fit everything. I need your help to reconstruct the house so that we can fit everything inside. Here is the location of the house `1, 6` in `r.0.0`.
>
> Note:
>
> * You don't need the Minecraft game to solve this challenge.
> * Add underscore to separate words in the flag.

Pada soal ini, kita diberikan sebuah [file zip](https://drive.google.com/file/d/1S0OV0zSiLtW9IOf4H2Up2t5FjNxhROde/view?usp=sharing) yang berisikan sebuah folder. Setelah saya telusuri, rupanya ini adalah folder yang merepresentasikan sebuah World di Minecraft. Setelah saya cari tahu lebih lanjut, Minecraft menggunakan [struktur data “NBT”](https://minecraft.fandom.com/wiki/NBT_format), yang bisa kita analisis menggunakan tool [NBTExplorer](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-tools/1262665-nbtexplorer-nbt-editor-for-windows-and-mac).

Pada NBTExplorer, klik File > Open Folder, lalu pilih folder World yang ingin kita buka.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXckzcEr23UOSeRkH0xgs6XBwi3izCIvL7D6MYiJ_9-fq_XvrY4A4fzakkPQx_MWqUJunzcpzuNN9ENxRhPZR2mu4Xr1m7rEhkqLvghmVupm1R6STMgY5IZqItafwfb-CJnRZxn1?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Berdasarkan petunjuk dari deskripsi, rumah terletak pada region `r.0.0` dan chunk `1,6`.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfIqUiOxmmcBTtJEMXj9rAGqb5vDRs0lc74iwkiFPbxmhF0xE6JngwT4_L5oGlDghAK0VMW3-jSWtACv5zF-eY2boXazd6ua-6jmxHvXgvfTMH1eD85LClduUTAR_4Phl7foHtEpA?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcJD8IDBz8MAAL_u19A6jGonWUJrg7mLVgSm5_ahCwq306PpFgUL2OU4rvqM6mKx_Z9wkg13xGZ9OcswwD_2n5qXiNm_Md4AnoUBWAzHaIphuPM-jnJaHUB6gdKffDPSfOCB7lkhw?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Di dalam chunk ini, ada properti yang bernama “block entities”. Sederhananya, ini adalah list dari semua block yang ada di chunk ini.

| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcGNJfZO8I9yqkt1LPqJGgFR7xeAvvFZDoct6SfJl5LRu6m8M-_Za4qrVPXw60FNjVkTV865cEccb1PivKOlm1xjs5j8heMO59YdixgWv0w-AFHMv2DO8HlIcNPjABY2ju52sRZXw?key=SxIcHc24jlwlBodtkfBf9D-E) | ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcflZv9dZP_I4XwZXY-9Ek2CP2_s8k7lWFmWjdvJKjwLo7LvSs69ho249I_NVEhAs5AuAb-9DjvTRv93IEKBiEC7apqciDdHwCrDGyAWnETiKOQx1Xds2g8a96L0_ktEPa507eEfQ?key=SxIcHc24jlwlBodtkfBf9D-E) | ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf86nLntQQ3yXvyr-vSxBZiofiT1aceTQ-ZqtSSBZ41njSORFODzSDurhSQVpwXgEXekTkFW5P2B5m2DXJyv03OWJh6XF0fENrS_L504uyjV3GilVHHue6UHvW2djhLL20j2etgfQ?key=SxIcHc24jlwlBodtkfBf9D-E) |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Terlihat bahwa di sini ada 2 bed, beberapa furnace, dan 1 double chest, sesuai dengan gambaran rumah yang ada di deskripsi soal. Nah menariknya, kita bisa expand lagi data dari ‘chest’ untuk melihat item-item yang ada di dalam chest.

| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcn40JNNZ_6bfrh57_-0idK8wvzlVUVgjqXYdZzSmFtuoC71jL6kdnFeYJtdN3wsMNK7tpnOWRL8IKaPgFrQ2CaTLtH9AjzXDtMj1-B0jGdGJ-7ZEp3arFbtupwWr5-a14kwHb4?key=SxIcHc24jlwlBodtkfBf9D-E) | ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdoltozoCqlneR8P92htf0ED5C6CbVgr6QV4BxX_9geSlRn0qMydNRxtA8qJ9EGytvDyGpwkURmu4bXDEF4jNDbmPawro-FKbSQOYAjnPOBIMuk_IuXqe1pGLZuoCBypaEumldchA?key=SxIcHc24jlwlBodtkfBf9D-E) | ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfNvgdBAgLudBwNwgsfh3GJWEhDmjM2f8vDpeju7ud0QfVx-7QQtRajoyhUC7FDeQ612ouZ3um3bHhlwD5cksEa2UjnGnDw-EhBVrmh0nuKm4IDixG8ozUaSlYmYr3ncu20TZpI?key=SxIcHc24jlwlBodtkfBf9D-E) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                           | ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf9tZs3bWc_aUN_78v0wmTudSxglONVbK3MNuP6psUH_w2i1OdNFuWWE-kzE5UP2xz-sZevIkx0cafZ9DH5Bld4-OHTN40MU8iG6wHw4oghFh2YIxdvCujW8zVRG_6hHqWAfEymXQ?key=SxIcHc24jlwlBodtkfBf9D-E) |                                                                                                                                                                                                                           |

Item di dalam chest terlihat arbitrary, jadi mungkin mengandung message. Setelah berpikir keras, saya menyadari bahwa message tersebut terletak pada huruf pertama dari setiap item.

| CHEST I                                                                                                                                                                                                                                              | CHEST II                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| <p>6 torch<br>1 wheat<br>7 obsidian<br>3 book<br>1 emerald<br>4 diamond<br>1 stone<br>1 iron_ingot<br>1 nether_star<br>1 apple<br>5 stone<br>6 minecart<br>1 apple<br>4 ladder<br>1 ladder<br>16 hopper<br>5 obsidian<br>3 minecart<br>7 emerald</p> | <p>16 pumpkin</p><p>14 leather</p><p>7 wheat_seeds</p><p>64 dirt</p> |
| <p>twobedsinasmallhome<br>two_beds_in_a_small_home (FLAG)</p>                                                                                                                                                                                        | plwd (tidak ada artinya)                                             |

Sedikit intermezzo, awalnya saya kesulitan untuk memahami folder World yang diberikan. Di tengah mengerjakan soal ini, saya menemukan tool untuk memvisualisasikan sebuah World di Minecraft tanpa perlu menggunakan Minecraft. Tool tersebut adalah [MCA Selector](https://github.com/Querz/mcaselector).&#x20;

Berikut adalah tampilan MCASelector saat me-load folder World dari challenge ini.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfOED7stgwXnk9Nbskpg-9RTNfoi2GJIhwr9Y6dS0n3pQaioL2plmaJJVu2YZoDXGj7q5w8ligxTT4d6O653349Fqh-EpYIziF59z54ZEtlE6tYvTwPTTPmfhdovHM1XQ?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Di sini terlihat bahwa rumah terletak pada region `0,0` dan chunk `1,6`.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcX9f7HYtVJogyRd5ssEeZGU_ALSf_7GOnyXUhl9r64vDGlBNTKLgvO8A1fL-d3yCfTfCe2R9rMLhJMIM-sNmJyLQT65p5xHH5qawamMRGR0VqBRrSxy3N2NkY9Fnws6rGBjoBTvA?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdtz3BcCJj7MGyLLq6an5jtCY9bRSZVzwF5ofaffKzHa7ZsfP3YIpWHe35iFnmjlJLjsF3mQbFc4VhuwAyRFhrAxS6gMlZaDAr1iZ10Rr3Qx4j_oy7c8ELotJFRLItolPmvVCKsbw?key=SxIcHc24jlwlBodtkfBf9D-E" alt=""><figcaption></figcaption></figure>

Flag: `RECURSION{two_beds_in_a_small_home}`
