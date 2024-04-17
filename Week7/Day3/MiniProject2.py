
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time


options = FirefoxOptions()
#options.add_argument("--headless") # headless means invisible- browser don't open
#options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful for headless mode)
driver = webdriver.Firefox(options=options)
url = 'https://www.scrapethissite.com/pages/frames/'
driver.get(url)
wait = WebDriverWait(driver, 10) 
    
iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe')))
family_name = []
total_buttons = driver.find_elements(By.CLASS_NAME, "btn.btn-default.btn-xs")
num_buttons = len(total_buttons)

for i in range(num_buttons):
    driver.switch_to.default_content()
    # Find the iframe by its ID or name (or other attributes like index)
    iframe = driver.find_element(By.ID, 'iframe')
    # Switch to the iframe
    driver.switch_to.frame(iframe)
    driver.execute_script("arguments[0].scrollIntoView();", iframe)
    links = driver.find_elements(By.CLASS_NAME, 'btn.btn-default.btn-xs')
    print(links[i].text)
    links[i].click()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source , 'html.parser')
    fam_name = soup.find('h3', class_='family-name')
    name = [name.get_text() for name in fam_name]
    family_name.append(name)
    print('fam name:', family_name)
    time.sleep(5)
    backlink = driver.find_element(By.CLASS_NAME, 'btn.btn-default.btn-xs')
    backlink.click()
    time.sleep(5)
print("DONE")

data = {'Turtle Name:', family_name}
df = pd.DataFrame(data)
df.to_csv('turtles.csv', index=False)
