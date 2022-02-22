import socket
import cv2 as cv
import pickle

import numpy
import numpy as np

"""Client
1.Open connection with socket;
2.Open connection with camera;
3.Read thread from camera;
4.Convert thread data to bytes;
5.Send data to server
...Profit
"""

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect with server
client_sock.connect(('127.0.0.1', 7071))

#############################
memory = []
#############################
# connect to cam
cap = cv.VideoCapture(0)
# if connect accepted, and don't give err , continue
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# trouble not found , continue
while True:
    # frame type -> numpy.ndarray , ret -> boolean
    # every sec we take matrix with color code in all points
    ret, frame = cap.read()
    a = pickle.dumps(frame)
    client_sock.sendto(a, ('127.0.0.1', 7071))
    # after convert need
