# -*- coding = utf-8 -*-
# @Time : 2021/10/27 21:00
# @Author : 冯小7
# @File: test_pymysql.py
# @Software: PyCharm

import pymysql

def test_1():
    List = []
    score=[]#电影分数
    numer=[]#电影分数对应数目
    conn = pymysql.connect(host='localhost', user='root',
                           password='Plm098765', database='test_pymysql')
    cursor = conn.cursor()
    sql = '''
                    SELECT score,COUNT(score) FROM doubantop250 GROUP BY score
                '''
    cursor.execute(sql)
    movieTup = cursor.fetchall()  # movieTup是一个大元组里面15个小元组
    movieList = list(movieTup)
    for item in movieList:
        List.append(list(item))
    for item in List:
        score.append(str(item[0])+"分")
        numer.append(item[1])
    print(score)
    print(numer)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    test_1()
