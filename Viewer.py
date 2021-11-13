import cv2
import zmq
import base64
import numpy as np
from threading import *
from time import sleep
def v():
	context = zmq.Context()
	footage_socket = context.socket(zmq.SUB)
	footage_socket.bind('tcp://192.168.1.8:8000')
	footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

	while True:
		try:
			frame = footage_socket.recv_string()
			img = base64.b64decode(frame)
			npimg = np.fromstring(img, dtype=np.uint8)
			source = cv2.imdecode(npimg, 1)
			print("stream")
			cv2.imshow("Stream", source)	
			cv2.waitKey(1)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		except KeyboardInterrupt:
			cv2.destroyAllWindows()
			break
def h():
	try:
		while True:
			print("hello")
	except KeyboardInterrupt:
		exit()
t1=Thread(target=v)
t2=Thread(target=h)
t1.start()
t2.start()
