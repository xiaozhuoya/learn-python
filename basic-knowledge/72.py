# requests

import requests
r = requests.get('https://badu.com')

print(r.status_code)
print(r.text)