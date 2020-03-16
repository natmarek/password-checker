import requests
# import hashlib
# import sys


url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)
print(res)