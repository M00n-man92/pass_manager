from tkinter import messagebox
from tkinter import *
from encrpt_ps import Encript
import pyperclip
import json

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

def piano():
    websiite=input_one.get()
    emailing=input_two.get()
    passing=input_three.get()
    new_dic={websiite:{"email":emailing,"password":passing}}
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
            with open('./data.json',mode="r",) as file:
                data=json.load(file)
                data.update(new_dic)
            with open('./data.json',mode='w')as filr:

                json.dump(data,filr,indent=2)
                print(data)
            input_one.delete(0,END)
            
            input_three.delete(0,END)
            input_one.focus()

def turn_it_up_a_noch():
    input_three.delete(0,END)
    gen_password=Encript.start()
    input_three.insert(0,gen_password)
    pyperclip.copy(gen_password)
def how_you_fell():
    a=input_one.get()
    try:
        with open("./data.json")as file:
        
            b=json.load(file)
        c=b[a]
    except KeyError:    
    
        messagebox.showerror(message=f"There appears to be no data for {a}") 
        input_one.delete(0,END) 
    else:
        

        email=c["email"]
        password=c["password"]
        messagebox.showinfo(title=a,message=f"  Email is {email}\n\n  Password is {password}")
          


    # if b[a]:
    #     messagebox.showinfo(title="","email is ")     
      

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
# input_two.insert(0,"your email@email.com")
print(input_one.get())
input_three=Entry(width=33)
input_three.grid(column=1,row=3)
butt_two=Button(width=9,text="Generate",highlightthickness=0,command=turn_it_up_a_noch)
butt_two.grid(column=2,row=3)
but_three=Button(text="Search",width=9,highlightthickness=0,command=how_you_fell)
but_three.grid(column=2,row=1)

window.mainloop()
