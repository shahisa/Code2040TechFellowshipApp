import requests, json

urlRevApi = 'http://challenge.code2040.org/api/reverse'
payload = {'token': 'a507960e4f5b9aaced42072be76bdb5b'}
r = requests.post(urlRevApi, params=payload)

print (r.status_code)
print(r.text)
print(r.text)[::-1]

reverseString = (r.text)[::-1]
payloadTwo = {'token': 'a507960e4f5b9aaced42072be76bdb5b','string':reverseString}

newUrl = 'http://challenge.code2040.org/api/reverse/validate'
rTwo = requests.post(newUrl, params=payloadTwo)
print(rTwo.status_code)
