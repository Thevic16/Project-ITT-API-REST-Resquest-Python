# Project-ITT-API-REST-Resquest-Python

https://www.nylas.com/blog/use-python-requests-module-rest-apis/

Starting with Requests version 2.4.2, you can use the json= parameter (which takes a dictionary) instead of data= (which takes a string) in the call:


>>> import requests
>>> r = requests.post('http://httpbin.org/post', json={"key": "value"})
>>> r.status_code
200
>>> r.json()
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx'},
 'json': {'key': 'value'},
 'origin': 'x.x.x.x',
 'url': 'http://httpbin.org/post'}
