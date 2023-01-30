# More Cookies

I forgot Cookies can Be modified Client-side, so now I decided to encrypt them! http://mercury.picoctf.net:34962/

## Solution

We're met with `Welcome to my cookie search page. Only the admin can use it!` on the website. Inspecting the HTML shows nothing weird, however, we have a cookie `auth_name` which is currently set to `M3ZvVTZUZEwxZHAzSFZKbkRHbEFTbzNyTGlDZ1RSKzZtS09IVmJOazdTcTZBc212MjBubzJVUG5VakNVTWovVWxNUUR5WGNqU0VNOEluNithVjJUWkpwRG9jUlRQSHdSOHdwTEwwQm1kVmM5U0Z3WVp5WG1xL0Vab0orbkxWVHA=`. 

Base64 decoding this results in `3voU6TdL1dp3HVJnDGlASo3rLiCgTR+6mKOHVbNk7Sq6Asmv20no2UPnUjCUMj/UlMQDyXcjSEM8In6+aV2TZJpDocRTPHwR8wpLL0BmdVc9SFwYZyXmq/EZoJ+nLVTp` -- which still seems to be decoded in Base64, so we need to decode it another time.

At this point I was feeling pretty stuck, so I decided to check one of the hints. The hint provided a link to [Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) on Wikipedia. I also realized that the capital letters of the problem description spells out CBC, which probably means that the cookie has been encrypted in CBC mode. CBC is homomorphic, and is vulnerable to the so-called bit flipping attack. (I remember this from my crypto course!!（＾ω＾))

We assume that the cookie contains a bit somewhere that indicates whether you are an admin or not. Since we're currently not an admin, we can assume that this bit is set to 0 in the plaintext. Since CBC is homomorphic, we can try flipping every bit (by doing ⊕ 1) until we have successfully managed to spoof an admin cookie. 

### General remarks

I got stuck on this problem for quite long, mostly because of the script I was writing to flip the bits. I didn't realize that `bytes(decoded[i]^x)` returned 4 bytes, which obviously didn't work. Instead, we need to use `(decoded[i]^x).to_bytes(1, 'big')` since we want 1 byte, not several bytes. 

Overall a very interesting problem, I recall this type of attack from my crypto course & it was interesting to actually implement it myself 🎉













