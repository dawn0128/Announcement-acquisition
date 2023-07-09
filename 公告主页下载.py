from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get('https://www.binance.com/en/support/announcement')
time.sleep(10)
pageSource = driver.page_source
fileToWrite = open("下载首页.html", "w", encoding="utf-8")
fileToWrite.write(pageSource)
fileToWrite.close()
driver.close()
