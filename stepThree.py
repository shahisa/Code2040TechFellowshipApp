import requests,json

url = 'http://challenge.code2040.org/api/haystack'
payload = {'token': 'a507960e4f5b9aaced42072be76bdb5b'}
r = requests.post(url, params=payload)
print(r.status_code)

dictionary = (r.json())
needle = dictionary['needle']
listWords = dictionary['haystack']

for i in range(len(listWords)):
	if needle == listWords[i]:
		payload['needle'] = i

print(i)
urlTwo = "http://challenge.code2040.org/api/haystack/validate"
rTwo = requests.post(urlTwo, params=payload)
print(rTwo.text)
