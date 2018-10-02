#!coding:utf-8 
# !@Time   : 2018/9/18 20:43
# !@Author : Aydin
# !@File   : mainGatherData.py

from commonMethod import *
from analyse import *

#抓取数据
for year in range(2008, 2019):
    print("开始抓取-" + str(year))
    if year < 2010:
        for _dt in range(int(str(year)[3:] + '001'), int(str(year)[3:] + '155')):
            gatherData("0" + str(_dt))
    else:
        for _dt in range(int(str(year)[2:] + '001'), int(str(year)[2:] + '155')):
            gatherData(str(_dt))
    print("完成-" + str(year))

#开始进行分析
print("开始进行分析！")
analysisOne()
print("结束分析！")

