import requests
from bs4 import BeautifulSoup
import pandas as pd

# with open('test.html', 'r') as file:
#    html = file.read()
    

# soup = BeautifulSoup(html, 'html.parser')
# print(soup.title.get_text()) #gets title
# #print(soup.p.get_text()) #this will get the first p
# #print(soup.find_all('p'))

# for link in soup.find_all('a'): #this will only get the a tag not actual url
#     print(link.get('href'))

# #2
# url = "https://en.wikipedia.org/wiki/Main_Page"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# #print(soup.prettify())

# #3
# headers = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
# for head in headers:
#     print(head.get_text().strip())

# #4
# title = soup.title.get_text()
# if title:
#     print(title)
# else:
#     print("no title found")

#6
url = "https://www.imdb.com/chart/top/"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
soup = BeautifulSoup(response.text, 'html.parser')
#html = soup.prettify()

#getting titles
movies = soup.find('ul', class_="ipc-metadata-list")
titles = movies.find_all('h3', class_ ='ipc-title__text')[:10]
titles = [title.get_text().strip() for title in titles]

#getting years
years = soup.find_all('div', class_ = 'cli-title-metadata')
release_years = [year.get_text()[0:4].strip() for year in years][:10]

name = []
year = []

#creating a df out of scraped data
for t,y in zip(titles, release_years):
    name.append(t)
    year.append(y)


#Getting the urls to get the summary in the end
links = soup.find_all('a', class_ ='ipc-title-link-wrapper')
hrefs = [link['href'] for link in links][:10]

url_start = "https://www.imdb.com/"
text = []
for link in hrefs:
    url = url_start+link
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
    soup = BeautifulSoup(response.text, 'html.parser')
    summary = soup.find('span', class_ = 'sc-466bb6c-2 chnFO')
    summary = [summary.get_text().strip() for summary in summary]
    text.append(summary)
print(text)

data = {'Title':name,
        'Release Year': year,
        'Summary': text
        }
df = pd.DataFrame(data)
print(df.head(10))

df.to_csv("top10.csv", index =False)