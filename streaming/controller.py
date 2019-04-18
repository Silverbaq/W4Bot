import requests
import json
from decouple import config

user_logins = ['silverbaq42']

def pull_stream_data(user_login):
    url ='https://api.twitch.tv/helix/streams?user_login={0}'.format(user_login)
    headers = {  'Client-ID': config('TWITCH_CLIENT_ID') }
    data = requests.get(url, headers=headers).text
    json_data = json.loads(data)
    return json_data['data']


def is_stream_online(user_login):
    data = pull_stream_data(user_login)
    if len(data) > 0:
        return True
    return False


def should_annouce(user):
    online = is_stream_online(user.user_login)
    return user.should_be_anounced(online)