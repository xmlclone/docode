import zmq
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


while True:
    # 主题用 name: message 消息格式，客户端就可以用name作为过滤器
    socket.send_string("new: this is new message.")
    socket.send_string("old: this is old message.")