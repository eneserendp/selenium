from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains






url = 'https://www.edenge.com.tr/'
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
driver.maximize_window()
time.sleep(1)

login=driver.find_element("xpath",'//*[@id="username_"]')
login.click()
time.sleep(1)
login.send_keys("gusta@megasav.com")

password=driver.find_element("xpath",'//*[@id="password_"]')
password.click()
time.sleep(1)
password.send_keys("usernamepassword")

log_in=driver.find_element("xpath",'//*[@id="loginForm"]/div[4]/div[1]/button')

log_in.click()
time.sleep(1)


continue_link = driver.find_element(By.CLASS_NAME, 'navigation-categories-item-title')
print(f"Kategori İsmi:{continue_link.text}")

time.sleep(1)
achains =ActionChains(driver)

time.sleep(1)
achains.move_to_element(continue_link).perform()
time.sleep(1)
morebutton=driver.find_element(By.CLASS_NAME, 'navigation-categories-dropdown-head-title').click()
time.sleep(1)

content =driver.find_element("xpath",'/html/body/main/section[2]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/a/h4').click()

time.sleep(1)


pruduct=driver.find_element(By.CLASS_NAME, 'product-title')
print(f"Ürün İsmi:{pruduct.text}")

time.sleep(1)

smallTitle=driver.find_element(By.CLASS_NAME, 'product-title-small')

print(f"Kısa Açıklama:{smallTitle.text}")

time.sleep(1)

stokMiktar=driver.find_element("xpath",'/html/body/main/section[2]/div/div/div/div[2]/div[2]/div[2]')

print(stokMiktar.text)

time.sleep(1)
ImageUrl=driver.find_element(By.CLASS_NAME, 'area-product-image').find_element(By.CSS_SELECTOR,'a').get_attribute('href')

print(f"Resim Url:{ImageUrl}")
time.sleep(1)






