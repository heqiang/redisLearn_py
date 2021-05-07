"""
增：
    单个增加 hset myhash  key1 value
    多个添加 hmset myhash  key3 values3 key4 value4
查
    单个获取  hget myhash  key1
    多个获取  hmget myhash  key3  key4
    获取所有 HGETALL myhash
    获取所有的键 HKEYS myahs
    获取所有的value   HVALS  myhash
删
    hdel myhash key1

判断某个键是否存在
    HEXISTS  myhash  key2
"""
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.hmset()