from cipherpy.base import substitution, atbash
import pytest

alphabet = "abcdefghijklmnopqrstuvwxyz"
inv_alph = "zyxwvutsrqponmlkjihgfedcba"
mixed_alph = "abcdefghijklmzyxwvutsrqpon"

def test_substitution():
    assert substitution("abcd", alphabet, inv_alph) == "zyxw"
    assert substitution("abcd", inv_alph, alphabet) == "zyxw"
    with pytest.raises(Exception) as diff_alphs:
        substitution("a", "abcd", "abde")
    assert "matching characters" in str(diff_alphs.value)
    with pytest.raises(Exception) as non_alph_char:
        substitution("abcdz", "abcd", "badc")
    assert "cannot be found" in str(non_alph_char.value)


def test_atbash():
    assert atbash("abcd") == "zyxw"
    assert atbash("abcd", mixed_alph) == "nopq"
    with pytest.raises(Exception) as non_alph_char:
        atbash("abcde", "abcd")
    assert "cannot be found" in str(non_alph_char.value)