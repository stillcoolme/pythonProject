import requests  # requests是HTTP库
import re
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
from bs4 import BeautifulSoup as bs  # bs:通过解析文档为用户提供需要抓取的数据
import os
import io
import sys
import sys


from utils.date_util import get_date_str, get_date_list_from_before_to_now
from utils.file import urldownload
from utils.reg import get_file_suffix
from utils.string import ifListElementStrInString

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


# 我们开始利用requests.get（）来获取网页并利用bs4解析网页：
def getData(src, date_str=None):
    # 默认查询当天
    if not date_str:
        date_str = get_date_str()

    html = requests.get(src).content  # requests.get(src)返回的是状态码<Response [200]>，加上.content以字节形式（二进制返回数据。
    # http://www.cnblogs.com/ranxf/p/7808537.html
    soup = bs(html, 'lxml')  # lxml解析器解析字节形式的数据，得到完整的类似页面的html代码结构的数据
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
        print('!!!! 正在处理：' + publishName)
        publishUrl = element.a['href']
        getJobDetailData(publishUrl, title = publishName)


def getJobDetailData(src, title):
    html = requests.get(src).content
    soup = bs(html, 'lxml')
    contentDiv = soup.find_all('div', class_="zhengwen")
    for element in contentDiv:
        # 招聘文件
        publishFileUrl = element.find_all('a')
        for element2 in publishFileUrl:
            temp_no = 1
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
            urldownload(downloadUrl, filePath + '/' + get_date_str() + '_' + str(temp_no) + '_' + title + suffix)
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
    'http://www.shiyebian.net/guangdong/guangzhou/',
    'http://www.shiyebian.net/guangdong/shenzhen/',
    'http://www.shiyebian.net/guangdong/heyuan/',
    'http://www.shiyebian.net/guangdong/qingyuan/'
]

# 用来排除的条件
## 不要那些链接名的文件
keyWord = ['参考目录', '疫情防控', '报名表', '报名人员信息表', '承诺书', '编外', '证明', '简历']
## 取哪些后缀的文件
keySuffix = ['.pdf', '.xls', '.xlsx', '.docx', '.doc']

# 文件保存路径
filePath = '/Users/stillcoolme/Downloads'



if __name__ == '__main__':
    print(sys.path[0])
    sys.path.append(os.path.dirname(sys.path[0]))

    # test = 'http://www.shiyebian.net/xinxi/392458.html'
    # getJobDetailData(test, 'xxx')

    day_list = get_date_list_from_before_to_now(search_day)
    for day in day_list:
        print("!!!! 数据日期：" + day)
        for url in sourceUrl:
            getData(url, day)

    # #  创建Excel表并写入数据
    # wb = workbook.Workbook()  # 创建Excel对象
    # ws = wb.active  # 获取当前正在操作的表对象
    # # 往表中写入标题行,以列表形式写入！
    # ws.append(['标题', '链接'])
    # wb.save('text.xlsx')  # 存入所有信息后，保存为filename.xlsx