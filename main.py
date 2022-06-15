import tkinter
import tkinter as tk
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import tkinter.messagebox
import seaborn as sns


window = tk.Tk()
window.title('Personal Finance Tracker')
window.geometry("700x650")
window.configure(bg='#5F7161')


# connecting to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234password",
    database = "expenses"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE exp (name VARCHAR(255), amount FLOAT(10), category VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("ALTER TABLE exp ADD COLUMN (month VARCHAR(255))")
# mycursor.execute("DELETE FROM exp WHERE month IS NULL")
# mycursor.execute("DELETE FROM exp")

sns.set_theme(style="whitegrid", palette="pastel")

name_var = tk.StringVar()
amount_var = tk.DoubleVar()

greeting = tk.Label(window, text="Personal Finance Tracker", pady=20, background="#5F7161")
greeting.pack()
label1 = tk.Label(window, text="Expense Name", background="#5F7161")
entry1 = tk.Entry(window, textvariable=name_var, background="#EFEAD8", foreground="#5F7161", highlightbackground="#5F7161")
label1.pack()
entry1.pack()
label2 = tk.Label(window, text="Amount ($)", background="#5F7161")
entry2 = tk.Entry(window, textvariable=amount_var, background="#EFEAD8", foreground="#5F7161", highlightbackground="#5F7161")
entry2.insert(2,0)
label2.pack()
entry2.pack()

label3 = tk.Label(window, text="Select Category", pady=10, background="#5F7161")
label3.pack()
categories_list = ["Pets", "Housing", "Travel", "Savings", "Utilities", "Investments", "Debt", "Transportation", "Groceries", "Food Out", "Insurance", "Medical", "Personal Spending", "Entertainment", "Miscellaneous"]
categories_list.sort()
value_inside = tkinter.StringVar(window)
category_menu = tkinter.OptionMenu(window, value_inside, *categories_list)
category_menu.configure(bg="#EFEAD8", fg="#5F7161")
category_menu.pack()
value_inside.set("Select Category")

label4 = tk.Label(window, text="What month is this expense for?", pady=10, background="#5F7161")
label4.pack()
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_choice = tkinter.StringVar(window)
month_menu = tkinter.OptionMenu(window, month_choice, *month_list)
month_menu.configure(bg="#EFEAD8", fg="#5F7161")
month_menu.pack()
month_choice.set("Select Month")


def add_database():
    expense_name = name_var.get()
    expense_amount = "{: .2f}".format(float(amount_var.get()))
    expense_category = value_inside.get()
    expense_month = month_choice.get()

    if (len(expense_name) != 0 and expense_category != "Select Category" and expense_month != "Select Month"):
        print("{} is {} dollars per month is a {} expense.".format(expense_name, expense_amount, expense_category,
                                                                   expense_month))
        sql_formula = "INSERT INTO exp (name, amount, category, month) VALUES (%s, %s, %s, %s)"
        expense1 = (expense_name, expense_amount, expense_category, expense_month)
        mycursor.execute(sql_formula, expense1)
        mydb.commit()
    else:
        tkinter.messagebox.showinfo(message="Please enter all required information: Expense Name, Amount, Select Category, and Select Month! Thank you!")
        print("Please enter all required information: Expense Name, Amount, Select Category, and Select Month! Thank you!")

    name_var.set("")
    amount_var.set("{: .2f}".format(float(0.00)))


# Add Button
button = tk.Button(window, text="Add", background="#D0C9C0", foreground="#5F7161", highlightbackground="#5F7161", command=add_database)
button.pack()

def view_table():
    month_selected = val_inside.get()
    sql_formula2 = "SELECT * FROM exp WHERE month='{}'".format(month_selected)
    mycursor.execute(sql_formula2)
    result = mycursor.fetchall()
    Names = []
    Amounts = []
    Categories = []
    for i in result:
        Names.append(i[0])
        Amounts.append(i[1])
        Categories.append(i[2])
    print("Names of Expenses = ", Names)
    print("Amounts of Expenses = ", Amounts)
    print("Categories of Expenses = ", Categories)

    fig = go.Figure(data=[go.Table(header=dict(values=["Name", "Amount", "Category"]),
                                   cells=dict(values=[Names, Amounts, Categories]))
                          ])
    fig.update_layout(title_text=month_selected + "'s Expenses", title_x=0.5)
    fig.show()

def view_bar():
    month_selected = val_inside.get()
    sql_formula2 = "SELECT category, ROUND(SUM(amount),2) FROM exp WHERE month='{}' GROUP BY category".format(month_selected)
    mycursor.execute(sql_formula2)
    result = mycursor.fetchall()
    Names = []
    Amounts = []
    Categories = []
    for i in result:
        # Names.append(i[0])
        Amounts.append(i[1])
        Categories.append(i[0])
    print("Names of Expenses = ", Names)
    print("Amounts of Expenses = ", Amounts)
    print("Categories of Expenses = ", Categories)

    # Visualize Data
    plt.bar(Categories, Amounts)
    plt.ylim(0,500)
    plt.xlabel("Categories")
    plt.ylabel("Amount ($)")
    plt.title("{}'s Expenses".format(val_inside.get()))
    plt.show()

def view_pie():
    month_selected = val_inside.get()
    sql_formula2 = "SELECT category, ROUND(SUM(amount),2) FROM exp WHERE month='{}' GROUP BY category".format(
        month_selected)
    mycursor.execute(sql_formula2)
    result = mycursor.fetchall()
    Names = []
    Amounts = []
    Categories = []
    for i in result:
        Categories.append(i[0])
        Amounts.append(i[1])
    print("Names of Expenses = ", Names)
    print("Amounts of Expenses = ", Amounts)
    print("Categories of Expenses = ", Categories)

    # Visualize Data
    y = np.array(Amounts)
    my_labels = Categories
    plt.pie(y, labels=my_labels)
    plt.title("{}'s Expenses by Categories".format(val_inside.get()))
    plt.legend(title="Categories:")
    plt.show()


frame1 = tkinter.Frame(window, highlightbackground="#EFEAD8", highlightthickness=2, pady = 30, padx=30, background="#6D8B74")
frame1.pack(padx=50, pady=50)

label5 = tk.Label(frame1, text="View Data", pady=5, background="#6D8B74", highlightbackground="#6D8B74")
label5.pack()
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
val_inside = tkinter.StringVar(frame1)
month_menu = tkinter.OptionMenu(frame1, val_inside, *month_list)
month_menu.configure(bg="#EFEAD8", fg="#5F7161")
month_menu.pack()
val_inside.set("Select Month")

# See Selected Month's Table Button
button4 = tk.Button(frame1, text="See Table", command=view_table, background="#D0C9C0", foreground="#5F7161", highlightbackground="#6D8B74")
button4.pack()

# See Selected Month's Bar Graph Button
button5 = tk.Button(frame1, text="See Bar Graph", command=view_bar, background="#D0C9C0", foreground="#5F7161", highlightbackground="#6D8B74")
button5.pack()

# See Selected Month's Pie Chart Button
button6 = tk.Button(frame1, text="See Pie Chart", command=view_pie, background="#D0C9C0", foreground="#5F7161", highlightbackground="#6D8B74")
button6.pack()

window.mainloop()
