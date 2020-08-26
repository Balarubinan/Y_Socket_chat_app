from socket import socket


# this is a server that  is going to handle multiple incoming connections!

# clients=int(input("enter number of max clients: "))

class CustomServer:
    def __init__(self, host, port, mx_clients):
        self.ser_socket = socket()
        self.ser_socket.bind((host, port))
        print("Socket intialised ", (host, port))
        self.mx_clients = mx_clients

    def start_server(self):
        self.ser_socket.listen(self.mx_clients)
        self.clients = []
        print("Ready and waiting for connections!")
        while len(self.clients)<self.mx_clients:
            con, addr = self.ser_socket.accept()
            self.clients.append((con, addr))
            print("A Player joined!!", (con, addr))
        print("All player have joined!")

    def ping_socket(self, index):
        ''' The idea of this function is to alert the specific client and get their move'''
        con, addr = self.clients[index]
        con.sendall(b'1')
        # 1 is my own code of saying "it's your move"
        print("Waiting for move for player")
        # make a broadcast wait message to all players here
        move = con.recv(1024)
        print("player played ",move)
        # processs move here

    def broadcast_to_all(self,msg):
        '''This fucntion call send on all the clients we have so far'''
        for con,addr in self.clients:
            con.sendall(b'0')
            #  '0' is my own code of saying "wait" to all the clients we can use any symbol
            # the idea is to minimise the number of characters used so as to reduce data usage

server_1=CustomServer('127.0.0.1',5000,1)
# player1=CustomPlayer('127.0.0.1',5000)
server_1.start_server()
if len(server_1.clients)>0:
    server_1.ping_socket(0)










