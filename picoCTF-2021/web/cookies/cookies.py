import requests

for i in range(0, 20):
    cookies = {'name': str(i)}
    r = requests.get('http://mercury.picoctf.net:29649/check', cookies=cookies)
    
    if not "I love" in r.text:
        print("The id was", i, r.text)
    