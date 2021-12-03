from phone import Phone

if __name__ == '__main__':
    # 用于匹配固定电话号码
    REGEX_FIXEDPHONE = "^(010|02\\d|0[3-9]\\d{2})?\\d{6,8}$";

    info = Phone().find('17728127873')
    print(info)