from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# 設定 Chrome 驅動程式的路徑
driver_path = 'chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 打開目標網站
driver.get('https://funcommunity.gameme.com/players/css2')

# 初始化數據列表
all_data = []

# 提取表頭，並去除不需要的標題
table_xpath = '/html/body/div[4]/div/div[2]/table'
table = driver.find_element(By.XPATH, table_xpath)
headers = [header.text for header in table.find_elements(By.XPATH, './/thead/tr/th') if header.text not in ["Activity Time", "Hpk", "Acc"]]
if not headers:
    headers = ["Rank", "Name", "Points", "Game Time", "Kills", "Deaths", "Kpd", "Hs"]

# 添加國家欄位到表頭
headers.append("Country")

# 找到總頁數
total_pages_xpath = '/html/body/div[4]/div/div[2]/table/tbody/tr[52]/td/span[3]/b[2]'
total_pages = int(driver.find_element(By.XPATH, total_pages_xpath).text)

# 遍歷每一頁
for page in range(1, total_pages + 1):
    # 確認頁面加載完畢
    time.sleep(3)

    # 提取當前頁面的表格數據
    table = driver.find_element(By.XPATH, table_xpath)
    rows = table.find_elements(By.XPATH, './/tbody/tr')
    data = []
    for row in rows:
        cells = row.find_elements(By.XPATH, './/td')
        if len(cells) == 11:  # 包括所有欄位的總數
            country_element = cells[1].find_element(By.XPATH, './a[1]/img')
            country = country_element.get_attribute("alt") if country_element else "Unknown"
            # 去除不需要的欄位
            row_data = [cells[i].text for i in range(len(cells)) if i not in [3, 9, 10]]  # 忽略索引 3, 9, 10 的欄位
            row_data.append(country)
            data.append(row_data)

    # 添加當前頁面的數據到總數據列表中
    all_data.extend(data)

    # 如果不是最後一頁，跳轉到下一頁
    if page < total_pages:
        input_box = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/table/tbody/tr[52]/td/input')
        input_box.clear()
        input_box.send_keys(str(page + 1))
        input_box.send_keys(Keys.RETURN)

# 關閉瀏覽器
driver.quit()

# 將所有數據存入 DataFrame
df = pd.DataFrame(all_data, columns=headers)

# 保存數據到 CSV 文件
df.to_csv('all_player_data.csv', index=False, encoding='utf-8')
print("All data has been written to all_player_data_with_country.csv")
