from ..base import keyed_alphabet, substitution
import string

### Caesar

def encode(plain_txt, shift, alphabet=string.ascii_lowercase):
    alph_len = len(alphabet)
    new_alphabet = keyed_alphabet(alphabet[shift % alph_len:], alphabet)
    return substitution(plain_txt, alphabet, new_alphabet)

def decode(encoded_txt, shift, alphabet=string.ascii_lowercase):
    return encode(encoded_txt, -shift, alphabet)