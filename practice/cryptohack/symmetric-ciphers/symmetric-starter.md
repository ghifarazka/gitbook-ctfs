# Symmetric Starter

### Modes of Operation Starter

Challenge website: [https://aes.cryptohack.org/block\_cipher\_starter](https://aes.cryptohack.org/block_cipher_starter)

In this challenge, we are given a simple implementation of AES-ECB, where we can just decrypt the encrypted flag with the given `decrypt()` function.

```py
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```

Here is the solution. I used python's `requests` library to connect to the website directly.

```py
import requests

url = "https://aes.cryptohack.org/block_cipher_starter/"

def encrypt_flag():
	response = requests.get(url + "encrypt_flag/")
	return response.json()['ciphertext']

def decrypt(ciphertext):
	response = requests.get(url + "decrypt/" + ciphertext)
	return response.json()['plaintext']

def hex_decoder(hex):
	try:
		decoded = bytes.fromhex(hex).decode()
		return decoded
	except:
		return "[unprintable]"

print(hex_decoder(decrypt(encrypt_flag())))
```

Flag: `crypto{bl0ck_c1ph3r5_4r3_f457_!}`

### Password as Keys

Challenge website: [https://aes.cryptohack.org/passwords\_as\_keys](https://aes.cryptohack.org/passwords_as_keys)

Here, the flag was encrypted with a random password from a wordlist.

```py
from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
FLAG = ?


@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())
```

My approach to solve it is to bruteforce each password to decrypt the flag. We can decrypt the flag using the decrypt endpoint from the website, or we can do it locally. Doing it locally is much faster. Here is the solver script.

```py
from Crypto.Cipher import AES
import hashlib
import requests

# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("./words") as f:
    words = [w.strip() for w in f.readlines()]

url = "https://aes.cryptohack.org/passwords_as_keys/"

def encrypt_flag():
    response = requests.get(url + "encrypt_flag/")
    return response.json()['ciphertext']

# Online
# def decrypt(ciphertext, password_hash):
#     response = requests.get(url + "decrypt/" + ciphertext + "/" + password_hash)
#     return response.json()['plaintext']

# Offline (Much faster)
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return decrypted.hex()

ciphertext = encrypt_flag()

for word in words:
    print(f"Trying word: {word}")
    password_hash = hashlib.md5(word.encode()).digest().hex()
    try:
        plaintext = bytes.fromhex(decrypt(ciphertext, password_hash)).decode()
        print(f"==========================")
        print(f"FOUND!!")
        print(f"Password: {word}")
        print(f"Plaintext: {plaintext}")
        break
    except:
        continue
```

Flag: `crypto{k3y5__r__n07__p455w0rdz?}`
