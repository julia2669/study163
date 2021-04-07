#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/6/2020 14:37 
# @Author : Julia
# @Version：V 0.1
# @File : test.py
# @desc :


# import requests
# import json
#
# url = "https://cae-cpapb-dev2.cisco.com/rest/v2/AppResources?app=Engineering:SBG:Cloud Security&page=1&pageSize=100&namePattern=&nameSearchType=startwith"
#
# payload={}
# headers = {
#   'Authorization': 'Basic ZWRzYXJ0YXBpLmdlbjpidWJydURBWmF5dXF1M0U4ZUY3Ng==',
#   'Cookie': '60a91611d335e8d99ccc42b8d391950b=5c509f7134eb175df3d744681a6835fe'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# a = len(response.json())
# for i in range(0,a):
#     print('"'+response.json()[i]['parentFQN']+':'+response.json()[i]['resourceName']+'"')


import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect("EDSART", "PrUr3#et", "ldap://ldap-ldprd.cisco.com:5000/cn=OracleContext,dc=cisco,dc=com/CEPMHSTG")

cursor = connection.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)



