#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_model_util.py
 * @Time    :  2020/04/28 15:44:23
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试model_util构件
'''

import sys
sys.path.append("../spl_sirna")
sys.path.append('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM')
from spl_sirna import data_util
from spl_sirna import model_util


def test_Word2vecModel(args):
    '''
    Desc：
        测试通用的word2vec模型
    '''
    flag = True
    testRes = "Return: \n"
    try:
        vocab_size = int(args[0])
        embed_size = int(args[1])
        model = model_util.Word2vecModel(vocab_size, embed_size)
        testRes += "Word2vecModel: \n{}".format(str(model.modules))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: Word2vecModel {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_MultiMotifLSTMModel(args):
    '''
    Desc：
        测试MultiMotifLSTMModel模型
    '''
    flag = True
    testRes = "Return: \n"
    try:
        vocab_size = args[0].split(',')
        vocab_size = [int(x) for x in vocab_size]
        embedding_dim = args[1].split(',')
        embedding_dim = [int(x) for x in embedding_dim]
        hidden_dim = int(args[2])
        output_dim = int(args[3])
        n_layers = int(args[4])
        bidirectional = True if args[5] == 'True' else False
        dropout = float(args[6])
        avg_hidden = True if args[7] == 'True' else False
        motif = args[8].split(",")
        model = model_util.MultiMotifLSTMModel(vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, bidirectional, dropout, avg_hidden, motif,False,'cuda')
        testRes += "MultiMotifLSTMModel: \n{}".format(str(model.modules))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: MultiMotifLSTMModel {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_EmbeddingLSTMModel(args):
    '''
    Desc：
        测试EmbeddingLSTMModel模型
    '''
    flag = True
    testRes = "Return: \n"
    try:
        vocab_size = int(args[0])
        embedding_dim = int(args[1])
        hidden_dim = int(args[2])
        output_dim = int(args[3])
        n_layers = int(args[4])
        bidirectional = True if args[5] == 'True' else False
        dropout = float(args[6])
        avg_hidden = True if args[7] == 'True' else False
        model = model_util.EmbeddingLSTMModel(vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, bidirectional, dropout)
        testRes += "EmbeddingLSTMModel: \n{}".format(str(model.modules))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: EmbeddingLSTMModel {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_count_parameters(args):
    '''
    Desc：
        测试count_parameters函数
    '''
    flag = True
    testRes = "Return: \n"
    try:
        vocab_size = int(args[0])
        embed_size = int(args[1])
        model = model_util.Word2vecModel(vocab_size, embed_size)
        para = model_util.count_parameters(model)
        testRes += "modules: \n{}\nparameters: {}".format(str(model.modules), str(para))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: count_parameters {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


if __name__ == "__main__":
    args = ["10,10,10", "10,10,10", "10", "10", "1", "False", "0.5", "False", "1,2,3"]
    test_MultiMotifLSTMModel(args)