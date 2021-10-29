
# 检查 lists里面的元素 是否 包含字符长串中
def ifListElementStrInString(lists, strs):
    for element in lists:
        if element in strs:
            return True
    return False
