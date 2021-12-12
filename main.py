import requests
import time
import hashlib
import hmac
import json

url = 'https://api.kuna.io/v3/auth/deposit'
api_path = '/v3/auth/deposit'

public_api = ""
secret_api = ""

body = {'currency': '',
        'amount': int(),
        'payment_service': 'default'}

nonce = str(int(time.time()) * 1000)
kun_sign = (api_path + nonce + json.dumps(body))
header_body = "{}{}{}".format(api_path, nonce, json.dumps(body))

signature = hmac.new(
    secret_api.encode('ascii'),
    header_body.encode('ascii'),
    hashlib.sha384).hexdigest()


headers = {"kun-nonce": nonce,
           "kun-apikey": public_api,
           'kun-signature': signature,
           "Content-Type": "application/json",
           "accept": "application/json"}

response = requests.request(
    "POST",
    'https://api.kuna.io/v3/auth/deposit',
    json=body,
    headers=headers)

print(response.text)
