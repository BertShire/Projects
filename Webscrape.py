import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
driver.get("https://www.pba.com/players")
Page2 = driver.find_element_by_name(2)
print(driver.title)
time.sleep(3)
driver.close()