### References
# http://httpbin.org/
# http://docs.python-requests.org/en/master/user/quickstart/



#first test
import requests
url = "http://google.com"
r = requests.get(url)
r.status_code

print("Requested url from Google and got this response: " + str(r.status_code))

#Key/Value Payload test
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

#JSON test
r = requests.get('https://api.github.com/events')
r.json()
print(r.json())

#form encoded data
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
