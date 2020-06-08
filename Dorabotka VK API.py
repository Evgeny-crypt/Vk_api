from urllib.parse import urlencode
import requests
from pprint import pprint

APP_ID = 7494777
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
   'client_id': APP_ID,
   'display': 'page',
   'scope': 'status,friends',
   'response_type': 'token',
   'v': '5.89',
}
print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = input('Введите TOKEN: ')


class User:

    def get_params(self):
        return {
            'v': '5.89',
            'access_token': TOKEN,
        }

    def __init__(self, ID):
        self.ID = ID

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.ID
        params['target_uid'] = other.ID
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        pprint(response.json()['response'])

    def __str__(self):
        vk_link = 'https://vk.com/id'
        return (f'{vk_link}{self.ID}')

user1 = User(22674190)
user2 = User(22819972)

user1 & user2
print(user1)
