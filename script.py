import string
import re

file = open("./plain_input.txt", "r")
inputs = [line for line in file]
file.close()

# reduce list comprehension in finished product for the love of god
inputs = [re.sub(r'[^\w]', '', line.strip()).split('\\n') for line in inputs]
clean_input = []
[[clean_input.append(split_line.lower()) for split_line in line] for line in inputs]


def caesar_encode(plain_txt, shift):
    new_string = ""
    alphabet = [char for char in string.ascii_lowercase]
    alph_len = len(alphabet)
    for char in plain_txt:
        pos = string.ascii_lowercase.index(char)
        new_pos = (pos + shift) % alph_len
        new_string = new_string + alphabet[new_pos]
    return new_string

def caesar_decode(encoded_text, shift):
    alphabet = [char for char in string.ascii_lowercase]
    alph_len = len(alphabet)
    new_shift = (-shift) % alph_len
    return caesar_encode(encoded_text, new_shift)

encoded = caesar_encode(clean_input[0], 1)
print(caesar_decode(encoded, 1))