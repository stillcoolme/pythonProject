import json
import os

if __name__ == '__main__':

    new_line_rate_dict = {}
    new_line_list = []
    if new_line_rate_dict:
        # 根据 应答率进行排序
        sorted_list = sorted(new_line_rate_dict.items(), key=lambda x: x[1], reverse=True)  # 根据value排序得到的是list
        for ele in sorted_list:
            new_line_list.append(ele[0])
        new_line_list_str = json.dumps(new_line_list)
        print("----: " + str(new_line_list_str))
    else:
        print("++++++")

    import re

    subject = 'http://www.wengyuan.gov.cn/attachment/0/133/133122/2066721.xls'
    result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', subject)
    print(result)
