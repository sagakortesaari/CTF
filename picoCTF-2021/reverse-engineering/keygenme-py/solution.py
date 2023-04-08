import hashlib 

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = "FRASER"
bUsername_trial = b"FRASER"

def check_key(key, username_trial):

    global key_full_template_trial
    print("len of key is", len(key_full_template_trial))

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial: # Initial part of the key should be equal to picoCTF{1n_7h3_|<3y_of_
            if key[i] != c:
                return False
            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True

def calc_key(): # Basically just repeating the steps found above
    mid = ""
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[4]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[5]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[3]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[6]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[2]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[7]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[1]
    mid += hashlib.sha256(username_trial.encode()).hexdigest()[8]
    return key_part_static1_trial + mid + key_part_static2_trial

user_key = calc_key()
if check_key(user_key, bUsername_trial):
        print("Found correct key! It is", user_key)
else:
    print("\nKey is NOT VALID. Check your data entry.\n\n")