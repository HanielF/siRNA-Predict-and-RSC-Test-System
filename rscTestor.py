#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  rscTestor.py
 * @Time    :  2020/05/06 23:07:32
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  用于后端进行构件测试
'''
from spl_test import test_data_util
from spl_test import test_file_util
from spl_test import test_sirna_util
from spl_test import test_plot_util
from spl_test import test_train_util
from spl_test import test_model_util


def rscFuncTest(packageName=None, funcName=None, paras=None):
    '''
    Desc：
        调用spl_test中的测试函数进行构件测试，并返回结果
    Args：
        packageName: string  --  构件名
        funcName: string  --  函数名
        paras: string -- 参数列表
    Returns：
        res: string  --  结果
    '''
    res = ""
    try:
        if packageName is None or funcName is None:
            raise ValueError("function name could not be None")
        result = eval("test_" + packageName + ".test_" + funcName)(paras)
        res += str(result)
    except Exception as e:
        res += "Error: " + str(e)
    return res

