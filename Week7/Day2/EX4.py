from datetime import date
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.jpost.com/israel-news'
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options = options)
# driver.get(url)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('h3', class_= 'itc-info-title')
titles = [title.get_text() for title in titles]
#print(titles)

dates = soup.find_all('span', class_='category-list-item-date')
dates = [date.get_text() for date in dates]
#print(dates)

data = {'title': titles,
        'publication date': dates}

df = pd.DataFrame(data)

df['publication date'] = pd.to_datetime(df['publication date'], format='%d/%m/%Y')


df['publication month'] = df['publication date'].dt.strftime('%B') #B will extract full month name


grouped_data = df.groupby('publication month').count()
print(grouped_data)