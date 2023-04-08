# keygenme-py

`keygenme-trial.py`

## Solution

Running the program, we see a menu with several options presented to us. While investigating `keygenme-trial.py`, it looks like option c) presents an opportunity to enter a license key, which in turn will decrypt the `full_version` ciphertext at the bottom of the file. This will output a file called `keygenme.py`, so this is probably what we need to do.

Looking at the `enter_license` function called when selecting option c):

```
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```

The snippet above reveals that we need to make the `check_key` call return true. We can do this by basically following the same pattern as in `check_key`. See solution in `solution.py` 

(＾▽＾)