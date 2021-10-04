from is_anagram import is_anagram


def test_initial():
    assert is_anagram('test', 'test')


def test_not_anagram():
    assert not is_anagram('test', 'not test')


def test_not_anagram2():
    assert not is_anagram('not test', 'test')


def test_real_anagram():
    assert is_anagram('test', 'tets')
