import binascii
from pwn import *

# pecah token menjadi ke dalam blocks (block ct/ciphertext)
token = "616161616161616161616161616161613158228d2906da956841283e1ced5ecf01b0f91e1ee6fba991e2e00b1424c13abf87394beb915c71a3a7e9e9dff5bf0bce1da0b07d3db0cbd3dbd9a313532d34c85dbe72d4c15eb712575d30fa6e96e362aeb61b3dbd527897153fa6c89ba9a8"
token = bytearray(binascii.unhexlify(token))
ct = [token[i:i+16] for i in range(0, len(token), 16)]

# untuk ct3, lakukan bit flipping
# note: kenapa index block ciphertextnya 4 dan bukan 3, karena kalau di token, block ke-0 nya itu IV
ct[4][-3] = ct[4][-3] ^ ord("0") ^ ord("9")
ct[4][-2] = ct[4][-2] ^ ord(".") ^ ord("e")
ct[4][-1] = ct[4][-1] ^ ord("0") ^ ord("9")

# print hasil token baru, submit ke server
for cipherblock in ct:
	print(binascii.hexlify(cipherblock).decode(), end="")

print()

# plaintext (per block)
pt0 = '{"username": "aa'
pt1 = '", "password": "'
pt2 = '23ca472302f49b3e'
pt3 = 'a5592b146a312da0'
pt4 = '", "saldo": "0.0'
pt5 = '00"}'

# untuk ct2, lakukan bit flipping
# note: lagi2 kenapa ct[3] dan bukan ct[2], itu karena index pertama dipake sama iv
newpt = '7b22757365726e616d65223a20226161222c202270617373776f7264223a20223233636134373233303266343962336561b0e2661a8e54b6234dc61f0eeacfa3222c202273616c646f223a20223965393030227d'
newpt = bytearray(binascii.unhexlify(newpt))
newpt = [newpt[i:i+16] for i in range(0, len(newpt), 16)]

ct[3] = xor(xor(ct[3], newpt[3]), pt3)

# print hasil token baru, submit ke server
for cipherblock in ct:
	print(binascii.hexlify(cipherblock).decode(), end="")

print()

# untuk ct1
newpt = '7b22757365726e616d65223a20226161222c202270617373776f7264223a202262a980d5cb7fe90d942a11435a8653e161353539326231343661333132646130222c202273616c646f223a20223965393030227d'
newpt = bytearray(binascii.unhexlify(newpt))
newpt = [newpt[i:i+16] for i in range(0, len(newpt), 16)]

ct[2] = xor(xor(ct[2], newpt[2]), pt2)

# print hasil token baru, submit ke server
for cipherblock in ct:
	print(binascii.hexlify(cipherblock).decode(), end="")

print()

# untuk ct0
newpt = '7b22757365726e616d65223a20226161446e1cbca0d127d59c1760010dedf79b3233636134373233303266343962336561353539326231343661333132646130222c202273616c646f223a20223965393030227d'
newpt = bytearray(binascii.unhexlify(newpt))
newpt = [newpt[i:i+16] for i in range(0, len(newpt), 16)]

ct[1] = xor(xor(ct[1], newpt[1]), pt1)

# print hasil token baru, submit ke server
for cipherblock in ct:
	print(binascii.hexlify(cipherblock).decode(), end="")

print()

# untuk iv
newpt = '39d69ec2f0e01242f809eb97a9279ec0222c202270617373776f7264223a20223233636134373233303266343962336561353539326231343661333132646130222c202273616c646f223a20223965393030227d'
newpt = bytearray(binascii.unhexlify(newpt))
newpt = [newpt[i:i+16] for i in range(0, len(newpt), 16)]

ct[0] = xor(xor(ct[0], newpt[0]), pt0)

# print hasil token baru, submit ke server
for cipherblock in ct:
	print(binascii.hexlify(cipherblock).decode(), end="")

print()

# Token akhir: 23958ad0f4f31d42f40da8cce8649ec0571a1e13f9b68e3383393a5b333a8976512a1aaae1ae209735fa977c77c0a1bebf02ee14c37d39f3b68b1cc7e37b1198ce1da0b07d3db0cbd3dbd9a3135a663dc85dbe72d4c15eb712575d30fa6e96e362aeb61b3dbd527897153fa6c89ba9a8