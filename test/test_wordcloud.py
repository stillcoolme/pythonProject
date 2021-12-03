
from faker import Faker
from wordcloud import WordCloud, STOPWORDS
from imageio import imread


if __name__ == '__main__':

    task_each_batch = 4
    temp_operators = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'z']
    task_operators = [temp_operators[i: i + task_each_batch] for i in range(0, len(temp_operators), task_each_batch)]
    # [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['j', 'z']]
    print(str(task_operators))
    for num, task in enumerate(task_operators):
        # ['a', 'b', 'c', 'd']
        print(task)

    # 注意分布式问题

    f = Faker(locale='zh_CN')
    contents = "学历高 还款能力强 还款能力强 还款能力强 还款能力强 还款能力强 还款能力强 学历高 学历高 学历高 单身 家庭成员多 "
    for i in range(1, 100):
        contents = contents + ' ' + f.name()
    mk = imread("file/img.png")
    w = WordCloud(font_path="file/字体.ttf",
                            width=1000, height=700, background_color="white", mask=mk
                            )
    w.generate(contents)
    w.to_file("file/词云.png")

