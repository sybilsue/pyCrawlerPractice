# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
}
df = pd.DataFrame(columns=['title','abstract','author','source','year'])
index = 1
def getConntent(url):
    html = requests.get(url, headers=headers, timeout = 20).text
    soup = BeautifulSoup(html,'html.parser')
    contentHtml = soup.find_all(class_ = 'sc_content')
    for html in contentHtml:
        global index
        thisArticl = []
        title = html.find('h3').text.strip()
        print(index,title)
        thisArticl.append(title)
        abstract = html.find(class_ = 'c_abstract').text.strip()
        thisArticl.append(abstract)
        author = ','.join([a.text.strip() for a in html.find(class_ = 'sc_info').find('span').find_all('a')])
        if len(html.find(class_ = 'sc_info').find_all('span')) < 4 :
            source = ''
            
        else:
            source = html.find(class_ = 'sc_info').find_all('span')[1].text.strip()
#        print(index,title,html.find(class_ = 'sc_time')['data-year'])
        if html.find(class_ = 'sc_time'):
            year = str(html.find(class_ = 'sc_time').text.strip())
        else:
            year = ''
        thisArticl.append(author)
        thisArticl.append(source)
        thisArticl.append(year)
        df.loc[index] = thisArticl
        index += 1
        
#        break
#    print(df)

if __name__ == '__main__':
    
    '''http://xueshu.baidu.com/
    s?wd="颠覆性技术"
    &pn=390
    &tn=SE_baiduxueshu_c1gjeupa
    &ie=utf-8
    &filter=sc_year%3D%7B2000%2C2019%7D
    &sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D
    &sc_hit=1'''
    pn = 0
    base = 'http://xueshu.baidu.com/s?wd="颠覆性技术"&pn='
    sufix = '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year%3D%7B2000%2C2019%7D&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_hit=1'
    for i in range(1,41):
        url = base + str(pn) + sufix
        getConntent(url)
        pn += 10
        time.sleep(random.randint(1, 3))
#        break
    df.to_excel('result.xlsx')
#    print(url)
    