import zmq
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")

socket.setsockopt_string(zmq.SUBSCRIBE, "new")
while True:
    logging.debug(f"new recv: {socket.recv()}")
    time.sleep(2)