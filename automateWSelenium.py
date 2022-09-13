from gettext import find
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()



driver = webdriver.Firefox()
driver.get("https://br.betano.com/casino/games/aviator/3337/?sbLoadEvent=true")
time.sleep(10000)
username = driver.find_element(By.NAME, 'username')
username.click()
username.send_keys(username)
