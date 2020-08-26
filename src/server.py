from socket import socket
from tkinter import Tk,font
from tkinter import *
from pickle import dumps,loads
from threading import Thread
x=socket()
frames=[]
con,addr=None,None
cnt=0
def connect_other_end():
    global con,addr
    x.bind(('127.0.0.1',5000))
    x.listen(1)
    print("Server started")
    con,addr=x.accept()
    print("Connected to other end!!")
    data=None

def send_message():
    global msg_box,con
    msg=msg_box.get()
    data=dumps(msg)
    con.sendall(data)
    update_chat_window(msg,'W')

def receive_message():
    while(True):
        if con!=None:
            data=con.recv(1024)
            message=loads(data)
            update_chat_window(message,'R')

root=Tk()
def update_chat_window(data,mode):
    global cnt
    if mode=='R':
        x=Frame(f1,bg='grey')
        Label(x, text=data, bg='lightblue',font=ff,justify=LEFT).pack()
        frames.append(x)
        x.pack()
        cnt+=1
    else:
        x = Frame(f1, bg='blue')
        Label(x, text=data, bg='white',font=ff).pack(side=RIGHT)
        frames.append(x)
        x.pack()
        cnt+=1

root.geometry('500x500')
root.title("Server side!!")
t=Thread(target=connect_other_end)
t2=Thread(target=receive_message)
t.start()
t2.start()
ff=font.Font(size=25)
f1=Frame(root,width=500,height=400,bg="lightyellow")
f2=Frame(root)
f1.pack()
f2.pack()
# use a canvase widget to make it look like a perfect chat app and only then uplaod that shit!
# okay??
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