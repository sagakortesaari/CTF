# Cookies

Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:29649/

## Solution

Searching for something obviously wrong gives: ```That doesn't appear to be a valid cookie```

Lets try something that actually *is* a valid cookie, ```snickerdoodle``` as the placeholder suggests. This gives: ```I love snickerdoodle cookies!```, upon inspecting the requests further we can see that a GET request is being sent to /check together with

```
Cookie: name=0
```

Let's try changing that to 1. We're now met with ```I love chocolate chip cookies!``` which suggests that each cookie must be represented by some kind of ID. We can write a simple python script for this: check all ID's up to 20 and return in case we don't get the ```"I love ..."``` 