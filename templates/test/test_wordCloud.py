# -*- coding = utf-8 -*-
# @Time : 2021/10/29 16:00
# @Author : 冯小7
# @File: test_wordCloud.py
# @Software: PyCharm
from itertools import chain

import jieba  #分词
from matplotlib import pyplot as plt #绘图，具体生成一张图片
from wordcloud import WordCloud, STOPWORDS  # 词云
from PIL import Image  #图像处理
import numpy  #矩阵运算
import pymysql #数据库

text=""
conn = pymysql.connect(host='localhost', user='root',
                       password='Plm098765', database='test_pymysql')
cursor = conn.cursor()
sql='''
    select title1 from doubantop250
'''
cursor.execute(sql)
movieNameTuples= cursor.fetchall()#一个带有250个小元组的大元组
resultlist = list(chain.from_iterable(movieNameTuples))#把含250个小元组的大元组转化为一个大列表，里面直接是250目标值即电影名
for item in resultlist:
    text=text+" "+item
cursor.close()
conn.close()
# print(text)
#分词
# cut=jieba.cut(text)
# str=' '.join(cut)
# print(len(str))
print(text)

#
# img = Image.open(r"..\..\static\assets\img\wordCloud\电影.jpeg")
# img_array = numpy.array(img)   #将图片转化为数组
#
#
# wc=WordCloud(
#     background_color='white',
#     mask=img_array,
#     stopwords=STOPWORDS.add("哈利"),
#     font_path='msyh.ttc'  #字体所在位置：C:\Windows\Fonts
#
# )
# wc.generate_from_text(text)
#
# #绘制图片
# fig = plt.figure(1)
# plt.imshow(wc)
# plt.axis('off')     #是否显示坐标轴
#
# #plt.show()    #显示生成的词云图片
# plt.savefig(r"..\..\static\assets\img\wordCloud\电影_wordCloud.jpeg",dpi=500)
