from cipherpy.base import numbers_to_letters, letters_to_numbers
import pytest

alphabet = "abcdefghijklmnopqrstuvwxyz"
alph_nums = [str(x) for x in range(1,27)]

def test_numbers_to_letters():
    assert numbers_to_letters(alph_nums) == alphabet
    assert numbers_to_letters(alph_nums[:15], alphabet) == alphabet[:15]
    assert numbers_to_letters(["3","2","4","1"], "dbace") == "abcd"
    assert numbers_to_letters(["1","1","1"], alphabet) == "aaa"
    with pytest.raises(Exception) as outside_alph:
        numbers_to_letters([1,5], "abcd")
    assert "outside the range of the given alphabet" in str(outside_alph.value)

def test_letters_to_numbers():
    assert letters_to_numbers(alphabet) == alph_nums
    assert letters_to_numbers(alphabet[:15], alphabet) == alph_nums[:15]
    assert letters_to_numbers("abcd", "dbace") == ["3","2","4","1"]
    with pytest.raises(Exception) as diff_alphs:
        letters_to_numbers("abcde", "abcdf")
    assert "not in the given alphabet" in str(diff_alphs.value)