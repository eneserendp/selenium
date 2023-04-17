from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager



url = 'https://www.edenge.com.tr/'
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
driver.maximize_window()
time.sleep(3)
login=driver.find_element("xpath",'//*[@id="username_"]')
login.click()
time.sleep(1)
login.send_keys("gusta@megasav.com")

password=driver.find_element("xpath",'//*[@id="password_"]')
password.click()
time.sleep(1)
password.send_keys("Girmemesilazım")

log_in=driver.find_element("xpath",'//*[@id="loginForm"]/div[4]/div[1]/button')

log_in.click()
time.sleep(1)

time.sleep(2)
driver.close()