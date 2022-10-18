import re
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)
# driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/week/index.htm')

# all_music = driver.find_elements(By.CLASS_NAME, 'lst100')
# print(all_music)

tbody = driver.find_element(By.XPATH, '//*[@id = "frm"]/div/table/tbody')
# print(tbody)
trs = tbody.find_elements(By.TAG_NAME, 'tr')
# print(trs)


datas = []
for i in trs:
    rank = i.find_element(By.CLASS_NAME, "rank").text.strip()
    title = i.find_element(By.CLASS_NAME, "rank01").text.strip()
    #title = i.find_element(By.CLASS_NAME, "wrap_song_info").find_element(By.TAG_NAME, 'a').text.strip()
    singer = i.find_element(By.CLASS_NAME, "rank02").text.strip()
    album = i.find_element(By.CLASS_NAME, "rank03").text.strip()
    like = i.find_element(By.CLASS_NAME, "cnt").text
    like = re.sub(',', '', like)
    datas.append([rank, title, singer, album, like])

music_df = pd.DataFrame(datas, columns=('순위', '제목', '가수', '앨범', '좋아요'))
print(music_df)
