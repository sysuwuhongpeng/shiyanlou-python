#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 
import csv 

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_cfgfile(self):
        index = self.args.index('-c')
        return self.args[index+1]
    def get_udfile(self):
        index = self.args.index('-d')
        return self.args[index+1]
    def get_gzfile(self):
        index = self.args.index('-o')
        return self.args[index+1]

class Config(object):
    def __init__(self, fileAddr):
        self._file = fileAddr
        self._datas = self.__read_datas() 
    def __read_datas(self):
        datas = {}
        file = open(self._file)
        for fileItem in file:
            data = fileItem.split('=')
            datas[data[0].strip()] = float(data[1].strip())
        return datas     
    def get_cfgItem(self):
        return self._datas

class UserData(object):
    def __init__(self, fileAddr):
        self._file = fileAddr
        self._datas = self.__read_datas() 
    def __read_datas(self):
        datas = {}
        file = open(self._file)
        for fileItem in file:
            data = fileItem.split(',')
            datas[int(data[0].strip())] = int(data[1].strip())
        return datas
    def get_userData(self):
        return self._datas

class InCalcu(object):
    def calc_for_all_userdata(self, cfgDatas, udDatas):
        self._cfgDatas = cfgDatas
        resultData = []
        for ghao,gzi in udDatas.items():
            dataOne =[]
            dataOne.append(ghao)
            dataOne.append(gzi)
            shebao = self.calc_shebao(gzi)
            dataOne.append('%.2f'%(shebao))
            geshui = self.calc_geshui(gzi,shebao)
            dataOne.append('%.2f'%(geshui))
            shuihou = gzi - shebao - geshui
            dataOne.append('%.2f'%(shuihou))
            resultData.append(dataOne)
        return resultData
    def calc_shebao(self,gzi):
        cfgDatas = self._cfgDatas
        jsl = cfgDatas['JiShuL']
        jsh = cfgDatas['JiShuH']
        ylao= cfgDatas['YangLao']
        yl  = cfgDatas['YiLiao']
        sye = cfgDatas['ShiYe']
        gs  = cfgDatas['GongShang']
        syu = cfgDatas['ShengYu']
        gjj = cfgDatas['GongJiJin']
        if gzi <= jsl:
            gzi = jsl
        elif gzi > jsh:
            gzi = jsh
        return gzi*(ylao+yl+sye+gs+syu+gjj)
    
    def calc_geshui(self,gzi,shebao):
        yj = gzi - shebao - 3500
        if yj > 0:
            if yj <= 1500:
                s = yj * 0.03
            elif yj <= 4500:
                s = yj*0.1 - 105
            elif yj <= 9000:
                s = yj*0.2 - 555
            elif yj <= 35000:
                s = yj*0.25 - 1005
            elif yj <= 55000:
                s = yj*0.3 - 2755
            elif yj <= 80000:
                s = yj*0.35 - 5505
            else:
                s = yj*0.45 - 13505
        else:
            s = 0
        return s
        
    def export(self, fileAddr, cfgDatas, udDatas):
        result = self.calc_for_all_userdata(cfgDatas, udDatas)
        with open(fileAddr, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)
if __name__ == '__main__':
    try:
        arg = Args()
        cfg = Config(arg.get_cfgfile())
        data = UserData(arg.get_udfile())
        calcu = InCalcu()

        cfgDatas = cfg.get_cfgItem()
        udDatas  = data.get_userData()
        calcu.export(arg.get_gzfile(), cfgDatas, udDatas)
    except:
        print("Paramenter Error")

