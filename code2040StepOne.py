import requests 
r = requests.post('http://challenge.code2040.org/api/register',
	data={'token':'a507960e4f5b9aaced42072be76bdb5b','github': 'https://github.com/shahisa/Code2040TechFellowshipApp'
})

print(r.status_code)
