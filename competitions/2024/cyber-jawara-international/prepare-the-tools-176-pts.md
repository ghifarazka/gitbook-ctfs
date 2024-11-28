# prepare the tools (176 pts)

> lets preparing our tools!

We're given a file named `preparingtools.pcapng`.&#x20;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

This is what we'll see if we follow the TCP stream.

<figure><img src="../../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

We can see a bunch of message with the format "flag\[number]letter". My theory is that the letters would make a clear message if ordered according to the numbers. To do that, I put all the messages in `message.txt` and wrote this code.

```python
content = open("message.txt", "r").read()

msg = ""

# using the format flag[xxxx]y
# look for xxxx, add the y to msg

for i in range(10000):
    search_string = f"flag[{i:04}]"
    print(search_string)

    index = content.find(search_string)

    if index != -1 and ((index + len(search_string)) < len(content)):
        msg += content[index+len(search_string)]
    else:
        print("searching is completed")
        break

result = open("result.txt", "w")
result.write(msg)
```

Here's the result :)

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

Flag: `CJ{warm_up_for_your_scapy/pyshark/tshark}`
