from cipherpy.base import keyed_alphabet, invert_alphabet
import pytest

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
    with pytest.raises(Exception) as not_in_alph:
        keyed_alphabet("hello99")
    assert "cannot be found in the given alphabet" in str(not_in_alph.value)
    assert keyed_alphabet("hello", "zyxwvutsrqponmlkjihgfedcba") == "helozyxwvutsrqpnmkjigfdcba"
    assert keyed_alphabet("") == regular_alph
    assert keyed_alphabet("", "") == ""