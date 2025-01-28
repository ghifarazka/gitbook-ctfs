# Day 24 - Mastermind

<figure><img src="../../../.gitbook/assets/Deck_Chairs_.png" alt=""><figcaption></figcaption></figure>

Question: Who reserved the deck chairs?

### Solution

From the picture, we can see that the seats were reserved by someone called "bknotbmoka1337". It sounds like a username. We can search whether that username has been used in any website previously. Here, I used [username.social](https://username.social/), but there are plenty of similar tools.

<figure><img src="../../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

Most of the results, however, are false positives. But we can be sure that the [GitHub account](https://github.com/bknotbmoka1337) definitely exists by visiting it.

<figure><img src="../../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

There's a repository that contains just one pdf file.

<figure><img src="../../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

As the contents of the file itself is not necessarily useful right now, we might want to look at the file's metadata. I used `exiftool` to extract the metadata of the file.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-01-27 221155.png" alt=""><figcaption></figcaption></figure>

The mastermind behind all of this, is "Big Red Joulupukki". Which means that The Thief... was Santa himself all along!

Flag: `Big Red Joulupukki`
