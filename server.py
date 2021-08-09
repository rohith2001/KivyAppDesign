import socket
import time
Headersize =10

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connnection from {address} has been established!")
    msg = "Welcome to the server!"
    msg= f"{len(msg):<{Headersize}}"+ msg

    clientsocket.send(bytes(msg,"utf-8"))
    while True:
        time.sleep(3)
        msg =f"The time is ! {time.time()}"
        msg= f'{len(msg):<{Headersize}}'+msg
        clientsocket.send(bytes(msg, "utf-8"))
