import json
from time import sleep
import requests


def request_get(data):
    session = requests.Session()
    session.trust_env = False
    URL = 'https://ai.easst.cn/easst/semantic'
    res = session.get(url=URL, params={
        'reqSource': 2,
        'appId': 'sgompqz8',
        'userId': 11697,
        'sign': '516bf5ca32aad5c0a7e64136c4923e58',
        'timestamp': 1586241210591,
        'isVoiceInput': True,
        'text': data,
    }).json()

    return res


def request_get_ceshi(data):
    session = requests.Session()
    session.trust_env = False
    URL = 'https://test-ai.easst.cn/easst/semantic'
    res = session.get(url=URL, params={
        'reqSource': 2,
        'appId': 'k55frqcd',
        'userId': 11634,
        'sign': 'bb820bab3135f4844417bfa28ebe9c6b',
        'timestamp': 1614137013279,
        'isVoiceInput': True,
        'text': data,
    }).json()

    return res


if __name__ == '__main__':
    response = json.loads(request_get_ceshi("申请加班")['data'])
    print(json.dumps(response, ensure_ascii=False, indent=4))

