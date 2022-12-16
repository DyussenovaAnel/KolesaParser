# import libraries
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

# define the URL to crawl & parse
# feel free to change this URL with your own app
app_url = 'https://kolesa.kz/cars/almaty/'

# crawling the page. This might take a few seconds
page = requests.get( app_url )

# to print the page contents type:
# print(page.content)


soup = bs(page.content, 'html.parser')

pages = soup.find("div", class_="pager")
page = int(pages.find_all("li")[-1].getText())
print(page)
# page = 53


def parsee(url):
    driver = webdriver.Firefox()
    driver.get(url)
    button = driver.find_element(By.CLASS_NAME, 'seller-phones__show-button')
    button.click()
    elementList_phone = ""
    try:
        parentElement = driver.find_element(By.CLASS_NAME, "seller-phones__phones-list")
        elementList = parentElement.find_element(By.TAG_NAME, "li").get_attribute('innerText')
        elementList_phone = elementList.replace(" ", "")
        elementList_phone = elementList_phone.replace("+", "")
        # print(elementList_phone)
        driver.close()
        return elementList_phone
    except:
        driver.close()


for i in range(2, page):
    url = app_url+'?page='+str(i)
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    aa = soup.find_all("a")
    aa = list(set(aa))
    for aaa in aa:
        a_href = aaa["href"]
        if "/a/show/" in a_href:
            print(a_href,"\n")
            app_url = 'https://kolesa.kz'+a_href
            print(parsee(app_url), "\n")



# print(parsee("https://kolesa.kz/a/show/127369030"))

