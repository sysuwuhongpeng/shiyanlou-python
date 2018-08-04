#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 
import csv 

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_cfg(self):
        index = self.args.index('-c')
        return self.args[index+1]
    def get_gz(self):
        index = self.args.index('-d')
        return self.args[index+1]
    def get_shuihou(self):
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
    def get_cfgItem(self, cfgitem):
        return self._datas[cfgitem]

if __name__ == '__main__':
    try:
        arg = Args()
    except:
        print("Paramenter Error")
    else:
