# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import glob

#解析url炖成soup
def getPageUrl(url):
#    url = 'http://172.16.14.69:8080/dbsearchplat/magazineList.action'
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    h1 = soup.find_all(class_ = "ptitle")[0]
    num = int(h1.find_all('em')[0].text)
    #    print(num)
    suffix = url.split('.')[-1]
    pageUrlPrefix = url.rstrip('.' + suffix)
    urlList = [url]
    for i in range(2,num+1):
        urlList.append(pageUrlPrefix + '_' + str(i) + '.' + suffix)
#    print(urlList)
    return urlList

def getPhotoUrl(pageUrlList):
    photoUrlList = []
    for pageUrl in pageUrlList:
        html = requests.get(pageUrl).text
        soup = BeautifulSoup(html,'html.parser')
        photoUrl = soup.find(class_ = 'paper-down').find('a')['href']
#        print(photoUrl)
        photoUrlList.append(photoUrl)
#    print(photoUrlList)
    return photoUrlList

def DownloadPhoto(photoUrlList):
    filelist = glob.glob('*.jpg')
    if len(filelist) == 0:
        startNum = 1
    else:
        startNum = max([int(i.split('.')[0]) for i in filelist]) + 1
#    startNum = 82
    for photoUrl in photoUrlList:
#        print(photoUrl)
        try:
            r = requests.get(photoUrl)
        except requests.exception.ConnectTimeout:
            print('Img NOT found')
        else:
            r.encoding = 'UFT-8'
            if r.status_code == 200:
                filename = str(startNum) + '.jpg'
                with open(filename, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
                startNum += 1
                print('downloaded: '+ filename)
            else:
                print(r.status_code)

if __name__ == '__main__':
    url = 'http://www.win4000.com/wallpaper_detail_155712.html'
    pageUrlList = getPageUrl(url)
    photoUrlList = getPhotoUrl(pageUrlList)
    DownloadPhoto(photoUrlList)
