import string

# Letters / Numbers

def letters_to_numbers(plain_txt, alphabet=string.ascii_lowercase):
    return [str(alphabet.index(char) + 1) for char in plain_txt]

def numbers_to_letters(plain_nums, alphabet=string.ascii_lowercase):
    # plain_nums must be list
    return ''.join([alphabet[int(num) - 1] for num in plain_nums])