import config


import socket

import threading


def sendeStr(komm_s, datenStr):
    datenBytes = bytes(datenStr, 'utf-8')
    komm_s.sendall(datenBytes)

    #sendeTrennByte(komm_s)


# Sendet das TrennByte
# daran erkennt der EmpfÃ¤nger, dass der Sender zunÃ¤chst keine weiteren Daten sendet
def sendeTrennByte(komm_s):
    trennByte = bytes([0])
    komm_s.sendall(trennByte)


# Hauptprogramm
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_s.bind(("0.0.0.0", config.PORT))
server_s.listen(20)

clients = []


def accept():
    global clients

    while True:
        clients += [server_s.accept()]


threading.Thread(target=accept).start()


def sendLink(link: str):
    global clients

    i = 0

    for komm_s, addr in clients:
        try:
            sendeStr(komm_s, link)

        except ConnectionResetError as e:
            print(e)
            del clients[i]
        i += 1

while True:
    sendLink(input("Link: "))