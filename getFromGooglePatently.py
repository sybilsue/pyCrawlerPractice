# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
}
# =============================================================================
#         'Referer': 'https://www.google.com/',
#         "X-Client-Data": "CIi2yQEIprbJAQjEtskBCKmdygEIqKPKAQixp8oBCOKoygEI8KnKAQi5rMoB"
# =============================================================================
baseUrl = 'https://patents.google.com/patent'
suffixUrl = 'zh'
proxies = {
  "http":"http://127.0.0.1:1080",
  "https":"https://127.0.0.1:1080"
}
def getContent(url):
    response = requests.get(url, headers=headers, proxies = proxies, timeout = 20)
    response.encoding = 'utf-8'
    html = response.text
#    with open('patent.html','w',encoding='utf8') as f:
#        f.write(html)
    soup = BeautifulSoup(html,'html.parser')
    line = ""
    title = "专利名称:" + soup.find(itemprop = "title").text.strip() + '\n'
    pubNum = "公开/公告号:" +soup.find(itemprop = "publicationNumber").text + '\n'
    abstrac = '摘要:' + soup.find(class_ = "abstract").text + '\n'
    inventor = '发明人:' + ','.join([i.text for i in soup.find_all(itemprop="inventor")]) + '\n'
    onwer = '申请人:' + soup.find(itemprop = "assigneeOriginal").text + '\n'
    line = line + title + pubNum + inventor + onwer + abstrac + '\n'
    return line

if __name__ == "__main__":
#    patentlyNum = 'CN1996290A'
    
#    url = 'https://patents.google.com/patent/CN1996290A/zh'
    with open('pubNums.txt','r') as f1:
        pub = f1.readlines()
    for i in pub:
        url = '/'.join([baseUrl, i.strip(), suffixUrl])
        with open('result.txt','a') as f2:
            f2.write(getContent(url))
#        print(getContent(url))
        time.sleep(random.randint(1, 3))