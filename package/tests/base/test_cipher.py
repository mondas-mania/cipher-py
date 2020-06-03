from cipherpy.base import substitution, atbash

alphabet = "abcdefghijklmnopqrstuvwxyz"
inv_alph = "zyxwvutsrqponmlkjihgfedcba"
mixed_alph = "abcdefghijklmzyxwvutsrqpon"

def test_substitution():
    assert substitution("abcd", alphabet, inv_alph) == "zyxw"
    assert substitution("abcd", inv_alph, alphabet) == "zyxw"
    # add test and handling for alphabets not matching 
    # and text not being in alpbhabet

# not worth mocking functions for atbash as it consists solely of two
# internal functions
def test_atbash():
    assert atbash("abcd") == "zyxw"
    assert atbash("abcd", mixed_alph) == "nopq"
    # add test and handling for if string chars not in alphabet