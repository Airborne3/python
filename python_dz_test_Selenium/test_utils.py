import pytest
from utils import common_numbers, words_starting_with_vowel



def test_common_numbers_basic():
    assert common_numbers([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_common_numbers_no_common():
    assert common_numbers([1, 2, 3], [4, 5, 6]) == []

def test_common_numbers_empty_lists():
    assert common_numbers([], [1, 2]) == []
    assert common_numbers([1, 2], []) == []
    assert common_numbers([], []) == []

def test_common_numbers_with_duplicates():
    assert common_numbers([1, 2, 2, 3, 3], [2, 3, 3, 4]) == [2, 3]

def test_common_numbers_order_preserved():
    assert common_numbers([3, 1, 2], [2, 1, 3]) == [3, 1, 2]

def test_common_numbers_negative_and_zero():
    assert common_numbers([-1, 0, 1, 2], [0, 2, -1, 5]) == [-1, 0, 2]



def test_words_starting_with_vowel_basic():
    assert words_starting_with_vowel("apple orange banana") == ["apple", "orange"]

def test_words_starting_with_vowel_mixed_case():
    assert words_starting_with_vowel("Apple Orange banana") == ["Apple", "Orange"]

def test_words_starting_with_vowel_no_vowel_words():
    assert words_starting_with_vowel("cat dog") == []

def test_words_starting_with_vowel_empty_string():
    assert words_starting_with_vowel("") == []

def test_words_starting_with_vowel_with_punctuation():
    assert words_starting_with_vowel("An apple, an orange!") == ["An", "apple", "an", "orange"]

def test_words_starting_with_vowel_only_punctuation():
    assert words_starting_with_vowel("!@#$%") == []

def test_words_starting_with_vowel_single_vowel_word():
    assert words_starting_with_vowel("umbrella") == ["umbrella"]

def test_words_starting_with_vowel_consonant_then_vowel():
    assert words_starting_with_vowel("hello universe") == ["universe"]