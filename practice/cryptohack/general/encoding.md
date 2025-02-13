# Encoding

### ASCII

just take `chr()` using Python

```python
num = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

msg = ""
for n in num:
	msg += chr(n)

print(msg)
```

Flag: `crypto{ASCII_pr1nt4bl3}`

### Hex

take `bytes.fromhex()` using python

```python
ct = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(ct))
```

Flag: `crypto{You_will_be_working_with_hex_strings_a_lot}`

### Base64

use `base64.b64encode()` and `base64.b64decode`

```python
import base64

ct = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(base64.b64encode(bytes.fromhex(ct)))

# b'crypto/Base+64+Encoding+is+Web+Safe/'
# b64encode gives byte output, and b64encode can only take byte as input
```

Flag: `crypto/Base+64+Encoding+is+Web+Safe`

### Bytes and Big Integers

`bytes_to_long` works the same as taking hex value of each byte, concatenating them, and then converting base16 to base10 using `int(hex_string, 16)`.

```python
from Crypto.Util.number import *

# test
msg = b"hello"
res = int(msg.hex(),16)
print(res)			# 448378203247
print(bytes_to_long(msg))	# 448378203247

# chall
ct = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(ct))
```

Flag: `crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`

### Encoding Challenge

from the server we get json containing encoding type and encoded message. we have to decode accordingly.

```python
#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener # this is cryptohack's server-side module and not part of python
import base64
import codecs
import random

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
with open('/usr/share/dict/words') as f:
    WORDS = [line.strip().replace("'", "") for line in f.readlines()]


class Challenge():
    def __init__(self):
        self.challenge_words = ""
        self.stage = 0

    def create_level(self):
        self.stage += 1
        self.challenge_words = "_".join(random.choices(WORDS, k=3))
        encoding = random.choice(ENCODINGS)

        if encoding == "base64":
            encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
        elif encoding == "hex":
            encoded = self.challenge_words.encode().hex()
        elif encoding == "rot13":
            encoded = codecs.encode(self.challenge_words, 'rot_13')
        elif encoding == "bigint":
            encoded = hex(bytes_to_long(self.challenge_words.encode()))
        elif encoding == "utf-8":
            encoded = [ord(b) for b in self.challenge_words]

        return {"type": encoding, "encoded": encoded}

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self, your_input):
        if self.stage == 0:
            return self.create_level()
        elif self.stage == 100:
            self.exit = True
            return {"flag": FLAG}

        if self.challenge_words == your_input["decoded"]:
            return self.create_level()

        return {"error": "Decoding fail"}


listener.start_server(port=13377)
```

here is the solver.

```python
from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()
    encoding = received["type"]
    encoded = received["encoded"]    # note that encoded type is 'str'

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(encoded[2:],16)).decode()
    elif encoding == "utf-8":
        decoded = ''.join([chr(b) for b in encoded])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)


received = json_recv()
print(received)

# crypto{3nc0d3_d3c0d3_3nc0d3}
```

Flag: `crypto{3nc0d3_d3c0d3_3nc0d3}`
