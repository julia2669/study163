#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/19/2021 16:03 
# @Author : Julia
# @Version：V 0.1
# @File : pysqlTest.py
# @desc :

import pymysql


def connMySQL(sql, params, host='localhost', user='julia',passwd='Julia123', db='study_163'):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='julia',#root
            passwd='Julia123',
            db='study_163'
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        cur.execute(sql,params)
        data = cur.fetchall()
        return data
    finally:
        cur.close()
        conn.close()

# sql = '''
# insert into user value (%s, %s, %s, %s);
# '''
# params = (4, 'wendy', 30, 'shanghai')

sql = '''
select * from user where id = %s
'''
params = (1)
# print(connMySQL(sql,params))


class MySqlHelper():

    def conn(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='julia',#root
                passwd='Julia123',
                db='study_163'
            )
            return conn
        except Exception as e:
            return e.args


    def get_one(self,sql,params):
        cur = self.conn().cursor()
        cur.execute(sql,params)
        result = cur.fetchone()
        return result

    def get_all(self,sql,params):
        cur = self.conn().cursor()
        cur.execute(sql,params)
        result = cur.fetchall()
        return result

def checkValid(sql,params):
    opera = MySqlHelper()
    result = opera.get_one(sql,params)
    if result:
        print('success')


print(checkValid(sql,params))