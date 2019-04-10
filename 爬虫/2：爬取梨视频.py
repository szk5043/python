#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/10 11:14
# @Author : Wesley
# @File   : 2：爬取梨视频.py
import requests
import re
import os
from threading import Thread
from concurrent.futures import  ThreadPoolExecutor

base_url = 'https://www.pearvideo.com/'

def get_index():
    '''获取主页'''
    res = requests.get(base_url,headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "referer":"https://page.pearvideo.com/webres/v4/css/style.css?v=4.67",
    })
    return res.text

def parser_index(text):
    '''解析主页'''
    urls = re.findall('<a href="(.*?)" class="vervideo-lilink actplay"',text)
    # 获取页面内容跳转地址，如video_1540834
    urls = [ base_url + i for i in urls]
    #进行地址拼接，如https://www.pearvideo.com/ + video_1540834
    return urls

def get_one_url(url):
    '''获取第一层页面跳转的URL'''
    res = requests.get(url)
    return res.text

def parser_one_url(text):
    '''解析第一层页面跳转URL中的mp4地址'''
    video_url = re.search('srcUrl="(.*?\.mp4)"',text).group(1)
    # 获取视频的地址
    video_title = re.search('<h1 class="video-tt">(.*?)</h1>',text).group(1)
    # 获取视频的标题
    video_date =  re.search('<div class="date">(.*?)</div>',text).group(1)
    # 获取视频的时间
    video_content = re.search('<div class="summary">(.*?)</div>',text).group(1)
    # 获取视频的详情
    video_count = re.search('<div class="fav" data-id=".*">(.*?)</div>', text).group(1)
    return {"video_url":video_url,"video_title":video_title,"video_date":video_date,"video_content":video_content,"video_count":video_count}

def download_video(url,title):
    video_data = requests.get(url)
    if not os.path.exists("videos"):
        os.makedirs("videos")
    filename = os.path.join("videos",title) + ".mp4"
    filename = filename.replace(":","_")
    print(filename)
    with open(filename,'wb') as f:
        f.write(video_data.content)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    data = get_index()
    one_url = parser_index(data)
    for i in one_url:
        t = get_one_url(i)
        dic = parser_one_url(t)
        #Thread(target=download_video,args=(dic["video_url"],dic["video_title"])).start()
        pool.submit(download_video, dic["video_url"], dic["video_title"])
        print("submit task", dic["video_title"])

    print("submit finished")