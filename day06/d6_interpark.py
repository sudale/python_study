import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:\\util\\chromedriver.exe"
# options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(path)
driver.get('http://tour.interpark.com/?mbn=tour_main&mln=tour_tour')

time.sleep(1)

input_text = driver.find_element(By.ID, 'SearchGNBText')
input_text.send_keys('제주도')
driver.execute_script('searchBarModule.ClickForSearch()')

time.sleep(2)

morebtn = driver.find_element(
    By.CSS_SELECTOR, 'div.searchAllBox.domesticHotel.col1 > div > button')
morebtn.click()

time.sleep(1)
pageNum_list = driver.find_elements(
    By.CSS_SELECTOR, 'div.pageNumBox > ul > li')
# #app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.pageNumBox > ul > li:nth-child(1)
datas = []
for j in range(1, len(pageNum_list)):
    product_list = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')
    for i in product_list:
        try:
            hotel_name = i.find_element(By.TAG_NAME, 'h5').text.strip()
            hotel_price = i.find_element(By.TAG_NAME, 'strong').text.strip()
            hotel_grade = i.find_element(
                By.CSS_SELECTOR, 'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]
            # print(hotel_name)
            datas.append([hotel_name, hotel_price, hotel_grade])

        except:
            continue
        if j == len(pageNum_list):
            break
    pageNum_list[j].click()
    time.sleep(1)
print(datas)

# hotel_df = pd.DataFrame(datas, columns=('호텔명', '가격', '평점'))
# # print(hotel_df)
# hotel_df.to_csv('hotel.csv', encoding='utf-8', mode='w', index=False)
