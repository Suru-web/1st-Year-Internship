from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry('500x400')
window.configure(bg='black')

txt = tk.Entry(window)
txt.place(x=100, y=100)

def Enter():
    text=txt.get()
    global l1
    l1=tk.Label(window,text=text)
    l1.place(x=250,y=100)

b1=tk.Button(window,text='Enter',command=Enter)
b1.place(x=200,y=150)


def clear():
    l1.destroy()
    txt.delete(0,END)
b2=tk.Button(window,text="Clear",command=clear)
b2.place(x=200,y=250)
window.mainloop()
