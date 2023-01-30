# Who are you?

Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:46199/

## Solution

Upon visiting the url we see `Only people who use the official PicoBrowser are allowed on this site!`. Okay, let's add `User-Agent: PicoBrowser`. 

After adding the `User-Agent` header, we instead see `Only people who use the official PicoBrowser are allowed on this site!` Solution is to simply add `Referer: http://mercury.picoctf.net:46199/`.

Again `Sorry, this site only worked in 2018.` Let's add `Date: Wed, 21 Oct 2018 07:28:00 GMT` to the request. 

`I don't trust users who can be tracked.` needs a `DNT: 1`.

`This website is only for people from Sweden.` all this requires is a Swedish IP-address added to the request: `X-Forwarded-For: 105.17.176.0`

`You're in Sweden but you don't speak Swedish?` requires a `Accept-Language: sv` header.

Finally, we can see the flag on the page `picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_8d5d8d77}` :)


