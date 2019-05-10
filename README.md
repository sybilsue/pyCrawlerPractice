
### downloadPhotoFromwin4000.py

从<a href = "http://www.win4000.com/">美桌网</a>下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。<br />
通过修改：


```python
url = 'http://www.win4000.com/wallpaper_detail_155712.html'
```

切换下载地址，要求该url为壁纸集的第一张壁纸。

### getWallpaperFrom5857.py

从<a href = "http://www.5857.com/">5857壁纸站</a>下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。<br />
通过修改：


```python
 url = 'http://www.5857.com/pcbz/82865.html'
```

切换下载地址，要求该url为壁纸集的第一张壁纸。

### getArticleNumFromOA.py

从<a href = "https://academic.oup.com/journals">oxford academic</a>旗下各期刊门户网站统计某期刊某一年的所有卷 期 文章数。<br />
通过修改：


```python
 url = 'https://academic.oup.com/abbs/issue-archive'
```

修改所统计的期刊，要求该url为期刊的issue-archive页。<br />
通过修改：


```python
if '2018' in years:
```

修改年份，要求年份为字符串

### getArticleFromBaiduxueshu.py

从百度学术搜索结果页获取文章的题目，摘要，作者和来源，并且在同目录下生成excal文档<br />
通过修改：


```python
pn = 0
base = 'http://xueshu.baidu.com/s?wd="软件网络"&pn='
sufix = '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year%3D%7B2000%2C2019%7D&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_hit=1'
for i in range(1,41):
```

来分别修改起始页码，url中页码前的部分和url，中页码后的部分以及结果的页码数。要求url为搜索结果页

### getFromGooglePatently.py

从谷歌专利的专利细览页面下载中文专利的专利名称，公开号，摘要，发明人，申请人信息<br />
在代码同路下创建<code>pubNums.txt</code>文件存放专利号，要求每行仅存放一个专利号<br />
下载结果存放在<code>result.txt</code>中。<b>仅只用于中文专利</b>

### netCrawler.py

尝试着写了一个主要针对搜索结果的爬虫类，适用于代码比较规范的搜索引擎，通过：


```python
import netCrawler
cr = netCrawler.Crawler(url = None, headers = None, proxies = None, timeout = None)
```

调用该类，可以选择在调用时就传入参数，或者不传入，后续通过set方法传入参数。<br />
调用后通过：


```python
cr.getConnet(self, url = None, headers = None, proxies = None, timeout = None, sleep = False)
```

获取服务器的响应，此时应该确保url参数已经设定，参数示例：


```python
url = 'https://patents.google.com/patent'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#         'Referer': 'https://www.google.com/',
#         "X-Client-Data": "CIi2yQEIprbJAQjEtskBCKmdygEIqKPKAQixp8oBCOKoygEI8KnKAQi5rMoB"
          }
#响应头，为一个字典，主要用于将来自python的请求伪装为chrome浏览器
proxies = {
  "http":"http://127.0.0.1:1080",
  "https":"https://127.0.0.1:1080"
}
#端口，为一个字典，分为http和https，根据需要处理的网页协议而定
#headers和proxies信息都可以直接通过浏览器打开网页查看响应头获取
timeout = 20
#响应时间
sleep = True
#每次获取一个页面后是否让程序休眠，适用于需要获取大量页面的时候
```

获取页面响应后通过：


```python
cr.getInformation(self, baseblock: '.sc_content', *args: {'selectword': 'h3', 'content': 'text', 'name': 'title'},)
```

获取页面信息，返回结果为list，其中：<br />
<b>baseblock</b>: 字符串，用于定位存放一个完整词条的基本容器，会根据基本容器循环获取页面内每一个容器中的相似内容<br />
<b>&#42;args</b>: 一或多个形如<code>{'selectword': 'h3', 'content': 'text', 'name': 'title'}</code>的字典，用于定位每一个基本容器中需要被获取的内容，多个字典用逗号分隔。<br />
<b>selectword</b>: 一般为标签，类或者id，用于定位获取元素。<br />
<b>content</b>: 获取该元素的哪个属性，比如说&lt;a&gt;的href或者text部分<br />,如果selectword在block中不唯一，则会直接返回<code>soup.select(selectword)</code>的结果，此时<b>content</b>无效<br />
<b>name</b>: 返回结果中对该元素的命名

