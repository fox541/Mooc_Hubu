import requests
from bs4 import BeautifulSoup

hyperlinks = [url + i['href'].split('./')[1] for i in links]

from IPython.display import display_html, HTML

#获得历年链接
url = "http://www.hprc.org.cn/wxzl/wxysl/lczf/" 
content = requests.get(url)

# 定义网页解析编码
content.encoding = 'utf8' # 'gb18030'
content = content.text

import sys
def flushPrint(s):
    sys.stdout.write('\r')
    sys.stdout.write('%s' % s)
    sys.stdout.flush()
    
def crawler(url_i):
    content = requests.get(url_i)
    content.encoding = 'utf8'  
    content = content.text
    soup = BeautifulSoup(content, 'html.parser') 
    year = soup.find('span', {'class', 'huang16c'}).text[:4]
    year = int(year)
    report = ''.join(s.text for s in soup('p'))
    # 找到分页信息
    scripts = soup.find_all('script')
    countPage = int(''.join(scripts[1]).split('countPage = ')[1].split('//')[0])
    if countPage == 1:
        pass
    else:
        for i in range(1, countPage):
            url_child = url_i.split('.html')[0] +'_'+str(i)+'.html'
            content = requests.get(url_child)
            content.encoding = 'gb18030'
            content = content.text
            soup = BeautifulSoup(content, 'html.parser') 
            report_child = ''.join(s.text for s in soup('p'))
            report = report + report_child
    return year, report

# 抓取50年政府工作报告内容
reports = {}
for link in hyperlinks:
    year, report = crawler(link)
    flushPrint(year)
    reports[year] = report
    
    
    
with open('v:/gov_reports.txt', 'w', encoding = 'utf8') as f:
    for r in reports:
        line = str(r)+'\t'+reports[r].replace('\n', '\t') +'\n'
        f.write(line)
        
import pandas as pd

df = pd.read_table('v:/gov_reports.txt', names = ['year', 'report'])

df[-5:]

