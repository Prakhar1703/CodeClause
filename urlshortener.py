import pyshorteners
from tkinter import *
win=Tk()
win.geometry("400x270")
win.configure(bg="light blue")
def shortener():
    url=box.get()
    s=pyshorteners.Shortener().tinyurl.short(url)
    box2.insert(END,s)
Label(win,text="Enter the URL to shorten",font="Arial 20 bold",fg="black").pack(fill="x")
box=Entry(win,font="15",bd=3,width=30)
box.pack(pady=20)
Button(win,text="Submit",bg="black",font="arial 12 bold",fg="white",command=shortener).pack()
Label(win,text="URL After Shortening",font="Arial 16 bold").pack(fill="x",pady=20)
box2= Entry(win,font="20",bd=3,width=30)
box2.pack(pady=20)
mainloop()
