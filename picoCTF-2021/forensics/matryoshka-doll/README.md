# Matryoshka doll

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: `dolls.jpg`

## Solution

Probably something hidden in `dolls.jpg`. I tried extracting data using the usual `exiftool`, `strings` etc but nothing found.

However, I checked for hidden embedded files with `binwalk -Me dolls.jpg` which recursively extracts any files embedded within the `.jpg`, where one of the embedded files contained the flag!

