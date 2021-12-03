import requests
import csv
from utils import date_util
##
#
# http://quote.eastmoney.com/f1.html?code=300059&market=2
# 对分时数据的详情页面 Network 进行观察后，发现数据存储在一个get开头的页面中，并以JQuery的方式存储。
# http://push2ex.eastmoney.com/getStockFenShi?pagesize=144&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&cb=jQuery1124001427171231610802_1636714981187&pageindex=0&id=3000592&sort=1&ft=1&code=300059&market=0&_=1636714981192
# 看一下各页URL之间的联系
# 就是 pageindex 参数改变而已
# 想要爬取以前的分时图，可以看到只要改 cookies 里的 st_sp 参数就行了


def get_fenshi_data():
    date_str = date_util.get_date_str()
    cookies = {
       'st_sp': f'{date_str}%2014%3A57%3A10',
    }
    stock_code_list = ['600025']

    for stock_code in stock_code_list:
        with open(f'{stock_code}.csv', 'a', newline='') as f:
           writer = csv.writer(f)
           writer.writerow(['时间','成交价','手数'])

        for page in range(27):
           params = (
               ('pagesize', '144'),
               ('ut', '7eea3edcaed734bea9cbfc24409ed989'),
               ('dpt', 'wzfscj'),
               ('cb', 'jQuery1124029337350072397084_1631343037828'),
               ('pageindex', str(page)),
               ('id', '6009051'),
               ('sort', '1'),
               ('ft', '1'),
               ('code', stock_code),
               ('market', '1'),
               ('_', '1631343037827'),
           )
           response = requests.get('http://push2ex.eastmoney.com/getStockFenShi', headers=headers, params=params, cookies=cookies, verify=False)
           for i in eval(response.text[43:-2])['data']['data']:
               with open(f'{stock_code}.csv','a',newline='') as f:
                   writer = csv.writer(f)
                   if len(str(i['t']))<6:
                       shi = str(i['t'])[0]
                       fen = str(i['t'])[1:3]
                       miao = str(i['t'])[3:]
                   else:
                       shi = str(i['t'])[0:2]
                       fen = str(i['t'])[2:4]
                       miao = str(i['t'])[4:]
                   if i['bs'] == 4:
                       a = '--'
                   elif i['bs'] == 2:
                       a = '买入'
                   elif i['bs'] == 1:
                       a = '卖出'


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }

if __name__ == '__main__':
    get_fenshi_data()