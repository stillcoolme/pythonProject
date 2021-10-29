import re


def get_file_suffix(file_url):
    result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', file_url)
    # print('提取文件后缀：' + str(result))
    if len(result) > 0:
        return result[0]
    else:
        return ''

if __name__ == '__main__':
    # xx = get_file_suffilx('http://www.wengyuan.gov.cn/attachment/0/133/133122/2066721.xls')
    xx = get_file_suffix('http://www.shiyebian.net/guangdong/wengyuanxian/')
    print(xx)