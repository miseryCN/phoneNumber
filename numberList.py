"""
这个文件用来定义一些常量
"""
from json import loads
from base64 import b64decode

class NumberList():

    def __init__(self):
        self.emergencyNumbers = {
        110 : '报警电话',
        120 : '急救电话',
        119 : '火警电话',
        122 : '交通事故报警电话'
        }

        self.special_numbers = {
            12345 : '市长热线',
            12580 : '一按我帮您',
            10086 : '中国移动客服热线',
            10010 : '中国联通客服热线',
            10000 : '中国电信客服热线'
        }

        self.mobile_head = ['134','135','136','137','138','139','147','150','151','152','157','158','159',
                            '178','182','183','184','187','188','198']

        self.unicom_head = ['130','131','132','155','156','145','176','185','186','166']

        self.net_head = ['133','149','153','153','173','177','180','181','189','199']

        self.zuoji_areaNumber = '带区号的座机号码'
        self.zuoji_noAreaNumber = '不带区号的座机号码'
        self.CN_mobile = '中国移动号码'
        self.CN_unicom = '中国联通号码'
        self.CN_net = '中国电信号码'
        self.mobile_number = '手机号,'
        self.special_number = '特殊号码'
        self.console_out = '电话号码是:'
        self.notNumber = '不是电话号码'
        self.lengthError = '号码长度错误'
        self.areaName = '地区为:'
        self.zuoji_lengthError = '座机号码长度错误'
        self.attributionNotFound = '未找到归属地'
        self.numberTypeNotFound = '未找到卡运营商'

        dbFile = open('areaNumber.db','rb').read()
        self.areaNumbers = loads(b64decode(dbFile).decode('utf-8'))


    def search_areaNumber(self,areaNumber):
        for province in self.areaNumbers:
            citiesInfo = self.areaNumbers[province]
            citiesInfo_new = {value:key for key,value in citiesInfo.items()}
            for city_areaNumber in citiesInfo_new.keys():
                if city_areaNumber == areaNumber:
                    city = citiesInfo_new[city_areaNumber]
                    return (province,city,city_areaNumber)
        return ()
