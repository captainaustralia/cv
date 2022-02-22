import encodings
import socket
import cv2 as cv
import pickle
# create server socket
import numpy as np


def bts_to_img(bts):
    buff = np.fromstring(bts, np.uint8)
    buff = buff.reshape(1, -1)
    img = cv.imdecode(buff, cv.IMREAD_COLOR)
    return img


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
# bind server socket with port 9595
serv_sock.bind(('', 7071))
serv_sock.listen(5)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_address = serv_sock.accept()
    print('Connected by', client_address)
    new_data = []
    while True:

        data = client_sock.recv(4096)
        new_data.append(data)
        print(new_data)


    client_sock.close()
