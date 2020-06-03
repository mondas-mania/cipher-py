from cipherpy.base import keyed_alphabet, invert_alphabet

regular_alph = "abcdefghijklmnopqrstuvwxyz"

def test_invert_alphabet():
    assert invert_alphabet() == "zyxwvutsrqponmlkjihgfedcba"
    assert invert_alphabet("zyxwvutsrqponmlkjihgfedcba") == regular_alph
    assert invert_alphabet("a") == "a"
    assert invert_alphabet("1234") == "4321"
    assert invert_alphabet("") == ""

def test_keyed_alphabet():
    assert keyed_alphabet("b") == "bacdefghijklmnopqrstuvwxyz"
    assert keyed_alphabet("hello") == "heloabcdfgijkmnpqrstuvwxyz"
    # Should remove any characters from the key that weren't in the alphabet
    assert keyed_alphabet("hello99") == "heloabcdfgijkmnpqrstuvwxyz"
    assert keyed_alphabet("hello", "zyxwvutsrqponmlkjihgfedcba") == "helozyxwvutsrqpnmkjigfdcba"
    assert keyed_alphabet("") == regular_alph
    assert keyed_alphabet("", "") == ""