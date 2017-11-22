# 携程航班信息爬取
根据不同城市的携程航班信息表，进行当天航班信息抓取
http://flights.ctrip.com/actualtime/airport-xiaoshan.p1

# 耗时难点分析
1. 各个城市机场 nickname 的获取（求助同事帮助获得，存于airport.txt）
2. 代理 ip 获取（代理ip网站购买）

# 文档说明
- proxy.txt     部分代理ip
- valid_ip.sql  部分代理ip

- airport.txt             机场名称信息
- ctripAirportName.sql    机场名称信息
- ctripFligtInfo.sql      航班时刻 mysql 表结构

# 函数说明
|program|desc|
|:---:|:---:|
|airport_ctrip.py     | 类封装的所有机场航班信息抓取 |
|airport_ctrip_pool.py| 所有机场航班信息多进程抓取   |
|yiw_flight.py        | 针对单个机场起降飞机抓取     |
|yiwFlight.py         | 类封装的单个机场信息抓取，使用proxyip |