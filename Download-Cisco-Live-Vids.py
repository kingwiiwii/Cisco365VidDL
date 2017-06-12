#import urllib2
from bs4 import BeautifulSoup
import requests
import sys
import time

print
vidURL = raw_input("Enter URL - ").strip()
#vidURL = "https://www.ciscolive.com/online/connect/sessionDetail.ww?SESSION_ID=4521&backBtn=true"
#vidURL = 'https://www.ciscolive.com/online/connect/sessionDetail.ww?SESSION_ID=89232&backBtn=true'

website_response_time_start = time.time()

s = requests.session()

r = s.get(vidURL)

sitecontent = r.content

website_response_time_stop = time.time()

print
print "Website Response Time - %.1fsecs" % (website_response_time_stop-website_response_time_start)

soup = BeautifulSoup(sitecontent, "html.parser")

videourl = []

for link in BeautifulSoup(sitecontent, "html.parser").findAll('a'):
	if "data-url" in link.attrs:
		videourl.append(link.attrs)


videourl = dict(videourl[0])
videourl = videourl['data-url']

print
print "Video URL is %s " % videourl
print

filename = videourl.split("/")[-1]

print "Beginning download of %s " % filename
print

DownloadStart = time.time()
response = requests.get(videourl, stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with open(filename, 'wb') as handle:
	for block in response.iter_content(1024):
		handle.write(block)

DownloadStop = time.time()

print "Download time - %.1fsecs" % (DownloadStop-DownloadStart)
print