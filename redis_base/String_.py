import redis

"""
字符串操作
    添加一个key value
    根据一个key获取值
    当value为数值类型时  可以自增或者自减 默认为1  通过incrby/decrby可以调整自增/自减的数值
    字符串截取->getrange  substr
    字符串替换 -> setrange(key,offset,value)  offset 偏移量 从哪里开始进行替换 
    字符串过期时间
        -> setex 设置字符串过期时间  查看过期时间 ->ttl 
        -> setnx  不存在设置（分布式锁中使用）存在不会替换 
    字符串批量设置/获取
        -> mset 以字典的形式传入
        -> mget 批量获取
        -> msetnx 不存在就设置 只有有一个存在就设置失败 原子性操作
    进阶：
        getset->先获取值在设置值
        
"""
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# r.delete("view")
# r.set("view",0)
# r.incrby("view",10)
# r.decrby()
# print(r.get("view"))
# r.set("amount","helloworld redis")
# # print(r.getrange("amount", 0, 3))
# # print(r.substr("amount", 0, 3))
# # r.setrange()
# # r.setex("k1",30,"timekey")
# # r.ttl("k1")
# r.mset({'k1':"v1","k2":"v2",'k3':"v3","k4":"v4"})
# print(r.mget("k1", "k2","k3", "k4"))
print(r.msetnx({'k1': "v1", "k5": "v5"}))

r.getset()