import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

url = 'https://www.dxsbb.com/news/5463.html'
html = getHtmlText(url)
soup = BeautifulSoup(html, "html.parser")
print(soup.tbody)