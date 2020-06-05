import string

# Letters / Numbers

def letters_to_numbers(plain_txt, alphabet=string.ascii_lowercase):
    non_chars = []
    for char in plain_txt:
        if char not in alphabet:
            non_chars.append(char)
    if non_chars:
        raise Exception(f"{non_chars} from the input are not in the given alphabet.")
    return [str(alphabet.index(char) + 1) for char in plain_txt]

def numbers_to_letters(plain_nums, alphabet=string.ascii_lowercase):
    # plain_nums must be list
    non_nums = []
    for num in plain_nums:
        if int(num) > len(alphabet):
            non_nums.append(num)
    if non_nums:
        raise Exception(f"{non_nums} from the input are outside the range of the given alphabet.")
    return ''.join([alphabet[int(num) - 1] for num in plain_nums])