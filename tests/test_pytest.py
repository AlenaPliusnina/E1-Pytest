import pytest

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

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

