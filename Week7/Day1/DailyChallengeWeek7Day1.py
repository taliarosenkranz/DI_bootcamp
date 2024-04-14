import requests
from bs4 import BeautifulSoup

url = "https://github.com/topics"
response = requests.get(url,)
print(response.status_code)
print(response.text[:100])
with open (response.text, 'webpage.html'):

soup = BeautifulSoup(response.text, 'html.parser')
