# Transformation

I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Solution

`enc` refers to a file that contains `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽`. Not entirely sure what language this is, but I cannot understand it.

I guess that the code given in the description is what was used to originally encode the flag. We'll have to reverse this, in order to obtain the plaintext.

Tldr of `solution.py` solving the problem:

- We loop through every character of `enc`.
- For every character, we first do `chr(ord(e_flag[i]) >> 8)` to obtain the first letter of the pair (cancels out the << 8).
- For the second letter of the pair, we need to do `chr(e_flag[i].encode('utf-16be')[-1])`. Basically, we convert the character to bytes, and then do `[-1]` to get the least significant byte, that is `ord(flag[i + 1])`. 
- We append these two letters to the `flag` variable which is printed at the end.

### Solution 2

After solving it using the approach above, I also realized that we can actually obtain the flag simply by reading it from the file & then doing `e_flag.encode('utf-16be')`. 


