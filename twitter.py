class Twitter(object):
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long.")
        self.tweets.append(message)


if __name__ == '__main__':
    twitter = Twitter()
    print(twitter.version, twitter.tweets)
    twitter.tweet("This is a test message")
    print(twitter.tweets)
