# It is my Birthday

I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:55343/

## Solution

Pretty simple, just google for two files that have the same md5 hash (I found mine [here](https://www.mathstat.dal.ca/~selinger/md5collision/)). Submit them on the website, and you'll see the flag. 

# General remarks

Not sure how this challenge is worth 100 points tbh. `more-cookies` was more difficult despite being worth less points. Oh well.

