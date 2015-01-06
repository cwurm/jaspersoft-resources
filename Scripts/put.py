#!/usr/bin/python

import sys
import base64
import requests
from requests.auth import HTTPBasicAuth
import json

headers_get = {'Accept': 'application/repository.file+json'}

r = requests.get('http://127.0.0.1:8080/jasperserver-pro/rest_v2/resources/themes/Flat/overrides_custom.css', auth=HTTPBasicAuth('jasperadmin', 'jasperadmin'), headers=headers_get)
data = json.loads(r.text)
version = data['version']


headers_put = {'content-type': 'application/repository.file+json'}

f = open(sys.argv[1])
payload = {'type': 'css', 'content': base64.b64encode(f.read()), 'version': version, 'label': 'css'}

r2 = requests.put('http://127.0.0.1:8080/jasperserver-pro/rest_v2/resources/themes/Flat/overrides_custom.css', data=json.dumps(payload), auth=HTTPBasicAuth('jasperadmin', 'jasperadmin'), headers=headers_put)

print r2.text

