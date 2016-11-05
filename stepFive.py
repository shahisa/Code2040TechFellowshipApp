import requests, json
from datetime import datetime, timedelta

token = "a507960e4f5b9aaced42072be76bdb5b"
tokens = {"token": token}
header = {'Content-Type': 'application/json'}
datingHTTP = 'http://challenge.code2040.org/api/dating'

challenge_endpoint = "http://challenge.code2040.org/api/dating/validate"
response1 = requests.post(datingHTTP, data=json.dumps(tokens),headers=header).json()

datestamp = response1["datestamp"]
interval = response1["interval"]

receiveTime = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
newTime = receiveTime + timedelta(seconds=interval)
newFormatTime = newTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    



datingResult = {"token": token,"datestamp":newFormatTime}
response1 = requests.post(challenge_endpoint, data=json.dumps(datingResult),headers=header)
print( response1.text)
