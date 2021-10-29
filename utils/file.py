import requests


def urldownload(url, filename=None):
    """
    下载文件到指定目录
    :param url: 文件下载的url
    :param filename: 要存放的目录及文件名，例如：./test.xls
    :return:
    """
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    down_res = requests.get(url, headers=send_headers)
    with open(filename, 'wb') as file:
        file.write(down_res.content)
        file.close()

if __name__ == '__main__':
    urldownload('http://www.wengyuan.gov.cn/attachment/0/133/133124/2066721.docx', './2066721.docx')

