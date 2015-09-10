# -*- coding: utf-8 -*-
__author__ = 'chhe'

import os
import urllib
from robobrowser import RoboBrowser

page_sum = 10  #设置下载页数

path = os.getcwd()
path = os.path.join(path,'暴走GIF')
if not os.path.exists(path):
    os.mkdir(path)                                  #创建文件夹

url = "http://baozoumanhua.com/gif/month/page/"     #url地址
headers = {                                         #伪装浏览器
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/32.0.1700.76 Safari/537.36'
}


browser = RoboBrowser(history=True,user_agent='Mozilla/5.0 ... Safari/537.36')

for count in range(page_sum):
    browser.open(url+str(count+1),method='get',headers=headers)
    if browser.response.status_code is not 200:
        break
    else:
        img_content = browser.find_all('img',attrs={'style':'width:460px'})
        url_list = [img['src'] for img in img_content]      #列表推导 url
        title_list = [img['alt'] for img in img_content]    #图片名称

        for i in range(url_list.__len__()) :
            imgurl = url_list[i]
            filename = path.decode('utf-8') + os.sep.decode('utf-8') + title_list[i] + ".gif"
            print(filename+":"+imgurl)                         #打印下载信息
            urllib.urlretrieve(imgurl,filename)        #下载图片