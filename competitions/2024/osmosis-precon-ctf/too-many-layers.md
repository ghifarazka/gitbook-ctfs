# Too many Layers

> gkkab://bgrsktsq.vk/NWPVF
>
> Hey there, fellow code-cracker! Today, my brother, who’s fond of ciphers and steganography, sent me a mysterious link to a file filled with secrets! 🕵️‍♂️🗝️ He hinted that I need to use an algorithm but was delierious from all the attempts. I couldn't tell what code to use but it sounded like cAFFINE and the magical code word is “today.”
>
> Can you help me unravel this enigma and uncover the elusive flag hidden within? Let’s put our detective hats on and decrypt this together! 🔍✨

We are given a link that seems to be encrypted. Based on the clue, the algorithm would most likely be "Affine cipher" and the key "today" which would be "9/21", the date of the CTF. I used [dcode.fr](https://www.dcode.fr/affine-cipher)'s tool for this.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

Now we can visil the link at [https://shorturl.at/CDIAE](https://shorturl.at/CDIAE) and we get an image.

<figure><img src="../../../.gitbook/assets/image (25) (1) (1).png" alt=""><figcaption></figcaption></figure>

I tried to do many steganoghraphy techniques on this image, such as `exiftool`, `binwalk`, basic lsb, etc. Then, as any desparate steganographer would do, I finally ran `zsteg -a` on the image to check for all bit plane possibilites and got this:

<figure><img src="../../../.gitbook/assets/image (26) (1) (1).png" alt=""><figcaption></figcaption></figure>

I assumed that the phrase is likely to be a question for the flag. The answer to the question is Alan Turing, who created a machine to crack the Enigma and helped the Allies won the war.

Flag: `flag{Alan Turing}`
