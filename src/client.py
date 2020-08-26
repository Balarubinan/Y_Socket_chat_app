from socket import socket
from tkinter import Tk,font
from tkinter import *
from pickle import dumps,loads
from threading import Thread
x=socket()
frames=[]
connected=False
exited=False
cnt=0

def connect_other_end():
    global connected
    print("Called from client1")
    x.connect(('127.0.0.1',5000))
    connected=True
    print("Connect Success!!")


def send_message():
    global msg_box
    msg=msg_box.get()
    data=dumps(msg)
    x.sendall(data)
    update_chat_window(msg,'W')

def receive_message():
    global connected
    while(True):
        if connected:
            data=x.recv(1024)
            message=loads(data)
            update_chat_window(message,'R')
        if exited:
            break

root=Tk()
def update_chat_window(data,mode):
    global cnt
    if mode=='R':
        x=Frame(f1,bg='grey')
        Label(x, text=data,bg='lightblue').grid(row=cnt,column=0)
        frames.append(x)
        x.pack()
        cnt+=1
    else:
        x = Frame(f1, bg='blue')
        Label(x,text=data,bg='white').grid(row=cnt,column=1)
        frames.append(x)
        x.pack()
        cnt+=1

root.geometry('500x500')
root.title("Client Chat!")
t=Thread(target=connect_other_end)
t2=Thread(target=receive_message)
t.start()
t2.start()
ff=font.Font(size=25)
f1=Frame(root,width=500,height=400,bg="lightyellow")
f2=Frame(root)
f1.pack()
f2.pack()
# scroll=Scrollbar(f1)
# scroll.pack(side=RIGHT,fill=Y)
# t=Text(f1,yscrollcommand=scroll.set,wrap=NONE)
# t.pack(side=TOP,fill=X)
# scroll.config(command=t.yview)
msg_box=Entry(f2,width=400,font=ff)
msg_box.pack()
send_btn=Button(f2,text="Send",font=ff,command=send_message)
send_btn.pack()
root.mainloop()