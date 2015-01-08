#!/usr/bin/python

import sys
import base64
import requests
from requests.auth import HTTPBasicAuth
import os
import json

filePath = sys.argv[1]
fileName = os.path.basename(filePath)
serverPath = 'http://127.0.0.1:8080/jasperserver-pro/rest_v2/resources/themes/Flat/' + fileName;
username = 'jasperadmin'
password = 'jasperadmin'

contentType = 'application/repository.file+json'
httpAuth = HTTPBasicAuth(username, password)

headers_get = {'Accept': contentType}

r = requests.get(serverPath, auth=httpAuth, headers=headers_get)
data = json.loads(r.text)
version = data['version']


headers_put = {'content-type': contentType}

f = open(filePath)
payload = {'type': 'css', 'content': base64.b64encode(f.read()), 'version': version, 'label': fileName}

r2 = requests.put(serverPath, data=json.dumps(payload), auth=httpAuth, headers=headers_put)

print r2.text

