import urllib.request
import requests
import os
from bs4 import BeautifulSoup
import re

URL = 'https://www.mywaifulist.moe/random'

agent = urllib.request.Request(URL, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

html = urllib.request.urlopen(agent)
bs = BeautifulSoup(html, 'html.parser')

image_title = bs.title.get_text()
image_title = image_title[:-14]
print(image_title)

for meta in bs.find_all('meta', property=re.compile('og:[a-z]*$')):
        if meta.attrs['property'] == 'og:image':
                r = requests.get(meta.attrs['content'])
                with open(image_title + '.jpeg', 'wb') as f:
                        f.write(r.content)
        print('-'*10)
        print(meta.attrs['property'][3:], ':' ,meta.attrs['content'])
    

os.system(f'sxiv {image_title}.jpeg')



