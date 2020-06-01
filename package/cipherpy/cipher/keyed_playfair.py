import string
from . import playfair_decode, playfair_encode
from ..base import keyed_alphabet

# Keyed Playfair

def encode(plain_txt, key, alphabet=string.ascii_lowercase, missed_char_dict={'j': 'i'}, padding_char="x"):
    new_alphabet = keyed_alphabet(key, alphabet)
    return playfair_encode(plain_txt, new_alphabet, missed_char_dict, padding_char)

def decode(encoded_txt, key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(key, alphabet)
    return playfair_decode(encoded_txt, new_alphabet)
