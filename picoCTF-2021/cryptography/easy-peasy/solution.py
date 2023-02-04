import pwn
from pwn import *

p = pwn.remote("mercury.picoctf.net", 36981)
p.recvuntil(b"flag!\n")
flag = p.recvline()[0:-1]
p.recvuntil(b"?")
num_encrypted = int(len(flag) / 2)

# Make the key "start over" so we're at the first bit again
while num_encrypted < 50000:
    if num_encrypted + 1000 < 50000:
        payload = b"a"*1000
    else:
        payload = b"a"*(50000 - num_encrypted)
    p.sendline(payload)
    p.recvuntil(b"?")
    num_encrypted += len(payload)

p.sendline(unhex(flag))
p.recvline()
print("Flag: ", unhex(p.recvline()).decode())




