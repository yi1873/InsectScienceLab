JGI 网页爬虫
================
November 15, 2018

网页爬虫
--------

-   爬取网页信息 <https://gold.jgi.doe.gov/organisms?id=Go0124868>

``` python
import re
import os
import random
import argparse
from bs4 import BeautifulSoup as BS
import mechanize
import cookielib
br = mechanize.Browser()  
cj = cookielib.LWPCookieJar()  
br.set_cookiejar(cj)  
br.set_handle_equiv(True)  
br.set_handle_gzip(True)  
br.set_handle_redirect(True)  
br.set_handle_referer(True)  
br.set_handle_robots(False)  
  
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)  
br.set_debug_http(False)  
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')]  
def get_info(goid):
        url = "https://gold.jgi.doe.gov/organisms?id=" + goid
        html = br.open(url).read()
        soup = BS(html, "html5lib")
        tabs = soup.findAll('table',{'class':'entity'})
        taxid = tabs[1].findAll('tr')[3].findAll('td')[1].text.replace('\n','').replace('\t','')
        taxname = tabs[1].findAll('tr')[2].findAll('td')[1].text.replace('\n','').replace('\t','')
        gram = tabs[2].findAll('tr')[5].findAll('td')[1].text.replace('\n','').replace('\t','')
        disease = tabs[2].findAll('tr')[20].findAll('td')[1].text.replace('\t','').replace('\n\n',';')[1:-1]
        try:
                host = tabs[3].findAll('tr')[14].findAll('td')[1].text.replace('\t','').replace('\n\n',';')[1:-1]
        except:
                host = ""
        res = [goid, taxid, taxname, gram, disease, host]
        return html, res
if __name__ == '__main__':
        goid = 'Go0471766'
        html,res = get_info(goid.strip())
        res = '\t'.join(res)
        print('Goid\tTaxid\tSpecies\tGram\tDisease\tHost')
        print(res + '\n')
```

    ## Goid Taxid   Species Gram    Disease Host
    ## Go0471766    90675   Camelina sativa
