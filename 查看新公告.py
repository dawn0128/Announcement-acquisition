from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime
n = 0
conn = sqlite3.connect('announcements.db')
cursor = conn.cursor()

for i in range(1, 9):
    fileToRead = open(str(i) + "模块.html", "rb")  # 以二进制方式打开文档
    html = fileToRead.read()
    bs = BeautifulSoup(html, "html.parser")  # 解析文档，用html的解析器
    a = bs.select('.css-eoufru')

    if i == 1:
        n = 'New Cryptocurrency Listing'
    elif i == 2:
        n = 'Latest Binance News'
    elif i == 3:
        n = 'Latest Activities'
    elif i == 4:
        n = 'New Fiat Listings'
    elif i == 5:
        n = 'API Updates'
    elif i == 6:
        n = 'Crypto Airdrop'
    elif i == 7:
        n = 'Wallet Maintenance Updates'
    else:
        n = 'Delisting'
    # 获取当前时间
    current_time = datetime.now()

    # 格式化时间输出
    formatted_time = current_time.strftime("%Y-%m-%d")

    for j in range(20):  # 循环打开每个模块
        timeout = a[j]
        film_name = re.findall('class="css-eoufru" data-bn-type="text">(.*?)</h6>', str(timeout))  #获取公告的时间，此时是元组形式

        '''
        print(film_name[0])      
        '''

        if film_name[0] == str(formatted_time):     #当公告时间在今天时，提取公告信息

            print('                      ', n + '模块', '有新公告')  # 如果有新公告，新公告的时间应为今天，然后输出是哪个模块里有新公告
            t = bs.select('.css-f94ykk')[j].get_text().strip(str(formatted_time))    #得到公告名称，并去除掉多余的时间显示
            print('第' + str(j + 1) + '个公告名为：', t)  # 打印出新公告的名称
            url = bs.select('.css-1ey6mep')[j].attrs['href']        #获取网址
            print('链接为：https://www.binance.com' + url)       #得到其完整网址

            '''   将模块名称，公告名，公告地址和时间写入之前创建的数据库中   '''
            announcements = [
                {
                    'module': n,
                    'name': t,
                    'link': 'https://www.binance.com' + url,
                    'time': formatted_time
                },

            ]

            for announcement in announcements:
                cursor.execute('''
                    INSERT INTO announcements (module, name, link, time)
                    VALUES (?, ?, ?, ?)
                ''', (announcement['module'], announcement['name'], announcement['link'], announcement['time']))

        else:
            continue

conn.commit()
conn.close()

print("Announcements added to the database successfully.")
