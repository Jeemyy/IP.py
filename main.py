from tkinter import*
import socket
def ip():
    ip=socket.gethostbyname(e1.get())
    l3=Label(text=ip,bg="#7B241C",fg='#ffffff',font=("arial",20))
    l3.place(x=120,y=210)
win=Tk()
win.geometry("400x400")
win.maxsize(400,400)
win.minsize(400,400)
win.title("IP")
win.config(bg='#7B241C')
l1=Label(text='IP',bg='#7B241C',font=('arial',25), fg="#2E86C1")
l1.place(x=180,y=60)
l2=Label(text='URL',font=("arial",10),bg="#7B241C",fg="#000000")
l2.place(x=80,y=120)
e1=Entry(font=("arial",13))
e1.place(x=120,y=120)
b1=Button(text="GET",font=("arial",10),bg="#C0392B",command=ip)
b1.place(x=180,y=160)
b2=Button(text="EXIT",bg="#535353",fg="#ffffff",width=10,command=exit)
b2.place(x=0,y=374)
win.mainloop()