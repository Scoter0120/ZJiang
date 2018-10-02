#!coding:utf-8 
# !@Time   : 2018/9/18 19:29
# !@Author : Aydin
# !@File   : commonMethod.py

import pymysql, configparser
import urllib.request as ur
from bs4 import BeautifulSoup as bs

cf = configparser.ConfigParser()
cf.read("db.conf")
server = cf.get("db", "db_host")
user = cf.get("db", "db_user")
password = cf.get("db", "db_pass")
dbname = cf.get("db", "db_name")


## 从网上获取数据
def gatherData(dt):
    if not isDataExit(dt, "ANALYSIS_TM_MAIN_DATA"):
        try:
            response = ur.urlopen("http://kaijiang.500.com/shtml/ssq/{0}.shtml?0_ala_baidu".format(dt))
            html = response.read()
            html = html.decode("gbk")  # 解码
            soup = bs(html)

            rb = ""
            bb = ""
            redBalls = soup.select("ul .ball_red")  # 选择器，类似JS选择器
            for li in redBalls:
                rb = rb + "," + li.text

            blueBalls = soup.select("ul .ball_blue")  # 选择器，类似JS选择器
            bb = blueBalls[0].text

            ## 去除有问题的数据
            if rb.find('Result') < 0:
                addMainData(dt, rb[1:], bb)
        except Exception:
            print(dt + "|ERROR")


## 给数据表中添加数据
def addMainData(dt, redBall, blueBall):
    try:
        conn = pymysql.connect(host=server, user=user, password=password, database=dbname, charset="utf8")
        cur = conn.cursor()
        if not cur:
            raise Exception('数据库连接失败！')
        sql = "INSERT INTO ANALYSIS_TM_MAIN_DATA (DT,RED_BALL,BLUE_BALL)VALUES('{0}','{1}','{2}') ".format(dt, redBall, blueBall)
        cur.execute(sql)
        conn.commit()
    except Exception:
        print(dt + "|ERROR")
    finally:
        cur.close()
        conn.close()


## 判断是否数据已存在
def isDataExit(dt, tableName):
    try:
        conn = pymysql.connect(host=server, user=user, password=password, database=dbname, charset="utf8")
        cur = conn.cursor()
        if not cur:
            raise Exception('数据库连接失败！')
        sql = "SELECT COUNT(*) FROM {0} WHERE DT='{1}'".format(tableName, dt)
        cur.execute(sql)
        _temp = cur.fetchall()
        _count = _temp[0][0]
        return _count
    except Exception:
        print(dt + "|ERROR")
    finally:
        cur.close()
        conn.close()


## 本方法自身测试
if __name__ == "__main__":
    print(isDataExit("18100"))
    if not isDataExit("18100"):
        print("获取")
