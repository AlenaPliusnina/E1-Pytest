import pytest
from game import word_choice, check_letter, update_underscore


def test_word_choice(word_generation):
    choice = word_choice()
    assert choice in word_generation


def test_check_letter_positive(word_generation):
    result = check_letter('s', word_generation[0])
    assert result


def test_check_letter_negative(word_generation):
    result = check_letter('p', word_generation[0])
    assert result == False


def test_check_update_underscore(word_generation):
    result = update_underscore('s', word_generation[0], ' _ _ _ _ _ _ _ _ _ _ _ _')
    assert result == 's _ _ _ _ _ _ _ _ _ _ _'

