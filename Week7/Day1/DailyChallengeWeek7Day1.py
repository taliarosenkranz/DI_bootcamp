import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/topics"
response = requests.get(url,)
print(response.status_code)
#print(response.text[:100])

with open ('webpage.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

with open('webpage.html','r', encoding= 'utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

h2 = soup.find('h2', class_='h2')
h2 = h2.get_text().strip()
print(h2)
print(len(h2))
links = soup.find_all('a', class_ = 'no-underline flex-grow-0')
urls = [link['href'] for link in links]
base_url = 'https://github.com/'
topic_urls = [base_url+url for url in urls]
print(len(urls))
print(len(topic_urls))

topics = soup.find_all('p', class_ = 'f3 lh-condensed mb-0 mt-1 Link--primary')
topics = [topic.get_text() for topic in topics]
print(len(topics))
print(topics)

data = {'Topics':topics,
        'Part_url':urls,
        'Full_url': topic_urls}
df = pd.DataFrame(data)
print(df)

df.to_csv('git_hub_topics.csv')