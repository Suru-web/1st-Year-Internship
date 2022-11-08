from tkinter import *
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x400')
window.configure(bg='black')

txt = tk.Entry(window)
txt.place(x=100, y=100)


def Enter():
    text = txt.get()
    global l1
    l1 = tk.Label(window, text=text)
    l1.place(x=250, y=100)


b1 = tk.Button(window, text='Enter', command=Enter)
b1.place(x=200, y=150)


def clear():
    l1.destroy()
    txt.delete(0, END)


def quit():
    if messagebox.askyesno('Quit?', 'Do you want to quit?'):                 #Message box is shown to quit the window
        window.destroy()


b2 = tk.Button(window, text="Clear", command=clear)
b2.place(x=200, y=250)
b3 = tk.Button(window, text="Quit", command=quit)
b3.place(x=300, y=300)
window.mainloop()
