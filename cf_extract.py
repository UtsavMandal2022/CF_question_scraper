from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Utsav Mandal

# Set up the Chrome driver
ser = Service('chromedriver.exe')  # Path to chromedriver executable
driver = webdriver.Chrome(service=ser)

cf_page='https://codeforces.com/problemset/page/'

def get_p_links(ind):
    driver.get(cf_page+str(ind))
    time.sleep(5)
    a_tags = driver.find_elements(By.TAG_NAME, 'a')
    links=[]
    for a in a_tags:
        if "/problem/" in a.get_attribute('href'):
            # print(a.get_attribute('href'))
            links.append(a.get_attribute('href'))
    links=list(set(links))
    return links

def rempat(arr,pat):
    arr2=[]
    for i in arr:
        if pat not in i:
            arr2.append(i)
    return arr2

arr=[]

for i in range(1,88):
    arr+=get_p_links(i)
arr=list(set(arr))

result=[]

result=rempat(arr,'/status/')

print(len(result))

with open('cf_links.txt','w') as f:
    for link in result:
        f.write(link+'\n')

driver.quit()