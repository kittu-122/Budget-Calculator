from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0 ,END)
    usernameEntry.delete(0 ,END)
    passwordEntry.delete(0 ,END)
    cpasswordEntry.delete(0 ,END)
    check.set(0)

def connectdatabase():
    if emailEntry.get() == '' or usernameEntry.get() == '' or cpasswordEntry.get() == '':
        messagebox.showerror('ERROR','All Fields Are Required')
    elif passwordEntry.get() != cpasswordEntry.get():
        messagebox.showerror('ERROR','Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('ERROR','Please accept Terms & Conditions')
    else:
        try:
            conn= pymysql.connect(host='localhost',user='root',password='KiR@pri#122')
            mycursor = conn.cursor()
        except:
            messagebox.showerror('ERROR','Database Connectivity Issue,Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null,email varchar(50),username varchar(45),password varchar(20)'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('ERROR', 'Username Already Exists')
            else:
                query='insert into data(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Registration is successful')
                clear()
                signup.destroy()
                import login

def login():
    signup.destroy()
    import login

signup=Tk()
signup.title('SIGNUP PAGE')
signup.resizable(FALSE,FALSE)

background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup,image=background)
bgLabel.grid()

frame=Frame(signup,bg='white')
frame.place(x=554,y=100)

heading =Label(frame, text= 'CREATE AN ACCOUNT',font=('Times New Roman',18,'bold'),bg='white',fg='firebrick')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Calibri',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame, width=33,font=('Calibri',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Calibri',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame, width=33,font=('Calibri',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Calibri',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame, width=33,font=('Calibri',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

cpasswordLabel=Label(frame,text='Confirm Password',font=('Calibri',10,'bold'),bg='white',fg='firebrick1')
cpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
cpasswordEntry=Entry(frame, width=33,font=('Calibri',10,'bold'),fg='white',bg='firebrick1')
cpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termscondn = Checkbutton(frame , text='I agree to the Terms & Conditions',font=('Calibri',9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termscondn.grid(row=9 , column=0 , pady=15 , padx=7)

signupbutton = Button(frame,text='SignUp',font=('Times New Roman',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=17,command=connectdatabase)
signupbutton.grid(row=10,column=0)

alreadyacc=Label(frame,text='Dont have an account?',font=('Calibri',9,'bold'),bg='white',fg='firebrick1')
alreadyacc.grid(row=11,column=0,sticky='w',padx=25 , pady=15)

loginbutton = Button(frame,text='Log In',font=('Times New Roman',9,'bold underline'),fg='blue',bg='white',bd=0,activeforeground='blue',activebackground='white',cursor='hand2',command=login)
loginbutton.place(x=150,y=358)

signup.mainloop()