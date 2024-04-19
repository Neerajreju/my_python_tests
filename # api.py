# api
# the kany aapi
import requests
response = requests.get(url="https://api.kanye.rest/")
for i in range(3):
    print(response.content)
