import json

import redis

if __name__ == '__main__':


    redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)

    # hash类型操作，对比基本的键值对操作，只是多了一个必传的键名name而已。
    # 记录本次客户请求的线路id
    redis_client.hset('ANQ_LINE_CUST_RECORD', 'cust_id001',
                      json.dumps({'line_name': 'xxxxx'}, ensure_ascii=False))

    history_line = redis_client.hget('ANQ_LINE_CUST_RECORD', 'cust_id001')

    print(history_line)