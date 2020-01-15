from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        driver = webdriver.Chrome()
        driver.get("https://instagram.com")
        sleep(2)
        driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)


InstaBot('USERNAME','PASSWORD')
