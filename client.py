import webbrowser
import socket

import config
def program():
    komm_s = socket.socket()
    adresse = ('127.0.0.1', config.PORT)
    komm_s.connect(adresse)

    while True:
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
