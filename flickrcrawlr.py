import requests
import sys
from sys import exit
from colorama import Fore
import BeautifulSoup
if len(sys.argv) >= 2:
	userid = sys.argv[1]
else:
	userid = raw_input("target user id: ")
try:
	initialrequest = requests.request('GET','http://www.flickr.com/photos/%s' % userid)
except:
	exit('['+Fore.RED+'!'+Fore.RESET+'] error getting data')
if not initialrequest.status_code == 200:
	exit('['+Fore.RED+'!'+Fore.RESET+'] no such user')
else:
	soup = BeautifulSoup.BeautifulSoup(initialrequest.text)
	pages = soup.findAll('a', {"class" : "rapidnofollow"})
	if len(pages) > 1:
		lastpage = str(pages[len(pages)-1])
		lastpage = lastpage.split(" ")[2].split("=")[1].split('-')[1].replace('"', "")
		lastpage = int(lastpage)
	else:
		exit('['+Fore.RED+'!'+Fore.RESET+'] fuck off plebe')
	pages = []
	for i in range(lastpage):
		pagenum = i + 1
		url = 'http://www.flickr.com/photos/{0}/page{1}'.format(userid, pagenum)
		pages.append(url)
	print '['+Fore.GREEN+'+'+Fore.RESET+'] found %s pages of photos' % str(len(pages))

