# 爬单页
import requests
from bs4 import BeautifulSoup

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
url = 'http://xcy.hubu.edu.cn/szqk/jsdw.htm'
data = requests.get(url,headers=header).content.decode('utf8')

soup = BeautifulSoup(data,'html.parser')

contentdiv = soup.find_all('div',{'class':'split'})
name = contentdiv[0].text

authordiv = soup.find_all('div',{'class':'infoArea'})
author = authordiv[0].find_all('span')
newsfrom = author[0].text
newsauthor = author[1].text


---------------------------------------
#采集单页URL目录   
#目标网页 ：首页 -> 师资情况 -> 教师队伍
import requests

from bs4 import BeautifulSoup

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url = 'http://xcy.hubu.edu.cn/szqk/jsdw.htm'
data = requests.get(url,headers=header).content.decode('utf8')
soup = BeautifulSoup(data,'html.parser')

urldiv = soup.find_all('div',{'class':'listguid'}) #我们院的快速导航，class名字竟然是右侧导航，哈哈哈哈

url_all=[]
for urltemp in urldiv:
    url = urltemp.a['href']
    url_all.append(url)
  
      
    
#采集多页URL  
#特点是页面下面是1234567导航，样本为学堂在线
import requests
from bs4 import BeautifulSoup
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url_path = 'http://www.xuetangx.com/courses?credential=0&page_type=0&cid=117&process=0&org=0&course_mode=0&page='   #
url_all=[]
for i in range(12):
    print(i)
    url = url_path + str(i+1)
    data = requests.get(url,headers=header).content.decode('utf8')
    soup = BeautifulSoup(data,'html.parser')    
    urldiv = soup.find_all('div',{'class':'coursename'})      
    for urltemp in urldiv:
        url_find = urltemp.a['href']
        url_all.append(url_find)






#采集多页URL+内页资料
import requests
from bs4 import BeautifulSoup
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url_path = 'https://www.shobserver.com/news/sublist?section=19&page='
url_all=[]
for i in range(3):
    print(i)
    url = url_path + str(i+1)
    data = requests.get(url, headers=header).content.decode('utf8')
    soup = Beautifulsoup(data, 'html parser')
    urldiv = soup.find_all('div',{'class': 'chengshi_wz_h'})
    for urltemp in urldiv:
        url_find = urltemp.a[ 'href']
        url_all.append(url_find)
        time_temp = random.randint(1, 7)
        time.sleep(time_temp)
                
name_all=[]
url_path='https://www.shobserver.com/'
for url_part in url_all
    print(url_part)
    url = url_path + url_part
    data = requests.get(url,headers=header).content.decode('utf8')
    soup = Beautifulsoup(data, 'html parser')
    namediv = soup.find_all('div',{'class':'wz_contents'})
    name = namediv[0].text
    authordiv = soup.find_all('div',{'class':'fenxiang_zz'})
    author = authordiv[0].find_all('span')
    newsfrom = author[0].text
    newsauthor =author[1].text
    contentdiv = soup.find_all('div',{'class':'newscontents'})
    content = contentdiv[0].text
    name_all.append(name)
    time_temp = random.randint(1,7)
    time.sleep(time_temp)
