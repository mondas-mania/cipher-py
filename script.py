import string
import re

file = open("./plain_input.txt", "r")
inputs = [line for line in file]
file.close()

# reduce list comprehension in finished product for the love of god
inputs = [re.sub(r'[^\w]', '', line.strip()).split('\\n') for line in inputs]
clean_input = []
[[clean_input.append(split_line.lower()) for split_line in line] for line in inputs]

### Caesar

def caesar_encode(plain_txt, shift, alphabet_str=string.ascii_lowercase):
    new_string = ""
    alphabet = [char for char in alphabet_str]
    alph_len = len(alphabet)
    for char in plain_txt:
        pos = alphabet.index(char)
        new_pos = (pos + shift) % alph_len
        new_string = new_string + alphabet[new_pos]
    return new_string

def caesar_decode(encoded_text, shift, alphabet_str=string.ascii_lowercase):
    alphabet = [char for char in alphabet_str]
    alph_len = len(alphabet)
    new_shift = (-shift) % alph_len
    return caesar_encode(encoded_text, new_shift, alphabet_str)

### Keyed Caesar

def keyed_caesar_encode(plain_txt, shift, alphabet_key, alphabet_str=string.ascii_lowercase):
    new_alphabet = create_alphabet(alphabet_key, alphabet_str)
    new_txt = caesar_encode(plain_txt, shift, alphabet_str)
    return substitution(new_txt, alphabet_str, new_alphabet)

def keyed_caesar_decode(encoded_text, shift, alphabet_key, alphabet_str=string.ascii_lowercase):
    new_alphabet = create_alphabet(alphabet_key, alphabet_str)
    new_txt = substitution(encoded_text, new_alphabet, alphabet_str)
    return caesar_decode(new_txt, shift, alphabet_str)


def create_alphabet(alphabet_key, alphabet_str=string.ascii_lowercase):
    new_alphabet = [char for char in alphabet_str]
    new_alphabet_key = ''.join(sorted(set(alphabet_key), key=alphabet_key.index))
    [new_alphabet.remove(char) for char in new_alphabet_key]
    new_alphabet = ''.join([char for char in new_alphabet_key] + new_alphabet)
    return new_alphabet

def substitution(input, alphabet, new_alphabet):
    idx = [alphabet.index(char) for char in input]
    new_txt = ''.join([new_alphabet[id] for id in idx])
    return new_txt

encoded = caesar_encode(clean_input[0], 1)
print(caesar_decode(encoded, 1))
encoded2 = (keyed_caesar_encode("helloworld", 1, "hello"))
print(keyed_caesar_decode(encoded2, 1, "hello"))