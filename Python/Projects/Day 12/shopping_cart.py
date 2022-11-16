import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import turtle

# create an empty list and push all tge items in the list after pressing add to cart button

window1 = tk.Tk()
window1.title("Shopping cart")
window1.geometry('1020x720')
welcome = tk.Label(window1, text="Welcome to PySu Shopping", font=40)
welcome.place(x=400, y=20)
category = tk.Label(window1, text='Choose the category', font=40)
category.place(x=425, y=100)

items = {'Shirt': 3000, 'Pant': 4000, 'Kurta': 6900, 'Mobile': 73000, 'Laptop': 114000, 'TV': 56900, 'Grinder': 2500,
         'Electric Stove': 2000, 'Water purifier': 6000}
list = []

coupan1 = 'DIWALI10'
coupan2 = 'WELCOME20'
coup_entered = 0


def cart():
    messagebox.askyesno('Cart..', 'Do you want to add item to cart?')


def backbut():
    window1.deiconify()


def cloth():
    window1.withdraw()
    # global window2
    window2 = tk.Toplevel()
    window2.geometry('1020x720')
    window2.title('Cloathing items')
    lable1 = tk.Label(window2, text='Shop Cloths', font=40)
    lable1.place(x=450, y=20)

    '''Shirt'''
    load4 = Image.open('Images/Cloth/shirt.png')
    ld4 = load4.resize((200, 200))
    render4 = ImageTk.PhotoImage(ld4)
    cl1 = tk.Label(window2, image=render4)
    cl1.place(x=78, y=250)

    def cart1():
        global shirt
        shirt = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            shirt = shirt + 1
            list.append('Shirt')

    cart1 = tk.Button(window2, text='Add to cart', command=cart1)
    cart1.place(x=130, y=600)
    shirt1 = tk.Label(window2, text='Shirt\nRs3000', font=30)
    shirt1.place(x=130, y=500)

    '''Pant'''
    load5 = Image.open('Images/Cloth/pant.png')
    ld5 = load5.resize((200, 200))
    render5 = ImageTk.PhotoImage(ld5)
    cl2 = tk.Label(window2, image=render5)
    cl2.place(x=390, y=250)

    def cart2():
        global pant
        pant = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            pant = pant + 1
            list.append('Pant')

    cart2 = tk.Button(window2, text='Add to cart', command=cart2)
    cart2.place(x=450, y=600)
    pant1 = tk.Label(window2, text='Pant\nRs4000', font=30)
    pant1.place(x=450, y=500)

    '''Kurta'''
    load6 = Image.open('Images/Cloth/kurta.png')
    ld6 = load6.resize((200, 200))
    render6 = ImageTk.PhotoImage(ld6)
    cl3 = tk.Label(window2, image=render6)
    cl3.place(x=680, y=250)

    def cart3():
        global kurta
        kurta = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            kurta = kurta + 1
            list.append('Kurta')

    cart3 = tk.Button(window2, text='Add to cart', command=cart3)
    cart3.place(x=750, y=600)
    kurta1 = tk.Label(window2, text='Kurta\nRs6900', font=30)
    kurta1.place(x=750, y=500)

    '''back button'''

    def backbut():
        window1.deiconify()
        window2.withdraw()

    bb = tk.Button(window2, text='Go back', command=backbut)
    bb.place(x=30, y=50)

    window2.mainloop()


