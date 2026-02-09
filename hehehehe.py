# just some random code nothing to see here hehe

import base64

def definitely_not_important():
    # gummy wrote this part
    x = "QlNVe2cwdF95MHVfZzAwZF9oM2gzfQ=="
    return x

def random_numbers():
    # these arent clues i just like numbers
    a = 192
    b = 168
    c = 1
    d = 1
    print(f"favorite numbers: {a}.{b}.{c}.{d}")

def party_encryption(message):
    # twilight taught me about "ciphers"
    result = ""
    for char in message:
        if char.isalpha():
            shift = 13
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

# testing my cipher!!!
secret = party_encryption("gummyisthebestpet")
print(secret)
