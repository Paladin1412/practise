PyTest Demo
============
    1、PyTest Demo 
    2、Http
    3、DataBase 
    4、LogConfig
    5、Report

目录结构
-----------

#### 目录结构描述
    ├── readme.md                        // help
    ├── main.py                          // main函数
    ├── common
    │   ├── __init__.py 
    │   ├── cassso.py                   // 单点登录                    
    │   ├── commFunc.py                 // 公共方法
    │   ├── dbConfig.py                 // 数据库
    │   ├── globalParams.py             // 公共参数
    │   ├── htmlReport.py               // 测试报告
    │   ├── httpConfig.py               // http
    │   ├── logConfig.py                // 日志配置
    │   ├── emailConfig.py              // 配置邮箱    
    │   └── readConfig.py               // 读取配置文件
    ├── config                           // 环境配置
    │   ├── testConfig.ini
    │   └── quasiConfig.ini
    ├── log                              // 日志log
    │   ├── error-20170227182905.log
    │   └── error-20170227182905.log.1 
    ├── testCase                         // 测试用例
    │   ├── projectA
    │   │   ├── testA.py 
    │   │   ├── testB.py     
    │   ├── projectB
    │   │   ├── testC.py    
    │   ├── projectC  
    │   │   ├── testD.py           
    │   └── projectD 
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