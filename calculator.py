from tkinter import *

def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def back_space():
    e.delete(len(e.get())-1,END)

def button_add():
    first_number=e.get()
    global f_num
    global math 
    math="addition"
    f_num=float(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math== "addition":
        e.insert(0,f_num + int(second_number))
    if math== "subtraction":
        e.insert(0,f_num  - int(second_number))
    if math== "multiplication":
        e.insert(0,f_num * int(second_number))
    if math== "division":

        e.insert(0,f_num / int(second_number))
def button_sub():
    first_number=e.get()
    global f_num
    global math 
    math="subtraction"
    f_num=float(first_number)
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global f_num
    global math 
    math="multiplication"
    f_num=float(first_number)
    e.delete(0,END)
def button_div():
    first_number=e.get()
    global f_num
    global math 
    math="division"
    f_num=float(first_number)
    e.delete(0,END)


calculator=Tk()
e=Entry(calculator,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#create a button
b1=Button(calculator,text="1",padx=40,pady=20,command=lambda:click(1))
b2=Button(calculator,text="2",padx=40,pady=20,command=lambda:click(2))
b3=Button(calculator,text="3",padx=40,pady=20,command=lambda:click(3))
b4=Button(calculator,text="4",padx=40,pady=20,command=lambda:click(4))
b5=Button(calculator,text="5",padx=40,pady=20,command=lambda:click(5))
b6=Button(calculator,text="6",padx=40,pady=20,command=lambda:click(6))
b7=Button(calculator,text="7",padx=40,pady=20,command=lambda:click(7))
b8=Button(calculator,text="8",padx=40,pady=20,command=lambda:click(8))
b9=Button(calculator,text="9",padx=40,pady=20,command=lambda:click(9))
b0=Button(calculator,text="0",padx=40,pady=20,command=lambda:click(0))
ba=Button(calculator,text="+",padx=40,pady=20,command=button_add)
be=Button(calculator,text="=",padx=40,pady=20,command=button_equal)
bc=Button(calculator,text="clear",padx=40,pady=20,command=button_clear)
bs=Button(calculator,text="BACK",padx=40,pady=20,command=back_space)
button_sub=Button(calculator,text="-",padx=40,pady=20,command=button_sub)
button_mul=Button(calculator,text="*",padx=40,pady=20,command=button_mul)
button_div=Button(calculator,text="/",padx=40,pady=20,command=button_div)

#put the button on the screen
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
ba.grid(row=4,column=1)
button_sub.grid(row=4,column=2)


be.grid(row=5,column=2,columnspan=2)
bc.grid(row=5,column=0)
bs.grid(row=5,column=1)

button_mul.grid(row=6,column=0)
button_div.grid(row=6,column=1)
calculator.mainloop()
