from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://apnews.com/article/strait-of-hormuz-vessel-33fcffde2d867380e98c89403776a8ac"
response = requests.get(url)
soup = bs(response.text, "html.parser")
#print(soup.prettify())

# print(soup.h1)
# print(soup.h1.getText())
# print(soup.p.get_text())
# print(soup.find_all("li"))

#find all paragraphs and put into a pandas df

content = soup.find_all(class_ = "RichTextStoryBody RichTextBody")
content = [con.get_text().strip() for con in content]
print(content[:5])

df=pd.DataFrame({"para1":content})

df.head()