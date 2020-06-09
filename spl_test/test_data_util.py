#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_data_util.py
 * @Time    :  2020/04/28 14:24:55
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试data_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import data_util
import numpy as np
import pandas as pd
import time
import torch.utils.data as tud


def test_char_remove(args):
    '''
    Desc：
        测试char_remove function 移除部分字符构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = ""
    try:
        print("Test data_util.char_remove Function")
        myStringList = []
        chrList = []
        if len(args) == 1:
            myStringList = args[0].split(",")
        elif len(args) == 2:
            myStringList = args[0].split(",")
            chrList = args[1].split(",")
        else:
            raise ValueError("参数个数错误!")

        print("data:", myStringList)
        print("chr_list:", chrList)
        resList = data_util.char_remove(myStringList, chrList)
        testRes += str(resList)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: char_remove {}".format(
            'is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = "Return: " + testRes + "\n" + logString
        print("End Test")
    return testRes


def test_cal_time(args):
    '''
    Desc：
        测试calculate time function 计算时间
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: "
    try:
        st = float(args[0])
        end = float(args[1])
        h, m, s = data_util.cal_time(st, end)
        testRes = testRes + str(h) + "h:" + str(m) + "m:" + str(s) + "s"
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: cal_time {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_copy_part_of_data(args):
    '''
    Desc：
        测试copy_part_of_data function 对文本进行部分复制增多
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        x = args[0].split(",")
        x = [float(i) for i in x]
        y = args[1].split(",")
        y = [float(i) for i in y]
        yrange = args[2].split(",")
        yrange = tuple([float(i) for i in yrange])
        print("x:", x, "y:", y, "range:", yrange)
        cptime = int(args[3])
        res_x, res_y = data_util.copy_part_of_data(x,
                                                   y,
                                                   yrange=yrange,
                                                   copytimes=cptime)
        testRes += "xdata: " + str(res_x) + "\nydata: " + str(res_y)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: copy_part_of_data {}".format(
            'is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_truncate_part_of_data(args):
    '''
    Desc：
        测试truncate_part_of_data function 截断部分数据
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        x = args[0].split(",")
        # x = [float(i) for i in x]
        y = args[1].split(",")
        y = [float(i) for i in y]
        yrange = args[2].split(",")
        yrange = tuple([float(i) for i in yrange])
        print("x:", x, "y:", y, "range:", yrange)
        res_x, res_y = data_util.truncate_part_of_data(x, y, yrange=yrange)
        testRes += "xdata: " + str(res_x) + "\nydata: " + str(res_y)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: truncate_part_of_data {}".format(
            'is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_get_sample_freq(args):
    '''
    Desc：
        测试get_sample_freq function 统计频次
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        data = args[0].split(',')
        data = [float(i) for i in data]
        f = data_util.get_sample_freq(data)
        x = f[:, 0].tolist()
        y = f[:, 1].tolist()
        testRes += "data: " + str(x) + "\nfreq: " + str(y)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: get_sample_freq {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_standardize_data(args):
    '''
    Desc：
        测试standardize_data function 通用的标准化构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        x = args[0].split(",")
        x = [float(i) for i in x]
        axis = int(args[1])
        std = int(args[2]) #因为界面里只能输入一维的，所以std有的话也只是一个数
        mean = int(args[3])
        res = data_util.standardize_data(x, axis, std, mean)
        testRes += "standardized data: " + str(res)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: standardize_data {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_normalize_data(args):
    '''
    Desc：
        测试normlize_data function 通用的归一化构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        x = args[0].split(",")
        x = [float(i) for i in x]
        ax = int(args[1])
        y = data_util.normalize_data(x, ax)
        testRes += "normalized data: " + str(y)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: normlize_data {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_split_dataset(args):
    '''
    Desc：
        测试 split_dataset function 通用的分割数据集构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        x = args[0].split(",")
        y = args[1].split(",")
        valid_size = float(args[2])
        test_size = float(args[3])
        shuffle = True if args[4] == 'True' or args[4] == '1' else False
        random_state = int(args[5])

        x_train, x_valid, x_test, y_train, y_valid, y_test = data_util.split_dataset(
            x, y, valid_size, test_size, shuffle, random_state)
        testRes += "x_train: {}\nx_valid: {}\nx_test: {}\ny_train: {}\ny_valid: {}\ny_test: {}".format(x_train, x_valid, x_test, y_train, y_valid, y_test)
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: split_dataset {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_EmbeddedTextDataset(args):
    '''
    Desc：
        测试 EmbeddedTextDataset function 通用的文本处理Dataset封装
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    testRes = "Return: \n"
    try:
        xdata = args[0].split(",")
        ydata = args[1].split(",")
        ydata = [float(i) for i in ydata]

        word_to_idx = args[2].split(",") if args[2]!='None' else None
        if word_to_idx is not None:
            k = [x.split(":")[0] for x in word_to_idx]
            v = [int(x.split(":")[1]) for x in word_to_idx]
            word_to_idx = dict(zip(k, v))
        idx_to_word = args[3].split(",") if args[3]!='None' else None

        max_vocab_size = int(args[4]) if args[4]!='None' else None
        encode_label = True if args[5]=="True" else False

        resDataset = data_util.EmbeddedTextDataset(xdata, ydata, word_to_idx, idx_to_word, max_vocab_size, encode_label)
        testRes += "resDataset: " + str(resDataset)
    except Exception as e:
        flag = False
        testRes += str(e)
    finally:
        logString = "RSC: EmbeddedTextDataet {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


if __name__ == "__main__":
    # test_char_remove()
    test_cal_time()
    # test_copy_part_of_data()
    # test_truncate_part_of_data()
    # test_get_sample_freq()
    # test_standardize_data()
    # test_normlize_data()
    # test_split_dataset()
    # test_EmbeddedTextDataset()