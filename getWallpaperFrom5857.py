# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import glob

#解析url炖成soup，并获取所有壁纸的url
def getPhotoUrl(url):
#    url = 'http://172.16.14.69:8080/dbsearchplat/magazineList.action'
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    h1 = soup.find_all('h1')[0]
    page = h1.find_all('span')[0].find_all('em')[0].text
    num = int(page.split('/')[-1])
#    print(num)
    photoUrl = soup.select('.title_czky')[0]['href']
#    print(photoUrl)
    NO = photoUrl.split('/')[-1].split('.')[0]
    fileFormat = photoUrl.split('/')[-1].split('.')[-1]
    templist = photoUrl.split('/')[:-1]
    urlPrefix = '/'.join(templist)
#    print(urlPrefix)
    photoUrlList = [urlPrefix + '/' + str(i).zfill(3) + '.' + fileFormat for i in range(1,num)]
#    print(photoUrlList)
    return photoUrlList
#下载壁纸到当前目录并从1开始编号
def DownloadPhoto(photoUrlList):
    filelist = glob.glob('*.jpg')
    if len(filelist) == 0:
        startNum = 1
    else:
        startNum = max([int(i.split('.')[0]) for i in filelist]) + 1
#    startNum = 64
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
    url = 'http://www.5857.com/pcbz/82865.html'
    photoUrlList = getPhotoUrl(url)
    DownloadPhoto(photoUrlList)
