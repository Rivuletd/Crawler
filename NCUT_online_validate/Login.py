# coding=utf-8
import urllib2
import urllib


Url = "http://192.168.254.251/0.htm"
username = '*********'
password = '*********'
postdata = {
'DDDDD': username,
'upass': password,
'0MKKey': 1,
'v6ip': 2,
}
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
}
data = urllib.urlencode(postdata)
request = urllib2.Request(Url, data, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
text = text.decode('gb2312').encode('utf-8')
print text
a = text.find('您已登陆成功')
print a
