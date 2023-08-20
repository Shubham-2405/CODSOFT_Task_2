# Task 2 : Random Password Generator

# importing libraries
from tkinter import *
import random

flag = 0

# function to display messages
def display():
    if txt2.get() <= 0 or txt2.get()=='':
        txt4.set("Enter Valid Password Length")
    else:
        txt4.set('Password Generated Successfully!')

# function to generate random password
def genpswd():
    pswd = ''
    x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'
    for i in range(txt2.get()):
        if txt2.get() <= 0 or txt2.get()=='':
            break
        else:
            pswd = pswd + random.choice(x)
    txt3.set(pswd)
    display()

# function to check whether password is already generated or not
def check():
    global flag
    flag = flag + 1
    if flag>1:
        txt4.set("Password already generated.")
        return 0 
    else:
        genpswd()

# function to reject the generated password
def reject():
    txt2.set('')
    txt3.set('')
    txt4.set("Enter Password Length Again.")

# function to accept the generated password
def accept():
    txt4.set("Password Saved Successfully!")
    txt1.set('')
    txt2.set('')
    txt3.set('')  
    while True:
        genpswd()  

# Creating main window
win = Tk()
win.title("Password Generator")
win.geometry("700x465")
win.minsize(300,200)
win.maxsize(900,700)
win.iconbitmap("password_icon_183742.ico")


mainframe = Frame(win, width=670, height=435, bg="#CD950C",)
mainframe.place(x=15,y = 15)
mainframe.propagate(0)
mainframe1 = Frame(win, width=640, height=405, bg="#CDC8B1",)
mainframe1.place(x=30,y = 30)
mainframe1.propagate(0)

lb1 = Label(text="Random Password Generator", font = ("Lucida Bright", 23,'underline'),bg="#CDC8B1")
lb1.place(x = 132, y = 55)

lb2 = Label(text="Name                      :", font = ("Calisto MT", 18,),bg="#CDC8B1")
lb2.place(x = 100, y = 130)

txt1 = StringVar()
Ent1 = Entry(mainframe1,justify="center", font=("Georgia",14), textvariable=txt1, width=21)
Ent1.place(x = 310, y = 105)

lb3 = Label(text="Password Length   :", font = ("Calisto MT", 18,),bg="#CDC8B1")
lb3.place(x = 100, y = 190)

txt2 = IntVar()
Ent2 = Entry(mainframe1,justify="center", font=("Georgia",14), textvariable=txt2, width=21)
Ent2.place(x = 310, y = 165)

lb4 = Label(text="Password                :", font = ("Calisto MT", 18,),bg="#CDC8B1")
lb4.place(x = 100, y = 250)

txt3 = StringVar()
lb6 = Label(mainframe1,justify="center", font=("Georgia",14), textvariable=txt3,bg = 'white', width = 23, relief='raised')
lb6.place(x = 310, y = 225)

Btn1 = Button(text="Generate Password", font=("Arial", 15), justify="center", relief="raised",command=check)
Btn1.place(x = 250, y = 310)

Btn2 = Button(text="Accept", font=("Arial", 15), justify="center", relief="raised",command=accept)
Btn2.place(x = 120, y = 370)

Btn3 = Button(text="Reject", font=("Arial", 15), justify="center", relief="raised", command=reject)
Btn3.place(x = 500, y = 370)

txt4 = StringVar()
lb5 = Label(textvariable=txt4, font=("Arial", 12),bg = "#CDC8B1",justify="center")
lb5.place(x = 223, y = 377 )


win.mainloop()