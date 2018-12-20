#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#A3.py 智育成绩汇总导入数据库
#1.创建数据库"Score.db"
#2.创建数据表"Score"，设置主键"学号 char(20) PRIMARY KEY"
#    数据表格式:学号 姓名 (科目)
#3.将"智育成绩汇总.xls"导入数据库"Score.db"
#
import sqlite3
import os
import xlrd
import xlwt

def A3():
    cn = sqlite3.connect('Score.db')
    cur = cn.cursor()

    path = "./智育成绩汇总.xls"
    data = xlrd.open_workbook(path) 
    table = data.sheets()[0]
    ncols = table.ncols
    nrows = table.nrows
    s1="学号 char(20) PRIMARY KEY, 姓名 char(10), "
    flag=0
    for i in table.row_values(0):
        if flag>=2:
            s1=s1+i+' DOUBLE'
            if flag!=ncols-1:
                s1=s1+','
        flag+=1
        
    try:
        cn.execute('''CREATE TABLE IF NOT EXISTS Score('''+s1+''');''')
    except:
        pass
    s2=''
    flag=0
    for i in table.row_values(0):
        s2=s2+i
        if flag!=ncols-1:
            s2=s2+','
        flag+=1

    for i in range(nrows):
        flag = 0
        s3 = ''
        if i!=0:
            for k in table.row_values(i):
                if flag==0:
                    s3 = s3 + str(int(k))
                elif flag==1:
                    s3 = s3 + "'"+str(k)+ "'"
                else:
                    s3 = s3 + str(k)
                if flag != ncols - 1:
                    s3+=','
                    flag += 1
            cn.execute('''insert into  Score ('''+s2+''') values('''+s3+''')''')
            cn.commit()
    cur.close()
    cn.close()
if __name__=="__main__":
    A3()

