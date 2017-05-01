import requests, json
from getpass import getpass

class ApiError(Exception):
    pass

class Api():
    def __init__(self):
        self.url = "https://app.timeweave.com.au/api/3.6/"
        self.headers = {
            "tw-app-version":"3.3.8",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type":"application/json; charset=UTF-8",
        }
    def get(self, endpoint, params={}):
        r = requests.get(self.url + endpoint, headers=self.headers, params=params)
        if r.status_code >= 400:
            raise ApiError("%s: %s" % (r.status_code, r.reason))
        return r.json()
    def post(self, endpoint, data):
        print(self.url + endpoint)
        r = requests.post(self.url + endpoint, headers=self.headers, data=data)
        if r.status_code >= 400:
            raise ApiError("%s: %s" % (r.status_code, r.reason))
        return r.json()
    def login(self):
        return self.post("auth/login", json.dumps({'email':input('email   : '),'password':getpass('password: ')}))
    def init(self):
        return self.get("app/init")

if __name__ == '__main__':
    api = Api()
    print(api.login())
    print(api.init())
