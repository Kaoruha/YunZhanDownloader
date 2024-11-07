import time
import os
import pyautogui
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

out_dir = "output"
os.system(f"mkdir {out_dir}")
url = "https://book.yunzhan365.com/xqcsj/yfly/mobile/index.html"
max_page = 1018

service = Service("/home/kaoru/Documents/docsdownload/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get(url)

page = 1


max_try = 3


def download_img():
    global page
    x_filter = f"//html/body/div[@id='tmpContainer']/div[@id='bookContainer']/div[@class='book'][1]/div[@id='pageMask{page}']/div[@id='page{page}']/div[@class='side-content']/div[@class='side-image']"
    ele = driver.find_element(By.XPATH, x_filter)
    ele = ele.find_element(By.TAG_NAME, "img")
    pic_url = ele.get_attribute("src")
    try_time = 0
    while try_time < max_try:
        try_time += 1
        file_path = os.path.join(out_dir, f"{page}.jpg")
        response = requests.get(pic_url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_counter(1024):
                    f.write(chunk)
        size = os.stat(file_path).st_size
        if size > 0:
            break
        else:
            print(f"Failed to download image. Status code: {response.status_code}")

    page += 1


time.sleep(5)


download_img()

while True:
    pyautogui.press("right")
    time.sleep(1)
    download_img()
    time.sleep(0.2)
    download_img()
    time.sleep(0.2)

    if page >= max_page:
        break


driver.quit()
