#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_sirna_util.py
 * @Time    :  2020/04/28 16:31:15
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试sirna_util构件
'''

import sys
sys.path.append('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM')
from spl_sirna import sirna_util
import numpy as np


def test_get_idx_base(args):
    '''
    Desc：
        测试get_idx_base function 获取idx_to_word和word_to_idx
    '''
    flag = True
    testRes = "Return: \n"
    try:
        motif = args[0].split(",")
        motif = [int(x) for x in motif]
        idx_to_base, base_to_idx = sirna_util.get_idx_base(motif)
        testRes += "idx_to_base: {}\nbase_to_idx: {}".format(str(idx_to_base), str(base_to_idx))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: get_idx_base {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_idx_to_seq(args):
    '''
    Desc：
        测试idx_to_seq function 获取idx_to_word和word_to_idx
    '''
    flag = True
    testRes = "Return: \n"
    try:
        seqs = args[0].split(',')
        seqs = [[int(w) for w in seq] for seq in seqs]
        motif = args[1].split(",")
        motif = [int(x) for x in motif]
        s = sirna_util.idx_to_seq(seqs, motif)
        testRes += "seqs: {}".format(str(s))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: idx_to_seq {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_get_seq_motif(args):
    '''
    Desc：
        测试get_seq_motif 获取序列的各个motif的编码
    '''
    flag = True
    testRes = "Return: \n"
    try:
        seqs = args[0].split(',')
        motif = args[1].split(',')
        motif = [int(x) for x in motif]
        m = sirna_util.get_seq_motif(seqs, motif)
        testRes += "seq_motif:\n{}".format(str(m))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: get_seq_motif {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_filter_sirna(args):
    '''
    Desc：
        测试filter_sirna 对序列进行过滤，筛选出只包含A/a, G/g, U/u, C/c, T/t的长度为21的部分
    '''
    flag = True
    testRes = "Return: \n"
    try:
        seqs = args[0].split(',')
        b = sirna_util.filter_sirna(seqs)
        testRes += "sirna seqs: \n {}".format(str(b))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: filter_sirna {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


if __name__ == "__main__":
    print(sys.path)
    args = ['augct,aua', '1']
    seqs = args[0].split(',')
    motif = args[1].split(',')
    motif = [int(x) for x in motif]
    m = sirna_util.get_seq_motif(seqs, motif)
    # test_get_seq_motif(args)