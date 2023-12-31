from tkinter import *  #can access all methods and classes present inside tkinter module
from PIL import ImageTk #pil=python image library
from tkinter import messagebox
import pymysql
from pip._internal.operations import check


#FUNCTIONALITY
def clear():
    usernameEntry.delete(0 ,END)
    passwordEntry.delete(0 ,END)
    check.set(0)

def check_credentials(username, password):
    # Connect to the MySQL database
    conn = pymysql.connect(host='localhost', user='root', password='KiR@pri#122', database='data')

    # Create a cursor object for executing SQL queries
    cursor = conn.cursor()

    # Execute the SQL query to check if the username and password exist in the database
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    messagebox.showerror('SUCCESS', 'Username and password is valid')

    # Get the results of the query
    result = cursor.fetchone()

    # Close the database connection
    conn.close()
    clear()

import os
import subprocess
import webbrowser

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showinfo('ERROR', 'All Fields Are Required')
    else:
        try:
            conn = pymysql.connect(host='localhost', user='root', password='KiR@pri#122')
            mycursor = conn.cursor()
        except:
            messagebox.showinfo('ERROR','Connectivity is not established. Please try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showinfo('ERROR', 'Invalid username or Password')
        else:
            messagebox.showinfo('WELCOME', 'Login is successful')
            app_path = os.path.join(os.getcwd(), 'budget_app.py')
            webbrowser.open_new_tab('file://' + 'E:/PyCharmProjects/budget app using python(tkinter)/venv/budget_app.py')
            subprocess.run(['python', 'E:/PyCharmProjects/budget app using python(tkinter)/venv/budget_app.py'])



def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmnewpass_entry.get()=='':
            messagebox.showinfo('ERROR','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmnewpass_entry.get():
            messagebox.showinfo('ERROR','Password doesnt match',parent=window)
        else:
            conn = pymysql.connect(host='localhost', user='root', password='KiR@pri#122',database='userdata')
            mycursor = conn.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('ERROR', 'Incorrect Username')
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Password is reset , Please login with new password',parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window,image=bgPic)
    bgLabel.grid()

    headinglabel = Label(window,text='RESET PASSWORD',font=('arial',18,'bold'),bg='white',fg='magenta2')
    headinglabel.place(x=480,y=60)

    userlabel = Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userlabel.place(x=470,y=130)
    user_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    user_entry.place(x=470, y=160)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    passlabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    passlabel.place(x=470, y=210)
    newpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    newpass_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpasslabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    confirmpasslabel.place(x=470, y=290)
    confirmnewpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='magenta2')
    confirmnewpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Times New Roman',16,'bold'),width=19,cursor='hand2',activeforeground='white',activebackground='magenta2',command=change_password)
    submitButton.place(x=470 , y=390)

    window.mainloop()

def budget_app():
    login_user.destroy()
    import budget_app

def Signup():
    login.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_entry(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_entry(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


#GUI PART
login = Tk()                            #login is object variable and tk is class name
login.title('LOGIN PAGE')
login.resizable(width=FALSE,height=FALSE) #disable maximize button and cant change size
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login,image=bgImage)
bgLabel.grid(row=0,column=0)

#heading
heading =Label(login, text= 'USER LOGIN',font=('Times New Roman',23,'bold'),bg='white',fg='firebrick')
heading.place(x=605 , y=120)

#username
usernameEntry = Entry(login,width=25,font=('Times New Roman',11,'bold'),bd=0,fg='firebrick')
usernameEntry.place(x=580 , y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>',user_entry)
Frame(login , width=250,height=2 ,bg='firebrick').place(x=580,y=222)

#password
passwordEntry = Entry(login,width=25,font=('Times New Roman',11,'bold'),bd=0,fg='firebrick')
passwordEntry.place(x=580 , y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>',pass_entry)
Frame(login , width=250,height=2 ,bg='firebrick').place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton = Button(login , image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

#forget button
forgetButton = Button(login , text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Times New Roman',9,'bold'),fg='firebrick1',activeforeground='firebrick',command=forget_pass)
forgetButton.place(x=735,y=295)

#login button
login_button = Button(login, text='LOGIN', font=('Times New Roman', 14, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=23,
                      command=login_user)
login_button.place(x=578, y=350)


newbutton = Button(login,text='Create new one',font=('Times New Roman',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=Signup)
newbutton.place(x=727,y=500)

#label
orLabel = Label(login,text='-------------------OR-------------------',font=('Calibri',16),fg='firebrick1',bg='white')
orLabel.place(x=580,y=400)

signupLabel = Label(login,text='Dont have an account?',font=('Calibri',9),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

#inserting logo
facebooklogo = PhotoImage(file='facebook.png')
fbLabel = Label(login , image=facebooklogo , bg='white')
fbLabel.place(x=640 , y=440)

googlelogo = PhotoImage(file='google.png')
gLabel = Label(login , image=googlelogo , bg='white')
gLabel.place(x=690 , y=440)

twitterlogo = PhotoImage(file='twitter.png')
tLabel = Label(login , image=twitterlogo , bg='white')
tLabel.place(x=740 , y=440)

login.mainloop()