# GerakSendiri (106 pts)

> Author: 53buahapel
>
> Could you analyze this?

Pada soal ini kita diberikan file `chall.pcapng` dan sebuah instance server yang berisi beberapa pertanyaan. Saya menggunakan kode berikut untuk connect ke server.

```python
import asyncio
import websockets

async def connect_to_websocket(uri):
    async with websockets.connect(uri) as websocket:
        print("Connection opened!")

        while True:
            try:
                # get message from server
                message = await websocket.recv()
                print(f"{message.decode()}")

                # send input
                user_input = input("Enter message: ")

                # input handling
                if user_input.lower() == 'exit':
                    break
                else:
                    await websocket.send(user_input + '\n')

            except websockets.ConnectionClosed:
                print("Connection closed!")
                break
            except Exception as e:
                print(f"Error: {e}")
                break


uri = "wss://ctf.intechfest.cc/api/proxy/079b7720-7140-44ea-82b5-337de9c52dff"
asyncio.get_event_loop().run_until_complete(connect_to_websocket(uri))
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWfq7BKvYjs9IXegwBYVfOiY3Ti4J4KlVlIpGYrTMM3C1JZxjQ9N9DMAGLhvJvWqEeQ-Zug9SamO2upG6xIRY_-BYwDIoXVj9Y7nkmNBugMQoGkGdFIk86uZexGVATpc4_WuG4-5sLJsmG0E6wAwNSUbby?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Langsung saja jawab pertanyaannya.

### \[1/6] What is the device that attacker use to attack victim device? (answer in lowercase e.g. cpu)

Jika dilihat di Wireshark, pada file ini semua interaksi-nya menggunakan protokol Bluetooth.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe-xrj56sWEnYILKwt5RtfywrkKhPjz2hwHxhxL_rD0kIWqFnXtxoPnST0Ku9KdP3GQcXFZlf1pumQjNAKbvJo1knIwJLs0AmubBK36bdboaOuoOxEUJg37tVSHsiYqpxfFzJ7sJezjcsVYDKa-bd2DWMig?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

**Answer:** bluetooth

### \[2/6] What is the victim bluetooth name? (answer in lowercase e.g. ujang)

Pada salah satu paket (yang berada cukup awal), disebutkan nama device attacker serta victimnya.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcekMU6CJc8-ZlqOiIeDBDrvEQcDiAnUD8ScWLeQ1f4Hc28aXSbbxAZCfqGaw-Q0Stwm9VtcaHty-gGMtKZf7Dq5AqjGxRODQrsHMAYdanUL-HpY9sadykmpK5TSv5GbtyGv-L-6YA-8_s_W9cuxhMe54sT?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

**Answer:** asep

### \[3/6] What is the victim device MAC address (e.g. 00:11:22:33:44:55)

Jawabannya dapat ditemukan di tempat yang sama dengan jawaban No. 2.

**Answer:** 10:82:d7:92:50:80

### \[4/6] What is the first app that attacker use to open victim whatsapp? (answer in lowercase e.g. twitter)

Di sini attacker menggunakan "https://wa.me" untuk mengakses WhatsApp, oleh karena itu attacker menggunakan browser.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcLc7RArH049I2_jerBCoUzY_GJeTQLq92ijPnZC0UAbbFGM5EqXIaT8TtNtUtU75sLDbGMkfhA6PwT81imjouJBXqBWcdWvVo4SUw7Z94GLDTK21v0ce_xe926oNVQRWS-agg7vPAOhBgiJUh7Ok2EN1U?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

**Answer:** browser

### \[5/6] What is the message that attacker send to victim whatsapp?

Sebagaimana terlihat pada soal No. 4, pada file capture ini kita bisa melihat key yang “ditekan” attacker pada keyboard. Sebagai contoh, nilai dari key dapat dilihat pada packet seperti berikut.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSKghdhw49FVrd8arQSousBMEfh1cgCQZIuacMTQ62rKEH6lJWXyRsac3-KD7t3cgWAsCqQr8Ipb1d6SvzXAOrBv-dNNIL7zJqcNWLw53Mj_BTah40gklBX7sStkhqQ2txcrs1uejM3aGq-IFD-wxrBec?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Di sini, terdapat bagian `“02 00 11”`. Byte `“02”` menunjukkan bahwa tombol SHIFT ditekan, dan byte `“11”` menunjukkan bahwa key yang ditekan adalah huruf “n”. Dengan begitu, karakter yang dihasilkan adalah “N”. Tentu di sini keyboard tidak menggunakan value ascii, tapi menggunakan [standar USB](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf) (Hal. 53). Maka dari itu, saya membuat script berikut untuk membaca packet-packet keyboard ini dan mengekstrak karakternya.

```python
from scapy.all import *

