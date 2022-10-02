# It provides us with an interface that allows to interact with the web easily
# lxml is a library to improve the parsing speed of XML files.
# requests is a library to simulate HTTP requests (such as GET and POST). We will
# It was mainly used in order to access the source code of any given website.

from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
import lxml
import urllib
import urllib.parse
import os
import requests


#url_p = str(input())
url_p = "http://slashdot.org"
how_deep = int(input())
my_file = open("urls.txt", "w+")
#print(dict[0])

#print(links)




i=0
set1 = set()
set2 = set()
set2.add(url_p)
set3 = set()

os.makedirs(name='./data', exist_ok=True)
req = requests.get(url_p, allow_redirects=False, timeout=5)
html_page = req.text
with open(f'data/0.html', 'w') as f:
    f.write(html_page)

idx = 0

def find_linkings(url_page, depth):
    #set2.add
    #global idx
    #idx += 1
    global set1
    global set2
    global set3
    def deep_i(linking):
        try:
            req = Request(linking)
            html_page = urlopen(req).read()
            soup = BeautifulSoup(html_page, "lxml")
            #sleep(15)
        except (ConnectionResetError, urllib.error.HTTPError, urllib.error.URLError, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, UnicodeEncodeError):
            print('parasha1')
        else:
            for link in soup.findAll('a'):
                if link.get('href') != None and link.get('href') != '' and link.get('href').startswith('/'):
                    url = urllib.parse.urljoin(url_page, link.get('href'))
                    if url not in set3 and url not in set1 and url not in set2:
                        set3.add(url)
                        try:
                            req = requests.get(url, allow_redirects=False, timeout=5)
                            html_page = req.text
                            global idx
                            idx += 1
                            # with open(os.path.join(data_dir_, f'{idx}.html'), 'w') as f:
                            with open(f'data/{idx}.html', 'w') as f:
                                f.write(html_page)
                        except (ConnectionResetError, urllib.error.HTTPError, urllib.error.URLError, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, UnicodeEncodeError):
                            print('parasha2')
                    #elif link.get('href').startswith('www') is True:
                    #    n = urllib.parse.urljoin('http://', link.get('href'))
                    #else:
                    #    set3.add(link.get('href'))
                    #elif link.get('href').startswith('htt') is True:
                        #set3.add(link.get('href'))
    while depth > 0:
        for url_page in set2.copy():
            deep_i(url_page)
        set1 = set1.union(set2, set3)
        set2 = set3
        set3 = set()
        depth = depth - 1
    set1 = set1.union(set2, set3)
    k = 0
    for unique_link in set1:
        k += 1
        my_file.write(str(k))
        my_file.write(" ")
        my_file.write(unique_link)
        my_file.write('\n')





#print(len(dict))

find_linkings(url_p, how_deep)
#print(len(dict))
print(set1)
print(len(set1))
