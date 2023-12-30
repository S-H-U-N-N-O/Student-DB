from tkinter import *
import tkinter.messagebox as Messagebox
import sqlite3
import bcrypt
import mysql.connector as mysql


def insert():
    name = en1.get()
    roll = en2.get()
    sec = en3.get()
    cls = en4.get()
    id = en5.get()
    cn = en6.get()

    if name == "" or roll == "" or sec == "" or cls == "" or id == "" or cn == "":
        Messagebox.showinfo("Insert Status", "All fields are required.")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="srs")
        cursor = con.cursor()
        cursor.execute(
            "insert into info values('"
            + name
            + "','"
            + roll
            + "','"
            + sec
            + "', '"
            + cls
            + "', '"
            + id
            + "', '"
            + cn
            + "')"
        )
        cursor.execute("commit")

        en1.delete(0, "end")
        en2.delete(0, "end")
        en3.delete(0, "end")
        en4.delete(0, "end")
        en5.delete(0, "end")
        en6.delete(0, "end")
        show()
        Messagebox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def delete():
    if en5.get() == "":
        Messagebox.showinfo("Delete Status", "ID is compolsary for delete.")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="srs")
        cursor = con.cursor()
        cursor.execute("delete from info where id='" + en5.get() + "'")
        cursor.execute("commit")

        en1.delete(0, "end")
        en2.delete(0, "end")
        en3.delete(0, "end")
        en4.delete(0, "end")
        en5.delete(0, "end")
        en6.delete(0, "end")
        show()
        Messagebox.showinfo("Delete Status", "Deleted Successfully")
        con.close()


def update():
    name = en1.get()
    roll = en2.get()
    sec = en3.get()
    cls = en4.get()
    id = en5.get()
    cn = en6.get()
    if name == "" or roll == "" or sec == "" or cls == "" or id == "" or cn == "":
        Messagebox.showinfo("Update Status", "All fields are required.")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="srs")
        cursor = con.cursor()
        cursor.execute(
            "update info set name='"
            + name
            + "', roll='"
            + roll
            + "',sec='"
            + sec
            + "',cls='"
            + cls
            + "' ,cn='"
            + cn
            + "' where id='"
            + id
            + "'"
        )
        cursor.execute("commit")

        en1.delete(0, "end")
        en2.delete(0, "end")
        en3.delete(0, "end")
        en4.delete(0, "end")
        en5.delete(0, "end")
        en6.delete(0, "end")
        show()
        Messagebox.showinfo("Update Status", "Updated Successfully")
        con.close()


