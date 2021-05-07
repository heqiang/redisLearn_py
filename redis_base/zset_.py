"""
有序集合 -> 排序
增加
    增加单个或者多个 zadd  myset 1  one，  zadd myset 2 two 3 three
排序
    -inf  +inf  负无穷到正无穷 给定一个范围
    [withscores] 结果显示数字
    [limit offset count]  offset 从第几个开始  count 显示几个
   zrangebyscore myset -inf +inf  [withscores]  [limit offset count]
   ex：zrangebyscore myset 2 12  limit 1 2  排序myset 显示数值在2到12的 从第二个开始 显示2个


删除
    zrem  myset one
"""