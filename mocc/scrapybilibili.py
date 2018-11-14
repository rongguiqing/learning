import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = request.get(url, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getMaxPage(html):
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all("div", class="page-box house-lst-page-box")
    max_page = eval(a[0].attrs["page-data"])["totalPage"]
    return max_page


def parsePage(tli, html):
    soup = BeautifulSoup(html, "html.parser")
    soup.find(

def printMovie(tli):
    pass


def main():
    start_url = "https://gz.lianjia.com/ershoufang/zengcheng/"
    depth = getMaxPage(start_url)
    for i in range(depth):
        if i == 0:
            url = start_url
            getHTMLText(url)
        else:
            url = start_url + "pg" + str(i+1)
            getHTMLText(url)

        
