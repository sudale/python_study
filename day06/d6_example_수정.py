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
datas = []


def PageSearch():
    list = driver.find_elements(By.XPATH,
                                f'/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody/tr')
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
            datas.append([stock_day, stock_closing,
                         stock_fluctuation, stock_volume])
            print([stock_day, stock_closing, stock_fluctuation, stock_volume])
        except:
            continue
    return None


def PageLength():
    pageLen = driver.find_elements(
        By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr/td')
    count = 0
    countFront = 0
    countBack = 0
    for i in pageLen:
        tag = i.get_attribute('class')
        if tag.startswith('pgRR') or tag.startswith('pgR'):
            countBack += 1
        elif tag.startswith('pgLL') or tag.startswith('pgL'):
            countFront += 1
        else:
            count += 1
    return countFront, count


page = 1
while True:

    PageLength()
    try:
        for i in range(PageLength()[0]+1, PageLength()[1]+1):
            driver.find_element(
                By.XPATH, f'/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr/td[{i}]/a').click()
            time.sleep(1)
            PageSearch()

    except:
        pass
    driver.find_element(
        By.XPATH, '#content > div.section.inner_sub > table.Nnavi > tbody > tr > td.pgR').click()
    if PageLength()[2] != 2:
        break
