# master_slave
> InfluxDB主从同步

### 介绍
该项目实现了InfluxDB的主从同步。

> 拓扑图

![InfluxDB同步系统](https://github.com/callELPSYCONGROO/master_slave/blob/master/refer/InfluxDB%E5%90%8C%E6%AD%A5%E7%B3%BB%E7%BB%9F.png?raw=true)

实现单边主从同步，只需要在主机侧启动该项目脚本。该项目需要结合[我的InfluxDB](https://github.com/callELPSYCONGROO/influxdb)使用。

### 启动运行

* 下载该项目，实际上需要的文件为：
    * /logs/**
    * /ms/**
    * /record/**
    * /main.py
    
* 安装或更新Influxdb-python插件模块，使用脚本 `pip install influxdb` 或 `pip install --upgrade influxdb`

* 配置脚本：
    * 打开配置文件 ms/util/constant.py
    * 修改以下配置为你的路径
        * 主机日志文件路径 INFLUXDB_MASTER_LOG，这个文件是Influxdb配置文件中配置的记录http请求的日志文件（access-log-path对应的那个文件）
        * 从机HOST INFLUXDB_SLAVE_HOST
        * 从机PORT INFLUXDB_SLAVE_PORT
        * 从机用户名 INFLUXDB_SLAVE_USER
        * 从机密码 INFLUXDB_SLAVE_PASSWORD
    * 其他配置可以不修改

* 运行，使用脚本 `python main.py`