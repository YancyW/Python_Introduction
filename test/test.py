import requests
import time
import json
import csv
import sys

sys.setdefaultencoding("utf-8")
reload(sys)
from lxml import etree

#下面这两步的意思是把爬取的数据存入csv文件，文件名为data.csv

csvfile = file('data.csv', 'wb')
writer = csv.writer(csvfile)

#因为数据在csv文件里面是按列排放的，所以下面的这行的意思是在第一行放上每列数据所代表的意思，这五列分别对应我们在上述第一步里面提到的所需要爬取的五个信息。

writer.writerow(["user_id","city","date","rating","comment"])

#下面这一步我故意把循环弄成很多次，之为了翻页能翻到最后一页，下面有语句判断如果翻到最后一页，就自动终止这个循环

for i in xrange(0,1000000,20):
    url = "https://book.douban.com/subject/26952485/collections?start=" + str(i) #每次i改变都代表翻到了新的一   页
    r=requests.get(url) #用requests函数来发送请求
    content=r.content #读取网页内容
    page=etree.HTML(content) #这步是把读取的内容转为HTML 格式方便下面用xpath来提取信息

table = page.xpath('//*[@id="collections_tab"]//tr') #因为评论是以表格的形式逐行排列的，所以这里先提取所有行的信息。

#这下面意思是是如果没有翻到最后一页就提取每页的信息

if table != []:

    for row in table: #用循环来提取每行的信息
        user_id = "".join(row.xpath('./td[2]/div/a/@href')) #提取用户ID
        city = "".join(row.xpath('./td[2]/div/a/span[2]/text()')) #提取用户所在城市
        date = "".join(row.xpath('./td[2]/p[1]/span[1]/text()')).strip() #提取评论发布时间
        rating = "".join(row.xpath('./td[2]/p[1]/span[2]/@class')) #提取评分

#有时候评分之前会插上书签，所以会改变评分的xpath，下面是来判断，如果有书签的话，就换一个xpath来提取评分信息

        if rating == "":
            rating = "".join(row.xpath('./td[2]/p[1]/span[3]/@class'))
            comment = "".join(row.xpath('./td[2]/p[2]/text()')).strip() #提取具体评论
            writer.writerow([user_id,city,date,rating,comment]) #将提取的信息写入csv文件

#下面这两步的作用是判断是否到了最后一页，如果到了最后一页，那么提取的内容就为空，那么就终止主循环

        else:
            break

#下面这步是在屏幕上打印出具体翻到了那一页以及打印出具体的时间

print ('page %d data was processed !!!'%i + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
