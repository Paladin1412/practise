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
    ├── common                           // 公共方法
    │   ├── singleSignOn.py                  
    │   ├── commFunc.py
    │   ├── dbConfig.py
    │   ├── globalParams.py
    │   ├── htmlReport.py
    │   ├── httpConfig.py
    │   ├── logConfig.py
    │   ├── emailConfig.py
    │   └── readConfig.py
    ├── config                           // 环境配置
    │   ├── testConfig.ini
    │   └── quasiConfig.ini
    ├── log                              // 日志log
    │   ├── error-20170227182905.log
    │   └── error-20170227182905.log.1 
    ├── proAPI                          // 接口API
    │   ├── projectA
    │   │   ├── testA.py 
    │   │   ├── testB.py     
    │   ├── projectB
    │   │   └── testB.py               
    ├── testCase                         // 测试用例
    │   ├── projectA
    │   │   ├── testA.py 
    │   │   ├── testB.py     
    │   ├── projectB
    │   │   └── testD.py           
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