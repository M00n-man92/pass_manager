from tkinter import messagebox
from tkinter import *
from encrpt_ps import Encript
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
def piano():
    websiite=input_one.get()
    emailing=input_two.get()
    passing=input_three.get()
    if websiite=="" or emailing=="" or passing=="":
        validate=messagebox.askretrycancel(title="Error",message="be sure to fill the boxes")
        if validate:
            print("hillside")
        else:
            input_one.delete(0,END)
            
            input_three.delete(0,END) 
    elif len(passing)<8:
        validate=messagebox.askretrycancel(title="Error",message="password can't be less than 8")
        if validate:
            print("hillside")
        else:
            input_one.delete(0,END)
            
            input_three.delete(0,END)            
            


    else:    
        check=messagebox.askokcancel(title=websiite,message=f"do you wanna save {passing} as a password for {websiite} ")
        if check:
            with open('./data.txt',mode="a",) as file:
                file.write(f"{websiite} | {emailing} | {passing}\n")
            input_one.delete(0,END)
            
            input_three.delete(0,END)
            input_one.focus()

def turn_it_up_a_noch():
    gen_password=Encript.start()
    input_three.insert(0,gen_password)


image=PhotoImage(file='./pass_manager/logo.png')
canvas=Canvas(width=200,height=200)
canvas.create_image(102,100,image=image)
canvas.grid(column=1,row=0)
label_one=Label(text="Website :")
label_one.grid(column=0,row=1)
label_two=Label(text="Username/Email :")
label_two.grid(column=0,row=2)
label_three=Label(text="Password :")
label_three.grid(column=0,row=3)
butt=Button(text="ADD",width=38,command=piano)
butt.grid(column=1,row=4,columnspan=2)
input_one=Entry(width=45)
input_one.grid(column=1,row=1,columnspan=2)
input_one.focus()
input_two=Entry(width=45)
input_two.grid(column=1,row=2,columnspan=2)
input_two.insert(0,"azraelnumb00@gmail.com")
print(input_one.get())
input_three=Entry(width=33)
input_three.grid(column=1,row=3)
butt_two=Button(width=9,text="Generate",highlightthickness=0,command=turn_it_up_a_noch)
butt_two.grid(column=2,row=3)

window.mainloop()
