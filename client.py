import socket
import webbrowser

import config


def program():
    komm_s = socket.socket()
    adresse = ('127.0.0.1', config.PORT)

    test = True

    try:
        komm_s.connect(adresse)
    except ConnectionError:
        test = False

    while test:
        t = komm_s.recv(200)
        try:
            webbrowser.open(t.decode("utf-8"), new=0, autoraise=True)
        except Exception as e:
            print(e)


while True:
    try:
        program()
    except ConnectionResetError as e:
        print(e)
        program()
