# coding:utf-8
# author:Ericam_
import re
import sys
from bs4 import BeautifulSoup
import urllib.request
import time

headers = ('User-Agent',
           'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
opener = urllib.request.build_opener()
opener.addheaders = {headers}
urllib.request.install_opener(opener)


def get_download(url):
    file = urllib.request.urlopen(url)
    data = BeautifulSoup(file, from_encoding="utf8")
    section_name = data.title.string
    section_text = data.select('#content .box #wrapper_main htmlContent')[0].text
    section_text = re.sub('\s+', '\r\n\t', section_text).strip('\r\n')
    fp = open('2.txt', 'a')
    fp.write(section_name + "\n")
    fp.write(section_text + "\n")
    fp.close()
    pt_nexturl = 'var next_page = "(.*?)"'
    nexturl_num = re.compile(pt_nexturl).findall(str(data))
    nexturl_num = nexturl_num[0]
    return nexturl_num


if __name__ == '__main__':
    url = "https://book.yanyiquan.com/book/70832/25497082.html"
    num = 228
    index = 1
    get_download(url)
    while (True):
        nexturl = get_download(url)
        index += 1
        sys.stdout.write("已下载:%.3f%%" % float(index / num * 100) + '\n')
        sys.stdout.flush()
        url = "https://book.yanyiquan.com/book/70832/" + nexturl
        if (nexturl == 'https://book.yanyiquan.com/book/70832/'):
            break
    print(time.clock())

