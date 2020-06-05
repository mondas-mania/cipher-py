from cipherpy.base import create_grid, playfair_digram_encode
import numpy as np
import pytest

alphabet = "abcdefghiklmnopqrstuvwxyz" # j has been removed
inv_alph = "zyxwvutsrqponmlkihgfedcba" # j has been removed
grid = np.array([
    ["a","b","c","d","e"],
    ["f","g","h","i","k"],
    ["l","m","n","o","p"],
    ["q","r","s","t","u"],
    ["v","w","x","y","z"]
    ])
inv_grid = np.array([
    ["z","y","x","w","v"],
    ["u","t","s","r","q"],
    ["p","o","n","m","l"],
    ["k","i","h","g","f"],
    ["e","d","c","b","a"]
])


def test_create_grid():
    assert (create_grid() == grid).all()
    assert create_grid().shape == (5,5)
    assert (create_grid(inv_alph) == inv_grid).all()
    with pytest.raises(Exception) as non_sqr_length:
        create_grid("abc")
    assert "is not a square" in str(non_sqr_length.value)
    with pytest.raises(Exception) as dup_chr_alph:
        create_grid("acab")
    assert "Duplicate" in str(dup_chr_alph.value)

def test_playfair_digram_encode():
    assert playfair_digram_encode("an", grid) == "cl"
    assert playfair_digram_encode("al", grid) == "fq"
    assert playfair_digram_encode("ac", grid) == "bd"
    assert playfair_digram_encode("aa", grid) == "gg"
    assert playfair_digram_encode("zz", grid) == "aa"
    assert playfair_digram_encode("zz", inv_grid) == "tt"
    with pytest.raises(Exception) as not_in_grid:
        playfair_digram_encode("jj", grid)
    assert "not found in the given grid" in str(not_in_grid.value)
    with pytest.raises(Exception) as malformed_grid:
        playfair_digram_encode("aa", np.array(["a", "b"]))
    assert "not of equal dimensions" in str(malformed_grid.value)
    with pytest.raises(Exception) as non_digram:
        playfair_digram_encode("abc", grid)
    assert "not two characters long" in str(non_digram.value) 
    # Test characters not in grid
    # Test malformed grid
    # Test input of length != 2