import redis

"""
set()集合操作
新增
    sadd key value
获取
    smembers key 获取所有的值
    scard key  获取数量
删除
    srem key value  指定删除一个集合中的元素
    
查看是否存在
    sismember()    
随机筛选一个从set集合中
    srandmember()
set中元素移动到另一个set集合中
    SMOVE  sourceset targetset value
集合和集合之间的操作：差集  交集 并集等
"""


r = redis.StrictRedis(host='localhost', port=6379, db=0)
# r.smembers()
r.srem("sset","set3")
# r.sismember()
print(r.scard("sset"))
print(r.srandmember("sset",2))