def get():
    if en5.get() == "":
        Messagebox.showinfo("Fetch Status", "ID is compolsary for Get.")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="srs")
        cursor = con.cursor()
        cursor.execute("select * from info where id='" + en5.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            en1.insert(0, row[0])
            en2.insert(0, row[1])
            en3.insert(0, row[2])
            en4.insert(0, row[3])
            en6.insert(0, row[5])

        con.close()


def show():
    con = mysql.connect(host="localhost", user="root", password="", database="srs")
    cursor = con.cursor()
    cursor.execute("select * from info")
    rows = cursor.fetchall()
    li1.delete(0, li1.size())

    for row in rows:
        insertdata = (
            str(row[0])
            + "                 "
            + str(row[1])
            + "                 "
            + str(row[2])
            + "                 "
            + str(row[3])
            + "                 "
            + str(row[4])
            + "                 "
            + str(row[5])
        )
        li1.insert(li1.size() + 1, insertdata)
    con.close()


def go_back():
    first_page()
    t3.destroy()
    la8.destroy()
    la9.destroy()
    e7.destroy()
    e8.destroy()
    b5.destroy()
    b6.destroy()


def go_back_l():
    first_page()
    t1.destroy()
    la1.destroy()
    la2.destroy()
    la3.destroy()
    la4.destroy()
    la5.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    b3.destroy()
    b4.destroy()


root = Tk()
root.geometry("800x500")
root.resizable(False, False)
root.title("Student Database")

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)"""
)


def signup():
    username = e1.get()
    password = e5.get()
    if username != "" and password != "":
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if cursor.fetchone() is not None:
            Messagebox.showerror("Error", "Username Already Exists")
        else:
            encoded_passwords = password.encode("utf-8")
            hashed_passwords = bcrypt.hashpw(encoded_passwords, bcrypt.gensalt())
            cursor.execute(
                "INSERT INTO users VALUES (?, ?)", [username, hashed_passwords]
            )
            conn.commit()
            Messagebox.showinfo("Success", "Account Has Been Created")
            t1.destroy()
            la1.destroy()
            la2.destroy()
            la3.destroy()
            la4.destroy()
            la5.destroy()
            e1.destroy()
            e2.destroy()
            e3.destroy()
            e4.destroy()
            e5.destroy()
            b3.destroy()
            first_page()

    else:
        Messagebox.showerror("Error", "Enter All Data")


def login():
    username = e7.get()
    password = e8.get()
    if username != "" and password != "":
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                Messagebox.showinfo("Success", "Logged in successfully. ")
                t3.destroy()
                la8.destroy()
                la9.destroy()
                e7.destroy()
                e8.destroy()
                b5.destroy()

                global en1
                global en2
                global en3
                global en4
                global en5
                global en6
                global li1

                title = Label(
                    root,
                    text="Student Database",
                    font=("times_new_roman", 20),
                    bg="Yellow",
                )
                title.place(x=280, y=5)

                name = Label(root, text="Name: ", font=("times_new_roman", 14)).place(
                    x=10, y=90
                )
                roll = Label(root, text="Roll: ", font=("times_new_roman", 14)).place(
                    x=10, y=130
                )
                sec = Label(root, text="Section: ", font=("times_new_roman", 14)).place(
                    x=10, y=170
                )
                cls = Label(root, text="Class: ", font=("times_new_roman", 14)).place(
                    x=10, y=210
                )
                id = Label(root, text="ID: ", font=("times_new_roman", 14)).place(
                    x=10, y=250
                )
                cn = Label(
                    root, text="Contact No: ", font=("times_new_roman", 14)
                ).place(x=10, y=290)

                en1 = Entry(root)
                en1.place(x=120, y=95)
                en2 = Entry(root)
                en2.place(x=120, y=135)
                en3 = Entry(root)
                en3.place(x=120, y=175)
                en4 = Entry(root)
                en4.place(x=120, y=215)
                en5 = Entry(root)
                en5.place(x=120, y=255)
                en6 = Entry(root)
                en6.place(x=120, y=295)

                bn1 = Button(
                    root,
                    width=8,
                    height=1,
                    text="INSERT",
                    font=("times_new_roman", 12),
                    command=insert,
                )
                bn1.place(x=50, y=340)
                bn2 = Button(
                    root,
                    width=8,
                    height=1,
                    text="DELETE",
                    font=("times_new_roman", 12),
                    command=delete,
                )
                bn2.place(x=150, y=340)
                bn3 = Button(
                    root,
                    width=8,
                    height=1,
                    text="UPDATE",
                    font=("times_new_roman", 12),
                    command=update,
                )
                bn3.place(x=50, y=380)
                bn4 = Button(
                    root,
                    width=8,
                    height=1,
                    text="GET(By ID)",
                    font=("times_new_roman", 12),
                    command=get,
                )
                bn4.place(x=150, y=380)

                fr1 = Frame(
                    root,
                    bg="#46FAFF",
                    highlightbackground="#004346",
                    highlightthickness=3,
                ).grid(padx=270, pady=94, ipadx=260, ipady=200)
                li1 = Listbox(fr1, width=83, height=23)
                li1.place(x=280, y=108)
                show()

            else:
                Messagebox.showerror("Error", "Invalid Password. ")
        else:
            Messagebox.showerror("Error", "Invalid Username. ")
    else:
        Messagebox.showerror("Error", "Enter All Data")


def first_page():
    def register_page():
        global t1
        global la1
        global la2
        global la3
        global la4
        global la5
        global e1
        global e2
        global e3
        global e4
        global e5
        global b3
        global b4

        f1.destroy()
        l1.destroy()
        l3.destroy()
        b1.destroy()
        b2.destroy()

        t1 = Label(root, text="Register With Your Info", font=("Arial", 30))
        t1.place(x=190, y=10)
        la1 = Label(root, text="Username", font=("Arial", 15))
        la1.place(x=250, y=100)
        la2 = Label(root, text="Email", font=("Arial", 15))
        la2.place(x=250, y=140)
        la3 = Label(root, text="Age", font=("Arial", 15))
        la3.place(x=250, y=180)
        la4 = Label(root, text="Phone No.", font=("Arial", 15))
        la4.place(x=250, y=220)
        la5 = Label(root, text="Password", font=("Arial", 15))
        la5.place(x=250, y=260)

        e1 = Entry(root, width=30)
        e1.place(x=360, y=105)
        e2 = Entry(root, width=30)
        e2.place(x=360, y=145)
        e3 = Entry(root, width=30)
        e3.place(x=360, y=185)
        e4 = Entry(root, width=30)
        e4.place(x=360, y=225)
        e5 = Entry(root, width=30, show="*")
        e5.place(x=360, y=265)

        b3 = Button(
            root, text="Submit", width=10, height=2, font=("Arial", 11), command=signup
        )
        b3.place(x=400, y=300)
        b4 = Button(
            root,
            text="Go Back",
            width=10,
            height=2,
            font=("Arial", 11),
            command=go_back_l,
        )
        b4.place(x=400, y=350)

    def login_page():
        global t3
        global la8
        global la9
        global e8
        global b5
        global e7
        global b6

        f1.destroy()
        l1.destroy()
        l3.destroy()
        b1.destroy()
        b2.destroy()

        t3 = Label(root, text="Log In With Your Info", font=("Arial", 30))
        t3.place(x=190, y=10)
        la8 = Label(root, text="Username", font=("Arial", 15))
        la8.place(x=250, y=160)
        la9 = Label(root, text="Password", font=("Arial", 15))
        la9.place(x=250, y=200)
        e7 = Entry(root, width=30)
        e7.place(x=360, y=165)
        e8 = Entry(root, width=30, show="*")
        e8.place(x=360, y=205)
        b5 = Button(
            root, text="Submit", width=10, height=2, font=("Arial", 11), command=login
        )
        b5.place(x=400, y=300)
        b6 = Button(
            root,
            text="Go Back",
            width=10,
            height=2,
            font=("Arial", 11),
            command=go_back,
        )
        b6.place(x=400, y=350)

    f1 = Frame(root, highlightbackground="#171762", highlightthickness=3)
    f1.grid(padx=50, pady=110, ipadx=1, ipady=1)
    l1 = Label(f1, text="STUDENT", font=("Arial", 45))
    l1.grid(padx=20, pady=20)
    l2 = Label(f1, text="DATABASE", font=("Arial", 45))
    l2.grid(padx=20, pady=25)

    l3 = Label(root, text="Log In/Register", font=("Arial", 20))
    l3.place(x=500, y=110)

    b1 = Button(root, text="Log in", font=("Arial", 20), width=9, command=login_page)
    b1.place(x=515, y=165)

    b2 = Button(
        root, text="Register", font=("Arial", 20), width=9, command=register_page
    )
    b2.place(x=515, y=245)


first_page()

root.mainloop()
