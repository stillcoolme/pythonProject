import os
import time

# https://mp.weixin.qq.com/s/WjGT3qjaw8VLbgDjdpbM1A

# io 操作就会导致这问题

if __name__ == '__main__':
    start = int(time.time())
    cmd = 'python test_wordcloud.py'
    # popen() 这方法不获取返回值的，所以 cmd 的执行本质上是异步的；
    # task.py 本main方法 能立刻执行完毕，然后自动关闭读取端的管道！！；
    # 当读取端关闭时，写入端输出到达管道最大缓存时会收到 SIGPIPE 信号，从而抛出 Broken pipe 异常。
    # 如果需要拿到子进程的输出，需要自行调用 read() 函数。
    os.popen(cmd)
    end = int(time.time())
    print('end***{}s'.format(end-start))

    # 关闭之后子进程会向 pipe 中输出  print '1000'*1024，由于这里输出的内容较多会一下子填满管道的缓冲区；
    # 于是写入端会收到 SIGPIPE 信号，从而导致 Broken pipe 的异常。


###############################


    start = int(time.time())
    cmd = 'python test_wordcloud.py'
    with os.popen(cmd) as p:
        print(p.read())
    end = int(time.time())
    print('end***{}s'.format(end - start))


