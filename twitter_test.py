import unittest
from twitter import Twitter


class TwitterTest(unittest.TestCase):
    # Given - metoda setUp wykona sie przed kazdym testem
    def setUp(self):
        self.twitter = Twitter()


    def test_initialization(self):
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test Message'])


if __name__ == "__main__":
    unittest.main()
