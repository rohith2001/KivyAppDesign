import socket
s=socket.socket()
host=socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print("waiting for 2 connections..")
conn,addr = s.accept()
print("Client one has connected..")
conn.send("welcome to the server".encode())
conn1,addr1 = s.accept()
print("Client two has connected")
conn1.send("welcome to the server".encode())
while True:
            message= input(str(">"))
            message= message.encode()
            conn.send(message )
            conn1.send(message)
            print("message sent...")
            recv_msg = conn.recv(1024)
            recv_msg1 = conn1.recv(1024)
            print("client",recv_msg1.decode())
            recv_msg = conn.recv(1024)
            print("client", recv_msg.decode())

            conn1.send(message)
