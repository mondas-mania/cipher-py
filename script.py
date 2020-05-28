import string
import re

file = open("./plain_input.txt", "r")
inputs = [line for line in file]
file.close()

inputs = [re.sub(r'[^\w]', '', line.strip()).split('\\n') for line in inputs]
clean_input = []
[[clean_input.append(split_line.lower()) for split_line in line] for line in inputs]

### Caesar

def caesar_encode(plain_txt, shift, alphabet=string.ascii_lowercase):
    alph_len = len(alphabet)
    new_alphabet = keyed_alphabet(alphabet[shift % alph_len:], alphabet)
    return substitution(plain_txt, alphabet, new_alphabet)

def caesar_decode(encoded_txt, shift, alphabet=string.ascii_lowercase):
    return caesar_encode(encoded_txt, -shift, alphabet)

### Keyed Caesar

def keyed_caesar_encode(plain_txt, shift, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    new_txt = caesar_encode(plain_txt, shift, alphabet)
    return substitution(new_txt, alphabet, new_alphabet)

def keyed_caesar_decode(encoded_txt, shift, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    new_txt = substitution(encoded_txt, new_alphabet, alphabet)
    return caesar_decode(new_txt, shift, alphabet)

# Create a keyed alphabet

def keyed_alphabet(alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = alphabet
    new_alphabet_key = ''.join(sorted(set(alphabet_key), key=alphabet_key.index))
    for char in new_alphabet_key:
        new_alphabet = new_alphabet.replace(char, '')
    new_alphabet = new_alphabet_key + new_alphabet
    return new_alphabet

# Substitution Cipher

def substitution(input, alphabet, new_alphabet):
    idx = [alphabet.index(char) for char in input]
    new_txt = ''.join([new_alphabet[id] for id in idx])
    return new_txt

# Atbash Cipher

def invert_alphabet(alphabet=string.ascii_lowercase):
    return alphabet[::-1]

def atbash(plain_txt, alphabet=string.ascii_lowercase):
    new_alphabet = invert_alphabet(alphabet)
    return substitution(plain_txt, alphabet, new_alphabet)

# Letters / Numbers

def letters_to_numbers(plain_txt, alphabet=string.ascii_lowercase):
    return [alphabet.index(char) + 1 for char in plain_txt]

def numbers_to_letters(plain_nums, alphabet):
    return [alphabet[num - 1] for num in plain_nums]

# Vigenere Cipher

def vigenere_encode(plain_txt, key, alphabet=string.ascii_lowercase):
    while len(plain_txt) > len(key):
        key = key + key
    new_txt = ''
    for pos, char in enumerate(plain_txt):
        shift_char = key[pos]
        shift = alphabet.index(shift_char)
        new_txt = new_txt + caesar_encode(char, shift, alphabet)
    return new_txt

def vigenere_decode(encoded_txt, key, alphabet=string.ascii_lowercase):
    new_key = atbash(key, alphabet)
    new_key = caesar_encode(new_key, 1, alphabet)
    return vigenere_encode(encoded_txt, new_key, alphabet)

# Keyed Vigenere

def keyed_vigenere_encode(plain_txt, key, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    return vigenere_encode(plain_txt, key, new_alphabet)

def keyed_vigenere_decode(encoded_txt, key, alphabet_key, alphabet=string.ascii_lowercase):
    new_alphabet = keyed_alphabet(alphabet_key, alphabet)
    return vigenere_decode(encoded_txt, key, new_alphabet)
    

encoded = caesar_encode(clean_input[0], 1)
print(caesar_decode(encoded, 1))
encoded2 = (keyed_caesar_encode("helloworld", 1, "hello"))
print(keyed_caesar_decode(encoded2, 1, "hello"))
print(atbash("abcd"))
print(vigenere_encode("helloworld", "cardiff"))
print(vigenere_decode("jecowbttlu", "cardiff"))
print(keyed_vigenere_encode("helloworld", "cardiff", "hello"))
print(keyed_vigenere_decode("cbtgmajxcy", "cardiff", "hello"))
