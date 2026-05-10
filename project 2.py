from tkinter import *
from tkinter import messagebox
import mysql.connector

# SAVE FUNCTION
def save_mysql():

    username = tf1.get()
    password = tf2.get()

    try:

        # MYSQL CONNECTION
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pruthvi@7",
            database="zcode"
        )

        cur = con.cursor()

        # CREATE TABLE
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees(
                username VARCHAR(50),
                password VARCHAR(50)
            )
        """)

        # INSERT DATA
        sql = "INSERT INTO employees(username,password) VALUES(%s,%s)"

        values = (username, password)

        cur.execute(sql, values)

        # SAVE DATA
        con.commit()

        print("Data Inserted Successfully")

        # DISPLAY TABLE DATA
        cur.execute("SELECT * FROM employees")

        rows = cur.fetchall()

        print("\nEmployees Table:\n")

        for row in rows:
            print(row)

        messagebox.showinfo(
            "Success",
            "Data Saved Successfully"
        )

        con.close()

    except Exception as e:

        print("Error :", e)

# WINDOW
myw = Tk()
myw.geometry("400x300")
myw.title("MYSQL GUI")
myw.configure(bg="yellow")

# USERNAME LABEL
Label(
    myw,
    text="Username",
    fg="red",
    bg="yellow",
    font=("Arial", 12)
).place(x=20, y=30)

# USERNAME ENTRY
tf1 = Entry(myw)
tf1.place(x=120, y=30)

# PASSWORD LABEL
Label(
    myw,
    text="Password",
    fg="red",
    bg="yellow",
    font=("Arial", 12)
).place(x=20, y=70)

# PASSWORD ENTRY
tf2 = Entry(myw, show="*")
tf2.place(x=120, y=70)

# BUTTON
Button(
    myw,
    text="SAVE MYSQL",
    fg="blue",
    bg="white",
    command=save_mysql
).place(x=120, y=120)

# RUN
myw.mainloop()