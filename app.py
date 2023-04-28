from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.edenge.com.tr/'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(1)
login=driver.find_element("xpath",'//*[@id="username_"]')
login.click()
time.sleep(1)
login.send_keys("gusta@megasav.com")
password=driver.find_element("xpath",'//*[@id="password_"]')
password.click()
time.sleep(1)
password.send_keys("pass")
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
time.sleep(2)
content =driver.find_elements(By.CLASS_NAME,"js_obasket_parents")
# pageNo=driver.find_elements(By.CLASS_NAME,'product-navigation')  
# disablePNo = driver.find_elements(By.CLASS_NAME,'PagedList-skipToNext')
content2=driver.find_element(By.CLASS_NAME,"PagedList-skipToNext").find_element(By.CLASS_NAME,'js_pagelink')


def get_data():
    pruduct=driver.find_element(By.CLASS_NAME, 'product-title')
    print(f"Ürün İsmi:{pruduct.text}")
    smallTitle=driver.find_element(By.CLASS_NAME, 'product-title-small')
    print(f"Description:{smallTitle.text}")
    stokMiktar=driver.find_element(By.CLASS_NAME,'product-stock ')
    splitText1=(stokMiktar.text).split('+')
    splitText2=splitText1[0]
    splitText3=splitText2.split(' ')
    print(f"Stok Miktarı:{splitText3[-1]}")
    imageArr=[]
    images = driver.find_elements(By.CLASS_NAME, 'owl-item') 
    for i in images:
        a=i.find_element(By.CLASS_NAME,'item').get_attribute('href')
        if a != None:    
            # print(f"YENİ URL:{a}") 
            imageArr.append(a)
    print(f"Resimler:{imageArr}")
    price=driver.find_element(By.CLASS_NAME, 'product-price-item-price').find_element(By.TAG_NAME,'strong')
    print(f"Özel Fiyat :{price.text}")
    table=driver.find_element(By.CLASS_NAME, 'table-1')
    row=table.find_elements(By.TAG_NAME,'tr')
    for i in row:
        col=i.find_element(By.TAG_NAME,'th')
        col2=i.find_element(By.TAG_NAME,'td')
        print(f"{col.text} : {col2.text}")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    time.sleep(1)
driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/a").click()
get_data()

# while True:
    
#     content = driver.find_elements(By.CLASS_NAME, "js_obasket_parents")
#     content2 = driver.find_element(By.CLASS_NAME, "PagedList-skipToNext").find_element(By.CLASS_NAME, 'js_pagelink')

#     i=2   
#     while  i-2 < len(content):
#         path="/html/body/main/section[2]/div/div/div[2]/div/div[2]/div[1]/div"
#         asilDiv="/div["+str(i)+"]"
#         devami="/div[3]/a"
#         yeniPath=path+asilDiv+devami

#         yeniClick=driver.find_element(By.XPATH,yeniPath)
#         actions=ActionChains(driver)
#         actions.move_to_element(yeniClick).perform()
#         time.sleep(1)
#         yeniClick.click()
#         get_data()
        
#         driver.back()
#         time.sleep(2)
#         i += 1
        
#     if i > 61:
#         content2.click()
#         print("SIRADAKİ SAYFAYA GEÇİLDİ")
#         time.sleep(2)
            
