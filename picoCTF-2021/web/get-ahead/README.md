# Get aHEAD

"Find the flag being held on this server to get ahead of the competition"
http://mercury.picoctf.net:34561/

## Solution

Looking at the website, we see two buttons "choose red" / "choose blue". The first one, "choose red", sends a GET-request meanwhile "choose blue" sends a POST-request to http://mercury.picoctf.net:34561/index.php. 

A bit strange that they're using two different request types, let's try some other ones. E.g. PUT, DELETE makes no difference. But HEAD gives us.. a flag! (＾▽＾)

```
$ curl --head http://mercury.picoctf.net:34561/index.php
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_8f878508}
Content-type: text/html; charset=UTF-8
```