def elec():
    window1.withdraw()
    # global window3
    window3 = tk.Toplevel()
    window3.geometry('1020x720')
    window3.title('Electronics')
    lablel = tk.Label(window3, text='Shop Electronics', font=40)
    lablel.place(x=450, y=20)

    '''Mobile'''
    load7 = Image.open('Images/Electronics/mobile.png')
    ld7 = load7.resize((280, 200))
    render7 = ImageTk.PhotoImage(ld7)
    el1 = tk.Label(window3, image=render7)
    el1.place(x=45, y=250)

    def cart4():
        global mobile
        mobile = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            mobile = mobile + 1
            list.append('Mobile')

    cart4 = tk.Button(window3, text='Add to cart', command=cart4)
    cart4.place(x=130, y=600)
    mob = tk.Label(window3, text='Pixel 7 Pro\nRs 73000', font=30)
    mob.place(x=130, y=500)

    '''laptop'''
    load8 = Image.open('Images/Electronics/laptop.png')
    ld8 = load8.resize((200, 200))
    render8 = ImageTk.PhotoImage(ld8)
    el2 = tk.Label(window3, image=render8)
    el2.place(x=390, y=250)

    def cart5():
        global laptop
        laptop = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            laptop = laptop + 1
            list.append('Laptop')

    cart5 = tk.Button(window3, text='Add to cart', command=cart5)
    cart5.place(x=450, y=600)
    lap = tk.Label(window3, text='Rog Strix\nRs 114000', font=30)
    lap.place(x=450, y=500)

    '''Tv'''
    load9 = Image.open('Images/Electronics/tv.png')
    ld9 = load9.resize((400, 400))
    render9 = ImageTk.PhotoImage(ld9)
    el3 = tk.Label(window3, image=render9)
    el3.place(x=600, y=150)

    def cart6():
        global tv
        tv = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            tv = tv + 1
            list.append('TV')

    cart6 = tk.Button(window3, text='Add to cart', command=cart6)
    cart6.place(x=750, y=600)
    tv = tk.Label(window3, text='Oneplus TV\nRs 56900', font=30)
    tv.place(x=750, y=500)

    '''back button'''

    def backbut():
        window1.deiconify()
        window3.withdraw()

    bb = tk.Button(window3, text='Go back', command=backbut)
    bb.place(x=30, y=50)

    window3.mainloop()


def kitch():
    window1.withdraw()
    # global window4
    window4 = tk.Toplevel()
    window4.geometry('1020x720')
    window4.title('Kitchen ware')
    lablel = tk.Label(window4, text='Shop Kitchen ware', font=40)
    lablel.place(x=450, y=20)

    '''Grinder'''
    load7 = Image.open('Images/Kitchen/GR-removebg-preview.png')
    ld7 = load7.resize((200, 200))
    render7 = ImageTk.PhotoImage(ld7)
    el1 = tk.Label(window4, image=render7)
    el1.place(x=45, y=250)

    def cart7():
        global grinder
        grinder = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            grinder = grinder + 1
            list.append('Grinder')

    cart7 = tk.Button(window4, text='Add to cart', command=cart7)
    cart7.place(x=130, y=600)
    mob = tk.Label(window4, text='Grinder\nRs 2500', font=30)
    mob.place(x=130, y=500)

    '''Electric Stove'''
    load8 = Image.open('Images/Kitchen/ES-removebg-preview.png')
    ld8 = load8.resize((200, 200))
    render8 = ImageTk.PhotoImage(ld8)
    el2 = tk.Label(window4, image=render8)
    el2.place(x=390, y=250)

    def cart8():
        global es
        es = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            es = es + 1
            list.append('Electric Stove')

    cart8 = tk.Button(window4, text='Add to cart', command=cart8)
    cart8.place(x=450, y=600)
    lap = tk.Label(window4, text='Electric stove\nRs 2000', font=30)
    lap.place(x=450, y=500)

    '''Water purifier'''
    load9 = Image.open('Images/Kitchen/WP-removebg-preview.png')
    ld9 = load9.resize((200, 200))
    render9 = ImageTk.PhotoImage(ld9)
    el3 = tk.Label(window4, image=render9)
    el3.place(x=690, y=250)

    def cart9():
        global wp
        wp = 0
        if messagebox.askyesno('Cart..', 'Add to cart?') == True:
            #wp = wp + 1
            list.append('Water purifier')

    cart9 = tk.Button(window4, text='Add to cart', command=cart9)
    cart9.place(x=750, y=600)
    tv = tk.Label(window4, text='Water Purifier\nRs 6000', font=30)
    tv.place(x=750, y=500)

    '''back button'''

    def backbut():
        window1.deiconify()
        window4.withdraw()

    bb = tk.Button(window4, text='Go back', command=backbut)
    bb.place(x=30, y=50)

    window4.mainloop()


'''Cloth Image and Lable'''
cloth_lable = tk.Button(window1, text='Cloth', command=cloth)
cloth_lable.place(x=120, y=500)
load1 = Image.open('Images/shirt_pant-removebg-preview.png')
ld1 = load1.resize((200, 200))
render1 = ImageTk.PhotoImage(ld1)
main_cloth = tk.Label(window1, image=render1)
main_cloth.place(x=40, y=250)

