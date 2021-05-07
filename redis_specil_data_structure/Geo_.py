"""
可以推算地理位置的信息，两地的距离，方圆几离的人
    geoadd：添加地理位置的坐标。
    geopos：获取地理位置的坐标。
    geodist：计算两个位置之间的距离。
    georadius：根据用户给定的经纬度坐标来获取指定范围内的地理位置集合。
    georadiusbymember：根据储存在位置集合里面的某个地点获取指定范围内的地理位置集合。
    geohash：返回一个或多个位置对象的 geohash 值。


geoadd  china:city 116.405285 39.904989 ﾱﾱﾾﾩ
(integer) 1
127.0.0.1:6379> geoadd  china:city
(integer) 1
127.0.0.1:6379> geoadd china:city
(integer) 1
127.0.0.1:6379> geoad  china:city  29.581 106.549 chongqin  126.645  45.758
(error) ERR unknown command 'geoad'
127.0.0.1:6379> geoadd  china:city  106.549  29.581   chongqin     126.645 45.758 haerbin  116.408  39.904 beijing   117.246  39.117 tianjin
(integer) 2
"""