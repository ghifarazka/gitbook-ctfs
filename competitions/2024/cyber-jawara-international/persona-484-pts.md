# Persona (484 pts)

> Author: farisv
>
> A hacker known as "Ed" has crafted an elaborate online persona, leaving traces scattered across their personal webpage and various digital platforms. Your mission is to investigate and find the traces.
>
> https://persona.chall.cyberjawara.pro

We are given a website that looks like this. Our first information is that the person's name is Edina Salmin, that he's a programmer, and that he has this website and a Facebook profile.

<figure><img src="../../../.gitbook/assets/image (34) (1).png" alt=""><figcaption></figcaption></figure>

Whenever we're given a website, we can take a look at a lot of things:

* the source code (inspect)
* the metadata (IP, CNAME, domain info, etc)
* how the website is made, etc

Inspecting the website give us the first part of the flag.

<figure><img src="../../../.gitbook/assets/image (35) (1).png" alt=""><figcaption></figcaption></figure>

We can try adding "/admin" (or any common routing) at the URL just to check how the website will response, and we'll get this.

<figure><img src="../../../.gitbook/assets/image (36) (1).png" alt=""><figcaption></figcaption></figure>

The website was probably made using Github Pages. That means that the website most probably had the original URL of something like `username.github.io`, where the username is the website owner's github username. We can check if the current domain of `persona.chall.cyberjawara.pro` is an alias to the website's original URL using a CNAME lookup tool like [https://mxtoolbox.com/CNAMELookup.aspx](https://mxtoolbox.com/CNAMELookup.aspx).

<figure><img src="../../../.gitbook/assets/image (37) (1).png" alt=""><figcaption></figcaption></figure>

Now we know that this person has a GitHub account at [https://github.com/edsalmin](https://github.com/edsalmin).

But for now, let's continue searching the person's Facebook first. Whenever we're given a social media profile, we can take a look at:

* the posts
* the photos (they might reveal something sensitive)
* the bio (it might reveal personal informations)
* the comments
* the person's friends and relation to other people
* how their account relates to other account
* etc

In this case, the person posted this photo, which stands out from other photos. It's a screenshot of VSCode.

<figure><img src="../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

Looking closely at the bottom (left), it seems that the person was accessing a Pastebin link.

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

If we try to visit `pastebin.com/raw/a9v29gi`, we'll meet a 404 error. This is because Pastebin links have 8-characters code, while what we know has 7. We can bruteforce the last character using BurpSuites' Intruder.

<figure><img src="../../../.gitbook/assets/Screenshot_2024-11-27_22-25-25 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot_2024-11-27_23-45-48 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot_2024-11-27_23-46-26 (2).png" alt=""><figcaption></figcaption></figure>

Finally, we found the correct link ([https://pastebin.com/raw/a9v29gie](https://pastebin.com/raw/a9v29gie)) and get the second part of the flag.

Now back to the person's GitHub. Whenever we're given a GitHub account, we can check:

* all the repo, along with past commits
* all the person's contributions (which might be in other people's repo)
* the person's GitHub Gist account (which will have the same username as his GitHub but completely different contents)

Looking at one of his repo, we can see that [this](https://github.com/edsalmin/edsalmin.github.io/commit/b194d5a8578bee2f373db07d84f19b4ef97c95eb) commit has the third part of the flag.

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

And when we check the Github Gist account of his ([https://gist.github.com/edsalmin](https://gist.github.com/edsalmin)), we find the fourth and last part of the flag :)

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

Flag: `CJ{19f43f6db7328114eea9e1b939f40bc453fdb0b69a4e0006575e49e55fc187cc}`
