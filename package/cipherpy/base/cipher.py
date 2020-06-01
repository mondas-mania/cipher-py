import string
from . import invert_alphabet

# Substitution Cipher

def substitution(input, alphabet, new_alphabet):
    idx = [alphabet.index(char) for char in input]
    new_txt = ''.join([new_alphabet[id] for id in idx])
    return new_txt

# Atbash Cipher

def atbash(plain_txt, alphabet=string.ascii_lowercase):
    new_alphabet = invert_alphabet(alphabet)
    return substitution(plain_txt, alphabet, new_alphabet)