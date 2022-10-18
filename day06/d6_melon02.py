import re
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/week/index.htm')

# all_music = driver.find_elements(By.CLASS_NAME, 'lst100')
# print(all_music)

tbody = driver.find_element(By.XPATH, '//*[@id = "frm"]/div/table/tbody')
# print(tbody)
trs = tbody.find_elements(By.TAG_NAME, 'tr')
# print(trs)


datas = []
for i in trs:
    rank = i.find_element(By.CLASS_NAME, 'rank').text
    song = i.find_element(By.CLASS_NAME, "wrap_song_info").find_element(
        By.TAG_NAME, 'a').text.strip()
    name = i.find_element(By.CSS_SELECTOR, 'div.rank02').find_element(
        By.TAG_NAME, 'a').text
    album = i.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(
        By.TAG_NAME, 'a').text
    likes = i.find_element(By.CLASS_NAME, 'like').find_element(
        By.CLASS_NAME, 'cnt').text
    likes = re.sub(',', '', likes)
    datas.append([rank, song, name, album, likes])
    # print(album)
# print(datas)

melon_df = pd.DataFrame(datas, columns=('순위', '곡명', '가수명', '앨범', '좋아요'))
# print(melon_df)
melon_df.to_csv('melon1.csv', encoding='utf-8', mode='w', index=False)
