from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import urllib
import time
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
driver.get('https://www.google.com/imghp?hl=ja&tab=ri&ogbl')

wait=WebDriverWait(driver, 10)

keyword="エスプレッソ"

driver.find_element(By.NAME, "q").send_keys(keyword)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > button").click()

time.sleep(5)

height=1000
while height <60000:
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height += 2500
    time.sleep(1)
#待機処理
wait.until(EC.presence_of_all_elements_located)

print("スクロール完了")

# コピーしたXPathを使って画像のWeb要素を取得
elements = driver.find_elements(By.TAG_NAME,"img")

# Web上の画像URLを取得
img_urls=[]
for img_url in elements:
    url_p=img_url.get_attribute("src")
    img_urls.append(url_p)
    print(img_urls)

#保存フォルダ作成、パス指定
save_dir="download/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

#バイナリデータ読み込み、保存
a=1
for img_url in img_urls:
    try:
        with urllib.request.urlopen(img_url) as rf:
            img_data = rf.read()
        with open(save_dir + f"{keyword}画像{a}.jpg","wb") as wf:
            wf.write(img_data)
        a=a+1
        time.sleep(1)
    except:
        pass

driver.quit()