from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


def login():
    login.destroy()
    import budget_Calculator

def clear():
    combo_month.set('')
    entry_income.delete(0, END)
    for entry in entries_spending.values():
        entry.delete(0, END)

def calculate():
    month = combo_month.get()
    income = entry_income.get()

    try:
        income = float(income)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid income.")
        return

    spending = 0
    for category, entry in entries_spending.items():
        try:
            category_spending = float(entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid spending for {} category.".format(category))
            return
        spending += category_spending

    if income < spending:
        messagebox.showwarning("Warning", "Your spending exceeds your income.")
    else:
        savings = income - spending

        # Connect to the MySQL database
        conn= pymysql.connect(host='localhost',user='root',password='KiR@pri#122',database='budgetdata')

        # Create a cursor object for executing SQL queries
        mycursor = conn.cursor()

        # Insert the budget data into the 'budget' table
        sql = "INSERT INTO budget (`Month`,`Monthly_Income`, `Housing`, `Transportation`, `Food` ,`Bills`,'Fees',`Insurance`,`Medical`, `Savings`,`Entertainment`,`Miscellaneous`) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
        val = (month, income, entries_spending["Housing"].get(), entries_spending["Transportation"].get(),
               entries_spending["Food"].get(), entries_spending["Bills"].get(), entries_spending["Insurance"].get(),
               entries_spending["Medical"].get(), savings, entries_spending["Entertainment"].get(),
               entries_spending["Miscellaneous"].get())
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()

        # Display the budget data in a message box
        messagebox.showinfo("Budget Calculator","Your total spending for {} is Rs.{:.2f}.\nYour savings is Rs.{:.2f}.".format(month, spending,savings))
        clear()
        root.destroy()



root=Tk()
root.title("Budget Calculator")
root.geometry("600x650")

categories = ["Savings","Housing","Transportation","Food","Bills","Insurance","Medical","Fees","Entertainment","Miscellaneous"]

label_title =Label(root, text="Budget Calculator", font=("Arial", 20)) #creating a label widget
label_title.pack(pady=10)

label_month = Label(root, text="Select Month:", font=("Arial", 12))
label_month.pack(pady=10)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
combo_month = ttk.Combobox(root, values=months)
combo_month.pack(pady=5)

label_income = Label(root, text="Enter Monthly Income:", font=("Arial", 12))
label_income.pack(pady=10)

entry_income = Entry(root, font=("Arial", 12)) #for textboxes we use entry widget
entry_income.pack(pady=5)

label_spending = Label(root, text="Enter Monthly Spending:", font=("Arial", 12))
label_spending.pack(pady=10)

frame_spending = Frame(root)
frame_spending.pack()

entries_spending = {}
for category in categories:
    label_category = Label(frame_spending, text=category, font=("Arial", 12))
    label_category.grid(row=categories.index(category), column=0, pady=5, padx=10) #displaying
    entry_category = Entry(frame_spending, font=("Arial", 12))
    entry_category.grid(row=categories.index(category), column=1, pady=5, padx=10)
    entries_spending[category] = entry_category

button_calculate = Button(root, text="Calculate", font=("Arial", 12), command=calculate)
button_calculate.pack(pady=10)


root.mainloop()

