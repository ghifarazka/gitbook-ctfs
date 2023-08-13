from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *


# get kpt blocks
# block akhir adalah padding
kpt = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
kpt_blocks = [kpt[i : i + 16] for i in range(0, len(kpt), 16)]
kpt_long = [bytes_to_long(block) for block in kpt_blocks]

# get kct blocks
# nilai kct didapat dari service
kct = long_to_bytes(6829951403668095693309986486905719260569051797920733302729965370271912526388434640204350969195421713114899203197885934717004778596521377164114674546876406246515072569075972400049924888032406986114289369421990665247175570930943928793049468915942681596697204857114479815014582084032067986263466346410844470912198444839419902147197659011658208607070301783523273433848482670178279509991871)
kct_blocks = [kct[i : i + 16] for i in range(0, len(kct), 16)]
kct_long = [bytes_to_long(block) for block in kct_blocks]

# get iv blocks
iv = []
for pt, ct in zip(kpt_long, kct_long):
	iv.append(pt ^ ct)


# get ct blocks
# nilai ct didapat dari service
ct = long_to_bytes(38198144279787283082101962426498963475592339373164672851410243695866139623602242834200207503977231528184195924441518387793673105101868024620672293724434121976042294194760387016674347449520323633716880022698049765002913443806371121997968768973993844710535293298796344978323974167410473156135000226332738944539088325979705730893316968886967264991045)
ct_blocks = [ct[i : i + 16] for i in range(0, len(ct), 16)]
ct_long = [bytes_to_long(block) for block in ct_blocks]

# get pt blocks (the original secret)
result = []
for m, ct in zip(ct_long, iv):
	result.append(m ^ ct)


# menyatukan blocks
res_blocks = [long_to_bytes(block) for block in result]
secret = b"".join(res_blocks)
secret = unpad(secret,16)		# jangan lupa unpad
print(bytes_to_long(secret))