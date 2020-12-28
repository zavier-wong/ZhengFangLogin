正方登录模块
--------
这是一个用于正方系统登录的脚本。login.py是核心模块，RSAJS.py和hex2b64.py为通用工具，辅助完成登录操作。

文件夹下的pingjia.py则是利用login模块来实现例子，通过pingjia.py可一键完成对教师的评价，当然给个学校可能会有略微不同。

通过此模块可自由实现各种有意思的操作，如自动抢课，以及本仓库带的自动评价。

首先，对于不同的学校务必将login.py里的url换为自己学校的url！！

使用例子：
```python
#从login.py导入session类
from login import session

class MyClass:
    def __init__(self,yhm,pw):
        #用学号和密码初始化session类，通过维护一个全局session来执行操作
        self.s=session(yhm,pw)
        #调用s的方法login来登录
        self.s.login()
    def do_something():
        head={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            }
        data={ "message" : "hello" }
        self.s.s.post(url,headers=head,data=data)
```
