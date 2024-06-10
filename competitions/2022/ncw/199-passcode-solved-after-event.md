# 199 passcode (Solved after event)

Diberikan file 199passcodehahahoho.pyc. Pertama-tama, kita decompile dulu file ini menggunakan tool [https://www.decompiler.com/](https://www.decompiler.com/). Setelah itu, kita dapatkan source code sebagai berikut.

```python
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04)
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: soal.py
# Compiled at: 2022-11-07 09:36:17
# Size of source mod 2**32: 4776 bytes
import tkinter as tk
from tkinter import *
from Crypto.Util.number import *
from tkinter.messagebox import *
import random
turn = 0
random.seed(0)

def main():
    global turn

    class Node:

        def __init__(self, data):
            self.data = data
            self.l = None
            self.r = None
            self.height = 1

    class AdelsonVelskiiLandis:

        def insert(self, root, key):
            if not root:
                return Node(key)
                if key < root.data:
                    root.l = self.insert(root.l, key)
                else:
                    root.r = self.insert(root.r, key)
                root.height = 1 + max(self.getHeight(root.l), self.getHeight(root.r))
                b = self.getBal(root)
                if b > 1:
                    if key < root.l.data:
                        return self.rRotate(root)
                if b < -1:
                    if key > root.r.data:
                        return self.lRotate(root)
            else:
                if b > 1:
                    if key > root.l.data:
                        root.l = self.lRotate(root.l)
                        return self.rRotate(root)
                if b < -1 and key < root.r.data:
                    root.r = self.rRotate(root.r)
                    return self.lRotate(root)
            return root

        def lRotate(self, z):
            y = z.r
            T2 = y.l
            y.l = z
            z.r = T2
            z.height = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
            y.height = 1 + max(self.getHeight(y.l), self.getHeight(y.r))
            return y

        def rRotate(self, z):
            y = z.l
            T3 = y.r
            y.r = z
            z.l = T3
            z.height = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
            y.height = 1 + max(self.getHeight(y.l), self.getHeight(y.r))
            return y

        def getHeight(self, root):
            if not root:
                return 0
            return root.height

        def getBal(self, root):
            if not root:
                return 0
            return self.getHeight(root.l) - self.getHeight(root.r)

        def check(self, state, root, n, x):
            state = root
            for i in n:
                if i == '0':
                    state = state.l
                else:
                    if i == '1':
                        state = state.r
                if state == None:
                    showwarning(title='error lur', message='Error invalid node!\nResetting level...')
                    return False
                if state.data == x:
                    return True
                showwarning(title='yah', message='Wrong answer! \nResetting level...')
                return False

    def decrypt(key, plain):
        dec = ''
        key = long_to_bytes(int(''.join(key), 2))
        for i in range(len(key)):
            dec += chr(key[i] ^ plain[i])
        else:
            return dec

    def initialization():
        tr = AdelsonVelskiiLandis()
        root = None
        for i in init:
            root = tr.insert(root, i)
        else:
            return (
            tr, root)

    def submit(root):
        global turn
        try:
            u = inp.get()
            if not tr.check(0, root, u, target[turn]):
                turn = 0
                validatedkey.clear()
            else:
                showinfo(title='anjay', message='Correct!')
                validatedkey.append(u)
                inp.delete(0, 'end')
                turn += 1
            if turn == len(target):
                showinfo(title='kelazzz', message=(decrypt(validatedkey, FLAG)))
        except SyntaxError:
            showerror(title='Error', message='Invalid input!')
        else:
            text.set(199 - turn)

    num = [i for i in range(1, 201)]
    init = num.copy()
    random.shuffle(init)
    FLAG = [70, 106, 196, 124, 8, 66, 39, 192, 6, 86, 222, 245, 244, 101, 138, 58, 30, 27, 51, 31, 63, 175, 0, 3, 25, 58, 24, 225, 209, 18, 7, 253, 185, 174, 197, 236, 7, 171, 127, 126, 232, 243, 65, 171, 144, 237, 160, 22, 105, 213, 23, 12, 35, 20, 105, 144, 235, 96, 74, 96, 37, 207, 95, 111, 24, 156, 0, 165, 123, 211, 243, 141, 213, 104, 71, 106, 157, 252, 198, 22, 19, 73, 6, 154, 31, 47, 157, 200, 255, 246, 161, 214, 226, 97, 196, 87, 61, 201, 204, 192, 130, 73, 143, 58, 243, 190, 72, 9, 131, 29, 20, 89, 235, 149, 143, 178, 154, 47, 102, 141, 11, 158, 96, 28, 34, 168, 62, 204, 204, 74, 9, 205, 209, 133, 2, 58, 20, 108, 206, 224, 125, 223, 66, 21, 143, 157, 21, 203]
    validatedkey = []
    tr, troot = initialization()
    target = init.copy()
    target.remove(troot.data)
    random.shuffle(target)

    def on_focus_in(entry):
        if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')

    def on_focus_out(entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.configure(state='disabled')

    root = tk.Tk()
    root.geometry('300x150')
    root.title('Kunci Pintu')
    root.maxsize(300, 150)
    root.minsize(300, 150)
    inp = Entry(root, width=33, borderwidth=3, relief=RIDGE)
    inp.grid(pady=5, row=0, sticky='w', padx=15)
    inp.insert(0, 'Input Secret Key')
    inp.configure(state='disabled')
    x_focus_in = inp.bind('<Button-1>', lambda x: on_focus_in(inp))
    submitbutton = Button(root, text='submit', width=30, command=(lambda : submit(troot)), bg='red', fg='white', borderwidth=3, relief=RIDGE)
    submitbutton.grid(row=1, sticky='w', padx=15, pady=5)
    text = StringVar()
    text.set(199 - turn)
    textbox = Label(root, textvariable=text, justify='center', width=13)
    textbox.config(font=('Courier', 30))
    textbox.grid(pady=5, row=2, sticky='w')
    root.mainloop()


if __name__ == '__main__':
    main()
```

Ketika kodenya dicoba di-run, muncul sebuah error yang mengarah pada fungsi insert di dalam kelas AdelsonVelskiiLandis. Rupanya pada bagian ini sepertinya ada error pada saat proses decompiling.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeP2zJZ4eDAlVCVxdIRbA6vy0kBvQm53xta2oZt6K67VUKltmAkDiMECaCerUOEbE5jXiJ_1mydzCOq5bWc6NX7b9rBUIfCelOMQwFGC47gbVY1Gy5Z5QAxiCaAoTtui68uWOgyUGByZiGDcfAFyYip7S0gu3hlL5eMCfLvJP2wBqWaYAHXNpI?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfp9B72c6AOGQNsShoryYNa5H5t4gW5d9molvGELvlirGcADnNXVJL2tzmdQ_PbBTI8aje9upe20JXFWrcj3CEFVG4dKSEWcf1yXMxwULD6N9Rqea71vHPeWUWWcFyZyk4Aogv-LGRse1tKIYzl-5mBZrhogrPpdzOS0g6pBwKymUKxeL2kMe8?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

Di sini yang terlihat aneh adalah adanya serangkaian if-else setelah return, padahal kalau seperti itu maka tidak akan terbaca. Oleh karena itu, kami mencoba untuk menggesernya 1 tab ke kiri. Selain itu, di bagian paling bawah tertulis if b < -1 and key < root.r.data: tapi untuk conditional if’s di atasnya tidak. Oleh karena itu kami coba samakan cara penulisannya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeYjXwccYmZY5qAhPhjIi422Unbx0cZtqlk0m7RrfAsz3Wbq_G7pmNfiAjJxoQF4hKQvbfkWI0nTQZHae6zTe6dkOJ_-igG3D54Lmo0vc-IfljLY71Gao6O7curwAKm7s3c1grTcGTlDbrGlbQqvgb7Cafh5fn24_nsccn8vbC-8-QALKXfl7Y?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

Setelah mencoba memahami kode dari source code-nya, kami menyadari bahwa ini adalah semacam program permainan guess the passcode di mana passcode yang diminta adalah sebuah string yang merepresentasikan path/langkah yang diambil untuk mencari sebuah node dalam AVL Balanced Binary Search Tree (BBST). Jadi misalnya node paling atas itu root, lalu child nodenya ada dua, node yang di kiri nilainya lebih kecil dan node yang di kanan nilainya lebih besar, lalu masing-masing node tersebut memiliki dua child node juga, yang kiri lebih kecil dan yang kanan lebih besar, dan seterusnya. Nah untuk mencari node-node tersebut, kita bisa menuliskan sebuah baris string di mana ‘0’ berarti ‘ke kiri’ dan ‘1’ berarti ‘ke kanan’ sebagaimana yang dijelaskan dalam fungsi check di dalam kelas AdelsonVelskiiLandis.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcNGo34AtDzgTxiEmsSEl4hwZCNfjz8DPA00csYGFhbv89mGZUt0-uopxScyqJ9xqMiWRe-4OmWjUMsD96SUQAP9blZB-iWAGDjsUt6zOazp2qilefuWp3a7SIPHtd0VXXonFYqqO46wHp5Ye-9rZYVF8849rP-mNtjHD0URp3euySUqnRLar0?key=Og-FONF8VP6Ffi-U5Fl57Q" alt="" width="375"><figcaption></figcaption></figure>

Sementara itu, di source code juga ada list target yang berisi nilai-nilai yang ingin dicari dari BBST tersebut. Jumlah angka dalam target ada 199 angka, dan jumlah turn yang kita miliki dalam permainan ini adalah 199, jadi kita harus menebak semua path dengan benar supaya variabel validatedkey terisi penuh dan fungsi decrypt terpanggil lalu kita mendapatkan flag.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfv6X8PsTSqwJm0m2wTkFtc7fhko43X51-ZObEOCIEvJEc5zMibS6-wV-AUWtAdPDqJNXb0ebuMZ1jBQHKIh7fSLVLU7L3asa48PEPY8AeL_tQ2v9xmWWGInnRVbkyCtHjno1Friykcgf1J04FrcYA_JAuxqBI-YVIxjDzX2XySiRy_-ETRvi0?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

Untuk mendapatkan path untuk semua elemen di target, kita bisa menambahkan fungsi search berikut ke dalam kelas AdelsonVelskiiLandis. Lalu kita loop untuk semua elemen di target dan kita masukkan ke dalam list key\_list. Kalau sudah selesai tinggal kita panggil fungsi decrypt lalu kita masukkan key\_list dan FLAG sebagai argumennya.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXd6Dzt-ULwiyp_eGnzCiBNrIK2T6Q_08hy-eSpe9yb-4wM15TZ3_kSLZgMPv8SSs-mmFTmzZXRotKxKyOeliY2yqnb57cnbMgUzMrgmGw8WRvKBbswH1Rbgu0DmDFwZzei8QCoVCWdJdGcxS0lF0iNAtXpgPMtVByp5fk05VLSO1acnZ3R-5Q?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXedpPNrYg8ceao7pZJpJv_waEKloBT3lfrbvAfk78ipznn7MQf5A8Rlp1t3p6MsE2lo_QmIPXN985z33m0ydSkcvHt4YNOygThmDHfq0dc_q6znBhRIc26RpZ5_ZVRXEXFkwKPqdxKUXbKQzt71jo9TImSPfgb8dTURPzsDy7IsuT_QCctThg?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

Flag-pun kita dapatkan.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeYHrW-X6_sJpCQ2hnnfhqQpd7_ubptJpS4_f3YmaPahSULMdEFgrqtX42vxLYhgN6llnEXiJOKV81kuCVnKwYqJNqqwHKh7_nOwnO5my8hGVHECvLlcjk3pnTq-of6YBybFj_dgqgebAKjAfS9tQVDqoxm7_Q-P10FqqVVsOBOil0johhbtg?key=Og-FONF8VP6Ffi-U5Fl57Q" alt=""><figcaption></figcaption></figure>

Flag: NCW22{congratz\_you\_have\_successfully\_decompiled\_the\_pyc\_then\_solving\_the\_tree\_traversal\_problem\_and\_find\_this\_flag\_damn\_you\_really\_deserve\_it\_champ}
