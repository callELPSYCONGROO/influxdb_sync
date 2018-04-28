# master_slave
> InfluxDB主从同步

### 介绍
该项目实现了InfluxDB的主从同步。

> 拓扑图

![InfluxDB同步系统](https://raw.githubusercontent.com/hongmaju/light7Local/master/img/productShow/20170518152848.png)

实现单边主从同步，只需要在主机侧启动该项目脚本。

### 运行

* 下载该项目，实际上需要的文件为：
    * /logs/**
    * /ms/**
    * /record/**
    * /main.py
    * /setup.py
    * /start.sh
    
* 安装项目，使用脚本 `python setup.py`