import string
from . import invert_alphabet

# Substitution Cipher

def substitution(input, alphabet, new_alphabet):
    if set(list(alphabet)) != set(list(new_alphabet)):
        raise Exception(f"Alphabets {alphabet} and {new_alphabet} do not have matching characters.")

    non_chars = []
    for char in input:
        if char not in alphabet or char not in new_alphabet:
            non_chars.append(char)
    if non_chars:
        raise Exception(f"{non_chars} in your input, {input}, cannot be found in one or both of your alphabets.")
    
    idx = [alphabet.index(char) for char in input]
    new_txt = ''.join([new_alphabet[id] for id in idx])
    return new_txt

# Atbash Cipher

def atbash(plain_txt, alphabet=string.ascii_lowercase):
    non_chars = []
    for char in plain_txt:
        if char not in alphabet:
            non_chars.append(char)
    if non_chars:
        raise Exception(f"{non_chars} in your input, {plain_txt}, cannot be found in the given alphabet.")
    new_alphabet = invert_alphabet(alphabet)
    return substitution(plain_txt, alphabet, new_alphabet)