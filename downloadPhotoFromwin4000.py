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
        photoUrl = soup.find(class_ = 'pic-large')["src"]
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

def downloadFromWin4000(url):
    pageUrlList = getPageUrl(url)
    photoUrlList = getPhotoUrl(pageUrlList)
    DownloadPhoto(photoUrlList)

def downFromNetbian(url):
    url = (".").join(url.split(".")[:-1]) + "-1920x1080.htm"
    soup = getConnect(url)
    photoUrl = soup.find_all("img")
    photoUrlList = []
    photoUrlList.append(photoUrl[-1]["src"])
    DownloadPhoto(photoUrlList)
    
def getConnect(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    return soup
if __name__ == '__main__':
    win4000Url = 'http://www.win4000.com/wallpaper_detail_165834.html'
    # netbianUrl = "http://www.netbian.com/desk/22381.htm"
#    downFromNetbian(netbianUrl)
    downloadFromWin4000(win4000Url)

