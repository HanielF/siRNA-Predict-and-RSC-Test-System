#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_plot_util.py
 * @Time    :  2020/04/28 16:23:25
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试plot_util构件
'''

import sys
import os
# sys.path.append("../spl_sirna")
sys.path.append("f:\\Learning\\siRNA\\Projects\\Tornado_LSTM")
from spl_sirna import plot_util
import numpy as np
import base64
os.chdir('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test')


def test_make_plot(args):
    '''
    Desc：
        测试make_plot function 通用的绘制折线图构件
    '''
    flag = True
    testRes = "Return: \n"
    filename = 'tmp_plot.jpg'
    try:
        data = args[0].split(';')
        data = [x.split(',') for x in data]
        for i, d in enumerate(data):
            for j, c in enumerate(d):
                data[i][j] = int(c)
        labels = args[1].split(',') if args[1] != 'None' else None
        titles = args[2].split(',') if args[1] != 'None' else None
        filename = args[3] if args[3] != 'None' else filename
        filename = "f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test\\" + filename
        plot_util.make_plot([data], [labels], titles=titles, filename=filename)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logstring = "RSC: make_plot {}".format('is OK' if flag else 'has bugs')
        print("logstring: ", logstring)
        testRes = testRes + "\n" + logstring
        print("end test")
    with open(filename, 'rb') as f:
        baseImg = base64.b64encode(f.read())
    testRes += str(baseImg)
    print(testRes)
    return testRes

def test_make_scatter(args):
    '''
    Desc：
        测试make_scatter function 通用的绘制折线图构件
    '''
    flag = True
    testRes = "Return: \n"
    filename = 'tmp_scatter.jpg'
    try:
        xdata = args[0].split(',')
        xdata = [int(x) for x in xdata]
        ydata = args[1].split(',')
        ydata = [int(x) for x in ydata]

        xlabels = args[2] if args[2] != 'None' else None
        ylabels = args[3] if args[3] != 'None' else None

        xticks = args[4].split(',') if args[4]!='None' else None
        xticks = [int(x) for x in xticks] if xticks is not None else None
        yticks = args[5].split(',') if args[5]!='None' else None
        yticks = [int(x) for x in yticks] if yticks is not None else None

        title = args[6] if args[6] != 'None' else None

        error = True if args[7] == 'True' else False
        pcc = True if args[8] == 'True' else False
        yxline = True if args[9] == 'True' else False

        filename = args[10] if args[10] != 'None' else filename
        filename = "f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test\\" + filename
        plot_util.make_scatter(xdata, ydata, xlabels, ylabels, xticks, yticks, title, error, pcc, yxline, filename)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logstring = "RSC: make_scatter {}".format('is OK' if flag else 'has bugs')
        print("logstring: ", logstring)
        testRes = testRes + "\n" + logstring
        print("end test")
    with open(filename, 'rb') as f:
        baseImg = base64.b64encode(f.read())
    testRes += str(baseImg)
    print(testRes)
    return testRes

if __name__ == "__main__":
    test_make_plot(['1,2,3', 'None', 'None', 'None'])
    # test_make_scatter()