import requests
import hashlib            # built in module 
# import sys


url = 'https://api.pwnedpasswords.com/range/' + '5BAA6' #by using first 5 characters of hashed password we make sure this API will never know our password
res = requests.get(url)
print(res)

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + '5BAA6' #by using first 5 characters of hashed password we make sure this API will never know our password
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code} check the API and try again')


def pwned_api_check(password):
    #print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    #checking if the password exists in the API response
    sha1password = hashlib.sha1(password.encode('utf-8'))
    return sha1password


pwned_api_check('123')