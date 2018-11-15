#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import random
import argparse
from bs4 import BeautifulSoup as BS
import mechanize
from time import sleep
from multiprocessing import Pool
import sys
import cookielib
reload(sys)
sys.setdefaultencoding('utf-8')


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
  
#response = br.open('https://gold.jgi.doe.gov/goldlogin')  
#br.select_form(name='home')  
#br.form['login'] = '315472136@qq.com'  
#br.form['password'] = 'ms19880708'  
#br.submit()  
#print('login successful.')


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
	infile = sys.argv[1]
	outfile = sys.argv[2]
	htmlfh = open('htmls','wa')
	outfh = open(outfile, 'wa')
	#nofindfh = open('nofind.txt','wa')
	with open(infile,'r') as fh:
		for goid in fh:
			print(goid)
			try:
				html,res = get_info(goid.strip())
				res = '\t'.join(res)
				outfh.write(res + '\n')
				htmlfh.write(html + '\n')
			except:
				print(goid + '\tno find')
				#nofindfh.write(goid + '\n')
			
	outfh.close()


