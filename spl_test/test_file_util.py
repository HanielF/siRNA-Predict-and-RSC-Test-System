#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_file_util.py
 * @Time    :  2020/04/28 14:07:04
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试file_util构件
'''

import sys
import os
sys.path.append("f:\\Learning\\siRNA\\Projects\\Tornado_LSTM")
print(sys.path)
from spl_sirna import file_util
import numpy as np
import pandas as pd
os.chdir('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test')


def test_get_data_from_file(args):
    '''
    Desc：
        测试read file 监督学习中通用的读csv/excel的构件
    '''
    flag = True
    testRes = "Return: \n"
    try:
        fp = os.path.join('spl_test\\', args[0])
        xname = None if args[1] == '' else args[1].split(",")
        yname = None if args[2] == '' else args[2]
        upper = True if args[3] == 'True' else False
        dropna = True if args[4] == 'True' else False
        encode = args[5]
        x, y = file_util.get_data_from_file(fp,
                                            xname=xname,
                                            yname=yname,
                                            upper=upper,
                                            dropna=dropna,
                                            encode=encode)
        res_x, res_y = x[:5], y[:5]
        testRes += "xdata: {}\nydata: {}".format(res_x, res_y)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logstring = "rsc: get_data_from_file {}".format(
            'is ok' if flag else 'has bugs')
        print("logstring: ", logstring)
        testres = testres + "\n" + logstring
        print("end test")
    return testres


def test_write_csv_excel(args):
    '''
    Desc：
        write to file 通用的写csv/excel/txt文件构件
    '''
    flag = True
    testRes = "Return: \n"
    try:
        data = args[0].split(',')
        fp = os.path.join('spl_test\\', args[1])
        columns = None if args[2] == 'None' else args[3].split(",")
        header = True if args[3] == 'True' else False
        sheet_name = args[4]
        nan_rep = args[5]
        encode = None if args[6] == 'None' else args[6]
        file_util.write_csv_excel(data, fp, columns, header, sheet_name,
                                  nan_rep, encode)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: write_csv_excel is {}".format(
            'is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


if __name__ == "__main__":
    # test_get_data_from_file()
    test_write_csv_excel(
        ['a,b,c,d', 'output.csv', 'None', 'False', 'None', 'NULL', 'None'])
