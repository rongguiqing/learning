import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parserPage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt.split(':')[1])
            title = eval(tlt.split(':')[1])
        ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for i in ilt:
        count = count + 1
        print(tplt.format(count, i[0], i[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://search.jd.com/Search?keyword=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&page=' + str(2 * i - 1)
            html= getHTMLText(url)
            parserPage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()