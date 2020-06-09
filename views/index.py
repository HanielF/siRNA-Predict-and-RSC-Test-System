import tornado.web
from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler
import os
import json
import uuid
import datetime
import time
import seqsPredictor
import rscTestor


# 视图类
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


# 显示临时界面
class TmpHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("tmp.html")


# 在新的websocket连接之后执行open函数
class PredictHandler(WebSocketHandler, RequestHandler):
    # 连接时的函数
    def open(self):
        print("ws Predict opened")

    # 当websocket连接关闭后调用，客户端主动的关闭
    def on_close(self):
        print("ws Predict closed")

    #  当客户端发送消息过来时调用
    def on_message(self, message):
        msg = json.loads(message)
        msgData = msg["seqs"][:-1].split(",") # list(str)
        print("msgData: ")
        print(msgData)
        resNum = seqsPredictor.predict(msgData)
        print("Predictions: ")
        print(resNum)
        self.write_message(json.dumps({
            'result': resNum
        }))

    # 判断请求源 对于符合条件的请求源允许连接
    def check_origin(self, origin):
        return True


# 视图类
class TestHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("testRSC.html")


# 用于构件测试
class TestRSCHandler(WebSocketHandler, RequestHandler):
    # 连接时的函数
    def open(self):
        print("ws TestRSC opened")

    # 当websocket连接关闭后调用，客户端主动的关闭
    def on_close(self):
        print("ws TestRSC closed")

    #  当客户端发送消息过来时调用
    def on_message(self, message):
        msg = json.loads(message)
        rscName = msg["packageName"]
        funcName = msg["funcName"]
        paraList = msg["paras"]

        print("rscName: ", rscName)
        print("funcName: ", funcName)
        print("paraList: ", paraList)
        res = rscTestor.rscFuncTest(rscName, funcName, paraList)
        print("res: ")
        print(res)
        self.write_message(json.dumps({
            'result': res
        }))

    # 判断请求源 对于符合条件的请求源允许连接
    def check_origin(self, origin):
        return True

