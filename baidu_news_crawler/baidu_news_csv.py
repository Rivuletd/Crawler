# coding=utf-8
import requests
import re
import csv

class GetAndStore:
    def __int__(self):
        pass
    def printHotNews(self, url):
        content = requests.get(url)
        content.encoding = 'gb2312'
        content = content.text
        pattern = re.compile('<i class="dot"></i>.*?<strong>.*?<a href="http://(.*?)".*?>(.*?)</a>.*?</strong>', re.S)
        hotNews = re.findall(pattern, content)
        with open('csvresult.csv', 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(('url', '标题'))
            for i in hotNews:
                f_csv.writerow(i)
                print(i)
instance = GetAndStore()
instance.printHotNews('http://news.baidu.com/')
