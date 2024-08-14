import zmq
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")

socket.setsockopt_string(zmq.SUBSCRIBE, "old")
while True:
    logging.debug(f"sub recv: {socket.recv()}")
    time.sleep(2)