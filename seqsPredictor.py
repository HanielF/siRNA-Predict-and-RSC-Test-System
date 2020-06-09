import torch
import numpy as np
from spl_sirna import sirna_util
from spl_sirna import train_util
import sys

TRAINMODEL_FILE = 'f:\\Learning\\siRNA\\Projects\\Tornado_LSTM\\model\\model-2020-05-01_17_58_56.pt'

def predict(data):
    '''
    Desc：
        对输入的data使用训练好的model预测结果，并返回
    Args：
        data:list/ndarray(n, )   --  长度为21bp的碱基序列
    Returns：
        res:list  --  预测出的标准化沉默效率，保留2位小数
    '''
    # 异常处理
    if len(data) == 0:
        return -1
    if type(data) != list:
        return -1
    if type(data) == str:
        data = [data]

    # model = torch.load('model/model-2020-05-01_17_58_56.pt')
    sys.path.append("f:\\Learning\\siRNA\\Projects\\Tornado_LSTM")
    model = torch.load(TRAINMODEL_FILE)
    encoded_data = sirna_util.get_seq_motif(data, motif=1)[0]

    # 预测并处理精度
    predictions = train_util.predict_samples(model, encoded_data).tolist()
    for i, p in enumerate(predictions):
        predictions[i] = ("%.2f" % p)

    return predictions

if __name__ == "__main__":
    msg = ['CCUAAGAUAAUUCUGCGCCtg', 'UUUCCUAAGAUAAUUCUGCgc', 'UUUAGAGUCGUGAAGGUAAaa', 'CCGGCAAACCGAAGAACUUct', 'GCCCAUCAAAUGGGAAGUUgt', 'CGUGCGCAUGGUGGAAAAGaa']
    res = predict(msg)
    print(res)


