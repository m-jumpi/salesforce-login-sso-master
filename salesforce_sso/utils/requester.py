import requests


class Requester:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url: str):
        response = self.session.get(url)
        response.raise_for_status()
        return response

    def post(self, url, data):
        response = self.session.post(url, data)
        response.raise_for_status()
        return response

    def get_session_cookie(self, name: str, domain: str):
        for cookie in self.session.cookies:
            if cookie.name == name and cookie.domain == domain:
                return cookie.value

        raise Exception("cookie '{}' for domain '{}' not found".format(name, domain))
