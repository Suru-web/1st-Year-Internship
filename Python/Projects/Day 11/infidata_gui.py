from tkinter import *
import tkinter as tk

window = tk.Tk()
l2=0
res=0
window.geometry('1920x1080')
window.title("Infidata")
window.configure(bg='#040C0E')

# Employee Details
l1 = tk.Label(window, text='Employee Details', font=('Garamond', 40), bg='#040C0E', foreground='#FBF8F3')
l1.place(x=580  , y=20)

# Name
name = tk.Label(window, text='Name : ', font=('Garamond',30), bg='#040C0E', foreground='#FBF8F3')
name.place(x=330, y=200)

# Entry box
name1 = tk.Entry(window,bg="#1B3239",foreground="#C1C1C1",font=("Garamond",27),width=30)
name1.place(x=500, y=205)


# Entry button
def search():
    global l2
    global res
    global l3
    res = name1.get()
    if (res == 'Anya'):
        l2 = tk.Label(window, text= '\tName : Anya\n'
                                    '\tBlood Group : B+\n'
                                    '\tDesignation : Design Engineer\n'
                                    '\tCompany : Infidata', font=('Garamond',30), bg='#040C0E', foreground='#FBF8F3')
        l2.place(x=350, y=300)
    else:
        l3=tk.Label(window, text="Can't find you in our company database, Sorry",font=('Garamond',35), bg='#040C0E', foreground='#FBF8F3')
        l3.place(x=330,y=300)


eb = tk.Button(window, text="Search", font=('Georgia', 17), bg='#DCA36A', foreground='#040C0E', command=search)
eb.place(x=1100, y=203.5)


#Clear button
def clear():
    name1.delete(0,END)
    if(res=='Anya'):
        l2.destroy()
    else:
        l3.destroy()

cb=tk.Button(window,text="Clear",font=('Georgia', 17), bg='#DCA36A', foreground='#040C0E',command=clear)
cb.place(x=718,y=600)



window.mainloop()
