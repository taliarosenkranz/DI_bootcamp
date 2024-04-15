from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pprint  # To tidy up
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
#options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode
# options.add_argument("--no-sandbox")  # Bypass OS security model
# options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
#driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))
print("here before url")
#driver.get(url)
print("here after url")
#wait = WebDriverWait(driver, 5)
#html_content = driver.page_source
#print(html_content)
soup = BeautifulSoup(response.text, 'html.parser')
#soup = BeautifulSoup(html_content, 'html.parser')
titles = soup.find_all('span', class_= 'p--small')[4:]
titles = [title.get_text().strip() for title in titles]
#print(titles)

dates = soup.find_all('span', class_='smaller')
dates = [date.get_text().strip()[10: ]for date in dates]
#print(dates)


# scores = soup.find('span',attrs = {'data_qa':'audience-score'})
# print(scores)
#scores = soup.find_all('span', attr = {'data_qa':'audience-score'})

movie_elements = soup.find_all('div', class_='flex-container')
scores = []

for movie in movie_elements:
    print(movie)
    score = movie.find('score-pairs-deprecated')['audiencescore']
    scores.append(score)
#scores = [score.get_text().strip() for score in scores]
print(scores)


data = {'title':titles,
        'date':dates,
        'score':scores}
print(len(titles))
print(len(dates))
print(len(scores))


df = pd.DataFrame(data)
print(df)

