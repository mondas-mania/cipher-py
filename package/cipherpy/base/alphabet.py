import string

# Create a keyed alphabet

def keyed_alphabet(alphabet_key, alphabet=string.ascii_lowercase):
    non_chars = [char for char in alphabet_key if char not in alphabet]
    if non_chars:
        raise Exception(f"{non_chars} in the key cannot be found in the given alphabet.")
    new_alphabet = alphabet
    new_alphabet_key = ''.join(sorted(set(alphabet_key), key=alphabet_key.index))
    for char in new_alphabet_key:
        new_alphabet = new_alphabet.replace(char, '')
        
    new_alphabet = new_alphabet_key + new_alphabet
    return new_alphabet

# Invert the alphabet
# It's a basic string comprehension but nice to give it a name

def invert_alphabet(alphabet=string.ascii_lowercase):
    return alphabet[::-1]