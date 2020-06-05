from cipherpy.cipher import caesar_decode, caesar_encode, keyed_caesar_decode, keyed_caesar_encode
import pytest

alph = "abcdefghijklmnopqrstuvwxyz"
inv_alph = "zyxwvutsrqponmlkjihgfedcba"

def test_caesar_encode():
    assert caesar_encode("hello", 1) == "ifmmp"
    assert caesar_encode("hello", -1) == "gdkkn"
    assert caesar_encode("hello", 26) == "hello"
    assert caesar_encode("hello", 1, inv_alph) == "gdkkn"
    assert caesar_encode("abcd", 1, "dacb") == "cdba"
    with pytest.raises(Exception) as not_in_alph:
        caesar_encode("hello", 1, "abcdefgh")
    assert "cannot be found in " in str(not_in_alph.value)

def test_caesar_decode():
    # uses encode function solely so doesn't need as many tests
    assert caesar_decode("hello", 1) == "gdkkn"
    assert caesar_decode("hello", -1) == "ifmmp"

def test_keyed_encode():
    assert keyed_caesar_encode("hello", 1, "zyx") == "fcjjm"
    assert keyed_caesar_encode("hello", 26, "zyx") == "ebiil"
    assert keyed_caesar_encode("hello", 3, "zyx") == "hello"
    assert keyed_caesar_encode("hello", 1, "abc", inv_alph) == "jgnnq"
    with pytest.raises(Exception) as not_in_alph_key:
        keyed_caesar_encode("hello", 1, "abcd", "abcefghijklmno")
    assert "cannot be found in the given alphabet" in str(not_in_alph_key.value)
    with pytest.raises(Exception) as not_in_alph_input:
        keyed_caesar_encode("hello", 1, "zyx", "abcdfghijk")
    assert "cannot be found in the given alphabet" in str(not_in_alph_input.value)

def test_keyed_decode():
    assert keyed_caesar_decode("hello", 1, "zyx") == "jgnnq"
    with pytest.raises(Exception) as not_in_alph_key:
        keyed_caesar_decode("hello", 1, "abcd", "abcefghijklmno")
    assert "cannot be found in the given alphabet" in str(not_in_alph_key.value)
    with pytest.raises(Exception) as not_in_alph_input:
        keyed_caesar_decode("hello", 1, "zyx", "abcdfghijk")
    assert "cannot be found in the given alphabet" in str(not_in_alph_input.value)
    pass
