#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/10 15:46
# @Author : Wesley
# @File   : 3：爬取链家.py
import requests
#import pymongo
from bs4 import BeautifulSoup
import csv

class LianjiaSpider():
    def __init__(self):
        self.baseurl = 'https://hf.lianjia.com/ershoufang/'
        self.headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
#        # 连接对象
#        self.conn = pymongo.MongoClient('127.0.0.1', 27017)
#        # 库对象
#        self.db = self.conn["Lianjia"]
#        # 集合对象
#        self.myset = self.db["houseInfo"]

    # 获取页面
    def getPage(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        #res.encoding = 'gbk'
        html = res.text
        self.parsePage(html)

    # 解析并保存页面
    def parsePage(self, html):
        # 创建解析对象
        soup = BeautifulSoup(html, 'lxml')
        # 解析对象的find_all()方法获取每个房源信息
        rList = soup.find_all('li', {'class': 'clear LOGCLICKDATA'})

        for r in rList:
            ########
            # houseInfo节点
            Info = r.find('div', {'class': 'houseInfo'}).get_text().split('|')
            # 小区名称
            name = Info[0].strip()
            # 户型
            huxing = Info[1].strip()
            # 面积
            area = Info[2].strip()
            ########
            # positionInfo节点
            positionInfo = r.find('div', {'class': 'positionInfo'}).get_text().split('-')
            # 楼层
            floor = positionInfo[0].strip()
            # 位置
            address = positionInfo[1].strip()
            #########
            # 总价
            totalPrice = r.find('div', {'class': 'totalPrice'}).get_text()
            # 单价
            unitPrice = r.find('div', {'class': 'unitPrice'}).get_text()
            #############
            d = {
                    "小区名称": name,
                    "户型": huxing,
                    "面积": area,
                    "楼层": floor,
                    "位置": address,
                    "总价": totalPrice,
                    "单价": unitPrice
                    }
#            self.myset.insert_one(d)
            #with open('链家二手房信息.csv', 'a', newline='',encoding='gbk') as f:
            with open('链家二手房信息.csv', 'a', newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([name, huxing, area, floor, address, totalPrice, unitPrice])

    # 主函数
    def workOn(self):
       # n = int(input("请输入页数："))
        n = int(20)
        m = 1
        for pg in range(1, n+1):
            # 拼接url
            url = self.baseurl + 'pg' + '/'
            self.getPage(url)
            print("\n第 %d 页爬取成功\n" % m)
            m += 1
        print("\n全部爬取成功")


if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.workOn()
