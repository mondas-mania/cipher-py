import string

# Letters / Numbers

def letters_to_numbers(plain_txt, alphabet=string.ascii_lowercase):
    return ''.join([alphabet.index(char) + 1 for char in plain_txt])

def numbers_to_letters(plain_nums, alphabet):
    return ''.join([alphabet[num - 1] for num in plain_nums])