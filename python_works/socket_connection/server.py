import socket

class Server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 7700
        self.socket_make(self.ip, self.port)


    def socket_make(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        self.s.bind((ip, port))
        self.s.listen(1)

        while True:
            print("Waiting Connection...")
            conn, addr = self.s.accept()
            print("Connected by {}".format(addr))
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.send(b"I received")

server = Server()