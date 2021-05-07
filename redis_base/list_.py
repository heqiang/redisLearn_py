import redis
"""
list 列表操作 -> 列表中可以有多个重复值 所以移除指定值 可以指定数量
    设置一个列表  lpush  rpush
    移除元素-> lpop rpop
    移除指定值-> LREM key count value  ex: lrem list 2 one 移除list列表中的两个one
    列表元素修改 -> lset key index value  下标不能越界 下标不存在会报错
    列表元素插入操作 ->LINSERT key  before/after pivot value ex:LINSERT list before  ceshi  beforevalue
    获取值 
        范围获取-> lrange  start stop 
        下标获取-> LINDEX  key  index  
    列表操作-> LTRIM  key start end  截取列 会将原来的列表改变  通过下标
    列表长度-> llen  key
    
            
    
"""
r = redis.StrictRedis(host='localhost', port=6379, db=0)

