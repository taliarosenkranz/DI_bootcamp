
from datetime import date
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://weather.com/weather/tenday/l/1113fba38e09773bd1c20c1f70b48f045cd0d1bd62eaa2d37a47c5cc58d12b7b'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temperatures = soup.find_all('span', class_ = 'DetailsSummary--highTempValue--3PjlX')
temperatures = [temp.get_text() for temp in temperatures]
print(len(temperatures))
#print(temperatures)


humidity = soup.find_all('span', 'DetailsTable--value--2YD0-')
humidity = [hum.get_text().strip() for hum in humidity if '%' in hum.get_text().strip()][:15]
print(len(humidity))
#print(humidity)


condition = soup.find_all('p', class_='DailyContent--narrative--3Ti6_')
condition = [con.get_text() for con in condition][:15]
print(len(condition))
#print(condition)

dates = soup.find_all('span', class_='DailyContent--daypartDate--3VGlz')
dates = [date.get_text() for date in dates][:15]
print(len(dates))
#print(dates)

data = {'date':dates,
        'temperature': temperatures,
        'humidity': humidity,
        'condition':condition
        }

df = pd.DataFrame(data)
print(df.head())
print(df.info())


df["temperature"]= df["temperature"].str[:-1]
df["humidity"]= df["humidity"].str[:-1]
df['temperature'] = pd.to_numeric(df['temperature'].str.replace('-', ''), errors='coerce')
print(df.head())

#df['date'] = pd.to_datetime(df['date'], format='%d/%m')
print(df.info())
avg_temp = df["temperature"].mean()
print('AVERAGE TEMOERATURE:',avg_temp)