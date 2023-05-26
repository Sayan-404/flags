import random

def str_xor(secret, key):
    # Extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])


flag_enc = chr(0x04) + chr(0x07) + chr(0x06) + chr(0x08) + chr(0x02) + chr(0x3c) + chr(0x05) + chr(0x5f) + chr(0x01) + chr(0x02) + chr(0x24) + chr(0x46) + chr(0x42) + chr(0x56) + chr(0x0c) + chr(0x48) + chr(0x02) + chr(0x1d) + chr(0x17) + chr(0x11) + chr(0x53) + chr(0x19) + chr(0x5f) + chr(0x1f) + chr(0x15) + chr(0x4e) + chr(0x02) + chr(0x1d) + chr(0x51) + chr(0x04) + chr(0x17) + chr(0x00) + chr(0x48) + chr(0x5b)

key = 'decryption_key'

flag = str_xor(flag_enc, key)
print('The flag is: ' + flag)

