import socket

s = socket.socket()
print("Socket is created")

s.bind(('localhost',9999))

s.listen(3)
print("Connection is waiting...")


while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print("Connect with : ",address,name)

    c.send(bytes("Welcome to MyChannel",'utf-8'))
    c.close()