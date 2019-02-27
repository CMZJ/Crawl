import re
import time
import random
import requests

header = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
           'Mozilla / 5.0(Windows;U;WindowsNT6.1;en - us) AppleWebKit / 534.50(KHTML, like\
            Gecko) Version / 5.1Safari / 534.50','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
           'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
           'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']

headers = {'User-Agent':random.choice(header)}

for i in range(1,10):
    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
    html = requests.get(url=url,headers=headers)
    print(html.status_code)
    html.encoding='gb2312'
    p = re.compile('<b>.*?<a href="(.*?)" class="ulink">',re.S)
    r = p.findall(html.text)
    # for n in r:
    #     print(n)
    for m in r:
        lastUrl = 'https://www.dytt8.net'+m
        lastHtml = requests.get(lastUrl)
        lastHtml.encoding = "gb2312"
        d = re.compile('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href.*?>(.*?)</a></td>',re.S)
        data = d.findall(lastHtml.text)
        # print(lastHtml.text)
        print(data)
        try:
            with open(r'C:\Users\Administrator\Desktop\电影天堂.txt','a') as f:
                f.write(data[0] + '\n')
        except:
            print("下载或保存出错")