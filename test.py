import requests
url = "http://google.com"
r = requests.get(url)
r.status_code

print("Requested url from Google and got this response: " + r.status_code)
