import requests
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    payload = {
        "long_url": url
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(token, url):
    payload = {
        "unit": "day",
        "units": -1
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                            headers=headers,
                            params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    return response.ok


def main():
    load_dotenv()
    try:
        token = os.environ['BITLY_TOKEN']
    except KeyError:
        print('API токен не найден')
        return
    url = input('Введите ссылку: ')
    if is_bitlink(url, token):
        try:
            print(f"По вашей ссылке прошли: {count_clicks(token, url)} раз(а)")
        except requests.exceptions.HTTPError as ex:
            print(ex)
    else:
        try:
            print(f'Битлинк: {shorten_link(token, url)}')
        except requests.exceptions.HTTPError as ex:
            print(ex)


if __name__ == '__main__':
    main()
