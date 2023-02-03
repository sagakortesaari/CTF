# Mind your Ps and Qs

In RSA, a small e value can be problematic, but what about N? Can you decrypt this?

## Solution

Problem contains a file with

```
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```

Having a small N means that it's easy to find the prime factors. With the prime factors, we can easily calculate φ(N). We know that e (public key) is calculated as:

e = pick a number e s.t. sgd(e, φ(N)) = 1

The secret key, d, is then calculated as:

d = e^(-1) mod φ(N)

Since we know e, and can calculate φ(N), we can easily find the secret key d, and then decrypt c.

I used https://www.dcode.fr/prime-factors-decomposition to calculate the prime factors :) 



