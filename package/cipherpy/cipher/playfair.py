import string
from ..base import create_grid, playfair_digram_encode, invert_alphabet

# Playfair

def encode(plain_txt, alphabet=string.ascii_lowercase, missed_char_dict={'j': 'i'}, padding_char="x"):
    new_alphabet_str = alphabet
    new_txt = plain_txt
    encoded_txt = ""
    for key, value in missed_char_dict.items():
        new_alphabet_str = new_alphabet_str.replace(key, "")
        new_txt = new_txt.replace(key, value)
    
    grid = create_grid(new_alphabet_str)
    
    i = 0
    while i < len(new_txt):
        digram = new_txt[i:i+2]
        if digram[0] == digram[1]:
            new_txt = new_txt[:i+1] + padding_char + new_txt[i+1:]
            digram = new_txt[i:i+2]
        
        encoded_txt = encoded_txt + playfair_digram_encode(digram, new_txt, grid)
        
        if len(new_txt) - i == 3:
            new_txt = new_txt + padding_char
        
        i = i+2
    return encoded_txt

def decode(encoded_txt, alphabet=string.ascii_lowercase):
    new_alphabet = invert_alphabet(alphabet)
    return encode(encoded_txt, new_alphabet)
