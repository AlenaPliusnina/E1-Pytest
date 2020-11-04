import pytest


@pytest.fixture()
def word_generation():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    return words

