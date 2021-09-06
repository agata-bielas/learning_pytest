from unittest.mock import patch, Mock, MagicMock
import pytest
import requests
from twitter import Twitter


class ResponseGetMock(object):
    def json(self):
        return {'documentation_url': 'test'}


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')


@pytest.fixture(name='backend')
def fixture_backend(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(params=[None, 'python'], name='username')
def fixture_username(request):
    return request.param


@pytest.fixture(params=['list', 'backend'], name='twitter')
def fixture_twitter(backend, username, request):
    if request.param == 'list':
        twitter = Twitter(username=username)
    elif request.param == 'backend':
        twitter = Twitter(backend=backend, username=username)
    return twitter


def test_twitter_initialization(twitter):
    assert twitter


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_single_messages(avatar_mock, twitter):
    twitter.tweet("Test Message")
    assert twitter.tweet_messages == ["Test Message"]


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweet_messages == []


def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet("Test 1")
    twitter1.tweet("Test 2")

    assert twitter2.tweet_messages == ["Test 1", "Test 2"]


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first test message", ["first"]),
        ("#FIRST test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])

))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_username(avatar_mock, twitter):
    if not twitter.username:
        pytest.skip()

    twitter.tweet('Test message')
    assert twitter.tweets == [{'avatar': 'test', 'message': "Test message", 'hashtags': []}]
    # to poniżej pozwala nam sprawdzic czy funkcja get_user_avatar byla wywolana podczas testu
    avatar_mock.assert_called()


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hashtag_mock(avatar_mock, twitter):
    twitter.find_hashtags = Mock()
    twitter.find_hashtags.return_value = 'first'
    twitter.tweet("Test #second")
    assert twitter.tweets[0]['hashtags'] == 'first'
    # sprawdzenie czy mock byl wywolany z takim argumentem
    twitter.find_hashtags.assert_called_with("Test #second")


def test_twitter_version(twitter):
    twitter.version = MagicMock()
    twitter.version.__eq__.return_value = '2.0'
    assert twitter.version == '2.0'
