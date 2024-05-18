# Path Traversal

#### Solutions

1. `../../../etc/passwd` -> absolute path is blocked
2. `/etc/passwd` -> the website blocks relative path (`../` sequences) but interestingly allows absolute path
3. `..././..././..././etc/passwd` -> the string `../` is stripped, but not recursively
4. `../../../etc/passwd` encoded to url twice -> url decode on ascii would give the same result (so encoding the `/etc/passwd` part is optional); the system does "strip pattern, then decode url" twice, so we encode the pattern twice
5. `/var/www/images/../../../etc/passwd` -> system make sure that the beginning must be `/var/www/images/`
6. `../../../etc/passwd%00.jpg` -> system make sure that the ending must be `.jpg`. Null byte (`%00`) is treated like space in url. So from server side it's like reading 2 files: `cat ../../../etc/passwd .jpg`. There's a `passwd`, but no `.jpg` file.

#### Notes

* use burpsuite, check hhtp histories (request header on the jpg), repeater, inject payload
* why 3 backtrack on directories? because usually website files are in `/var/www/html`
