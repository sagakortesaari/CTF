# Easy Peasy

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 36981 otp.py

## Solution

OTP is calculated as cipher = message ⊕ key, where the message and key are of equal size.

From `otp.py`: Initially, it encrypts the flag, and then keeps accepting new plaintext messages to encrypt until it hits 50k encrypted characters, and then it just loops around again (re-using the same key). We can utilize the fact that It's using the same key, in order to break the OTP. 

Connecting to the netcat instance reveals: 

```
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c

What data would you like to encrypt?
```

If we first make it encrypt stuff until it has encrypted 50k characters, the key will start over so it'll use the same sequence for the next message we want to encrypt. What we want to input then is a message of same size as the plaintext flag, which is `len(encrypted flag)/2` (It's in hex, so ascii length is / 2). Even better, we can just send `unhex(flag)` and it'll just give us the flag (in plaintext) back. This is due to the initial encrypted flag being encrypted as c = plaintext-flag ⊕ key. If we input this c into the OTP again, with the same key, what will happen is: new_c = c ⊕ key = plaintext-flag ⊕ key ⊕ key = plaintext-flag



