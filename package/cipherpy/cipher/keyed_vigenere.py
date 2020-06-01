import string
from . import vigenere_encode, vigenere_decode
from ..base import keyed_alphabet

# Keyed Vigenere

def encode(plain_txt, key, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    return vigenere_encode(plain_txt, key, new_alphabet)

def decode(encoded_txt, key, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    return vigenere_decode(encoded_txt, key, new_alphabet)