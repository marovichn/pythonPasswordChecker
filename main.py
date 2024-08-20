import requests
import hashlib


def req_appi_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'password123'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}')
    return res


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8').hexdigest().upper())
    return sha1password
