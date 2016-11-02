import requests as r

payload = {'token':'a507960e4f5b9aaced42072be76bdb5b'}

def prefix():

   r = requests.post("http://challenge.code2040.org/api/prefix",
                     data={'token': token})

   words = r.json()
   len_pref = len(words['prefix'])

   non_prefixed = [str(word) for word in words['array'] if word[0:len_pref] != words['prefix']]

   payload = {'token': token, 'array': non_prefixed}
   r = requests.post("http://challenge.code2040.org/api/prefix/validate",
                     json=payload)
   print(r.status_code, r.reason) 