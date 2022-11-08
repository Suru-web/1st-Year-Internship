from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('1020x720')
window.title('GUI inside GUI')


def gui2():
    window.withdraw()
    window1 = tk.Toplevel()
    window1.geometry('1020x720')
    #window1.configure(bg='red')
    window1.title('Toyota Supra')
    load1 = Image.open('supra720p.jpeg')
    render1 = ImageTk.PhotoImage(load1)
    supra = tk.Label(window1, image=render1)
    supra.place(x=10, y=10)
    window1.mainloop()
    window1.withdraw()


b1 = tk.Button(window, text="Click to see Supra", command=gui2)
b1.place(x=450, y=360)
window.mainloop()


