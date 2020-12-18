from pytube import YouTube

from tkinter import *

root = Tk()


root.geometry("300x400")
root.title("You Tube Video Download")

def youtube():
    a = var.get()  #https://www.youtube.com/watch?v=iCvmsMzlF7o
    ytvideo = YouTube(a).streams.filter(file_extension="mp4").order_by('resolution').desc().first()
    
    ytvideo.download(r"F:\pooja\letsupgrade")
    
    
    print("Entry Box",a)
l1 = Label(text="Enter YouTube Video Link", fg="Red",font=("bold",20))
l1.place(x=30,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=40,y=80)

b1 = Button(root,text = "Download",command=youtube,bg="Green",width=25,fg="White")
b1.place(x=80,y=120)

root.mainloop()