'''Electronics images'''
electronic_lable = tk.Button(window1, text='Electronics', command=elec)
electronic_lable.place(x=470, y=500)
load2 = Image.open('Images/ele-removebg-preview.png')
ld2 = load2.resize((200, 200))
render2 = ImageTk.PhotoImage(ld2)
main_ele = tk.Label(window1, image=render2)
main_ele.place(x=400, y=250)

'''kitchen images'''
kitchen_lable = tk.Button(window1, text='Kitchen Ware', command=kitch)
kitchen_lable.place(x=850, y=500)
load3 = Image.open('Images/Non-Stick-Kitchen-Accessories-removebg-preview.png')
ld3 = load3.resize((200, 200))
render3 = ImageTk.PhotoImage(ld3)
main_kit = tk.Label(window1, image=render3)
main_kit.place(x=780, y=250)

'''Bill Button'''


def item_in_cart():
    global allincart, total, i
    window1.withdraw()
    i, total = 0, 0
    allincart = 0
    allincart = list
    allincart.sort()
    window5 = tk.Toplevel()
    window5.geometry('1020x720')
    window5.title('Items in cart')
    lable1 = tk.Label(window5, text='Billing Section', font=40)
    lable1.pack(pady=10)
    incart = tk.Label(window5, text="Items in cart are :")
    incart.place(x=100, y=200)
    total_price = tk.Label(window5, text='Your total is : ')
    total_price.place(x=100, y=400)

    def cp_gui():

        window6 = tk.Toplevel()
        window6.geometry('700x300')
        window6.title('Coupan Page')
        cp_lab = tk.Label(window6, text='Enter Your coupan..')
        cp_lab.pack(pady=50)
        cp = tk.Entry(window6)
        cp.place(x=265, y=150)

        def get_coup():
            global coup_entered, total
            coup_entered = cp.get()
            cap_coup = coup_entered.upper()
            if cap_coup == coupan1:
                success = tk.Label(window6, text="Yay !! 10% discount applied on your total bill amount..🥳🥳", font=40)
                success.place(x=175, y=200)
            elif cap_coup == coupan2:
                success = tk.Label(window6, text="Yay!! 20% discount applied on your total bill amount..", font=40)
                success.place(x=175, y=200)
            else:
                fail = tk.Label(window6, text="Invalid Coupan!! Please try a different one next time..", font=40)
                fail.place(x=175, y=200)
            for i in items:
                for j in list:
                    if i == j:
                        total = total + items.get(i)
            total *= (0.9 if cap_coup == coupan1 else 0.8)
            tot_lab = tk.Label(window5, text=total)
            tot_lab.place(x=250, y=400)

        enter = tk.Button(window6, text='Enter', command=get_coup)
        enter.place(x=500, y=147)

        def continue_butt():
            window6.destroy()
            window5.deiconify()

        ok = tk.Button(window6, text="Continue", command=continue_butt)
        ok.place(x=300, y=250)

        window6.mainloop()

    if_cp_l = tk.Label(window5, text="Do you have a coupan?")
    if_cp_l.place(x=100, y=300)
    if_cp_b = tk.Button(window5, text='Yes', command=cp_gui)
    if_cp_b.place(x=300, y=297)

    def no():
        global total
        no_lab = tk.Label(window5, text='Ok, your Total price is listed below..')
        no_lab.place(x=470, y=300)
        for i in items:
            for j in list:
                if i == j:
                    total = total + items.get(i)
                    tot_lab = tk.Label(window5, text=total)
                    tot_lab.place(x=250, y=400)

    if_cp_b1 = tk.Button(window5, text='No', command=no)
    if_cp_b1.place(x=400, y=297)

    bill_lable = tk.Label(window5, text=",".join(allincart))
    bill_lable.place(x=220, y=200)
    '''back button'''

    def backbut():
        window1.deiconify()
        window5.withdraw()

    bb = tk.Button(window5, text='Go back', command=backbut)
    bb.place(x=30, y=50)
    window5.mainloop()


bill_bt = tk.Button(window1, text='Bill', command=lambda: [item_in_cart()])
bill_bt.place(x=700, y=600)

'''Quit button'''


def quit():
    window1.destroy()


quit_bt = tk.Button(window1, text='Quit', command=quit)
quit_bt.place(x=300, y=600)



'''Clear cart'''


clear_butt = tk.Button(window1, text="Clear Cart" )
clear_butt.place(x=470,y=600)




window1.mainloop()
