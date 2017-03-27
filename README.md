# PyTest Demo 
============
    1、PyTest Demo 
    2、Http
    3、DataBase 
    4、LogConfig
    5、Report

目录结构
-------

#### 目录结构描述
    ├── readme.md                        // help
    ├── demo                             // 主目录 
    │	 ├── ziroomer  
    │   │   ├── demo.py
    │   │   └── getappid.py
    │   ├── __init__.py                 // 初始化
    │   ├── commfunc.py                 // 公共方法
    │   ├── dbconfig.py                 // 数据库
    │   ├── globalparams.py             // 参数
    │   ├── htmlreport.py               // 测试报告
    │   ├── httpconfig.py               // http
    │   ├── logconfig.py                // 日志
    │   └── main.py                     // 主函数
    ├── log
    │   ├── error-20170227182905.log
    │   └── error-20170227182905.log.1 
    ├── test                             // 单元测试
    │   └── testdemo.py 
    ├── report                           // 测试报告
         └── report20170227182905.html 


DateBase
-------

### MySQL
```Python
pip install `pymysql`
```

### Oracle
```Python
pip install `cx-Oracle`
```

版本
-------
* 编程语言
    * Python 3.4

更新
-------
#### V1.0.0 版本内容更新
1. demo框架
2. 日志配置
3. 单元测试
4. 测试报告