import zmq
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.PUSH)
# 客户端也可以(应该)启动多个，会把消息均匀分配给不同的客户端
# 但默认情况下，服务端不知道客户端的处理情况，故下面的i会一直递增，客户端收到的消息也就是不定的
socket.bind("tcp://*:5555")

i = 0

while True:
    socket.send_string(str(i))
    i += 1