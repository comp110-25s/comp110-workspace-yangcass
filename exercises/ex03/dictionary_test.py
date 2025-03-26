"""This is where I test the dictionary function"""

__author__: str = "730717480"

import pytest
from dictionary import invert, count, favorite_color, bin_len

with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_invert_use_1() -> None:
    """Test for use case for invert"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    """Test for use case  for invert"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge_1() -> None:
    """Test using edge case for invert"""
    assert invert({}) == {}


def test_count_use_1() -> None:
    """Test for use case for count"""
    assert count(["tree", "apple", "orange", "tree"]) == {
        "tree": 2,
        "apple": 1,
        "orange": 1,
    }


def test_count_use_2() -> None:
    """Test for use case for count"""
    assert count(["house", "house", "bus"]) == {
        "house": 2,
        "bus": 1,
    }


def test_count_edge_1() -> None:
    """Test for edge  case for count"""
    assert count([]) == {}


def test_favorite_color_use_1() -> None:
    """Test for use case for favorite color"""
    assert favorite_color({"Sophie": "blue", "Jame": "red", "Grace": "pink"}) == "blue"


def test_favorite_color_use_2() -> None:
    """Test for use case for favorite color"""
    assert (
        favorite_color({"person 1": "pink", "person 2": "red", "person 3": "pink"})
        == "pink"
    )


def test_favorite_color_edge_1() -> None:
    """Test for edge case for favorite color"""
    assert favorite_color({}) == ""


def test_bin_len_use_1() -> None:
    """Test for use case for bin len"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_2() -> None:
    """Test for use case for bin len"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_1() -> None:
    """Test for edge case for bin len"""
    assert bin_len([]) == {}
