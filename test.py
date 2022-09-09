import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Here Chrome  will be used
driver = webdriver.Firefox()

# URL of website
url = "https://kolesa.kz/a/show/127369030"

# Opening the website
driver.get(url)

# getting the button by class name
button = driver.find_element(By.CLASS_NAME, 'seller-phones__show-button')
# button = driver.find_element_by_class_name('seller-phones__show-button')

# clicking on the button
button.click()

print("heello")
parentElement = driver.find_element(By.CLASS_NAME,"seller-phones__phones-list")
# parentElement = driver.find_element_by_class_name("seller-phones__phones-list")
elementList = parentElement.find_element(By.TAG_NAME,"li").get_attribute('innerText')
elementList = elementList.replace(" ", "")
elementList = elementList.replace("+", "")
print(elementList)

# for ele in elementList:
#     print(ele.get_attribute('innerText'))

# try:
#     parentElement = driver.find_element(By.CLASS_NAME, "seller-phones__phones-lis")
#     elementList = parentElement.find_element(By.TAG_NAME, "li").get_attribute('innerText')
#     elementList = elementList.replace(" ", "")
#     elementList = elementList.replace("+", "")
#     print(elementList)
#     driver.close()
# except:
#     driver.close()