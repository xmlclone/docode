import zmq
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5555")

for i in range(3):
    message = socket.recv()
    logging.debug(f"recv: {message}")
    # 处理消息
    time.sleep(2)