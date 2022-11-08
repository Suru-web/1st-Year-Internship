from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

window = tk.Tk()
window.geometry('500x400')
window.configure(bg='black')


#CODE TO LOAD IMAGE

load=Image.open('toyota-supra-FT1-NAIAS-designboomth.jpg')
render=ImageTk.PhotoImage(load)
img=tk.Label(window, image=render)
img.place(x=0,y=0)


window.mainloop()
