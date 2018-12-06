"""
获取手机号码归属地
"""
from bs4 import BeautifulSoup as bs
from requests import get
from requests_headers import header
from numberList import NumberList

class Attribution():

    def __init__(self,number):
        self.NL = NumberList()
        self.number = number

    def ip138_search(self):

        headers = header()
        url = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile='+str(self.number)
        flag = True
        try_count = 0
        while flag:
            try:
                r = get(url,headers=headers,timeout=10)
                flag = False
            except:
                try_count += 1
            if try_count >3:
                print('网络错误，请重试！')
                return

        r.encoding='gb2312'
        html = bs(r.text,'html.parser')
        numberInfo = html.select('table[style="border-collapse: collapse"] tr[class="tdc"] td[class="tdc2"]')
        try:
            self.city = numberInfo[1].get_text()
            self.numberType = numberInfo[2].get_text()
        except IndexError:
            self.city = self.NL.attributionNotFound
            self.numberType = self.NL.numberTypeNotFound

