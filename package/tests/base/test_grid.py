from cipherpy.base import create_grid, playfair_digram_encode
import numpy as np

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
    # Test non-square number length alphabets
    # and handling for it

def test_playfair_digram_encode():
    assert playfair_digram_encode("an", grid) == "cl"
    assert playfair_digram_encode("al", grid) == "fq"
    assert playfair_digram_encode("ac", grid) == "bd"
    assert playfair_digram_encode("aa", grid) == "gg"
    assert playfair_digram_encode("zz", grid) == "aa"
    assert playfair_digram_encode("zz", inv_grid) == "tt"
    # Test characters not in grid
    # Test malformed grid
    # Test input of length != 2