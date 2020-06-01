import string
from . import caesar_encode, caesar_decode
from ..base import keyed_alphabet, substitution

### Keyed Caesar

def encode(plain_txt, shift, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    new_txt = caesar_encode(plain_txt, shift, alphabet)
    return substitution(new_txt, alphabet, new_alphabet)

def decode(encoded_txt, shift, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    new_txt = substitution(encoded_txt, new_alphabet, alphabet)
    return caesar_decode(new_txt, shift, alphabet)