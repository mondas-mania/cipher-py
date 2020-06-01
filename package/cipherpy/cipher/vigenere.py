import string
from . import caesar_encode
from ..base import atbash

# Vigenere Cipher

def encode(plain_txt, key, alphabet=string.ascii_lowercase):
    while len(plain_txt) > len(key):
        key = key + key
    new_txt = ''
    for pos, char in enumerate(plain_txt):
        shift_char = key[pos]
        shift = alphabet.index(shift_char)
        new_txt = new_txt + caesar_encode(char, shift, alphabet)
    return new_txt

def decode(encoded_txt, key, alphabet=string.ascii_lowercase):
    new_key = atbash(key, alphabet)
    new_key = caesar_encode(new_key, 1, alphabet)
    return encode(encoded_txt, new_key, alphabet)