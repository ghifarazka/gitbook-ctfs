# Stream Ciphers

### Symmetry

Challenge website: [https://aes.cryptohack.org/symmetry/](https://aes.cryptohack.org/symmetry/)

OFB works like a basic stream cipher, using an XOR operation between the plaintext and a keystream to produce ciphertext. Because XOR is reversible, if you apply the same process to the ciphertext using the same keystream, you’ll get back the original plaintext.

In OFB sense, encrypting a plaintext twice will get you to the original plaintext.

```py
import requests

url = "https://aes.cryptohack.org/symmetry/"

def encrypt(plaintext, iv):
    response = requests.get(url + "encrypt/" + plaintext + "/" + iv)
    return response.json()['ciphertext']

def encrypt_flag():
    response = requests.get(url + "encrypt_flag/")
    return response.json()['ciphertext']

# Get encrypted flag
ct = encrypt_flag()

# Encryption == Decryption
plaintext = ct[32:]
iv = ct[:32]
flag = encrypt(plaintext, iv)

print(bytes.fromhex(flag))
```

Flag: `crypto{0fb_15_5ymm37r1c4l_!!!11!}`

### Bean Counter

Challenge website: [https://aes.cryptohack.org/bean\_counter/](https://aes.cryptohack.org/bean_counter/)

Analyzing the code, we realize that the value for `self.stup` never changes. Consequently, all blocks are encrypted with the same key. We can get the key by XOR-ing the first block's ciphertext with its plaintext. The plaintext is known to us because the first 16 bytes of a PNG file is the same everywhere. After obtaining the key, we could just decrypt the rest of the blocks.

```py
import requests

url = "https://aes.cryptohack.org/bean_counter/"

def encrypt():
    response = requests.get(url + "encrypt/")
    return response.json()['encrypted']

def hex_xor(hex1, hex2):
    hex1 = bytes.fromhex(hex1)
    hex2 = bytes.fromhex(hex2)
    res = b""
    for x, y in zip(hex1, hex2):
        res += (x^y).to_bytes()
    return res.hex()

# Encrypted image
encrypted = encrypt()

# Keystream is the same for all blocks
# To get key, XOR the 1st block ciphertext and the known plaintext
known_plaintext = "89504e470d0a1a0a0000000d49484452"
key = hex_xor(encrypted[:32], known_plaintext)

# XOR all blocks with the key to get the original image
encrypted_blocks = [encrypted[i:i+32] for i in range(0, len(encrypted), 32)]
plain = ""
for block in encrypted_blocks:
    plain += hex_xor(block, key)

# Create the resulting image
file = open("result.png", "wb")
file.write(bytes.fromhex(plain))
print("File result.png created!")
```

Flag: `crypto{hex_bytes_beans}`

### CTRIME

Challenge website: [https://aes.cryptohack.org/ctrime/](https://aes.cryptohack.org/ctrime/)

In this challenge, we are given an oracle. The oracle takes our input and append it with the flag. Then, the combined data are compressed using `zlib` before being encrypted using the CTR mode.

In `zlib`, there's a [matching and replacement of duplicate strings with pointers.](https://en.wikipedia.org/wiki/Deflate) So, what happens if we input a known part of the flag to the encrypt function? Here, I replicated the code locally, and added a dummy flag for testing.

```py
from Crypto.Cipher import AES
from Crypto.Util import Counter
import zlib
import os

KEY = b"aaaaaaaaaaaaaaaa"
FLAG = "crypto{this_is_a_dummy_flag}"

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)
    iv = int.from_bytes(os.urandom(16), 'big')
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=iv))
    compressed = zlib.compress(plaintext + FLAG.encode())
    encrypted = cipher.encrypt(compressed)
    return encrypted.hex()

random = "abcdefg"
known = "crypto{"
length_random = len(encrypt((random).encode().hex()))   # 82
length_known = len(encrypt((known).encode().hex()))     # 74
```

As we can see, encrypting `crypto{` gave us shorter ciphertext, as the data was able to be compressed further because of the duplicate string. The logic for the exploit is that we could brute-force characters to append to `known` and choose the character that produces the shortest ciphertext.

However, in practice, it's not that simple. Most of the time, adding characters that are already in the flag should not even change the length of the original ciphertext. But of course, there are times where adding any character would result in adding the length of the ciphertext, no matter what character. For this, I make a modification to the code so that the code stops and ask for my own input on what I think the character should be (this would make sense if you run the code below). In addition, from trial and errors, I noticed that you should just shift the known characters instead of always appending them, because this can mess with the compression stuffs.

Anyways, here's the solver script.

```py
import string
import requests

url = "https://aes.cryptohack.org/ctrime/"

def encrypt(plaintext):
    response = requests.get(url + "encrypt/" + plaintext)
    return response.json()['ciphertext']

known = "crypto{"
length = len(encrypt((known).encode().hex()))
compiled = known

# Loop until the correct char is "}"
while True:
    correct_char = ""
    length = len(encrypt((known).encode().hex()))

    # Find a character who keeps the ciphertext length
    for c in string.printable:
        length_c = len(encrypt((known+c).encode().hex()))
        if length_c == length:
            print(f"Found!! c = {c} --- len_c = {length_c}")
            correct_char = c
            break

    # If it's not found / the string got longer anyways,
    # ... find the one that uniquely changes the length 
    # (the value different than the others)
    if correct_char == "":
        new_len = {}
        correct_char = []
        for c in string.printable:
            length_c = len(encrypt((known+c).encode().hex()))
            if length_c not in new_len.keys():
                new_len[length_c] = [c]
            else:
                new_len[length_c].append(c)
            print(f"c = {c}, length_c = {length_c}, length = {length}")

        # Check if a unique length exist
        try:
            assert (1 in [len(val) for val in new_len.values()])
            print("Unique character exists!")
        except:
            print("Unique character doesn't exist.")

        # Extract that unique character
        for val in new_len.values():
            if len(val) == 1:
                correct_char = val[0]
        
        # In case where a unique length doesn't exist, input the character manually
        inp = input("> ")
        if inp == "N":  # To cancel the whole process
            break
        else:
            correct_char = inp

    # Correct character is found, add it to compiled
    # Keep 'known' not more than 8 characters
    known += correct_char
    compiled += correct_char
    if len(known) >= 8:
        known = known[1:]
    print(known)

    # If end-of-flag found, stop code
    if correct_char == "}":
        break

# Print the flag
print(compiled)
```

Flag: `crypto{CRIME_571ll_p4y5}`
