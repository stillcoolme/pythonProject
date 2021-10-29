
# coding: utf-8
# spider_xueqiu_following

import requests
import pandas as pd
import time
import urllib.request
import re

headers ={
    'Cookie': 'device_id=7378f1460e605d6bbb9d845df28a042f; __utma=1.146408891.1483277965.1507822021.1507904229.10; __utmz=1.1496161318.8.4.utmcsr=xueqiu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=7c56ad53fa7fbf66f33a52ae7ce3fa82e0affea4; xq_a_token.sig=oPtXoO1FnzRynhx-pSwvF9YvvK0; xq_r_token=c28549d2af9dd8bbf353559f49868e46425a254b; xq_r_token.sig=WclLch4ntYyswevQw1-mjVCs_f0; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=3094390085; u.sig=EsGua0pSN_rwwiOGMVwjjbUXF_s; aliyungf_tc=AQAAAI1aplruAwEAh95b0/CSScREtven; Hm_lvt_1db88642e346389874251b5a1eded6e3=1516710527,1516710801,1516888695; Hm_lvt_9d483e9e48ba1faa0dfceaf6333de846=1516711294,1516888696; s=gk1prcz9cq; bid=269d98283aafb9910fb4cab2ed6e57c8_jcxf0jb8; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1516889894; Hm_lpvt_9d483e9e48ba1faa0dfceaf6333de846=1516889894',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

# 抓取多页，翻页处理

user_data = []

def get_data():


    url = 'https://xueqiu.com/'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html_page = resp.read().decode('utf-8')
    send_headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive',
        'Host':'xueqiu.com',
        'Cookie':r'xxxxxx',
    }
    req = urllib2.Request(url, headers=send_headers)
    resp = urllib2.urlopen(req)
    html = resp.read()


def get_user_data(page):
    for i in range(page):
        url = 'https://xueqiu.com/friendships/groups/members.json?uid=3094390085&page={}&gid=0'.format(i + 1)
        response = requests.get(url, headers=headers).json()['users']
        user_data.extend(response)
        print('正在打印%s页' % str(i + 1))
        time.sleep(2)


# 暂停爬虫


# 调用函数，并保存到本地
if __name__ == '__main__':
    get_user_data(10)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv('xueqiu-following.csv')