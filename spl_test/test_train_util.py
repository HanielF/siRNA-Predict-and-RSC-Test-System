#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_train_util.py
 * @Time    :  2020/04/28 16:41:05
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试train_util构件
'''

import sys
sys.path.append("../spl_sirna")
sys.path.append('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM')
from spl_sirna import train_util
from spl_sirna import model_util
from spl_sirna import data_util
from spl_sirna import file_util
from spl_sirna import sirna_util
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data as tud
import torch.optim as optim

model = model_util.EmbeddingLSTMModel(5,
                                      100,
                                      100,
                                      1,
                                      1,
                                      False,
                                      dropout=0.5,
                                      avg_hidden=False,
                                      device='cuda')
model = model.to('cuda')


def test_train(args):
    '''
    Desc：
        测试train_util.train构件
    '''
    flag = True
    testRes = "Return: \n"
    try:
        xname = args[0]
        yname = args[1]
        valid_size = float(args[2])
        test_size = float(args[3])
        optimizer = args[4]
        learning_rate = args[5]
        criterion = args[6]
        epochs = int(args[7])
        seq, seq_freq = file_util.get_data_from_file('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test\\input.csv',
                                                        xname,
                                                        yname,
                                                        upper=True)
        x_train, x_valid, x_test, y_train, y_valid, y_test = data_util.split_dataset(
            seq, seq_freq, valid_size, test_size)
        idx_to_word, word_to_idx = sirna_util.get_idx_base()
        train_data = data_util.EmbeddedTextDataset(x_train, y_train,
                                                    word_to_idx, idx_to_word)
        train_dataloader = tud.DataLoader(train_data,
                                            batch_size=10,
                                            shuffle=True,
                                            num_workers=0)
        optimizer = eval("optim." + optimizer + "(model.parameters(), lr=" +
                            learning_rate + ")")
        criterion = eval("nn." + criterion + "().to('cuda')")
        train_epoch_loss = []
        for epoch in range(epochs):
            train_loss = train_util.train(model,
                                            train_dataloader,
                                            optimizer,
                                            criterion,
                                            device='cuda')
            train_epoch_loss.append(train_loss)
        testRes += "train loss: {}".format(str(train_epoch_loss))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: train{}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes


def test_evaluate(args):
    '''
    Desc：
        测试train_util.evaluate构件
    '''
    flag = True
    testRes = "Return: \n"
    try:
        xname = args[0]
        yname = args[1]
        valid_size = float(args[2])
        test_size = float(args[3])
        optimizer = args[4]
        learning_rate = args[5]
        criterion = args[6]
        epochs = int(args[7])
        pcc = True if args[8] == 'True' else False
        acc = True if args[9] == 'True' else False
        seq, seq_freq = file_util.get_data_from_file('f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\spl_test\\input.csv',
                                                        xname,
                                                        yname,
                                                        upper=True)
        x_train, x_valid, x_test, y_train, y_valid, y_test = data_util.split_dataset(
            seq, seq_freq, valid_size, test_size)
        idx_to_word, word_to_idx = sirna_util.get_idx_base()
        valid_data = data_util.EmbeddedTextDataset(x_valid, y_valid,
                                                    word_to_idx, idx_to_word)
        valid_dataloader = tud.DataLoader(valid_data,
                                            batch_size=10,
                                            shuffle=True,
                                            num_workers=0)
        criterion = eval("nn." + criterion + "().to('cuda')")
        valid_epoch_loss = []
        valid_r = []
        valid_acc = []
        for epoch in range(epochs):
            valid_res = train_util.evaluate(model,
                                                valid_dataloader,
                                                criterion,
                                                device='cuda',
                                                pcc=pcc,
                                                acc=acc)
            valid_epoch_loss.append(valid_res[0])
            if pcc:
                valid_r.append(valid_res[1])
            if acc:
                valid_acc.append(valid_res[2])

        testRes += "evaluate loss: {}\n pcc: {}\n acc: {}".format(str(valid_epoch_loss), str(valid_r), str(valid_acc))
    except Exception as e:
        testRes += str(e)
        flag = False
    finally:
        logString = "RSC: evaluate {}".format('is OK' if flag else 'has bugs')
        print("logString: ", logString)
        testRes = testRes + "\n" + logString
        print("End Test")
    return testRes



if __name__ == "__main__":
    args = ["Guide strand", "Normalized inhibitory activity", "0.1", "0.1", "Adam", "0.001", "MSELoss", "MSELoss", "Guide strand", "Normalized inhibitory activity", "0.1", "0.1", "Adam", "0.001", "MSELoss"]
    test_train(args)
