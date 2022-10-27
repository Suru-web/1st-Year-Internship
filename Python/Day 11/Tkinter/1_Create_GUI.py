from tkinter import *
import tkinter as tk

# Whatever styling/coding is to be done, it should be place before window.mainloop()
window = tk.Tk()  # Creates the window of GUI
window.geometry('1080x720')  # For window size
window.title("My GUI")  # For title on window screen
window.configure(bg='#565656')  # For background color

# text in the window
l1 = tk.Label(window, text="Hello", bg='red', foreground='yellow', font=('Joker', 40))
l1.place(x=470, y=10)


# button inside the window
def pri():
    global lable
    lable = tk.Button(window, text="Hello")
    lable.place(x=100,y=0)

b1 = tk.Button(window, text='Click me', bg='Pink', foreground='Black', font=("New Times Roman", 10), command=pri)    #Command does the function
b1.place(x=100, y=100)

def clear():
    lable.destroy()
b2=tk.Button(window,text="Clear",command=clear)
b2.place(x=700,y=700)

window.mainloop()
