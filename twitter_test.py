import pytest
from twitter import Twitter


@pytest.fixture
def twitter():
    twitter = Twitter()
    return twitter


def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet("Test Message")
    assert twitter.tweets == ["Test Message"]


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first test message", ["first"]),
        ("#FIRST test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])

))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
