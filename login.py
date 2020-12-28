import requests
import base64
import re
import sys
#import rsa
import six
import RSAJS
from hex2b64 import HB64 
#加密密码
def password(pw,modulus,exponent):
    exponent = HB64().b642hex(exponent)   
    modulus = HB64().b642hex(modulus)        
    rsa = RSAJS.RSAKey()
    rsa.setPublic(modulus, exponent)                         
    cry_data = rsa.encrypt(pw)
    return HB64().hex2b64(cry_data)

class session():
    def __init__(self,yhm,pw):
        self.yhm=yhm
        self.pw=pw
        #self.s为类的核心
        self.get_url='http://172.16.1.205/jwglxt/xtgl/login_slogin.html'#登录链接
        self.post_url='http://172.16.1.205/jwglxt/xtgl/login_slogin.html'#提交链接
        self.s=requests.Session()

    #核心代码,登录
    def login(self):
        try:
            head = {
                 "Referer": "http://172.16.1.205/jwglxt/xtgl/login_slogin.html?time=1598366187884",
                 "Cache-Control": "max-age=0",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Upgrade-Insecure-Requests": "1",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
                 "Accept-Encoding": "gzip, deflate",
                 "Host": "172.16.1.205",
                 "Connection": "Keep-Alive"
                }
            #获取登录页面
            r=self.s.get(url=self.get_url,headers=head,verify=False)
            
            csrftoken=re.findall('<input type="hidden" id="csrftoken" name="csrftoken" value="(.*?)"/>',r.text)[0]
            
            head = {
                     "Referer": "http://172.16.1.205/jwglxt/xtgl/login_slogin.html",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
                     "Accept": "application/json, text/javascript, */*; q=0.01",
                     "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
                     "X-Requested-With": "XMLHttpRequest",
                     "Accept-Encoding": "gzip, deflate",
                     "Host": "172.16.1.205",
                     "Connection": "Keep-Alive",
                     "Pragma": "no-cache"
                   }
            
            #获取公钥
            r=self.s.get('http://172.16.1.205/jwglxt/xtgl/login_getPublicKey.html',headers=head,verify=False)

            modulus=r.json()['modulus']
            exponent=r.json()['exponent']

            enpassword=password(self.pw,modulus,exponent)

            
            #要提交的表单
            data={
            'csrftoken':csrftoken,
            'yhm':self.yhm,
            'mm':enpassword,
            'mm':enpassword
            }
            #表单请求头
            head={
                 "Referer": "http://172.16.1.205/jwglxt/xtgl/login_slogin.html",
                 "Cache-Control": "max-age=0",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Upgrade-Insecure-Requests": "1",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
                 "Accept-Encoding": "gzip, deflate",
                 "Host": "172.16.1.205",
                 "Connection": "Keep-Alive"
                }
            #提交表单
            r=self.s.post(self.post_url,data=data,headers=head)
            #print(r.text)
            #input()
            ppot = r'用户名或密码不正确'
            if re.findall(ppot, r.text):
                print('用户名或密码错误,请查验..')
                return False
            else:
                print('登录成功\n')
                return True
        
        except:
            print('登录失败,请连接校园网...')
            return False
        
    #对外方法,进行重新登录
    def relogin(self):
        count=0
        while 1:
            count+=1
            if self.login():
                return True
            if count >10:
                #如果多次失败则停止登录
                return False

    