keymap = {
            '04': 'a', '05': 'b', '06': 'c', '07': 'd', 
            '08': 'e', '09': 'f', '0a': 'g', '0b': 'h', 
            '0c': 'i', '0d': 'j', '0e': 'k', '0f': 'l', 
            '10': 'm', '11': 'n', '12': 'o', '13': 'p', 
            '14': 'q', '15': 'r', '16': 's', '17': 't', 
            '18': 'u', '19': 'v', '1a': 'w', '1b': 'x', 
            '1c': 'y', '1d': 'z', '1e': '1', '1f': '2', 
            '20': '3', '21': '4', '22': '5', '23': '6', 
            '24': '7', '25': '8', '26': '9', '27': '0', 
            '28': '\n', '2b': '\t', '2c': ' ', '2d': '-',
            '2e': '=', '2f': '[', '30': ']', '31': '\\',
            '32': '`', '33': ';', '34': '\'', '35': '`', 
            '36': ',', '37': '.', '38': '/'}
keymap_shift = {
            'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
            'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
            'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
            'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
            'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
            'z': 'Z',
            '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
            '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
            '-': '_', '=': '+', '[': '{', ']': '}', 
            ';': ':', "'": '"',
            ',': '<', '.': '>', 
            '/': '?',
            '`': '~',
            '\\': '|'
}

# get char from keyboard value
def convert_char(byte_value, shift):
    char = keymap[format(byte_value, '02x')]
    if shift:
        char = keymap_shift[char]
    return char

msg = ''

packets = rdpcap('chall.pcapng')

# iterate all packets, filter those that 
# ...contain keyboard value, length = 24
for i, packet in enumerate(packets):
    shift_on = False
    if len(bytes(packet)) == 24:
        data = bytes(packet)

        # data in this position checks if SHIFT button is pressed
        if data[15] == 2:
            shift_on = True

        # data in this position tells the values
        try:
            char = convert_char(data[17], shift_on)
            msg += char
        except:
            continue
        
print(msg)
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXey7RIYjEcknAZArVPnINlbnmhnZVhrnpuGEy1HJNcydbcHFHiY3HhmvnNjnHzRgtyEsLFpg-kTThD4jUo4LmBts1q2pJkgy873EPOr_J7xFHelUY5zxIBoLhjs63ModaVqNrpXm7FhCb3UQ0Z5Cz4Sb-4?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Pesan yang dikirim adalah string yang ditulis tepat setelah link whatsapp, yakni `l33t1337`

**Answer:** l33t1337

### \[6/6] Attacker trying to open browser again in private mode, there are an attachment that you can see.

Pertanyaan ini terjawab bersamaan dengan pertanyaan No. 5. Dengan meng-klik link undipmail yang diketikkan oleh attacker, kita akan mendapatkan sebuah video yang memiliki sebuah teks.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXetybKrCPVd3FT9AsOKTRLhZszMgifm3khfEGYJZcRZxvTXxclRsP6ioSB06VaRxiXDJVpbTeITBwSP2jcZ2fD3AGKynbNCmdYvaNDbTnA8i7bC77-50kuMjc0ibxy1CyrY9-nbt0xMnVs5QZB14pGQYHxJ?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

**Answer:** akhirnya aku dapet flag asikkkk

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfi7ZmJV0psZ3woQsOVcU6i_ZQ-9jwJok7W3PKEWsVRI7mwJbWAgHYDnvavkwCYqCK7k98Bw91yBX7dSw6HeGuhTsQeFJXi7qpBKLBOLy148EliXidvLlwevckaknTdvbLny-I6hfxNHBnq0j7Fh2Lk1PpD?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Flag: `INTECHFEST{bluetooth_could_be_dangerous_5dff7d}`
