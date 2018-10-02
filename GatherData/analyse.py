#!coding:utf-8 
# !@Time   : 2018/9/18 21:50
# !@Author : Aydin
# !@File   : analyse.py

import pymysql, configparser
from commonMethod import *

cf = configparser.ConfigParser()
cf.read("db.conf")
server = cf.get("db", "db_host")
user = cf.get("db", "db_user")
password = cf.get("db", "db_pass")
dbname = cf.get("db", "db_name")


### 获取每个红球之间的差值  红球的和   红球的积
def analysisOne():
    try:
        conn = pymysql.connect(host=server, user=user, password=password, database=dbname, charset="utf8")
        cur = conn.cursor()
        if not cur:
            raise Exception('数据库连接失败！')
        sql = "SELECT * FROM ANALYSIS_TM_MAIN_DATA ORDER BY DT"
        cur.execute(sql)
        tempResult = cur.fetchall()
        for _temp in tempResult:
            _dt = _temp[1]

            ## 判断是否已做过数据处理
            if not isDataExit(_dt, "ANALYSIS_TA_DATA_RESULT"):
                print("开始处理-" + str(_dt))
                _blueB = int(_temp[3])
                _redBs = str(_temp[2]).split(',')

                _result_cha = ""
                _he = 0
                _ji = 1
                _first = int(_redBs[0])
                for ball in _redBs:
                    _add = int(ball) - _first
                    _result_cha = _result_cha + "," + str(_add)
                    _first = int(ball)

                    _he = _he + int(ball)

                    _ji = _ji * int(ball)

                _sql = "INSERT INTO ANALYSIS_TA_DATA_RESULT (DT,SOURCE_DATA,RED_S_BALL,BLUE_BALL,CHA,HE,JI)VALUES('{0}','{1}',{2},{3},'{4}',{5},{6}) ".format(
                    _dt, str(_temp[2]), int(_redBs[0]), _blueB, _result_cha[1:], _he, _ji)
                # print(_sql)
                cur.execute(_sql)
                conn.commit()
                print("结束处理-" + str(_dt))
    except Exception as e:
        print("ERROR")
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    analysisOne()
