import requests
import hashlib
import sys

def req_appi_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = req_appi_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):

    for a in args:
        count = pwned_api_check(a)
        if count:
            print(f'"{a}" was found {count} times, you should probably change your password')
        else:
            print(f'Password "{a}" was NOT found you are safe')


main(sys.argv[1:])
