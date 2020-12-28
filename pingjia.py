from login import session
import re
class pj:
    def __init__(self,yhm,pw):
        self.s=session(yhm,pw)
    def login_in(self):
        return self.s.login()
    def pingjia(self):
        url=f'http://172.16.1.205/jwglxt/xspjgl/xspj_cxXspjIndex.html?doType=query&gnmkdm=N401605&su={self.s.yhm}'
        data='_search=false&nd=1598407957839&queryModel.showCount=50&queryModel.currentPage=1&queryModel.sortName=&queryModel.sortOrder=asc&time=1'
        #获取教师列表
        r=self.s.s.post(url,headers={'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'},data=data)

        items=r.json()['items']

        head={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            }
            #获取课程页面
        data={
            'jxb_id':items[0]['jxb_id'],
            'kch_id':items[0]['kch_id'],
            'jgh_id':items[0]['jgh_id'],
            'xsdm':items[0]['xsdm'],
            'tjzt':-1,
            'pjmbmcb_id':'',
            'sfcjlrjs':1
            }
        url=f'http://172.16.1.205/jwglxt/xspjgl/xspj_cxXspjDisplay.html?gnmkdm=N401605&su={self.s.yhm}'
        r=self.s.s.post(url,headers=head,data=data)
        xzid=re.findall(r'data-pfdjdmxmb_id="(.+?)"', r.text)[0:4]
        bid=re.findall(r'data-pjzbxm_id="(.+?)"', r.text)
        cid=re.findall(r'data-pfdjdmb_id="(.+?)"', r.text)
        did=re.findall(r'data-pjmbmcb_id="(.+?)"', r.text)[0]           
        pjid=re.findall(r'data-pjmbmcb_id="(.+?)"', r.text)[0]
        #xspfb_id=re.findall(r'data-xspfb_id="(.+?)"', r.text)
        
        for i in items:
            if i['tjzt']==0:
                continue
            elif i['tjzt']==1:
                break
            head={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            }

            #可拓展评价
            manyi=''
            gaijin=''
            pingyu=''
            url=f'http://172.16.1.205/jwglxt/xspjgl/xspj_bcXspj.html?gnmkdm=N401605&su={self.s.yhm}'
            
            data={
             "ztpjbl": "100",
             "jszdpjbl": "0",
             "xykzpjbl": "0",
             'jxb_id':i['jxb_id'],
            'kch_id':i['kch_id'],
            'jgh_id':i['jgh_id'],
            'xsdm':i['xsdm'],
             "modelList[0].pjmbmcb_id": pjid,
             "modelList[0].pjdxdm": "01",
             "modelList[0].py": pingyu,
             "modelList[0].xspfb_id": "",
             "modelList[0].xspjList[0].childXspjList[0].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[0].pjzbxm_id": bid[1],
             "modelList[0].xspjList[0].childXspjList[0].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[0].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[1].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[1].pjzbxm_id": bid[2],
             "modelList[0].xspjList[0].childXspjList[1].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[1].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[2].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[2].pjzbxm_id": bid[3],
             "modelList[0].xspjList[0].childXspjList[2].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[2].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[3].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[3].pjzbxm_id": bid[4],
             "modelList[0].xspjList[0].childXspjList[3].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[3].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[4].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[4].pjzbxm_id": bid[5],
             "modelList[0].xspjList[0].childXspjList[4].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[4].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[5].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[5].pjzbxm_id": bid[6],
             "modelList[0].xspjList[0].childXspjList[5].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[5].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[6].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[6].pjzbxm_id": bid[7],
             "modelList[0].xspjList[0].childXspjList[6].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[6].zsmbmcb_id": did,
             "modelList[0].xspjList[0].childXspjList[7].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[0].childXspjList[7].pjzbxm_id": bid[8],
             "modelList[0].xspjList[0].childXspjList[7].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[0].childXspjList[7].zsmbmcb_id": did,
             "modelList[0].xspjList[0].pjzbxm_id": bid[0],
             
             "modelList[0].xspjList[1].childXspjList[0].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[1].childXspjList[0].pjzbxm_id": bid[10],
             "modelList[0].xspjList[1].childXspjList[0].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[1].childXspjList[0].zsmbmcb_id": did,
             "modelList[0].xspjList[1].childXspjList[1].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[1].childXspjList[1].pjzbxm_id": bid[11],
             "modelList[0].xspjList[1].childXspjList[1].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[1].childXspjList[1].zsmbmcb_id": did,
             "modelList[0].xspjList[1].childXspjList[2].pfdjdmxmb_id": xzid[1],
             "modelList[0].xspjList[1].childXspjList[2].pjzbxm_id": bid[12],
             "modelList[0].xspjList[1].childXspjList[2].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[1].childXspjList[2].zsmbmcb_id": did,
             "modelList[0].xspjList[1].childXspjList[3].pfdjdmxmb_id": xzid[2],
             "modelList[0].xspjList[1].childXspjList[3].pjzbxm_id": bid[13],
             "modelList[0].xspjList[1].childXspjList[3].pfdjdmb_id": cid[0],
             "modelList[0].xspjList[1].childXspjList[3].zsmbmcb_id": did,         
             "modelList[0].xspjList[1].pjzbxm_id": bid[9],
             
             "modelList[0].xspjList[2].childXspjList[0].zgpj": manyi,
             "modelList[0].xspjList[2].childXspjList[0].pjzbxm_id": bid[15],
             "modelList[0].xspjList[2].childXspjList[0].pfdjdmb_id": cid[-1],
             "modelList[0].xspjList[2].childXspjList[0].zsmbmcb_id": did,
             "modelList[0].xspjList[2].childXspjList[1].zgpj": gaijin,
             "modelList[0].xspjList[2].childXspjList[1].pjzbxm_id": bid[16],
             "modelList[0].xspjList[2].childXspjList[1].pfdjdmb_id": cid[-1],
             "modelList[0].xspjList[2].childXspjList[1].zsmbmcb_id": did,
             "modelList[0].xspjList[2].pjzbxm_id": bid[14],
             "modelList[0].pjzt": "1",
             "tjzt": "0"
            }
            
            r=self.s.s.post(url,headers=head,data=data)
            print(i['jxbmc']+r.text+'\n')

        url='http://172.16.1.205/jwglxt/xspjgl/xspj_tjXspj.html?gnmkdm=N401605&su={self.s.yhm}'
        r=self.s.s.post(url,headers=head,data=data)
        print(r.text)
        input()
if __name__=="__main__":
    print("——————教学评价,请连接校园网操作——————")
    xh=input("请输入学号：")
    pw=input("请输入密码：")
    a=pj(xh,pw)
    while not a.login_in():
        xh=input("请输入学号：")
        pw=input("请输入密码：")
        a=pj(xh,pw)
    print("爬取中，请耐心等待~")
    a.pingjia()
