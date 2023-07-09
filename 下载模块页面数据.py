from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
fileToRead = open("下载首页.html", "rb")  # 以二进制方式打开文档
html = fileToRead.read()
bs = BeautifulSoup(html, "html.parser")  # 解析文档，用html的解析器
url_all = bs.select('.css-ugp5z3')

for i in range(len(url_all)):
    url=url_all[i].attrs['href']
    driver.get(url)
    time.sleep(5)
    pageSource = driver.page_source
#以变量i的值加上".html"后缀，表示将创建以该值命名的HTML文件
    fileToWrite = open(str(i+1)+"模块.html", "w", encoding="utf-8")
    fileToWrite.write(pageSource)
    fileToWrite.close()
driver.close()