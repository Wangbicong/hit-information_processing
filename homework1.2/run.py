# -*- coding:utf-8 -*-
from flask import Flask, render_template
from utils.csv import Parser

app = Flask(__name__)


@app.route('/')
def index():

    forest = Parser.parser('data/forestfires.csv')
    iris = Parser.parser('data/iris.data', ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
    crx = Parser.parser('data/crx.data', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',
                                          'A13', 'A14', 'A15', 'A16'])
    texi = Parser.parser('data/GPSSample', [u'车辆标识', u'触发事件', u'运营状态', u'GPS时间', u'GPS经度', u'GPS纬度',
                                           u'GPS速度', u'GPS方位', u'GPS状态'])

    return render_template('index.html', forest=forest, iris=iris, crx=crx, texi=texi)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)