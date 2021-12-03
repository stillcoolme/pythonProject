import concurrent.futures
import os
import sys
import codecs
import time

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# 用于脚本直接执行时能拿到引用的其他python文件
sys.path[0] = os.path.abspath(os.path.join(os.getcwd(), ".."))

import requests  # requests是HTTP库
import re
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
from bs4 import BeautifulSoup as bs  # bs:通过解析文档为用户提供需要抓取的数据

from utils.date_util import get_date_str, get_date_list_from_before_to_now, get_now_millisecond
from utils.file import urldownload
from utils.reg import get_file_suffix
from utils.string import ifListElementStrInString

def getData_thread(website_list, date_str=None):
    if not date_str:
        date_str = get_date_str()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for website in website_list:
            future = executor.submit(getData, website, date_str)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()


# 我们开始利用requests.get（）来获取网页并利用bs4解析网页：
def getData(src, date_str=None):
    # 默认查询当天
    if not date_str:
        date_str = get_date_str()

    html = requests.get(src)  # requests.get(src)返回的是状态码<Response [200]>，加上.content以字节形式（二进制返回数据。
    html.encoding = 'gbk'
    # http://www.cnblogs.com/ranxf/p/7808537.html
    soup = bs(html.text, 'lxml')  # lxml解析器解析字节形式的数据，得到完整的类似页面的html代码结构的数据
    # print(soup.prettify())

    # 正则表达式查找href
    # urls = Find(soup.decode('utf-8'))
    # print(urls)

    LS = soup.find_all('ul', class_="lie1")
    # 搜索子标签
    for i in LS:
        # print(i)
        LS = i.find_all("li")

    for element in LS:

        publishDate = element.em.string  # 公告发布日期, 格式 10-22
        if date_str[5:10] != publishDate:
            continue
        # 处理每个公告
        publishName = element.a.string

        if ifListElementStrInString(keyWord, publishName):
            print('\n!!!! 不处理：' + publishName)
            file = open(filePath + '/_' + date_str[5:10] + '_不处理_' + publishName + '.txt', 'w')
            file.write(element.a['href'])  # 写入内容信息
            file.close()
            continue
        print('\n!!!! 正在处理：' + publishName)
        publishUrl = element.a['href']
        getJobDetailData(publishUrl, title = publishName)


def getJobDetailData(src, title):
    html = requests.get(src).content
    soup = bs(html, 'lxml')
    contentDiv = soup.find_all('div', class_="zhengwen")
    for element in contentDiv:
        # 招聘文件
        publishFileUrl = element.find_all('a')
        temp_no = 1
        for element2 in publishFileUrl:
            downloadFileName = element2.string
            downloadUrl = element2['href']
            suffix = get_file_suffix(downloadUrl)

            if get_file_suffix(downloadUrl) not in keySuffix:
                continue
            # 排除掉 '专业参考目录', '疫情防控' 等文件
            if ifListElementStrInString(keyWord, downloadFileName):
                print('跳过：' + downloadFileName)
                continue
            print(downloadFileName + ': ' + downloadUrl)
            urldownload(downloadUrl, filePath + '/' + get_date_str() + '_' + str(temp_no) + '_' + title + '_' + downloadFileName + suffix)
            temp_no += 1

# findall() 查找匹配正则表达式的字符串
def Find(string):
    url = re.findall(r'href="http://www.shiyebian.net/xinxi/(.*?)"', string)
    url.remove('')
    url1 = []
    for i in url:
        url = 'http://www.shiyebian.net/xinxi/' + i
        url1.append(url)
    return url1


# 查询多少天前的数据
search_day = 1

sourceUrl = [
    'http://www.shiyebian.net/guangdong/shaoguan/',
    'http://www.shiyebian.net/guangdong/foshan/',
    'http://www.shiyebian.net/guangdong/guangzhou/'
]

# 用来排除的条件
## 不要那些链接名的文件
keyWord = ['编外', '服务人员', '合同制', '雇员'
    , '参考目录', '专业目录', '疫情防控', '报名', '承诺书', '登记表', '委托书', '资格审核'
    , '证明', '简历', '资格复审材料', '联系方式']
## 取哪些后缀的文件
keySuffix = ['.pdf', '.xls', '.xlsx', '.docx', '.doc']

# 文件保存路径
filePath = '/Users/stillcoolme/Downloads'



if __name__ == '__main__':
    # print(sys.path[0])
    # test = 'http://www.shiyebian.net/xinxi/393405.html'
    # getJobDetailData(test, 'xxx')

    day_list = get_date_list_from_before_to_now(search_day)

    for day in day_list:
        start_time = get_now_millisecond()
        print("\n!!!! 数据日期：" + day)

        # for url in sourceUrl:
        #     getData(url, day)
        # 改造成多线程并行执行
        getData_thread(sourceUrl, day)
        print('耗时：' + str(get_now_millisecond() - start_time))

    # #  创建Excel表并写入数据
    # wb = workbook.Workbook()  # 创建Excel对象
    # ws = wb.active  # 获取当前正在操作的表对象
    # # 往表中写入标题行,以列表形式写入！
    # ws.append(['标题', '链接'])
    # wb.save('text.xlsx')  # 存入所有信息后，保存为filename.xlsx