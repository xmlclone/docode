import zmq
import time
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

for i in range(10):
    socket.send_string(f"This is send {i}s.")
    message = socket.recv()
    logging.debug(f"client recv: {message}")