import json
import re
from urllib.parse import urljoin
import requests

USER_API = "https://api.github.com/users"


class Twitter(object):
    version = '1.0'

    def __init__(self, backend=None, username=None):
        self.backend = backend
        self._tweets = []
        self.username = username

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            backend_text = self.backend.read()
            if backend_text:
                self._tweets = json.loads(backend_text)
        return self._tweets

    @property
    def tweet_messages(self):
        return [tweet['message'] for tweet in self.tweets]

    def get_user_avatar(self):
        if not self.username:
            return None

        url = urljoin(USER_API, self.username)
        res = requests.get(url)
        return res.json()['documentation_url']


    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long.")
        self.tweets.append({'message': message, 'avatar': self.get_user_avatar()})
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall("#(\w+)", message)]


if __name__ == '__main__':
    twitter = Twitter()
    print(twitter.version, twitter.tweets)
    twitter.tweet("This is a test message")
    print(twitter.tweets)
