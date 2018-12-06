"""
本程序体现的是面向对象编程思想，简单判断电话号码
可判断的内容如下：
1 紧急电话，如110,119,120等。如需增加号码，可到目录下的numberList中增加
2 5位数的特殊服务号码。如需增加，同上
3 8位数的座机号码
4 11位数的手机号码，可判断运营商
5 带区号的座机号码
6 区号格式:
    010-1234567
    010-12345678
    0571-1234567
    0571-12345678
    0101234567
    01012345678
    05711234567
    057112345678
    统一规律：开头为0
    """

import numberList
from attribution import Attribution


class numberRecognize():
    #类的初始化
    def __init__(self,number):
        self.NL = numberList.NumberList()
        self.number = str(number).replace(' ','')
        self.attribution = Attribution(self.number)
        self.lengthList = {
            3 : self.pn3,
            5 : self.pn5,
            7 : self.pn8,
            8 : self.pn8,
            11: self.pn11
        }

    #判断是不是数字
    def is_number(self):
        try:
            self.number = int(self.number)
        except ValueError:
            return False    #如果报错了表示里面有字符串
        return True


    #判断号码的长度，选择相应的函数执行
    def number_length(self):
        length = len(str(self.number))
        if length not in self.lengthList.keys():
            print(self.NL.lengthError)
            return
        if not self.lengthList[length]():
            print(self.NL.notNumber)
        else: #当flase的时候
            pass

    #判断三位数的紧急电话
    def pn3(self):
        if self.number in self.NL.emergencyNumbers.keys():
            print(self.NL.console_out,self.NL.emergencyNumbers[self.number])
            return True
        return False

    #判断五位数的特殊号码
    def pn5(self):
        if self.number in self.NL.special_numbers.keys():
            print(self.NL.console_out,self.NL.special_numbers[self.number])
            return True
        return False

    #判断座机
    def pn8(self):
        print(self.NL.console_out,self.NL.zuoji_noAreaNumber)
        return True

    #判断手机号，移动联通电信
    def pn11(self):
        number_head = str(self.number)[:3]
        self.attribution.ip138_search()
        if number_head in self.NL.mobile_head:
            print(self.NL.console_out,self.NL.mobile_number,self.NL.CN_mobile,self.NL.areaName,self.attribution.city,self.attribution.numberType)
            return True
        elif number_head in self.NL.unicom_head:
            print(self.NL.console_out,self.NL.mobile_number,self.NL.CN_unicom,self.NL.areaName,self.attribution.city,self.attribution.numberType)
            return True
        elif number_head in self.NL.net_head:
            print(self.NL.console_out,self.NL.mobile_number,self.NL.CN_net,self.NL.areaName,self.attribution.city,self.attribution.numberType)
            return True
        else:
            return False

    #判断带区号的座机号码
    def has_areaNumber(self):
        if self.number[0] == '0' and len(self.number) >3:
            areaAndNumber = self.NL.search_areaNumber(self.number[:3]) + self.NL.search_areaNumber(self.number[:4])
            try:
                minLen = len(areaAndNumber[2])+7
                maxLen = minLen + 4
                if len(self.number) in range(minLen, maxLen):
                    print(self.NL.console_out, self.NL.zuoji_areaNumber, self.NL.areaName,
                          areaAndNumber[0] + areaAndNumber[1])
                    return True
                else:
                    print(self.NL.zuoji_lengthError)
                    return True
            except IndexError:
                print(self.NL.notNumber)
                return True

        return False

    #入口，从这里开始执行
    def main_recognize(self):
        if not self.has_areaNumber():   #运行has_areaNumber()函数 返回Ture或者False
            if self.is_number():
                self.number_length()
            else:
                print(self.NL.notNumber)

if __name__ == '__main__':
    while True:
        number = input("请输入号码:")
        N = numberRecognize(number)
        N.main_recognize()
        print('\n')