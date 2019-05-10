# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random

class Crawler:
    def __init__(self, url = None, headers = None, proxies = None, timeout = None):
        self.url = url
        self.headers = headers
        self.proxies = proxies
        self.timeout = timeout
        self.connetionState = False
        self.sleep = False
    
    def getConnet(self, url = None, headers = None, proxies = None, timeout = None, sleep = False):
        if (url is None and self.url is None):
            raise NameError("No url information!")
        elif url:
            self.url = url
        else:
            pass
        if headers:
            self.headers = headers
        if proxies:
            self.proxies = proxies
        if timeout:
            self.timeout = timeout
        if sleep:
            self.sleep = sleep
        try:
            response = requests.get(self.url, headers= self.headers, proxies = self.proxies, timeout = self.timeout)
#            print(self.url, self.headers, self.proxies, self.timeout, self.sleep)
        except Exception as reason:
            print(str(reason))
        else:
            print(response)
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html,'html.parser')
            self.response = response
            self.soup = soup
            self.connetionState = True
            if self.sleep:
                time.sleep(random.randint(1,3))
    
    def getInformation(self, baseblock: '.sc_content', *args: {'selectword': 'h3', 'content': 'text', 'name': 'title'},):
        result = []
        if not self.connetionState:
            raise NameError('connection must be made first')
        blocks = self.soup.select(baseblock)
        if len(blocks) == 0:
            raise ValueError('cannot find ' + baseblock)
        for block in blocks:
            resultDict = {}
            for i in args:
                if type(i) != type({}):
                    raise TypeError('input must be dict, ' + str(type(args)) + ' is not allowed')
                selectword = i['selectword']
                content = i['content']
                name = i['name']
                valueTemp = block.select(selectword)
                if len(valueTemp) > 1:
#                    raise ValueError('the selectwork ' + selectword + ' is not unique in block')
                    print('warning:' +'the selectwork ' + selectword + ' is not unique in block')
                    value = block.select(selectword)
                elif len(valueTemp) == 0:
                    raise ValueError('cannot find ' + selectword)
                else:
                    if content == 'text':
                        value = block.select(selectword)[0].text.strip()
                    else:
                        value = block.select(selectword)[0][content]
                resultDict[name] = value
            result.append(resultDict)
        return result

    def testGetInformation(self, baseblock: '.sc_content', *args: {'selectword': 'h3', 'content': 'text', 'name': 'title'},):
        if not self.connetionState:
            raise NameError('connection must be made first')
        block = self.soup.select_one(baseblock)
        if not block:
            raise ValueError('cannot find ' + baseblock)
        resultDict = {}
        for i in args:
            if type(i) != type({}):
                raise TypeError('input must be dict, ' + str(type(args)) + ' is not allowed')
            selectword = i['selectword']
            content = i['content']
            name = i['name']
            valueTemp = block.select(selectword)
            if len(valueTemp) > 1:
#                    raise ValueError('the selectwork ' + selectword + ' is not unique in block')
                print('warning:' +'the selectwork ' + selectword + ' is not unique in block')
                value = block.select(selectword)
            elif len(valueTemp) == 0:
                raise ValueError('cannot find ' + selectword)
            else:
                if content == 'text':
                    value = block.select(selectword)[0].text.strip()
                else:
                    value = block.select(selectword)[0][content]
            resultDict[name] = value
        return resultDict
                
                
    def getUrl(self):
        return self.url
    def getHeaders(self):
        return self.headers
    def getProxies(self):
        return self.proxies
    def getTimeout(self):
        return self.timeout
    def getConnetionState(self):
        return self.connetionState
    def getResponse(self):
        return self.response
    def getSoup(self):
        return self.soup
    def getSleep(self):
        return self.sleep
    
    def setUrl(self,url):
        self.url = url
    def setHeaders(self,headers):
        self.headers = headers
    def setProxies(self,proxies):
        self.proxies = proxies
    def setTimeout(self,timeout):
        self.timeout = timeout
    def setSleep(self,sleep):
        self.sleep = sleep

    def printExample(self,arg):
        print("example1: 'a'#label")
        print("example2: '.sister'#class")
        print("example3: '#link'#id")
        print("example4: 'p #link1'#mix")
#        print("example5: 'a'#mix")

    def __Nonetype(Ass1,Ass2):
        if Ass1 is None and Ass2 is None:
            return False
        else:
            return True
        
            
            
if __name__ == "__main__":
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#        }
#    url = 'https://www.baidu.com/'
    cr = Crawler()
#    cr.setHeaders(headers)
#    cr.setUrl(url)
#    cr.getConnet(sleep = True)
#    print(cr.headers)
    cr.getConnet(url = 'http://xueshu.baidu.com/s?wd="软件网络"&pn=0&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year%3D%7B2000%2C2019%7D&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_hit=1')
#    a = {'keyword': 'a', 'content': 'href', 'name': 'link'}, {'keyword': 'b', 'content': 'text', 'name': 'highlight'}
    result = cr.getInformation('.sc_content', {'selectword': 'h3', 'content': 'text', 'name': 'title'}, {'selectword': '.sc_info', 'content': 'text', 'name': 'info'})
    print(result)
