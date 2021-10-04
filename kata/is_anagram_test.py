from is_anagram import is_anagram
import pytest


def test_initial():
    assert is_anagram('test', 'test')


@pytest.mark.parametrize('message1, message2', (
        ('test', 'not test'),
        ('not test', 'test')
))
def test_not_anagram(message1, message2):
    assert not is_anagram(message1, message2)


def test_real_anagram():
    assert is_anagram('test', 'tets')
