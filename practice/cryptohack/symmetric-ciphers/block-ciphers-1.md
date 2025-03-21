# Block Ciphers 1

### ECB CBC WTF

Challenge website: [https://aes.cryptohack.org/ecbcbcwtf/](https://aes.cryptohack.org/ecbcbcwtf/)

Take each block separately. Decrypt the block (using ECB decryption), then XOR the result with the previous block's ciphertext.

<figure><img src="../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

```py
import requests

url = "https://aes.cryptohack.org/ecbcbcwtf/"

def encrypt_flag():
    response = requests.get(url + "encrypt_flag/")
    return response.json()['ciphertext']

def decrypt(ciphertext):
    response = requests.get(url + "decrypt/" + ciphertext)
    return response.json()['plaintext']

def hex_xor(hex1, hex2):
	hex1 = bytes.fromhex(hex1)
	hex2 = bytes.fromhex(hex2)
	res = b""
	for x, y in zip(hex1, hex2):
		res += (x^y).to_bytes()
	return res.hex()


ciphertext = encrypt_flag()
CT_NO_OF_BLOCKS = len(ciphertext)//32	# 3 -- The first block is iv

plaintext = ""
for i in range(1, CT_NO_OF_BLOCKS):
	cipher_block = ciphertext[i*32:(i+1)*32]
	xored_block = decrypt(cipher_block)
	plain_block = hex_xor(xored_block, ciphertext[(i-1)*32:i*32])
	plaintext += plain_block

print(bytes.fromhex(plaintext))
```

Flag: `crypto{3cb_5uck5_4v01d_17_!!!!!}`

### ECB Oracle

Challenge website: [https://aes.cryptohack.org/ecb\_oracle/](https://aes.cryptohack.org/ecb_oracle/)

ECB mode encrypts the same block to the ciphertext. Using the oracle, we can try encrypting 15 bytes of known data, leaving the last byte to be the first byte from the flag. Then, we can brute-force all the possible bytes and match the resulting ciphertext to the one we got with the unknown last byte from the flag. The ciphertext that matches would reveal what the first character of the flag is. To get the next characters, we can put the known byte of the flag into the encryption input, and still leaving the last byte to be the second character of the flag.

Using the approach explained above, we wouldn't be able to read the whole flag if the flag length is longer than 16. That's why knowing the flag length is important. We can use the oracle to encrypt a few bytes of data, adding one after each. When the ciphertext shows an additional block of data, that's when we stop.

```py
# Increment plaintext length until new block is added
def get_flag_length(buffer=b'\x00'.hex()):
	buffer_len = 1
	ct_len = len(encrypt(buffer*buffer_len))//2
	new_ct_len = -1
	while ct_len >= new_ct_len:
		buffer_len += 1
		new_ct_len = len(encrypt(buffer*buffer_len))//2
	flag_len = ct_len - (buffer_len - 1) - 1 	# 1 is padding
	return flag_len

# Result: 25
# Therefore, we need 2 blocks as buffer
# We will do the encryption & brute-forcing stuffs on the 2nd block
```

Now here's the solver code.

```py
import requests

url = "https://aes.cryptohack.org/ecb_oracle/"

def encrypt(plaintext):
    response = requests.get(url + "encrypt/" + plaintext)
    return response.json()['ciphertext']

# Leaving 1 byte for the flag's byte
buff_len = 31

# Store found characters here
flag = b""

# Main code
for _ in range(buff_len):
	buffer = (b"\x00"*buff_len).hex()
	ct = bytes.fromhex(encrypt(buffer))
	ct2_real = ct[16:32]		# 2nd block of the ciphertext

	# Try all possible bytes
	for x in range(256):
		guess = buffer + flag.hex() + f"{x:02x}"
		ct2_guess = bytes.fromhex(encrypt(guess))[16:32]
		if ct2_guess == ct2_real:
			flag += x.to_bytes()
			buff_len -= 1
			break

	print(flag)
```

Flag: `crypto{p3n6u1n5_h473_3cb}`

### Flipping Cookie

Challenge website: [https://aes.cryptohack.org/flipping\_cookie/](https://aes.cryptohack.org/flipping_cookie/)

This is a basic case of CBC mode bit flipping attack. Here, we know the structure of the plaintext. When decrypting in CBC, the decryption result is XOR-ed with the previous block's ciphertext (for the first block, with the `iv`). We can reverse the process (XOR-ing the known plaintext and the `iv`) to get the data after decryption (we will call it `xored` here). Then, we XOR `xored` with the new plaintext that we crafted. The result is then put as the new `iv`. This way, when the decryption happens, the block will decrypts to the new plaintext instead of the original plaintext.

```py
import requests

url = "https://aes.cryptohack.org/flipping_cookie/"

def get_cookie():
    response = requests.get(url + "get_cookie/")
    return response.json()['cookie']

def check_admin(cookie, iv):
    response = requests.get(url + "check_admin/" + cookie + "/" + iv)
    try:
    	return response.json()['flag']
    except:
    	return response.json()['error']

def hex_xor(hex1, hex2):
	hex1 = bytes.fromhex(hex1)
	hex2 = bytes.fromhex(hex2)
	res = b""
	for x, y in zip(hex1, hex2):
		res += (x^y).to_bytes()
	return res.hex()

# Get the cookie
full_cookie = get_cookie()
iv = full_cookie[:32]
cookie = full_cookie[32:]

# Flip the bytes
plain = b"admin=False;expi".hex()
new_plain = b"admin=True;expir".hex()
xored = hex_xor(iv, plain)
new_iv = hex_xor(xored, new_plain)

# Get flag
print(check_admin(cookie, new_iv))
```

Flag: `crypto{4u7h3n71c4710n_15_3553n714l}`

### Lazy CBC

Challenge website: [https://aes.cryptohack.org/lazy\_cbc/](https://aes.cryptohack.org/lazy_cbc/)

In this implementation of CBC, the key itself is used as the IV. Our goal is to leak the key using two available functionalities:

* `encrypt()` – Encrypts any input using the same key used for encrypting the flag.
* `receive()` – Takes a ciphertext as input and gives you the plaintext but only if the plaintext is unprintable.

To exploit the system, we begin by encrypting a block of empty bytes (`00000000000000000000000000000000`). This gives us the ciphertext `33a689f7d458770d1c1744e5ae5e38a2`.

Since XOR-ing any value with zero leaves it unchanged, this ciphertext is essentially the encrypted key (kind of like using ECB mode). If we could decrypt it directly, we'd obtain the key. Putting the ciphertext into `receive()` would only give us the original empty bytes, because using CBC, the decryption result is XOR-ed with the IV, or in this case the key.

To work around this, we could construct a new ciphertext, putting two of the ciphertext we have side-by-side, and adding an invalid block at the end to trick `receive()` into giving us the decryption result.

```
ciphertext + ciphertext + invalid block
33a689f7d458770d1c1744e5ae5e38a233a689f7d458770d1c1744e5ae5e38a2000000000000000000000000000000ff
```

Due to how CBC decryption works, the second block's plaintext will be the key XOR-ed with the previous block's ciphertext. Reversing the XOR operation will finally give us the key. And with the key, we can decrypt the flag.

Here is the full solver script.

```py
import requests

url = "https://aes.cryptohack.org/lazy_cbc/"

def encrypt(plaintext):
    response = requests.get(url + "encrypt/" + plaintext)
    return response.json()['ciphertext']

def get_flag(key):
    response = requests.get(url + "get_flag/" + key)
    try:
    	return response.json()['plaintext']
    except:
    	return response.json()['error']

def receive(ciphertext):
    response = requests.get(url + "receive/" + ciphertext)
    try:
    	return response.json()['success']
    except:
    	return response.json()['error'].split(": ")[-1]

def hex_xor(hex1, hex2):
	hex1 = bytes.fromhex(hex1)
	hex2 = bytes.fromhex(hex2)
	res = b""
	for x, y in zip(hex1, hex2):
		res += (x^y).to_bytes()
	return res.hex()

# Prepare the parameters
empty_bytes = "00000000000000000000000000000000"
invalid_block = "000000000000000000000000000000ff"
ciphertext = encrypt(empty_bytes)

# Get key and flag
dec_key = receive(ciphertext + ciphertext + invalid_block)[32:64]
key = hex_xor(dec_key, ciphertext)
flag = bytes.fromhex(get_flag(key))

print(flag)
```

Flag: `crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}`

### Triple DES

Challenge website: [https://aes.cryptohack.org/triple\_des/](https://aes.cryptohack.org/triple_des/)

DES is known to have several weak keys and semi-weak keys (more on [https://en.wikipedia.org/wiki/Weak\_key](https://en.wikipedia.org/wiki/Weak_key)). These keys can make DES encryption act as decryption. For example using a pair of semi-weak keys, this property holds:

```
Ek1(Ek2(m)) = m
```

Now, since we're dealing with triple DES, we can use a pair of weak keys for the first two encryption. For the third encryption, use half of the pair. Then, we encrypt the encrypted flag with a new set of keys. The first key being the other half, and the second and third key being another pair of semi-weak keys. In the end, we will be left with the flag's plaintext.

```py
import requests

url = "https://aes.cryptohack.org/triple_des/"

def encrypt(key, plaintext):
    response = requests.get(url + "encrypt/" + key + "/" + plaintext)
    return response.json()['ciphertext']

def encrypt_flag(key):
    response = requests.get(url + "encrypt_flag/" + key)
    return response.json()['ciphertext']

# Prepare the keys
DES_SEMI_WEAK_KEY_1 = "011f011f010e010e"
DES_SEMI_WEAK_KEY_2 = "1f011f010e010e01"
key1 = DES_SEMI_WEAK_KEY_1 + DES_SEMI_WEAK_KEY_2 + DES_SEMI_WEAK_KEY_1
key2 = DES_SEMI_WEAK_KEY_2 + DES_SEMI_WEAK_KEY_1 + DES_SEMI_WEAK_KEY_2

# Encrypt the flag
flag = encrypt_flag(key1)
flag = encrypt(key2, flag)

print(bytes.fromhex(flag))
```

Flag: `crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}`
