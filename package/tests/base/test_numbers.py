from cipherpy.base import numbers_to_letters, letters_to_numbers

alphabet = "abcdefghijklmnopqrstuvwxyz"
alph_nums = [str(x) for x in range(1,27)]

def test_numbers_to_letters():
    assert numbers_to_letters(alph_nums) == alphabet
    assert numbers_to_letters(alph_nums[:15], alphabet) == alphabet[:15]
    # test different alphabets
    # numbers that are greater than length of alphabet

def test_letters_to_numbers():
    assert letters_to_numbers(alphabet) == alph_nums
    assert letters_to_numbers(alphabet[:15], alphabet) == alph_nums[:15]
    # test different alphabets
    # letters that don't appear in given alphabet