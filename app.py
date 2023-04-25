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
password.send_keys("Mert1606")

log_in=driver.find_element("xpath",'//*[@id="loginForm"]/div[4]/div[1]/button')

log_in.click()
time.sleep(1)


continue_link = driver.find_element(By.CLASS_NAME, 'navigation-categories-item-title')
print(f"Kategori İsmi:{continue_link.text}")

time.sleep(1)
achains =ActionChains(driver)

time.sleep(1)
achains.move_to_element(continue_link).perform()
time.sleep(3)
morebutton=driver.find_element(By.CLASS_NAME, 'navigation-categories-dropdown-head-title').click()
time.sleep(2)

content =driver.find_elements(By.CLASS_NAME,"js_obasket_parents")
# pageNo=driver.find_elements(By.CLASS_NAME,'product-navigation')  
# disablePNo = driver.find_elements(By.CLASS_NAME,'PagedList-skipToNext')
content2=driver.find_element(By.CLASS_NAME,"PagedList-skipToNext").find_element(By.CLASS_NAME,'js_pagelink')




# for indexP , k in enumerate(content2):
#     time.sleep(5)
#     clickedPad = k.find_element(By.CLASS_NAME,'js_pagelink').click()
#     time.sleep(5)
    
    

    

    # if k == disablePNo:

        # for index , i in enumerate(content) :
        #     exam=i.find_elements(By.CLASS_NAME,"table-cell")
        #     print(f"{index}.üründe")

        #     for idx , j in enumerate(exam):
        #         if idx==2 :
        #             innerexam=j.find_element(By.TAG_NAME,'a').click()
        #             single page'e gitti, verileri çek
        #             driver.back()

    # else:
    #     clickedPad = k.find_element(By.CLASS_NAME,'js_pagelink').click()

    #     time.sleep(3)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Sayfayı aç
driver.get("http://example.com")

for index , i in enumerate(content) :
     exam=i.find_elements(By.CLASS_NAME,"table-cell")
     print(f"{index}.üründe")
     



     for idx , j in enumerate(exam):
         if idx==2 :
            innerexam=j.find_element(By.TAG_NAME,'a').click()
                    # single page'e gitti, verileri çek

            driver.back()
time.sleep(3)             
content2.click()    
time.sleep(3)
       

    
    

            

        
    


# pruduct=driver.find_element(By.CLASS_NAME, 'product-title')
# print(f"Ürün İsmi:{pruduct.text}")

# time.sleep(1)

# smallTitle=driver.find_element(By.CLASS_NAME, 'product-title-small')

# print(f"Description:{smallTitle.text}")

# time.sleep(1)

# stokMiktar=driver.find_element(By.CLASS_NAME,'product-stock ')

# splitText1=(stokMiktar.text).split('+')
# splitText2=splitText1[0]
# splitText3=splitText2.split(' ')
# print(f"Stok Miktarı:{splitText3[-1]}")



# time.sleep(1)
# imageArr=[]

# images = driver.find_elements(By.CLASS_NAME, 'owl-item') 
# for i in images:
#     a=i.find_element(By.CLASS_NAME,'item').get_attribute('href')

#     if a != None:    
#         # print(f"YENİ URL:{a}") 
#         imageArr.append(a)
 
# print(f"Resimler:{imageArr}")

# price=driver.find_element(By.CLASS_NAME, 'product-price-item-price').find_element(By.TAG_NAME,'strong')
# print(f"Özel Fiyat :{price.text}")

# time.sleep(1)


# table=driver.find_element(By.CLASS_NAME, 'table-1')
# row=table.find_elements(By.TAG_NAME,'tr')



# for i in row:

#     col=i.find_element(By.TAG_NAME,'th')
#     col2=i.find_element(By.TAG_NAME,'td')
#     print(f"{col.text} : {col2.text}")
    
# print("----------------------------------------------------------------")
# print("----------------------------------------------------------------")

# driver.back()







