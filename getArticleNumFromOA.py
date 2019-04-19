# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import telnetlib
urlRepository = {'Acta Biochimica et Biophysica Sinica': 'https://academic.oup.com/abbs/issue-archive/issue-archive', 
        'Applied Mathematics Research eXpress': 'https://academic.oup.com/amrx/issue-archive', 
        'Astronomy & Geophysics': 'https://academic.oup.com/astrogeo/issue-archive ', 
        'Bulletin of the London Mathematical Society': 'https://academic.oup.com/blms/issue-archive',
        'Chemical Senses': 'https://academic.oup.com/chemse/issue-archive', 
        'The Computer Journal': 'https://academic.oup.com/comjnl/issue-archive', 
        'Database': 'https://academic.oup.com/database/issue-archive', 
        'Geophysical Journal International': 'https://academic.oup.com/gji/issue-archive', 
        'Geophysical Supplements to the Monthly Notices of the Royal Astronomical Society': 'https://academic.oup.com/gsmnras/issue-archive', 
        'ILAR Journa': 'https://academic.oup.com/ilarjournal/issue-archive', 
        'IMA Journal of Applied Mathematics': 'https://academic.oup.com/imamat/issue-archive', 
        'IMA Journal of Management Mathematics': 'https://academic.oup.com/imaman/issue-archive', 
        'IMA Journal of Mathematical Control and Information': 'https://academic.oup.com/imamci/issue-archive', 
        'IMA Journal of Numerical Analysis': 'https://academic.oup.com/imajna/issue-archive', 
        'Interacting with Computers': 'https://academic.oup.com/iwc/issue-archive', 
        'International Mathematics Research Notices': 'https://academic.oup.com/imrn/issue-archive', 
        'International Mathematics Research Papers': 'https://academic.oup.com/imrp/issue-archive', 
        'International Mathematics Research Surveys': 'https://academic.oup.com/imrs/issue-archive', 
        'ITNOW': 'https://academic.oup.com/itnow/issue-archive', 
        'Journal of Chromatographic Science': 'https://academic.oup.com/chromsci/issue-archive', 
        'Journal of Complex Networks': 'https://academic.oup.com/comnet/issue-archive', 
        'Journal of the International Commission on Radiation Units and Measurements': 'https://academic.oup.com/jicru/issue-archive', 
        'Journal of Logic and Computation': 'https://academic.oup.com/logcom/issue-archive', 
        'Journal of the London Mathematical Society': 'https://academic.oup.com/jlms/issue-archive', 
        'Journal of Radiation Research': 'https://academic.oup.com/jrr/issue-archive', 
        'Journal of Topology': 'https://academic.oup.com/jtopol/issue-archive', 
        'Law, Probability and Risk': 'https://academic.oup.com/lpr/issue-archive', 
        'Logic Journal of the IGPL': 'https://academic.oup.com/jigpal/issue-archive', 
        'Mathematical Medicine and Biology: A Journal of the IMA': 'https://academic.oup.com/imammb/issue-archive',
        'Mutagenesis': 'https://academic.oup.com/mutage/issue-archive', 
        'National Science Review': 'https://academic.oup.com/nsr/issue-archive', 
        'Philosophia Mathematica': 'https://academic.oup.com/philmat/issue-archive', 
        'Proceedings of the London Mathematical Society': 'https://academic.oup.com/plms/issue-archive', 
        'Progress of Theoretical Physics': 'https://academic.oup.com/ptp/issue-archive', 
        'Progress of Theoretical Physics Supplement': 'https://academic.oup.com/ptps/issue-archive', 
        'Progress of Theoretical and Experimental Physics': 'https://academic.oup.com/ptep/issue-archive', 
        'The Quarterly Journal of Mathematics': 'https://academic.oup.com/qjmath/issue-archive', 
        'The Quarterly Journal of Mechanics and Applied Mathematics': 'https://academic.oup.com/qjmam/issue-archive', 
        'Radiation Protection Dosimetry': 'https://academic.oup.com/rpd/issue-archive', 
        'Teaching Mathematics and its Applications: An International Journal of the IMA': 'https://academic.oup.com/teamat/issue-archive', 
        'Transactions of the London Mathematical Society': 'https://academic.oup.com/tlms/issue-archive', 
        }
#proxie = { 
#        'https' : 'https://117.91.255.85:9999'
#    } 
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
#
#def testProxie():
#    try:
#        telnetlib.Telnet('112.85.169.120', port='9999', timeout=20)
#    except:
#        print('connect failed')
#    else:
#        print('success')

def getIssues(url):
    html = requests.get(url, headers=head, timeout = 20).text
    soup = BeautifulSoup(html,'html.parser')
    issueUrls = {}
    issues = soup.find(class_ = 'widget widget-IssueYears widget-instance-OUP_Issues_Year_List').find_all('a')
    years = []
    for i in issues:
        years.append(i.text.strip())
    if '2018' in years:
        issueUrl = '/'.join([url,'2018'])
        try:
            html2 = requests.get(issueUrl, headers=head, timeout = 20).text
        except:
            print('connect: ' + issueUrl + ', failed!')
        else:
            soup2 = BeautifulSoup(html2,'html.parser')
            tempList = soup2.find_all(class_ = 'customLink')
            for temp in tempList:
                issueUrls[temp.find('a').text.strip()] = temp.find('a')['href']
    else:
        print('The latest issue is ' + years[-1])
    return issueUrls
    

def getArticleNum(issueUrl):
    html = requests.get(issueUrl, headers=head, timeout = 20).text
    soup = BeautifulSoup(html,'html.parser')
    return len(soup.find_all(class_ = 'al-article-items'))



if __name__ == '__main__':
    url = 'https://academic.oup.com/abbs/issue-archive'
    issueUrls = getIssues(url)
#    testProxie()
    baseUrl = 'https://academic.oup.com'
    if len(issueUrls) > 0:
        
        for i in issueUrls:
            issueUrl = baseUrl + issueUrls[i]
    #        print(getArticleNum(issueUrl))
            print(i + '\t' + str(getArticleNum(issueUrl)))
