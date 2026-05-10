from tkinter import *
import xlsxwriter

# WINDOW
my = Tk()
my.geometry("400x400+500+200")
my.title("first Gui prog")
my.configure(bg="yellow")

# LABELS
Label(my, text="username", fg="red",
      font=("arial", 12)).place(x=10, y=20)

tf1 = Entry(my)
tf1.place(x=110, y=20)

Label(my, text="Password", fg="red",
      font=("arial", 12)).place(x=10, y=60)

tf2 = Entry(my, show="*")
tf2.place(x=110, y=60)


# EXCEL FUNCTION
def excel_fun():

    uname = tf1.get()
    pwd = tf2.get()

    workbook = xlsxwriter.Workbook(
        r"C:\Users\Public\login.xlsx"
    )

    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Username")
    worksheet.write(0, 1, "Password")

    worksheet.write(1, 0, uname)
    worksheet.write(1, 1, pwd)

    workbook.close()

    # DISPLAY DATA IN TERMINAL
    print("Data Saved to Excel File")
    print("Username :", uname)
    print("Password :", pwd)


# MYSQL FUNCTION
def mysql_fun():

    uname = tf1.get()
    pwd = tf2.get()

    print("Data Saved to MYSQL")
    print("Username :", uname)
    print("Password :", pwd)


# BUTTONS
b1 = Button(my, text="EXCEL",
            fg="red", bg="yellow",
            command=excel_fun)

b1.place(x=60, y=100)

b2 = Button(my, text="MYSQL",
            fg="red", bg="yellow",
            command=mysql_fun)

b2.place(x=150, y=100)

my.mainloop()