import time
import os
import pyautogui
import random
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
        os.system(f"wget {pic_url} -O {out_dir}/{page}.jpg")
        size = os.stat(f"{out_dir}/{page}.jpg").st_size
        if size > 0:
            break

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
