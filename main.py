from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from urls import urls
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



lista = {}
for url in urls:
    driver.get("https://instagram.com/" + url)
    driver.implicitly_wait(3)
    try:
        followers = driver.find_elements(By.CLASS_NAME, "html-span")[1].text
        followers = int(followers.replace(',', ''))
        lista[url] = followers
    except:
        lista[url] = "0"
name_list, follow_list = [], []
for key in lista:
    name_list.append(key)
    follow_list.append(lista[key])

df = {'Names': name_list, 'Follows': follow_list}
df = pd.DataFrame.from_dict(df)
df.to_excel('Follow list.xlsx')
