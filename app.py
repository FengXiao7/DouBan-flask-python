# -*- coding = utf-8 -*-
# @Time : 2021/10/20 20:45
# @Author : 冯小7
# @File: test_Pymysql.py
# @Software: PyCharm
from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/movie')
def movie():
    List=[]
    conn = pymysql.connect(host='localhost', user='root',
                           password='Plm098765', database='test_pymysql')
    cursor = conn.cursor()
    sql = '''
            select*from doubantop250
            '''
    cursor.execute(sql)
    movieTup = cursor.fetchall()#movieTup是一个大元组里面250个小元组
    movieList=list(movieTup)
    for item in movieList:
        List.append(list(item))
    cursor.close()
    conn.close()
    return render_template("movie.html", movies=List)


@app.route('/score')
def score():
    List = []
    score = []  # 电影分数
    numer = []  # 电影分数对应数目
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
    return render_template("score.html",score=score,number=numer)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
