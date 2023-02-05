f = open("enc", "r")
e_flag = f.read()

flag = ""
for i in range(0, len(e_flag)):
    flag += chr(ord(e_flag[i]) >> 8)
    flag += chr(e_flag[i].encode('utf-16be')[-1])

print(flag)

## Alternative solution

print(e_flag.encode("utf-16be"))