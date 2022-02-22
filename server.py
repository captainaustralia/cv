import encodings
import socket
import cv2 as cv
import pickle
# create server socket
import numpy as np


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
# bind server socket with port 7071
serv_sock.bind(('', 7071))
serv_sock.listen(5)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_address = serv_sock.accept()
    print('Connected by', client_address)
    new_data = []
    while True:
        data = client_sock.recv(921765)  # lol size fixed 921754 always...
        data_numpy = pickle.loads(data)
        print(data_numpy)
        display = cv.cvtColor(data_numpy, cv.COLOR_BGR2GRAY)
        cv.imshow('Camera', display)
        cv.waitKey()
    client_sock.close()
