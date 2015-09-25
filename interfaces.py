import requests


class UserProfile:
    def __init__(self, username=None):
        self.url = self.build_url(username)
        self.headers = {'user-agent': 'name-taken/0.0.1'}

    def build_url(self, username):
        pass

    def fetch_profile(self):
        pass

    def set_username(self, username):
        self.url = self.build_url(username)


class Instagram(UserProfile):
    def build_url(self, username):
        return 'https://instagram.com/{}/'.format(username)

    def fetch_profile(self):
        r = requests.get(self.url, self.headers)
        return r.status_code


class Twitter(UserProfile):
    def build_url(self, username):
        return 'https://twitter.com/{}/'.format(username)

    def fetch_profile(self):
        r = requests.head(self.url)
        return r.status_code