<b>selectword</b>和<b>baseblock</b>都需要按照<code>beautifulsoup</code>包中<code>select()</code>函数所要求的格式输入，可以通过<code>printExample()</code>函数获取样例：


```python
example1: 'a'#label
example2: '.sister'#class
example3: '#link'#id
example4: 'p #link1'#mix
```

完整示例：


```python
from netCrawler import Crawler
cr = Crawler()
cr.getConnet(url = 'http://xueshu.baidu.com/s?wd="软件网络"&pn=0&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year%3D%7B2000%2C2019%7D&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_hit=1')
result = cr.getInformation('.sc_content', {'selectword': 'h3', 'content': 'text', 'name': 'title'}, {'selectword': '.c_abstract', 'content': 'text', 'name': 'abstract'})
result
```

    <Response [200]>
    
    [{'title': '基于软件网络的服务自动分类和推荐方法研究',
      'abstract': '服务的分类和推荐方法对于服务 管理和组合都具有重要意义.文中利用服务组合历史,从面向服务软件的结构角度研究了服务分类和推荐方法:提出面向服务软件的软件网络模...'},
     {'title': '软件网络的多粒度拓扑特性分析及其应用',
      'abstract': '摘\u3000要: 随着软件与网络的融合,以网络为基础的软件系统在规模、用户数量、组成单元的交互关系方面都成数量级的增长,成为一类重要的复杂系统,超出了开发人员的理解...'},
     {'title': '恶意软件网络协议的语法和行为语义分析方法',
      'abstract': '摘\u3000要: 网络协议逆向分析是恶意软件分析的一项重要内容.现有的网络协议逆向分析方法主要考虑获取消息格式和协议语法,缺少数据的行为语义,导致分析者难以在网络数...'},
     {'title': '复杂软件系统的软件网络结点影响分析',
      'abstract': '目前一些研究利用复杂网络理论揭示了软件网络的特性,为人们从系统的角度了解软件的结构提供了方法.但这些研究的一些结论却与软件的实际表现有着较大的差异.分析了...'},
     {'title': '基于软件网络的服务自动分类和推荐方法研究',
      'abstract': '本文对基于软件网络的服务自动分类和推荐方法进行了研究。服务的分类和推荐方法对于服务管理和组合都具有重要意义。利用服务组合历史,从面向服务软件结构角度研究...'},
     {'title': '基于复杂软件网络的回归测试用例优先级排序',
      'abstract': 'Test case prioritization is one of the effective and practical regression testing techniques.This paper proposed a new test case prioritization techniqu...'},
     {'title': '软件网络和知识产权',
      'abstract': '本书由从事软件网络有关法律研究和软件网络律师实务工作所撰写的文章中精选汇集而成,内容涉及案件代理、实务评论、案例探讨、法律研究等方面。'},
     {'title': '软件网络名案新析',
      'abstract': '本书的案例主要取材于上海市第二中级人民法院近年审理的软件网络案例,所进行的评析着重从不同于法院判决的思路和角度。'},
     {'title': '软件网络案件代理与评析',
      'abstract': '本书由上海市律师协会信息网络法律研究会面向广大律师征稿后择优汇集而成的,这些论文既有律师针对自己代理的软件网络案件的评述,也有对其他案件或软件网络法律新问...'},
     {'title': '软件网络和知识产权——从实务到理论',
      'abstract': '寿步. 软件网络和知识产权--从实务到理论[M].长春:吉林人民出版社,2001.寿步.软件网络和知识产权--从实务到理论[M].长春:吉林人民出版社,2001.寿步. 软件网络和知识产权--从实务到理论[M].长春:吉林人民出版社 2001...'}]




```python

```
