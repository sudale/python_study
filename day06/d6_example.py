import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path)
# driver.implicitly_wait(2)
driver.get('https://finance.naver.com/item/frgn.nhn?code=263050')

time.sleep(1)

pageNum_list = driver.find_elements(
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr/td/a')
# /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr/td[2]/a
print(len(pageNum_list))
time.sleep(1)
# print(len(list), "@@@@@@@@@@@@@@@@@@@@@@@@@@")
# /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr[4]
# /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr[5]
# /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr[12]
datas = []

for j in range(1, len(pageNum_list)):
    list = driver.find_elements(By.XPATH,
                                f'/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr')
    # /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr[4]
    # /html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr[5]
    # time.sleep(1)
    for i in list:
        try:
            stock_day = i.find_element(
                By.CLASS_NAME, 'p10').text.strip()
            stock_closing = i.find_element(
                By.CLASS_NAME, 'p11').text.strip()
            stock_fluctuation = i.find_element(
                By.XPATH, 'td[4]/span').text.strip()
            stock_volume = i.find_element(
                By.XPATH, 'td[5]/span').text.strip()
            # print(stock_closing)
            datas.append([stock_day, stock_closing,
                          stock_fluctuation, stock_volume])
        except:
            continue
        if i == len(pageNum_list):
            break
    # driver.find_element(
    #     By.CSS_SELECTOR, '#content > div.section.inner_sub > table.Nnavi > tbody > tr > td.pgR > a').click()

    #content > div.section.inner_sub > table.Nnavi > tbody > tr > td.on > a

    pageNum_list[j].click()

    time.sleep(1)
    pageNum_list = driver.find_elements(
        By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr/td/a[not(@class="pgLL")]')
print(datas)
