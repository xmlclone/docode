import zmq
import time
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

context = zmq.Context()
# 也是可以接收多个客户端链接的，也就是demo1_req.py可以启动多个进行链接
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    logging.debug(f"Recv: {message=}")
    time.sleep(1)
    socket.send_string(f"You send: {message}")
