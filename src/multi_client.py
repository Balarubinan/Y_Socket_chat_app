from socket import socket
from tkinter import Tk, font
from tkinter import *
from pickle import dumps, loads
from threading import Thread
from threading import Thread

class CustomPlayer:
    def __init__(self,host,port):
        self.x=socket()
        self.cards=[]
        self.host=host
        self.port=port
        self.status=0
        # status variable determines i the player can play or not play now


    def connect_to_host(self):
        print("connect called!")
        self.x.connect((self.host,self.port))
        print("Connect Success!!")

    def start_recv(self):
        self.t=Thread(target=self.recve)
        self.t.start()

    def recve(self):
        while True:
            self.status=self.x.recv(1024)
            print("status:",self.status)
            if self.status==b'1':
                print("Got pinged!")
                self.active_function()

    def send_to_server(self,msg):
        self.x.sendall(b"To got hatt shit!")
        self.status=0
        # pass

    def active_function(self):
        move=input("Enter a move to play:")
        self.send_to_server(move)
        # get the input of the user from the UI in this part