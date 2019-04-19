downloadPhotoFromwin4000.py
从‘http://www.win4000.com/’下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。
通过修改
    url = 'http://www.win4000.com/wallpaper_detail_155712.html'
切换下载地址，要求该url为壁纸集的第一张壁纸。


getWallpaperFrom5857.py
从‘http://www.5857.com/’下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。
通过修改
    url = 'http://www.5857.com/pcbz/82865.html'
切换下载地址，要求该url为壁纸集的第一张壁纸。


getArticleNumFromOA.py
从oxford academic旗下各期刊门户网站统计某期刊某一年的所有卷 期 文章数。
通过修改
    url = 'https://academic.oup.com/abbs/issue-archive'
修改所统计的期刊，要求该url为期刊的issue-archive页。
通过修改
if '2018' in years:
修改年份，要求年份为字符串
