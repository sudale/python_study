import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time


path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path)
# driver.implicitly_wait(2)
driver.get('https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun')

time.sleep(2)

pageNum_list = driver.find_elements(By.CLASS_NAME, 'num_page')

datas = []

for j in range(1, len(pageNum_list)):
    webtoon_list = driver.find_elements(
        By.CSS_SELECTOR, '#content > table > tbody tr')
    # print(webtoon_list)
    for i in webtoon_list:
        try:
            webtoon_name = i.find_element(
                By.CSS_SELECTOR, 'td.title > a').text.strip()
            webtoon_star = i.find_element(
                By.TAG_NAME, 'strong').text.strip()
            webtoon_date = i.find_element(
                By.CSS_SELECTOR, '#content > table > tbody > tr > td.num').text.strip()
            datas.append([webtoon_name, webtoon_star, webtoon_date])
            # print(datas)
        except:
            continue
        if j == len(pageNum_list):
            break
    driver.find_element(
        By.CSS_SELECTOR, '#content > div.paginate > div > a.next > span.cnt_page').click()
    time.sleep(1)
print(datas)
