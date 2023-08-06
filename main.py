import requests
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    data = {
        "long_url": f"{url}"
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    return f'Битлинк: {json_response["id"]}'


def count_clicks(token, url):
    data = {
        "unit": "day",
        "units": -1
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                            headers=headers,
                            params=data)
    response.raise_for_status()
    json_response = response.json()
    return f"По вашей ссылке прошли: {json_response['total_clicks']} раз(а)"


def is_bitlink(url, token):
    bitlink = False
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    if response.ok:
        bitlink = True
        return bitlink
    return bitlink


def main():
    load_dotenv(dotenv_path='config/.env')
    token = os.environ.get('TOKEN')
    url = input('Введите ссылку: ')
    if not is_bitlink(url, token):
        try:
            print(shorten_link(token, url))
        except requests.exceptions.HTTPError as ex:
            print(ex)
    else:
        try:
            print(count_clicks(token, url))
        except requests.exceptions.HTTPError as ex:
            print(ex)


if __name__ == '__main__':
    main()
