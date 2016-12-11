# coding=utf-8


import urllib2
import re


html = urllib2.urlopen('http://daily.zhihu.com/').read().decode('utf8')
r = r'<div class="wrap"><div class="box"><a href="(.*?)" class="link-button"><img src=".*?" class="preview-image"><span class="title">(.*?)</span></a></div></div>'
reg = re.compile(r)
html = re.findall(reg, html)
for i in html:
    reg = re.compile(r'<div class="content">(.*?)<div class="view-more">', re.S)
    url = 'http://daily.zhihu.com'+ i[0]
    html = urllib2.urlopen(url).read()
    html = re.findall(reg, html)
    print i
    try:
        with open('%s.html' % i[1], 'wb') as f:
            f.write(html[0])
    except Exception, e:
        print e
        continue
