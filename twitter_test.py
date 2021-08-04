import pytest
from twitter import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet("Test Message")
    assert twitter.tweets == ["Test Message"]


def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []


def test_tweet_with_hashtag():
    twitter = Twitter()
    message = "Test #first message"
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)


def test_tweet_with_hashtag_on_beginig():
    twitter = Twitter()
    message = "#first test message"
    twitter.tweet(message)
    assert "first" in twitter.find_hashtags(message)


def test_tweet_with_hashtag_uppercase():
    twitter = Twitter()
    message = "#FIRST test message"
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)


