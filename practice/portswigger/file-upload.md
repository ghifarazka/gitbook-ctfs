# File Upload

## Description

* uploading some kind of script (in a file) into the server
* triggering the script by requesting the file
* for example, entering `example.com/file.php` would **run** the php file
* we can put malicious code in the php file
* most dangerous outcome from this attack is running a webshell (RCE), basically giving the hacker full-control of the target

**Times where File Upload could be malicious:**

* uploading code then running it -> RCE
* uploading large sized files -> DoS attack
* uploading files very frequently -> rate-limit attack

In the wild, websites implement some kind of validations. The vulns are in the flaws of those validations. Interestingly, the validations might be applied inconsitently throughout a network and even between directories.

### Validations

Usually, what are validated by the server?

* file name
* file extension (by name, by http header, by file header)
* file size
* file hash
* file path (?)(to prevent directory traversal)

What a server would do to files? **non-exe** -> send the file contents **exe & run** -> get input from the request, then send output **exe & don't run** -> give error & maybe send the code as plaintext

### Bypassing server configurations

By default, servers won't execute files unless configured to do so. Devs have to add this to the `/etc/apache2/apache2.conf` file:

```
LoadModule php_module /usr/lib/apache2/modules/libphp.so
    AddType application/x-httpd-php .php
```

There's also special configurations for directories. In apache, it uses the `.htaccess` file. The "language" used in `.htaccess` is the same with `apache2.conf`. Meanwhile, IIS servers use `web.config` file. This one allows json:

```
<staticContent>
    <mimeMap fileExtension=".json" mimeType="application/json" />
    </staticContent>
```

Usually, you can't access config files via http requests (forbidden error), but some servers don't prevent you to upload one.

### Obfuscating file extensions

Original file name: `exploit.php`

* validation code do case sensitive, while MIME mapper don't: `exploit.pHp`
* multiple extensions: `exploit.php.jpg`
* trailing chars: `exploit.php.`
* URL encoding; works if the decode is server-side: `exploit%2Ephp`
* if validation code use high-level (PHP/Java) but the server uses lower-level (C/C++), we can manipulate the filename ending with `;` or null byte: `exploit.asp;.jpg` or `exploit.asp%00.jpg`
* multibyte unicode characters, like `xC0 x2E`, `xC4 xAE` or `xC0 xAE` may be translated to `x2E` in UTF-8: `exploit%C0%2Ephp`
* string stripping: `exploit.p.phphp`

### Other types of flawed validation:

* checking if the file has dimensions (to make sure it's an image)
* checking the file signature, usually using the `file` program on linux (much better, but still not foolproof)

### File upload race conditions

* some apps dont upload files directly to the filesystem, but uses temporary place and randomize name to prevent overwriting
* only then would they validate and send it to the actual filesystem
* some system doesn't; a system may let the file sit in the file system, then remove it if it doesn't pass the validation. this is usually the case if they rely on some antivirus program.
* if the file upload is using url, the server has to fetch from the internet and then perform the validation. when the file is loaded using http, devs cant use framework built in functions, so they make their own implementation in storing and validating the file
* we can bruteforce the directory name if it's generated using pseudo-random functions like PHP's uniqid(). we can lengthen the time window of file processing by uploading large file and putting the payload at the beginning

### other exploit than RCE

* client-side scripts: upload html or svg, then use the `<script>` tag for XSS (restricted by the same origin policy)
* vulns specific to the parsing or processing of diff file formats (exp. xml-based files like .doc and .xls might be a potential vector for XXE injection attacks)

### using PUT requests

* check by sending OPTIONS requests
* put can upload files, even when it's not possible in the web interface

```
PUT /images/exploit.php HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-httpd-php
Content-Length: 49

<?php echo file_get_contents('/path/to/file'); ?>
```

## Lab solutions

**Lab 1**&#x20;

Just upload the file

**Lab 2**&#x20;

Upload, then change content-type to image/png

**Lab 3**

* change file name utilizing directory traversal -> `filename="../exploit.php"`
* notice the msg `The file avatars/exploit.php has been uploaded.`, meaning that the payload has been stripped
* obfuscate payload with url encode, `filename="%2e%2e%2fexploit.php"`
* script is uploaded, now `GET files/exploit.php`

**Lab 4**

* upload `.htaccess` with this setting: `AddType application/x-httpd-php .evil` ('evil' is an arbitrary file ext)
* it basically will read any file ending in `.evil` as php file, so it's able to run `exploit.evil` as php
* it will bypass the php filter, and will show like this in the http header:

```
Content-Disposition: form-data; name="avatar"; filename="exploit.evil"
Content-Type: application/octet-stream
```

* after `exploit.evil` is uploaded, just do access/http request to the file

**Lab 5**&#x20;

It seems that the validator only accepts a file if it ends in `.png`, and the MIME type mapping is based on the file extension. Here we can still put the `.png` while cutting the filename in the middle with a null byte. Payload: `filename="exploit.php%00.png"`

**Lab 6**&#x20;

Get a png file and append the php code at the end of the file, then upload. php code would still run even when there's gibberish at the beginning. Payload: `filename="exploit.php"` and `Content-Type: application/x-php`
