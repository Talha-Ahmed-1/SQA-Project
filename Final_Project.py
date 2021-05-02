from tkinter import *
# from MySQLdb import MySQLdb
import mysql.connector as MySQLdb
from tkinter import ttk
from datetime import date
import re


class Staff:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        self.cursor = self.db.cursor()

        self.tk2 = Tk()
        self.tk2.iconbitmap('Icon.ico')
        self.tk2.title("Staff Panel")
        self.tk2.geometry("1920x1080+0+0")
        self.tk2.configure(bg="cadetblue")
        self.lab = Label(self.tk2, text="Staff", bg="cadetblue", font=("Helvetica", 30))
        self.lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.lgbutton = Button(self.tk2, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                               command=lambda: self.tk2.destroy())
        self.lgbutton.place(x=1435, y=0)
        self.back = Button(self.tk2, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                           command=lambda:[self.tk2.destroy(), self.new_win()])
        self.back.place(x=30, y=0)
        self.add_staff = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.add_staff.grid(row=2, column=0)
        self.delete_staff = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.delete_staff.grid(row=3, column=1)
        self.frame7 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame7.grid(row=3, column=0)
        self.frame8 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame8.grid(row=2, column=1)
        self.label5 = Label(master=self.add_staff, text="Add Staff", font=("times", 30), bg="honeydew3")
        self.label6 = Label(master=self.delete_staff, text="Delete Staff", font=("times", 30), bg="honeydew3")
        self.label7 = Label(master=self.frame7, text="Update Staff", font=("times", 30), bg="honeydew3")
        self.label8 = Label(master=self.frame8, text="Search Staff", font=("times", 30), bg="honeydew3")
        self.label5.place(x=250, y=0)
        self.label6.place(x=250, y=0)
        self.label7.place(x=250, y=0)
        self.label8.place(x=250, y=0)
        """"Search Frame works start here """
        self.name_search = StringVar()
        self.label_name_search = Label(master=self.frame8, text="Name", font="times 15", bg="honeydew3")
        self.label_name_search.place(x=100, y=100)
        self.c_name_search = StringVar()
        self.entry_name_search = Entry(master=self.frame8, font="times 15", textvariable=self.c_name_search)
        self.entry_name_search.place(x=200, y=100, height=30, width=185)

        self.button_search = Button(master=self.frame8, text="Search", font="halvatica 13", bd=3, height=1,
                                    cursor="hand2", width=10, bg="cadet blue",
                                    command=lambda: Staff.search_c(self))
        self.button_search.place(x=150, y=200)

        self.button_search_all = Button(master=self.frame8, text="Show All", font="halvatica  13", bd=3, height=1,
                                        cursor="hand2", width=10,
                                        bg="cadet blue", command=lambda: Staff.search_all_c(self))
        self.button_search_all.place(x=300, y=200)
        """Frame 5 ALL Fucntions and widnows"""

        self.name = StringVar()
        self.working = StringVar()
        self.salary = StringVar()
        self.address = StringVar()

        # ALL LABELS OF ADD Staff WINDOW STARTS FROM HERE

        self.label_name = Label(master=self.add_staff, text="Name", font="Times 15  ", bg="honeydew3")
        self.label_name.place(x=140, y=100)

        self.label_address = Label(master=self.add_staff, text="Address", font="Times15 ", bg="honeydew3")
        self.label_address.place(x=140, y=140)

        self.label_Working = Label(master=self.add_staff, text="Working", font="Times 15", bg="honeydew3")
        self.label_Working.place(x=140, y=180)

        self.label_Salary = Label(self.add_staff, text="Salary", font="Times 15", bg="honeydew3")
        self.label_Salary.place(x=140, y=220)

        # ALL ENTRY OF ADD Staff WINDOW
        self.entry1 = Entry(self.add_staff, font="Times 15", textvariable=self.name)
        self.entry1.place(x=260, y=100,width=185,height=30)
        self.entry2 = Entry(self.add_staff, font="Times 15", textvariable=self.address)
        self.entry2.place(x=260, y=140,width=185,height=30)
        self.entry3 = Entry(self.add_staff, font="Times 15", textvariable=self.working)
        self.entry3.place(x=260, y=180,width=185,height=30)
        self.entry4 = Entry(self.add_staff, font="Times 15", textvariable=self.salary)
        self.entry4.place(x=260, y=220,width=185,height=30)
        self.button_sub = Button(self.add_staff, text="Submit", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                 cursor="hand2", command=lambda: Staff.add(self))
        self.button_sub.place(x=410, y=280)
        self.button_clear = Button(self.add_staff, text="Clear All", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                   cursor="hand2",
                                   command=lambda: [self.name.set(''), self.working.set(''), self.address.set(''),
                                                    self.salary.set('')])
        self.button_clear.place(x=280, y=280)
        self.button_refresh = Button(self.add_staff, text=" Refresh", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                     cursor="hand2")
        self.button_refresh.place(x=150, y=280)

        """WORK OF FRAME 6 STARTS HERER"""
        self.ID = StringVar()
        self.new = StringVar()
        self.value = StringVar()

        # self.head_label = Label(self.delete_staff,text="Update Staff", bg="honeydew3", fg="black", font="cabri 24 bold underline")
        # self.head_label.place(x=300, y=100)
        self.label1 = Label(self.frame7, text=" ID", bg="honeydew3", font="Times 15 ")
        self.label1.place(x=170, y=100)
        self.id_entry = Entry(self.frame7, textvariable=self.ID, font="Times 15 ")
        self.id_entry.place(x=260, y=100)
        self.new_entry = Entry(self.frame7, textvariable=self.new, font="Times 15")
        self.new_entry.place(x=260, y=150)
        self.menu = OptionMenu(self.frame7, self.value, "Name", "Address", "Working", 'Salary')
        self.menu.place(x=170, y=150)
        self.value.set("Name")
        self.button = Button(self.frame7, text="Clear All ",
                             command=lambda: [self.value.set("Name"), self.ID.set('0'), self.new.set("")],
                             font="Halvatica 13", bg="cadet blue", bd=3, width=10)
        self.button.place(x=280, y=250)
        self.main_button = Button(self.frame7, text="Submit", command=lambda: Staff.Update(self),
                                  font="Halvatica 13  ", bg="cadet blue", bd=3, width=10)
        self.main_button.place(x=410, y=250)

        """work for delete frame starts here
        assigning fucntions to delete widnow"""
        self.id_del_in = StringVar()
        self.label1 = Label(self.delete_staff, text="Staff ID", bg="honeydew3", font="times 15")
        self.label1.place(x=100, y=100)
        self.id_entry = Entry(self.delete_staff, textvariable=self.id_del_in, font=" times 15")
        self.id_entry.place(x=200, y=100)
        self.del_button = Button(self.delete_staff, text="Delete Staff", bd=3, font="Halvatica 13  ",
                                 command=lambda: Staff.delete(self), bg='cadet blue')
        self.del_button.place(x=250, y=150)
        self.tk2.mainloop()


    def search_c(self):
        name_search = self.c_name_search.get()

        # print(name_search)
        def improper():
            msg = Message(master=self.frame8, text="Enter Proper Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        def no_name():
            msg = Message(master=self.frame8, text="Please Enter Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        def name_searching():
            msg = Message(master=self.frame8, text="Searching for Staff")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=100)
            msg.after(2000, lambda: msg.destroy())

        def name_found():
            msg = Message(master=self.frame8, text="Staff Found")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=150)
            msg.after(2000, lambda: msg.destroy())

        def name_not_found():
            msg = Message(master=self.frame8, text="No Staff were  Found")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(2000, lambda: msg.destroy())

        counter = 0

        if name_search == '':
            counter += 1
            no_name()
        else:
            if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', name_search):
                name_searching()
            else:
                counter += 1

        def search():
            res = []
            for i in cursor:
                res.append(i)
            if len(res) > 0:
                name_found()
                tk = Tk()
                tk.geometry("660x500")
                tk.config(bg="cadet blue")
                tk.title("Booking Database")
                f = Frame(tk)
                f.pack(fill=Y)  # side=LEFT,fill=Y)
                f.config(bg="white")
                s = Scrollbar(tk)
                c = Canvas(tk, width=660, height=500, bg="cadet blue", yscrollcommand=s.set)
                s.pack(side=RIGHT, fill=Y)

                fr = Frame(c, bg="white")
                fr.pack()
                c.pack()  # side="left",fill="both")
                c.create_window(0, 0, window=fr, anchor='nw')
                s.config(command=c.yview)
                lst = ["ID", "Name", "Address ", 'Working','Salary']
                for i in range(len(lst)):
                    if i == 1:
                        width = 15
                    else:
                        width = 10
                    Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0,
                                                                                                         column=i)
                for i in range(len(res)):
                    for j in range(len(res[i])):
                        if i % 2 == 0:
                            color = "honeydew3"
                        else:
                            color = "white"
                        if j == 1:
                            width = 15
                        else:
                            width = 10
                        Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
                tk.mainloop()
            else:
                name_not_found()

        if counter == 0:
            db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
            cursor = db.cursor()
            name_search = name_search,
            sql = """select * from Staff where Name = %s"""
            try:
                cursor.execute(sql, name_search)
                cursor.fetchall()
                name_searching()
                search()
            except:
                improper()
    def search_all_c(self):
        def display():
            msg = Message(master=self.frame8, text="Displaying All Booking")
            msg.config(width=150, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        # name_search = name_search,
        sql = """select * from staff """
        try:
            cursor.execute(sql)
            cursor.fetchall()
            display()
        except:
            pass
        res = []
        for i in cursor:
            res.append(i)

        tk = Tk()
        tk.geometry("660x500")
        tk.config(bg="cadet blue")
        tk.title("Booking Database")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)  # side=LEFT,fill=Y)
        f.config(bg="cadet blue")
        s = Scrollbar(tk)
        c = Canvas(tk, width=660, height=500, bg="honeydew3", yscrollcommand=s.set)
        s.pack(side=RIGHT, fill=Y)

        fr = Frame(c, bg="honeydew3")
        fr.pack()
        c.pack()  # side="left",fill="both")
        c.create_window(0, 0, window=fr, anchor='nw')
        s.config(command=c.yview)
        lst = ["ID", "Name", "Address", "Working", "Salary"]
        for i in range(len(lst)):
            if i == 1:
                width = 15
            else:
                width = 10
            Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "honeydew3"
                else:
                    color = "white"
                if j == 1:
                    width = 15
                else:
                    width = 10
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
        tk.mainloop()
        sql = """select * from banquet.staff"""



    def add(self):
        """Completes add Staff"""
        self.count = 0

        def insert():
            sql = """insert into Staff(Name,Address,Working,Salary) values(%s,%s,%s,%s)"""
            tup = (self.namea, self.addressa, self.workinga, self.salarya)

            try:
                self.cursor.execute(sql, tup)
                self.db.commit()
                msg = Message(self.add_staff, text="Registration Completed")
                msg.config(width=200, bg="honeydew3", fg="Blue", font="times 12")
                msg.place(x=250, y=250)
                msg.after(4000, lambda: msg.destroy())
            except:
                self.db.rollback()
                msg = Message(self.add_staff, text="Something Went Wrong")
                msg.config(width=200, bg="honeydew3", fg="Red", font="times 12")
                msg.place(x=250, y=250)
                msg.after(4000, lambda: msg.destroy())
            self.db.close()

        def proceed_name():
            msg = Message(self.add_staff, text="Valid  Name")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def proceed_address():
            msg = Message(self.add_staff, text="Valid Address")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=140)
            msg.after(4000, lambda: msg.destroy())

        def proceed_Working():
            msg = Message(self.add_staff, text="Valid Working")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=180)
            msg.after(4000, lambda: msg.destroy())


        def e_Working():
            msg = Message(self.add_staff, text="Working Cannot be Empyty")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=180)
            msg.after(4000, lambda: msg.destroy())

        def e_Salary():
            msg = Message(self.add_staff, text="Salaray Cannot be Empty")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=220)
            msg.after(4000, lambda: msg.destroy())

        def not_name():
            msg = Message(self.add_staff, text="Incorrect Name")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name.set('')

        def e_name():
            msg = Message(self.add_staff, text=" Name Cannot be Empty")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def not_Salary():
            msg = Message(self.add_staff, text="Incorrect Salary")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=220)
            msg.after(4000, lambda: msg.destroy())
            self.salary.set('')

        def salary():
            msg = Message(self.add_staff, text="Valid Salary")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=220)
            msg.after(4000, lambda: msg.destroy())

        def not_address():
            msg = Message(self.add_staff, text="Incorrect Address")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=140)
            msg.after(4000, lambda: msg.destroy())
            self.address.set('')

        def e_address():
            msg = Message(self.add_staff, text="Address Cannot be Empty")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=140)
            msg.after(4000, lambda: msg.destroy())
            self.address.set('')

        def not_Working():
            msg = Message(self.add_staff, text="Incorrect Number")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=180)
            msg.after(4000, lambda: msg.destroy())
            self.working.set('')

        def get_name():
            self.namea = self.name.get()
            if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', self.namea):
                    proceed_name()
                    self.count += 1
            else:
                if self.namea == '':
                    e_name()
                else:
                    not_name()

        def get_working():
            self.workinga = self.working.get()
            counter = 0
            for l in ['1','2','3','4','5','6','7','8','9']:
                if (l) in str(self.workinga):
                    counter += 1

            if self.workinga == '':
                counter += 1
                e_Working()
            else:
                if counter != 0:
                    not_Working()
                else:
                    self.count += 1
                    proceed_Working()

        def get_Salary():
            self.salarya = self.salary.get()
            if re.findall(r'^[1-9][0-9]{4,5}$',self.salarya):
                self.count += 1
                salary()
            else:
                if self.salarya == '':
                    e_Salary()
                else:
                    not_Salary()


        def get_address():
            #  #print("caling get_address")
            self.addressa = self.address.get()
            counter = 0
            if self.addressa == '':
                e_address()
                counter += 1
            else:
                if len(self.addressa) > 5:
                    proceed_address()
                    self.count += 1
                else:
                    not_address()
        get_name()
        get_address()
        get_Salary()
        get_working()
        if self.count == 4:
            insert()
        """REdesigning Update Module"""
    def Update(self):

        def updated_values():
            msg = Message(self.frame7, text="Updated Values")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=250, y=200)
            msg.after(4000, lambda: msg.destroy())

        def update_name():
            insert_val = (self.upd, int(self.ids))
            sql = """update  Staff set Name = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def update_address():
            insert_val = (self.upd, self.ids)
            sql = """update  Staff set Address = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def update_working():
            insert_val = (self.upd, (self.ids))
            sql = """update  Staff set Working = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val, )
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()
        def update_Salary():

            insert_val = (self.upd, self.ids)
            sql = """update  Staff set Salary = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()

            except:
                self.db.rollback()
        def clear_value():
            self.new.set("")
        def check():
            def proceed_name():
                msg = Message(self.frame7, text="Correct Name")
                msg.config(width=100, bg="honeydew3", fg="green", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_name()

            def proceed_address():
                msg = Message(self.frame7, text="Correct Address")
                msg.config(width=100, bg="honeydew3", fg="green", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_address()

            def proceed_Salary():
                msg = Message(self.frame7, text="Correct Salary")
                msg.config(width=100, bg="honeydew3", fg="green", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_Salary()

            def proceed_working():
                msg = Message(self.frame7, text="Correct Wroking")
                msg.config(width=100, bg="honeydew3", fg="green", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_working()

            def not_name():
                msg = Message(self.frame7, text="Incorrect Name")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                clear_value()

            def empty():
                msg = Message(self.frame7, text="Field Cannot be Empty")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                clear_value()

            def not_address():
                msg = Message(self.frame7, text="Incorrect Address")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                clear_value()

            def not_working():
                msg = Message(self.frame7, text="Incorrect Value")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(5000, lambda: msg.destroy())
                clear_value()

            def not_Salary():
                msg = Message(self.frame7, text="Incorrect Salary", font="times 12")
                msg.config(width=150, bg="honeydew3", fg="red")
                msg.place(x=490, y=150)
                msg.after(5000, lambda: msg.destroy())
                clear_value()

            def get_name():

                if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}',self.upd):
                    proceed_name()
                    update_name()
                else:
                    if self.upd != '':
                        not_name()


            def get_address():
                counter = 0
                for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if str(j) in str(self.upd):
                        counter += 1
                if counter != len(str(self.upd)):
                    proceed_address()
                    update_address()
                else:
                    not_address()
                # counter = 0

            def get_working():
                if re.findall(r'[A-Z][a-z]{3,10}',self.upd):
                    update_working()
                    proceed_working()
                else:
                    not_working()

            def get_Salary():
                if re.findall(r'^[1-9][0-9]{4,6}$', self.upd):
                    proceed_Salary()
                    update_Salary()
                else:
                    if self.upd == '':
                        not_Salary()
            def e_id():
                msg = Message(self.frame7, text="Cannot be empty")
                msg.config(width=100, bg="honeydew3", fg="red", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())

            def no_id():
                msg = Message(self.frame7, text="Invalid ID")
                msg.config(width=100, bg="honeydew3", fg="red", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())

            def id():
                msg = Message(self.frame7, text="Valid ID")
                msg.config(width=100, bg="honeydew3", fg="Blue", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())
            self.upd = self.new.get()
            self.ids = self.ID.get()

            if re.findall(r'(^[1-9]+)', self.ids):
                id()
            else:
                if self.ids == '':
                    e_id()
                else:
                    no_id()
            val = self.value.get()
            self.upd = self.new.get()
            if self.upd == '':
                empty()
            else:
                if val == "Name":
                    get_name()
                elif val == "Address":
                    get_address()
                elif val == "Working":
                    get_working()
                elif val == "Salary":
                    get_Salary()

        check()

    def delete(self):
        del_id = self.id_del_in.get()

        def no_id():
            msg = Message(self.delete_staff, text="Invalid ID")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=250, y=100)
            msg.after(3000, lambda: msg.destroy())
            self.ID.set('')

        def del_message():
            msg = Message(self.delete_staff, text="Staff Deleted")
            msg.config(width=150, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=300, y=200)
            msg.after(3000, lambda: msg.destroy())

        def clear():
            self.set('')

        if del_id == '' or del_id == '0':
            msg = Message(self.delete_staff, text="Invalid ID")
            msg.config(width=250, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=450, y=100)
            msg.after(3000, lambda: msg.destroy())
        else:
            counter = 0
            for l in range(58, 128):
               if chr(l) in str(del_id):
                    counter += 1
            if counter != 0:
                no_id()
                clear()
            else:
                del_message()
                sql = """delete from Staff where ID =%s"""
                insert_val = del_id,
                try:
                    self.cursor.execute(sql, insert_val)
                    self.db.commit()
                    del_message()

                except:
                    no_id()
                    self.db.rollback()







class Customer:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        self.cursor = self.db.cursor()

        self.tk2 = Tk()
        self.tk2.geometry("1920x1080+0+0")
        self.tk2.iconbitmap('Icon.ico')
        self.tk2.configure(bg="cadetblue")
        self.tk2.title("Customer Panel")
        self.lab = Label(self.tk2, text="Customer", bg="cadetblue", font=("Helvetica", 30))
        self.lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.lgbutton = Button(self.tk2, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                               command=lambda: self.tk2.destroy())
        self.lgbutton.place(x=1435, y=0)
        self.back = Button(self.tk2, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                           command=lambda: [self.tk2.destroy(),Admin.new_win(self)])
        self.back.place(x=30, y=0)
        self.frame5 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame5.grid(row=2, column=0)
        self.frame6 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame6.grid(row=3, column=1)
        self.frame7 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame7.grid(row=3, column=0)
        self.frame8 = Frame(self.tk2, height=400, width=770, bg="honeydew3", highlightthickness=30,
                            highlightcolor="cadetblue4",
                            highlightbackground="cadetblue")
        self.frame8.grid(row=2, column=1)
        self.label5 = Label(self.frame5, text="Add Customer", font=("times", 30), bg="honeydew3")
        self.label6 = Label(self.frame6, text="Delete Customer", font=("times", 30), bg="honeydew3")
        self.label7 = Label(self.frame7, text="Update Customer", font=("times", 30), bg="honeydew3")
        self.label8 = Label(self.frame8, text="Search Customer", font=("times", 30), bg="honeydew3")
        self.label5.place(x=250, y=0)
        self.label6.place(x=250, y=0)
        self.label7.place(x=250, y=0)
        self.label8.place(x=250, y=0)

        """Frame 5 ALL Fucntions and widnows"""

        self.name = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.address = StringVar()

        # ALL LABELS OF ADD CUSTOMER WINDOW STARTS FROM HERE

        self.label_name = Label(self.frame5, text="Name", font="Times 15  ", bg="honeydew3")
        self.label_name.place(x=140, y=100 - 50)

        self.label_address = Label(self.frame5, text="Address", font="Times 15", bg="honeydew3")
        self.label_address.place(x=140, y=140 - 50)

        self.label_mobile = Label(self.frame5, text="Mobile", font="Times 15", bg="honeydew3")
        self.label_mobile.place(x=140, y=180 - 50)

        self.label_email = Label(self.frame5, text="Email", font="Times 15", bg="honeydew3")
        self.label_email.place(x=140, y=220 - 50)

        # ALL ENTRY OF ADD CUSTOMER WINDOW
        self.entry1 = Entry(self.frame5, font="Times 15", textvariable=self.name)
        self.entry1.place(x=260, y=100 - 50, width=185, height=30)

        self.entry2 = Entry(self.frame5, font="Times 15", textvariable=self.address)
        self.entry2.place(x=260, y=140 - 50, width=185, height=30)

        self.entry3 = Entry(self.frame5, font="Times 15", textvariable=self.mobile)
        self.entry3.place(x=260, y=180 - 50, width=185, height=30)

        self.entry4 = Entry(self.frame5, font="Times 15", textvariable=self.email)
        self.entry4.place(x=260, y=220 - 50, width=185, height=30)

        self.button_sub = Button(self.frame5, text="Submit", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                 cursor="hand2", command=lambda: Customer.add(self))
        self.button_sub.place(x=410, y=280)
        self.button_clear = Button(self.frame5, text="Clear All", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                   cursor="hand2",
                                   command=lambda: [self.name.set(''), self.mobile.set(''), self.address.set(''),
                                                    self.email.set('')])
        self.button_clear.place(x=280, y=280)
        self.button_refresh = Button(self.frame5, text=" Refresh", font="Halvatica 13", width=10, bg="cadet blue", bd=3,
                                     cursor="hand2")
        self.button_refresh.place(x=150, y=280)

        """WORK OF FRAME 6 STARTS HERER"""
        self.ID = StringVar()
        self.new = StringVar()
        self.value = StringVar()

        self.label1 = Label(self.frame7, text=" ID", bg="honeydew3", font="Times 15")
        self.label1.place(x=170, y=100)
        self.id_entry = Entry(self.frame7, textvariable=self.ID, font="Times 15")
        self.id_entry.place(x=260, y=100, width=185, height=30)
        self.new_entry = Entry(self.frame7, textvariable=self.new, font="Times 15")
        self.new_entry.place(x=260, y=150, width=185, height=30)
        self.menu = OptionMenu(self.frame7, self.value, "Name", "Address", "Mobile", 'Email')
        self.menu.config(width=7)
        self.menu.place(x=170, y=150)
        self.value.set("Name")
        self.button = Button(self.frame7, text="Clear All ",
                             command=lambda: [self.value.set("Name"), self.ID.set('0'), self.new.set("")],
                             font="times 13", bg="cadet blue", bd=3, width=10)
        self.button.place(x=280, y=250)
        self.main_button = Button(self.frame7, text="Submit", command=lambda: Customer.Update(self),
                                  font="halvatica 13  ", bg="cadet blue", bd=3, width=10)
        self.main_button.place(x=410, y=250)

        """work for delete frame starts here
        assigning fucntions to delete widnow"""
        self.label1 = Label(self.frame6, text="ID", bg="honeydew3", font=" times 15")
        self.label1.place(x=100, y=50 + 50)

        self.del_id = StringVar()

        self.id_entry = Entry(self.frame6, textvariable=self.del_id, font="times 15")
        self.id_entry.place(x=200, y=100, width=185, height=30)

        self.del_button = Button(self.frame6, text="Delete Customer", bd=3, font="Halvatica 13  ",
                                 command=lambda: Customer.delete(self), bg='cadet blue')
        self.del_button.place(x=200, y=200)
        """"Search window works start here """
        self.name_search = StringVar()
        self.label_name_search = Label(master=self.frame8, text="Name", font="times 15", bg="honeydew3")
        self.label_name_search.place(x=100, y=100)
        self.c_name_search = StringVar()
        self.entry_name_search = Entry(master=self.frame8, font="times 15", textvariable=self.c_name_search)
        self.entry_name_search.place(x=200, y=100, height=30, width=185)

        self.button_search = Button(master=self.frame8, text="Search", font="halvatica 13", bd=3, height=1,
                                    cursor="hand2", width=10, bg="cadet blue",
                                    command=lambda: Customer.search_c(self))
        self.button_search.place(x=150, y=200)

        self.button_search_all = Button(master=self.frame8, text="Show All", font="halvatica  13", bd=3, height=1,
                                        cursor="hand2", width=10,
                                        bg="cadet blue", command=lambda: Customer.search_all_c(self))
        self.button_search_all.place(x=300, y=200)
        self.tk2.mainloop()

    def search_c(self):
        def final(res):
            if len(res) == 0:
                msg = Message(self.frame8, text="Customer Not Found")
                msg.config(width=150, bg="honeydew3", fg="Red", font="Times 12")
                msg.place(x=490, y=120)
                msg.after(4000, lambda: msg.destroy())
            else:

                tk = Tk()
                tk.geometry("900x500")
                tk.config(bg="cadet blue")
                tk.title("Customer Database")
                tk.config(bg="cadet blue")
                f = Frame(tk)
                f.pack(side=LEFT, fill=Y)  # side=LEFT,fill=Y)
                f.config(bg="honeydew3")
                s = Scrollbar(tk)
                c = Canvas(tk, width=900, height=500, bg="honeydew3", yscrollcommand=s)
                s.pack(side=RIGHT, fill=Y)

                fr = Frame(c, bg="white")
                fr.pack()
                c.pack()  # side="left",fill="both")
                c.create_window(0, 0, window=fr, anchor='nw')
                s.config(command=c.yview)
                lst = ["ID", "Name", "Address", "Mobile", "Email"]
                for i in range(len(lst)):
                    if i == 0:
                        width = 10
                    # elif i == 3:
                    #    width = 20
                    elif i == 4:

                        width = 25
                    else:
                        width = 15
                    Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
                for i in range(len(res)):
                    for j in range(len(res[i])):
                        if i % 2 == 0:
                            color = "honeydew3"
                        else:
                            color = "white"
                        if j == 0:
                            width = 10
                        #
                        elif j == 4:
                            width = 25
                        else:
                            width = 15
                        Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
                tk.mainloop()

        def wrong():
            msg = Message(self.frame8, text="Something went wrong")
            msg.config(width=150, bg="honeydew3", fg="Red", font="Times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def display():
            sql = """select * from customer where CName = %s"""
            db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
            cursor2 = db.cursor()
            res = []
            try:
                cursor2.execute(sql, c_name)
                cursor2.fetchall()
                for i in cursor2:
                    res.append(i)
                searching()
                final(res)

            except:
                wrong()
            db.close()

        def invalid():
            msg = Message(self.frame8, text="Please Check Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="Times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def searching():
            msg = Message(self.frame8, text="Searching for Customer")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="Times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        c_name = self.c_name_search.get()
        if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', c_name):
            c_name = c_name,
            display()
        else:
            invalid()

    def search_all_c(self):

        def display_all():
            msg = Message(self.frame8, text="Displaying All Records")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="Times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def not_display():
            msg = Message(self.frame8, text="Something went WRONG")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="Times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        sql = """select * from customer"""
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            display_all()
        except:
            not_display()

        res = []
        for i in cursor:
            res.append(i)

        tk = Tk()
        tk.geometry("900x500")
        tk.config(bg="cadet blue")
        tk.title("Customer Database")
        tk.config(bg="cadet blue")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)  # side=LEFT,fill=Y)
        f.config(bg="honeydew3")
        s = Scrollbar(tk)
        c = Canvas(tk, width=900, height=500, bg="honeydew3", yscrollcommand=s)
        s.pack(side=RIGHT, fill=Y)

        fr = Frame(c, bg="white")
        fr.pack()
        c.pack()  # side="left",fill="both")
        c.create_window(0, 0, window=fr, anchor='nw')
        s.config(command=c.yview)
        lst = ["ID", "Name", "Address", "Mobile", "Email"]
        for i in range(len(lst)):
            if i == 0:
                width = 10
            # elif i == 3:
            #    width = 20
            elif i == 4:

                width = 25
            else:
                width = 15
            Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "honeydew3"
                else:
                    color = "white"
                if j == 0:
                    width = 10
                #
                elif j == 4:
                    width = 25
                else:
                    width = 15
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
        tk.mainloop()

    def add(self):
        """Completes add Customer"""
        self.count = 0

        def insert():
            sql = """insert into Customer(Cname,Address,Mobile,Email) values(%s,%s,%s,%s)"""
            tup = (self.namea, self.addressa, self.mobilea, self.emaila)

            try:
                self.cursor.execute(sql, tup)
                self.db.commit()
                msg = Message(self.frame5, text="Registration Completed")
                msg.config(width=200, bg="honeydew3", fg="Blue", font="times 12")
                msg.place(x=250, y=250)
                msg.after(4000, lambda: msg.destroy())
            except:
                self.db.rollback()
            self.db.close()

        def proceed_name():
            msg = Message(self.frame5, text="Valid  Name")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=100 - 50)
            msg.after(4000, lambda: msg.destroy())

        def proceed_address():
            msg = Message(self.frame5, text="Valid Address")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=140 - 50)
            msg.after(4000, lambda: msg.destroy())

        def proceed_mobile():
            msg = Message(self.frame5, text="Valid Number")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=180 - 50)
            msg.after(4000, lambda: msg.destroy())

        def proceed_email():
            msg = Message(self.frame5, text="Valid Email")
            msg.config(width=150, bg="honeydew3", fg="blue", font="times 12")
            msg.place(x=490, y=220 - 50)
            msg.after(4000, lambda: msg.destroy())

        def not_name():
            msg = Message(self.frame5, text="Incorrect Name")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=100 - 50)
            msg.after(4000, lambda: msg.destroy())
            self.name.set('')

        def not_email():
            msg = Message(self.frame5, text="Incorrect Email")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=220 - 50)
            msg.after(4000, lambda: msg.destroy())
            self.email.set('')

        def not_address():
            msg = Message(self.frame5, text="Incorrect Address")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=140 - 50)
            msg.after(4000, lambda: msg.destroy())
            self.address.set('')

        def not_mobile():
            msg = Message(self.frame5, text="Incorrect Number")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=490, y=180 - 50)
            msg.after(4000, lambda: msg.destroy())
            self.mobile.set('')

        def get_name():
            self.namea = self.name.get()
            # #print("get name")
            if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', self.namea):
                self.count += 1
                proceed_name()
            else:
                not_name()

        def get_phone():
            # rint("GEt mobile")
            self.mobilea = self.mobile.get()
            counter = 0
            for l in range(58, 128):
                if chr(l) in str(self.mobilea):
                    counter += 1
            if (len(self.mobilea)) != 11:
                counter += 1

            if counter != 0:
                not_mobile()
            else:
                self.count += 1
                proceed_mobile()

        def get_email():
            # #print("CAliing get Email")
            self.emaila = self.email.get()
            int_counter = 0
            str_counter = 0
            n_counter = 0
            for p in range(1, 10):
                if str(p) in str(self.emaila):
                    int_counter += 1
            for o in range(58, 128):
                if chr(o) in str(self.emaila):
                    str_counter += 1
            if '@' in str(self.emaila):
                n_counter += 1
            if '.com' in str(self.emaila):
                n_counter += 1
            # #print(n_counter,str_counter,int_counter)
            if str_counter != 0 and int_counter >= 0 and n_counter == 2:
                proceed_email()
                self.count += 1
            else:
                not_email()

        def get_address():
            #  #print("caling get_address")
            self.addressa = self.address.get()
            counter = 0
            for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if str(j) in str(self.addressa):
                    counter += 1

            if self.addressa == '':
                not_address()
            elif counter == len(str(self.addressa)):
                not_address()
            else:
                self.count += 1
                proceed_address()

        get_name()
        get_address()
        get_email()
        get_phone()
        if self.count == 4:
            insert()

    def Update(self):
        self.db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        self.cursor = self.db.cursor()

        def updated_values():
            msg = Message(self.frame7, text="Updated Values")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=250, y=200)
            msg.after(4000, lambda: msg.destroy())

        def update_name():

            insert_val = (self.upd, int(self.ids))
            sql = """update  Customer set Cname = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def update_address():
            insert_val = (self.upd, self.ids)
            sql = """update  Customer set Address = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def update_phone():
            insert_val = (self.upd, (self.ids))
            sql = """update  Customer set Mobile = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val, )
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def update_email():
            self.cursor = self.db.self.cursor()
            insert_val = (self.upd, self.ids)
            sql = """update  Customer set Email = %s where ID =%s"""
            try:
                self.cursor.execute(sql, insert_val)
                self.db.commit()
                updated_values()
            except:
                self.db.rollback()

        def clear_value():
            self.new.set("")

        def check():
            def proceed_name():
                msg = Message(self.frame7, text="Correct Name")
                msg.config(width=100, bg="honeydew3", fg="blue", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_name()

            def proceed_address():
                msg = Message(self.frame7, text="Correct Address")
                msg.config(width=100, bg="honeydew3", fg="blue", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_address()

            def proceed_email():
                msg = Message(self.frame7, text="Correct Email")
                msg.config(width=100, bg="honeydew3", fg="blue", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_email()

            def proceed_phone():
                msg = Message(self.frame7, text="Correct Number")
                msg.config(width=100, bg="honeydew3", fg="blue", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                update_phone()

            def not_name():
                msg = Message(self.frame7, text="Incorrect Name")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                clear_value()

            def not_address():
                msg = Message(self.frame7, text="Incorrect Address")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(4000, lambda: msg.destroy())
                clear_value()

            def not_phone():
                msg = Message(self.frame7, text="Incorrect Phone Number")
                msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
                msg.place(x=490, y=150)
                msg.after(5000, lambda: msg.destroy())
                clear_value()

            def not_email():
                msg = Message(self.frame7, text="Incorrect Email", font="times 12")
                msg.config(width=150, bg="honeydew3", fg="red")
                msg.place(x=490, y=150)
                msg.after(5000, lambda: msg.destroy())
                clear_value()

            def valid_id():
                msg = Message(self.frame7, text="Valid ID")
                msg.config(width=100, bg="honeydew3", fg="blue", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())

            def invalid_id():
                msg = Message(self.frame7, text="Invalid ID")
                msg.config(width=100, bg="honeydew3", fg="red", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())

            def no_id():
                msg = Message(self.frame7, text="No ID")
                msg.config(width=100, bg="honeydew3", fg="red", font="arial 13")
                msg.place(x=490, y=100)
                msg.after(4000, lambda: msg.destroy())

            def get_name():
                if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', self.upd):
                    proceed_name()
                    update_name()
                else:
                    not_name()

            def get_address():
                counter = 0
                for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if str(j) in str(self.upd):
                        counter += 1
                if counter != len(str(self.upd)):
                    proceed_address()
                    update_address()
                else:
                    not_address()

            def get_phone():
                counter = 0
                for l in range(58, 128):
                    if chr(l) in str(self.upd):
                        counter += 1

                if (len(self.upd)) != 11:
                    counter += 1

                if counter != 0:
                    not_phone()
                else:
                    proceed_phone()
                    update_phone()

            def get_email():
                int_counter = 0
                str_counter = 0
                n_counter = 0
                for p in range(1, 10):
                    if str(p) in str(self.upd):
                        int_counter += 1
                for o in range(58, 128):
                    if chr(o) in str(self.upd):
                        str_counter += 1
                if '@' in str(self.upd):
                    n_counter += 1
                if '.com' in str(self.upd):
                    n_counter += 1
                if str_counter != 0 and int_counter != 0 and n_counter == 2:
                    proceed_email()
                    update_email()
                else:
                    not_email()

            self.ids = self.ID.get()
            counter = 0
            for i in range(58, 128):
                if chr(i) in str(self.ids):
                    counter += 1
                if self.ids == '':
                    counter += 1
                    no_id()
                else:

                    if counter != 0:
                        invalid_id()
                    else:
                        valid_id()
            self.val = self.value.get()
            self.upd = self.new.get()
            if self.val == "Name":
                # print(" Calling get_name")
                get_name()
            elif self.val == "Address":
                # print("calling get_Address")
                get_address()
            elif self.val == "Mobile":
                # print("Caliing get_phone")
                get_phone()
            elif self.val == "Email":
                # print("Calling ge_email")
                get_email()

        check()

    def delete(self):
        self.Id = self.del_id.get()

        def no_id():
            msg = Message(self.frame6, text="Invalid ID")
            msg.config(width=150, bg="honeydew3", fg="red", font="times 12")
            msg.place(x=400, y=100)
            msg.after(3000, lambda: msg.destroy())
            self.ID.set('')

        def del_message():
            msg = Message(self.frame6, text="Customer Deleted")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=200, y=150)
            msg.after(3000, lambda: msg.destroy())

        def clear():
            self.ID.set('')

        if self.Id == '':
            msg = Message(self.frame6, text="Please Enter an ID")
            msg.config(width=250, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=400, y=100)
            msg.after(3000, lambda: msg.destroy())

        else:

            counter = 0
            for l in range(58, 128):
                #  print("running loop")
                if chr(l) in str(self.Id):
                    counter += 1
            if counter != 0:
                no_id()
                clear()
            else:
                del_message()
                sql = """delete from Customer where ID =%s"""
                insert_val = self.Id,
                try:
                    self.cursor.execute(sql, insert_val)
                    self.db.commit()
                    clear()
                except:
                    no_id()

                    self.db.rollback()



class Booking(object):

    def __init__(self):

        """defined a connection of database

         to be used in all methods"""
        self.db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        self.cursor = self.db.cursor()

        self.book_wid = Tk()
        self.book_wid.title("Booking Panel")
        self.book_wid.iconbitmap('Icon.ico')
        self.book_wid.geometry("1920x1080+0+0")
        self.book_wid.configure(bg="cadetblue")
        self.lab = Label(self.book_wid, text="Booking Panel", bg="cadetblue", font=("Helvetica", 30))
        self.lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.lgbutton = Button(self.book_wid, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                               command=lambda: self.book_wid.destroy())
        self.lgbutton.place(x=1435, y=0)
        self.back = Button(self.book_wid, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                           command=lambda: [self.book_wid.destroy(), self.new_win()])
        self.back.place(x=30, y=0)
        self.booking = Frame(self.book_wid, height=400, width=770, bg="honeydew3", highlightthickness=30,
                             highlightcolor="cadetblue4",
                             highlightbackground="cadetblue")
        self.booking.grid(row=2, column=0)
        self.cancel_booking = Frame(self.book_wid, height=400, width=770, bg="honeydew3", highlightthickness=30,
                                    highlightcolor="cadetblue4",
                                    highlightbackground="cadetblue")
        self.cancel_booking.grid(row=3, column=1)
        self.change_event = Frame(self.book_wid, height=400, width=770, bg="honeydew3", highlightthickness=30,
                                  highlightcolor="cadetblue4",
                                  highlightbackground="cadetblue")
        self.change_event.grid(row=3, column=0)
        self.search_booking = Frame(self.book_wid, height=400, width=770, bg="honeydew3", highlightthickness=30,
                                    highlightcolor="cadetblue4",
                                    highlightbackground="cadetblue")
        self.search_booking.grid(row=2, column=1)
        self.label5 = Label(self.booking, text="Booking", font=("times", 30), bg="honeydew3")
        self.label6 = Label(self.cancel_booking, text="Cancel Booking", font=("times", 30), bg="honeydew3")
        self.label7 = Label(self.change_event, text="Change Event", font=("times", 30), bg="honeydew3")
        self.label8 = Label(self.search_booking, text="Search booking", font=("times", 30), bg="honeydew3")
        self.label5.place(x=250, y=0)
        self.label6.place(x=250, y=0)
        self.label7.place(x=250, y=0)
        self.label8.place(x=250, y=0)

        """Search Window"""
        self.name_search = StringVar()
        self.label_name_search = Label(master=self.search_booking, text="Name", font="times 15", bg="honeydew3")
        self.label_name_search.place(x=100, y=100)

        self.entry_name_search = Entry(master=self.search_booking, font="times 15", textvariable=self.name_search)
        self.entry_name_search.place(x=200, y=100, height=30, width=185)

        self.button_search = Button(master=self.search_booking, text="Search", font="times 13", bd=3, height=1,
                                    cursor="hand2", width=10, bg="cadet blue",
                                    command=lambda: Booking.Search_b(self))
        self.button_search.place(x=150, y=200)

        self.button_search_all = Button(master=self.search_booking, text="Show All", font="times 13", bd=3, height=1,
                                        cursor="hand2", width=10,
                                        bg="cadet blue", command=lambda: Booking.search_all_b(self))
        self.button_search_all.place(x=300, y=200)

        """Booking Window Work"""

        self.name = StringVar()
        self.event = StringVar()
        self.date_day = StringVar()
        self.date_month = StringVar()
        self.package = StringVar()
        self.price = StringVar()

        self.label_name = Label(master=self.booking, text="Name", font="times 15", bg="honeydew3")
        self.label_name.place(x=100 + 50, y=150 - 50 - 50)
        self.label_name = Label(master=self.booking, text="Event", font="times 15", bg="honeydew3")
        self.label_name.place(x=100 + 50, y=200 - 50 - 50)
        self.label_name = Label(master=self.booking, text="Event Date", font="times 15", bg="honeydew3")
        self.label_name.place(x=100 + 50, y=250 - 50 - 50)
        self.label_name = Label(master=self.booking, text="Package", font="times 15", bg="honeydew3")
        self.label_name.place(x=100 + 50, y=300 - 50 - 50)
        self.entry_name = Entry(master=self.booking, font="times 15", textvariable=self.name)
        self.entry_name.place(x=220 + 50, y=150 - 50 - 50, height=30, width=185)
        self.event_option = OptionMenu(self.booking, self.event, "Wedding", "Mehendi", "Valima Reception", "Birthday",
                                       "Engagement")
        self.event.set("Wedding")
        self.event_option.config(font=("times", 13), bg="honeydew3", highlightbackground="cadetblue",
                                 highlightcolor="cadetblue4", width=16)
        self.event_option.place(x=220 + 50, y=200 - 50 - 50)
        self.date_option = ttk.Combobox(master=self.booking, textvariable=self.date_day,
                                        values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
                                                '13', '14', '15', '16', '17', '18', '19', '20'
                                            , '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
        self.date_option.config(width=5, font="times 13")
        self.date_option.place(x=220 + 50, y=250 - 50 - 50)
        self.date_day.set('01')

        self.month_option = ttk.Combobox(master=self.booking, textvariable=self.date_month,
                                         values=["January", "February", "March", "April", "May", "June", "July",
                                                 "August", "September", "October", "November", "December"])
        self.month_option.config(width=10, font="times 13")
        self.date_month.set("January")
        self.month_option.place(x=290 + 50, y=250 - 50 - 50)
        self.event_option = OptionMenu(self.booking, self.package, "Bronze", "Silver", "Gold", "Platinium")
        self.package.set("Bronze")
        self.event_option.config(font=("times", 13), bg="honeydew3", highlightbackground="cadetblue",
                                 highlightcolor="cadetblue4", width=16)
        self.event_option.place(x=220 + 50, y=300 - 50 - 50)
        self.label_price = Label(master=self.booking, text="Price", font="times 15", bg="honeydew3")
        self.label_price.place(x=150, y=250)
        self.entry_price = Entry(master=self.booking, font='times 15', textvariable=self.price)
        self.entry_price.place(x=270, y=250, width=185, height=30)
        self.submit = Button(master=self.booking, text="Submit", font="times 13", bd=3, height=1, cursor="hand2",
                             width=10, bg="cadet blue",
                             command=lambda: Booking.add_booking_b(self))
        self.submit.place(x=280, y=350 - 50)
        self.clear = Button(master=self.booking, text="Clear", font="times 13", bd=3, height=1, width=10,
                            cursor="hand2",
                            bg="cadet blue",
                            command=lambda: [self.name.set(""), self.date_day.set("01"), self.date_month.set("January"),
                                             self.package.set("Bronze")])
        self.clear.place(x=170, y=350 - 50)
        """Delete Booking window work"""
        self.Id = StringVar()
        self.id_label = Label(master=self.cancel_booking, text="Booking ID", font="times 15", bg="honeydew3")
        self.id_label.place(x=100, y=100)
        self.id_label = Entry(master=self.cancel_booking, textvariable=self.Id, font="times 15", bg="white")
        self.id_label.place(x=200, y=100, height=30, width=185)
        self.del_button = Button(master=self.cancel_booking, bd=3, width=10, text=" Sumbit", cursor="hand2",
                                 font="times 13", bg="cadet blue", command=lambda: Booking.delete_b(self))
        self.del_button.place(x=250, y=200)

        """Update BOoking Widnow"""

        self.name_u = StringVar()
        self.event_u = StringVar()
        self.Id_u = StringVar()
        self.label_id_u = Label(master=self.change_event, text="ID", font="times 15", bg="honeydew3")
        self.label_id_u.place(x=100 + 50, y=50)
        self.entry_id_u = Entry(master=self.change_event, textvariable=self.Id_u, font="times 13")
        self.entry_id_u.place(x=200 + 50 + 20, y=50)
        self.label_name_u = Label(master=self.change_event, text="Name", font="times 15", bg="honeydew3")
        # self.label_name_u.place(x=180,y=50)
        self.label_name_u.place(x=100 + 50, y=100)
        self.label_name_u = Label(master=self.change_event, text="Event", font="times 15", bg="honeydew3")
        self.label_name_u.place(x=100 + 50, y=150)
        self.entry_name_u = Entry(master=self.change_event, textvariable=self.name_u, font="times 13")
        self.entry_name_u.place(x=200 + 50 + 20, y=100)
        self.event_u_o = OptionMenu(self.change_event, self.event_u, "Wedding", "Mehendi", "Valima Reception",
                                    "Birthday", "Engagement")
        self.event_u_o.config(font=("times", 13), bg="honeydew3", highlightbackground="cadetblue",
                              highlightcolor="cadetblue4", width=15)
        self.event_u_o.place(x=200 + 50 + 20, y=150)
        self.event_u.set('Wedding')
        self.button_change = Button(master=self.change_event, text="Change", font="times 13", cursor="hand2", width=10,
                                    bd=3, bg="cadet blue",
                                    command=lambda: Booking.update_booking_b(self))
        self.button_change.place(x=250, y=220)
        self.button_clear = Button(master=self.change_event, text="Reset", font="times 13", cursor="hand2", width=10,
                                   bd=3,
                                   bg="cadet blue",
                                   command=lambda: [self.Id_u.set(''), self.name_u.set(""), self.event_u.set('')])
        self.button_clear.place(x=140, y=220)
        self.booking.mainloop()

    def search_all_b(self):
        def display():
            msg = Message(master=self.search_booking, text="Displaying All Booking")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        # name_search = name_search,
        sql = """select * from Booking """
        try:
            cursor.execute(sql)
            cursor.fetchall()
            display()
        except:
            pass
        res = []
        for i in cursor:
            res.append(i)

        tk = Tk()
        tk.geometry("900x500")
        tk.config(bg="cadet blue")
        tk.title("Booking Database")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)  # side=LEFT,fill=Y)
        f.config(bg="cadet blue")
        s = Scrollbar(tk)
        c = Canvas(tk, width=900, height=500, bg="white", yscrollcommand=s)
        s.pack(side=RIGHT, fill=Y)

        fr = Frame(c, bg="white")
        fr.pack()
        c.pack()  # side="left",fill="both")
        c.create_window(0, 0, window=fr, anchor='nw')
        s.config(command=c.yview)
        lst = ["ID", "Name", "Event", "Package", "Booking Date", 'Event Date', 'Price']
        for i in range(len(lst)):
            if i == 1:
                width = 15
            else:
                width = 10
            Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "#f5f5f5"
                else:
                    color = "white"
                if j == 1:
                    width = 15
                else:
                    width = 10
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
        tk.mainloop()

    def Search_b(self):
        name_search = self.name_search.get()

        # print(name_search)
        def improper():
            msg = Message(master=self.search_booking, text="Enter Proper Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        def no_name():
            msg = Message(master=self.search_booking, text="Please Enter Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.name_search.set('')

        def name_searching():
            msg = Message(master=self.search_booking, text="Searching for booking")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=100)
            msg.after(2000, lambda: msg.destroy())

        def name_found():
            msg = Message(master=self.search_booking, text="Bookings Found")
            msg.config(width=150, bg="honeydew3", fg="Blue", font="times 12")
            msg.place(x=490, y=150)
            msg.after(2000, lambda: msg.destroy())

        def name_not_found():
            msg = Message(master=self.search_booking, text="No Bookings were  Found")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(2000, lambda: msg.destroy())

        counter = 0

        if name_search == '':
            counter += 1
            no_name()
        else:
            if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', name_search):
                name_searching()
            else:
                counter += 1

        def search():
            res = []
            for i in cursor:
                res.append(i)
            if len(res) > 0:
                name_found()
                tk = Tk()
                tk.geometry("900x500")
                tk.config(bg="cadet blue")
                tk.title("Booking Database")
                f = Frame(tk)
                f.pack(fill=Y)  # side=LEFT,fill=Y)
                f.config(bg="white")
                s = Scrollbar(tk)
                c = Canvas(tk, width=900, height=500, bg="white", yscrollcommand=s.set)
                s.pack(side=LEFT, fill=Y)

                fr = Frame(c, bg="white")
                fr.pack()
                c.pack()  # side="left",fill="both")
                c.create_window(0, 0, window=fr, anchor='nw')
                s.config(command=c.yview)
                lst = ["ID", "Name", "Event", "Package", "Booking Date", 'Event Date', 'Price']
                for i in range(len(lst)):
                    if i == 1:
                        width = 15
                    else:
                        width = 10
                    Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0,
                                                                                                         column=i)
                for i in range(len(res)):
                    for j in range(len(res[i])):
                        if i % 2 == 0:
                            color = "#f5f5f5"
                        else:
                            color = "white"
                        if j == 1:
                            width = 15
                        else:
                            width = 10
                        Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
                tk.mainloop()

        if counter == 0:
            db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
            cursor = db.cursor()
            name_search = name_search,
            sql = """select * from Booking where Name = %s"""
            try:
                cursor.execute(sql, name_search)
                cursor.fetchall()
                name_searching()
                search()
            except:
                improper()

    def update_booking_b(self):
        name_u = self.name_u.get()
        event_u = self.event_u.get()
        id_u = self.Id_u.get()
        val_u = name_u, event_u, id_u

        def incomplete():
            msg = Message(master=self.change_event, text="Complete All fields")
            msg.config(width=150, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def proper():
            msg = Message(master=self.change_event, text="Booking Updated")
            msg.config(width=150, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def improper():
            msg = Message(master=self.change_event, text="Invalid Details Check again")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def improper_name():
            msg = Message(master=self.change_event, text="Invalid Name")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=150)
            msg.after(4000, lambda: msg.destroy())

        counter = 0
        for l in range(58, 128):
            if chr(l) in str(id_u):
                counter += 1

        if event_u == '':
            incomplete()
            counter += 1
        if id_u == '':
            counter += 1
            incomplete()

        if name_u == '':
            counter += 1
        else:
            if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', name_u):
                counter = counter
            else:
                counter += 1
                improper_name()

        if counter == 0:
            sql = """update Booking set Name = %s,Event = %s where Id = %s"""
            try:

                self.cursor.execute(sql, val_u)
                self.db.commit()
                proper()
            except:
                improper()
                self.db.rollback()
        else:
            improper()
            self.db.rollback()

    def delete_b(self):
        """Fetches id form ui and and deletes from database """
        Id = self.Id.get()

        def proceed_delete():

            msg = Message(master=self.cancel_booking, text="Booking Deleted")
            msg.config(width=150, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())

        def not_delete():
            msg = Message(master=self.cancel_booking, text="Enter Correct ID")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.Id.set('')

        def no_id():
            msg = Message(master=self.cancel_booking, text="Please Enter an ID")
            msg.config(width=150, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=100)
            msg.after(4000, lambda: msg.destroy())
            self.Id.set('')

        counter = 0

        if Id == '':
            counter += 1
            no_id()
        else:
            for l in range(58, 128):
                print("Loop")

                if chr(l) in str(Id):
                    print(counter)
                    counter += 1
            if counter == 0:
                sql = """delete from Booking where ID=%s"""
                new_val = Id,
                try:
                    self.cursor.execute(sql, new_val)
                    self.db.commit()
                    proceed_delete()
                except:
                    print("Except")
                    self.db.rollback()
                    not_delete()
            else:
                not_delete()

    def add_booking_b(self):
        """Fetchoes values from the user interface and inserts it in the data base"""

        def improper():
            msg = Message(master=self.booking, text="Enter Correct Values")
            msg.config(width=100, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=150)
            msg.after(4000, lambda: msg.destroy())

        def proper():
            msg = Message(master=self.booking, text="Booking Succesfill")
            msg.config(width=100, bg="honeydew3", fg="Green", font="times 12")
            msg.place(x=490, y=150)
            msg.after(4000, lambda: msg.destroy())

        def incomplete():
            msg = Message(master=self.booking, text="Enter Complete Values")
            msg.config(width=100, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=150)
            msg.after(4000, lambda: msg.destroy())

        def date_error():
            msg = Message(master=self.booking, text="Incorrect Date Please Check Again")
            msg.config(width=100, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=200)
            msg.after(4000, lambda: msg.destroy())

        def empty_name():
            msg = Message(master=self.booking, text="Name cannot be empty")
            msg.config(width=100, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=50)
            msg.after(4000, lambda: msg.destroy())

        def invalid_price():
            msg = Message(master=self.booking, text="Invalid Price")
            msg.config(width=100, bg="honeydew3", fg="Red", font="times 12")
            msg.place(x=490, y=200)
            msg.after(4000, lambda: msg.destroy())

        count = 0
        name = self.name.get()
        date_month = self.date_month.get()
        date_day = self.date_day.get()
        event_date = self.date_day.get() + ',' + self.date_month.get()
        package = self.package.get()
        event = self.event.get()
        today = date.today()
        book_date = today.strftime("%d,%B")
        price = self.price.get()
        sql = """insert into Booking(Name,Event,Package,Booking_Date,Ocassion_Date,Price) values(%s,%s,%s,%s,%s,%s)"""
        val = (name, event, package, book_date, event_date, price)
        if package == '' or self.date_day.get() == '' or self.date_month.get() == '':
            count += 1
            incomplete()

        if date_month in ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]:
            count = count
        else:
            improper()
            count += 1
        if date_day in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20'
            , '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
            count = count
        else:
            improper()
            count += 1

        if re.findall(r'[A-Z][a-z]{2,25}\s[A-Z][a-z]{2,25}', name):
            count = count
        else:
            if name == '':
                empty_name()
                count += 1
            else:
                improper()
                count += 1

        if date_day == '31' and date_month == "February":
            count += 1
            date_error()
        if date_day == '30' and date_month == "February":
            count += 1
            date_error()
        if date_day == '29' and date_month == "February":
            count += 1
            date_error()
        if re.findall(r'^[1-9][0-9]{4,5}$', price):
            count = count
            # valid_price()
        else:
            invalid_price()
            count += 1
        if count == 0:
            try:
                self.cursor.execute(sql, val)
                self.db.commit()
                proper()
            except:
                self.db.rollback()
                improper()





class Inventory:
    def __init__(self):
        from tkinter import ttk
        tk2 = Tk()
        tk2.geometry("1920x1080+0+0")
        tk2.configure(bg="cadetblue")
        tk2.iconbitmap('Icon.ico')
        lab = Label(tk2, text="Inventory", bg="cadetblue", font=("Helvetica", 30))
        lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        lgbutton = Button(tk2, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                          command=lambda: tk2.destroy())
        lgbutton.place(x=1435, y=0)
        back = Button(tk2, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                      command=lambda: [tk2.destroy(), self.new_win()])
        back.place(x=30, y=0)
        frame5i = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                        highlightbackground="cadetblue")
        frame5i.grid(row=2, column=0)
        # frame6=Frame(tk2,height=400,width=770,bg="honeydew3",highlightthickness=30,highlightcolor="cadetblue4",highlightbackground="cadetblue")
        # frame6.grid(row=3,column=1)
        frame7i = Frame(tk2, height=400, width=1000, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                        highlightbackground="cadetblue")
        frame7i.grid(row=3, column=0, columnspan=2)
        frame8i = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                        highlightbackground="cadetblue")
        frame8i.grid(row=2, column=1)
        label5 = Label(frame5i, text="Add Inventory", font=("times", 30), bg="honeydew3")
        # label6=Label(frame6,text="Delete Inventory",font=("times", 30),bg="honeydew3")
        label7 = Label(frame7i, text="Search Inventory", font=("times", 30), bg="honeydew3")
        label8 = Label(frame8i, text="Delete Inventory", font=("times", 30), bg="honeydew3")
        label5.place(x=240, y=0)
        # label6.place(x=240,y=0)
        label7.place(x=330, y=0)
        label8.place(x=230, y=0)

        label9 = Label(frame5i, text="Item :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame5i, text="Quantity :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=100)
        label10.place(x=200, y=150)
        i = StringVar()
        i.set("Chair")
        self.entry90 = OptionMenu(frame5i, i, "Chair", "Table", "Glass", "Plate", "Spoon", "Fan", "Ac")
        self.entry90.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry90.place(x=330, y=100, height=30, width=185)
        self.entry100 = Entry(frame5i, font=("times", 13))
        self.entry100.place(x=330, y=150, height=30)
        button1 = Button(frame5i, text="Add", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.addi(i.get(), self.entry100.get(), frame5i))
        button1.place(x=300, y=200)

        label9 = Label(frame8i, text="Item :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame8i, text="Quantity :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=100)
        label10.place(x=200, y=150)
        i1 = StringVar()
        i1.set("Chair")
        self.entry91 = OptionMenu(frame8i, i1, "Chair", "Table", "Glass", "Plate", "Spoon", "Fan", "Ac")
        self.entry91.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry91.place(x=330, y=100, height=30, width=185)
        self.entry10 = Entry(frame8i, font=("times", 13))
        self.entry10.place(x=330, y=150, height=30)
        button1 = Button(frame8i, text="Delete", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.deletei(i1.get(), self.entry10.get(), frame8i))
        button1.place(x=300, y=200)

        label9 = Label(frame7i, text="Item :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame7i, text="Quantity :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=100)
        label10.place(x=200, y=150)
        i2 = StringVar()
        i2.set("Chair")
        self.entry92 = OptionMenu(frame7i, i2, "Chair", "Table", "Glass", "Plate", "Spoon", "Fan", "Ac")
        self.entry92.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry92.place(x=330, y=100, height=30, width=185)
        button1 = Button(frame7i, text="Show Available Quantity", width=30, bg="cadetblue", bd=3,
                         font=("Helvetica", 13), command=lambda: self.showi(i2.get(), frame7i))
        button1.place(x=300, y=200)
        button2 = Button(frame7i, text="Show All Inventory", width=30, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.searchalli(tk2))
        button2.place(x=300, y=230)

    def searchalli(self, tk):
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        sql = """select * from inventory """
        try:
            cursor.execute(sql)
            cursor.fetchall()
        except:
            pass
        res = []
        for i in cursor:
            res.append(i)

        tk = Toplevel(tk)
        tk.geometry("400x200+280+100")
        tk.config(bg="grey")
        tk.title("Inventory Database")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)
        f.config(bg="white")
        c = Canvas(tk, width=400, height=200, bg="cadetblue")  # , yscrollcommand=s)

        fr = Frame(c, bg="cadetblue")
        fr.pack()
        c.pack()
        c.create_window(0, 0, window=fr, anchor='nw')
        lst = ["Item", "Quantity"]
        for i in range(len(lst)):
            if i == 1:
                width = 15
            else:
                width = 10
            Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "honeydew3"
                else:
                    color = "white"
                if j == 1:
                    width = 15
                else:
                    width = 20
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)

    def addi(self, a, b, frame):
        print(a)
        print(b)
        import MySQLdb
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        try:
            cursor.execute("""update inventory set quantity=quantity+%s where item='%s'""" % (b, a))
            db.commit()
            self.entry100.delete(0, END)
            msg = Message(frame, text="Succesfull")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
        except:
            db.rollback()
            msg = Message(frame, text="Unsuccesfull")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())

    def deletei(self, a, b, frame):
        print(a)
        print(b)
        b = int(b)
        import MySQLdb
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        cursor.execute("""select quantity from inventory where item=%s""", (a,))
        result = cursor.fetchone()
        result = int(result[0])
        if result >= b:
            cursor.execute("""update inventory set quantity=quantity-%s where item='%s'""" % (b, a))
            db.commit()
            msg = Message(frame, text="Succesfull")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
            self.entry10.delete(0, END)
        else:
            db.rollback()
            msg = Message(frame, text="Quantity isn't enough to delete")
            msg.config(width=700, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())

    def showi(self, a, frame):
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        cursor.execute("""select quantity from inventory where item=%s""", (a,))
        result = cursor.fetchone()
        show_label1 = Label(frame, text=result[0], bd=10, width=20).place(x=330, y=150)
        db.close()





class Package:
    def __init__(self):
        tk2 = Tk()
        tk2.geometry("1920x1080+0+0")
        tk2.configure(bg="cadetblue")
        tk2.iconbitmap('Icon.ico')
        lab = Label(tk2, text="Admin", bg="cadetblue", font=("Helvetica", 30))
        lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        lgbutton = Button(tk2, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                          command=lambda: tk2.destroy())
        lgbutton.place(x=1435, y=0)
        back = Button(tk2, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                      command=lambda: [tk2.destroy(), self.new_win()])
        back.place(x=30, y=0)
        frame5 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame5.grid(row=2, column=0)
        frame6 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame6.grid(row=3, column=0)
        frame7 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame7.grid(row=3, column=1)
        frame8 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame8.grid(row=2, column=1)
        label5 = Label(frame5, text="Add Package", font=("times", 30), bg="honeydew3")
        label6 = Label(frame7, text="Delete Package", font=("times", 30), bg="honeydew3")
        label7 = Label(frame6, text="Update Package", font=("times", 30), bg="honeydew3")
        label8 = Label(frame8, text="Search Package", font=("times", 30), bg="honeydew3")
        label5.place(x=250, y=0)
        label6.place(x=250, y=0)
        label7.place(x=250, y=0)
        label8.place(x=250, y=0)

        label69 = Label(frame5, text="Package Name :", font=("times", 15), bg="honeydew3")
        label69.place(x=0, y=0)
        self.entry69 = Entry(frame5, font=("times", 13))
        self.entry69.place(x=0, y=30, height=30, width=185)
        label9 = Label(frame5, text="Themes :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame5, text="No. Of Guests :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=50)
        label10.place(x=200, y=100)
        label9 = Label(frame5, text="Duration :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame5, text="Functions :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=150)
        label10.place(x=200, y=200)
        label9 = Label(frame5, text="Price :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=250)
        i = StringVar()
        i.set("Hollywood Night")
        self.entry9 = OptionMenu(frame5, i, "Hollywood Night", "Casual Night", "Rose Flowers", "Fun Forest",
                                 "Spoony Hood", "Laveder Blush", "Honeydew Houl")
        self.entry9.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                           highlightcolor="cadetblue4")
        self.entry9.place(x=330, y=50, height=30, width=185)
        i1 = StringVar()
        i1.set("150")
        self.entry10 = OptionMenu(frame5, i1, "150", "250", "350", "450", "550", "650", "750")
        self.entry10.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry10.place(x=330, y=100, height=30, width=185)
        i2 = StringVar()
        i2.set("2")
        self.entry11 = OptionMenu(frame5, i2, "2", "3", "4", "5", "6")
        self.entry11.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry11.place(x=330, y=150, height=30, width=185)
        i3 = StringVar()
        i3.set("Wedding")
        self.entry12 = OptionMenu(frame5, i3, "Wedding", "Mehendi", "Valima Reception", "Birthday", "Engagement")
        self.entry12.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry12.place(x=330, y=150, height=30, width=185)
        self.entry12.place(x=330, y=200, height=30, width=185)
        self.entry13 = Entry(frame5, font=("times", 13))
        self.entry13.place(x=330, y=250, height=30, width=185)
        button1 = Button(frame5, text="Add", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.addp(self.entry69.get(), i.get(), i1.get(), i2.get(), i3.get(),
                                                   self.entry13.get(), frame5))
        button1.place(x=300, y=300)

        label690 = Label(frame6, text="Package Name :", font=("times", 15), bg="honeydew3")
        label690.place(x=0, y=0)
        self.entry690 = Entry(frame6, font=("times", 13))
        self.entry690.place(x=0, y=30, height=30, width=185)
        label9 = Label(frame6, text="Themes :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame6, text="No. Of Guests :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=50)
        label10.place(x=200, y=100)
        label9 = Label(frame6, text="Duration :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame6, text="Functions :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=150)
        label10.place(x=200, y=200)
        label9 = Label(frame6, text="Price :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=250)
        i0 = StringVar()
        i0.set("Hollywood Night")
        self.entry90 = OptionMenu(frame6, i0, "Hollywood Night", "Casual Night", "Rose Flowers", "Fun Forest",
                                  "Spoony Hood", "Laveder Blush", "Honeydew Houl")
        self.entry90.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                            highlightcolor="cadetblue4")
        self.entry90.place(x=330, y=50, height=30, width=185)
        i10 = StringVar()
        i10.set("150")
        self.entry100 = OptionMenu(frame6, i10, "150", "250", "350", "450", "550", "650", "750")
        self.entry100.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                             highlightcolor="cadetblue4")
        self.entry100.place(x=330, y=100, height=30, width=185)
        i20 = StringVar()
        i20.set("2")
        self.entry110 = OptionMenu(frame6, i20, "2", "3", "4", "5", "6")
        self.entry110.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                             highlightcolor="cadetblue4")
        self.entry110.place(x=330, y=150, height=30, width=185)
        i30 = StringVar()
        i30.set("Wedding")
        self.entry120 = OptionMenu(frame6, i30, "Wedding", "Mehendi", "Valima Reception", "Birthday", "Engagement")
        self.entry120.config(font=("times", 13), bg="honeydew3", height=30, highlightbackground="cadetblue",
                             highlightcolor="cadetblue4")
        self.entry120.place(x=330, y=150, height=30, width=185)
        self.entry120.place(x=330, y=200, height=30, width=185)
        self.entry130 = Entry(frame6, font=("times", 13))
        self.entry130.place(x=330, y=250, height=30, width=185)
        button1 = Button(frame6, text="Update", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.updatep(self.entry690.get(), i0.get(), i10.get(), i20.get(), i30.get(),
                                                      self.entry130.get(), frame6))
        button1.place(x=300, y=300)

        label11 = Label(frame7, text="Package Name :", font=("times", 15), bg="honeydew3")
        # label12=Label(frame7,text="Updated Password :",font=("times", 15),bg="honeydew3")
        label11.place(x=200, y=100)
        # label12.place(x=168,y=150)
        self.entry5 = Entry(frame7, font=("times", 13))
        self.entry5.place(x=330, y=100, height=30)
        # self.entry6=Entry(frame7,font=("times", 13))
        # self.entry6.place(x=330,y=150,height=30)
        button1 = Button(frame7, text="Delete", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.deletep(self.entry5.get(), frame7))
        button1.place(x=300, y=200)

        label14 = Label(frame8, text="Package Name :", font=("times", 15), bg="honeydew3")
        label14.place(x=200, y=100)
        self.entry7 = Entry(frame8, font=("times", 13))
        self.entry7.place(x=330, y=100, height=30)
        button1 = Button(frame8, text="Search by Name", width=20, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.searchp(self.entry7.get(), frame8))
        button1.place(x=300, y=180)
        button1 = Button(frame8, text="View all Packages", width=20, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.searchallp(tk2))
        button1.place(x=300, y=230)
        tk2.mainloop()

    def searchallp(self, tk):
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        sql = """select * from package """
        try:
            cursor.execute(sql)
            cursor.fetchall()
        except:
            pass
        res = []
        for i in cursor:
            res.append(i)

        tk = Toplevel(tk)
        tk.geometry("1005x500+280+100")
        tk.config(bg="cadetblue")
        tk.title("Package Database")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)
        f.config(bg="white")
        s = Scrollbar(tk)
        c = Canvas(tk, width=1000, height=500, bg="cadetblue", yscrollcommand=s)
        s.pack(side=RIGHT, fill=Y)

        fr = Frame(c, bg="cadetblue")
        fr.pack()
        c.pack()
        c.create_window(0, 0, window=fr, anchor='nw')
        s.config(command=c.yview)
        lst = ["ID", "Package Name", "Theme", "Guest", "Duration", 'Function', 'Price']
        for i in range(len(lst)):
            if i == 1:
                width = 15
            else:
                width = 10
            Label(fr, bg="black", fg="cadetblue", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "honeydew3"
                else:
                    color = "white"
                if j == 1:
                    width = 15
                else:
                    width = 15
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)

    def addp(self, a, b, c, d, e, f, frame):
        try:
            f = int(f)
            try:
                a = int(a)
                msg = Message(frame, text="Name must contain alphabet")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
            except:
                a = a.lower()
                db = MySQLdb.connect("localhost", "root", "test123", "banquet")
                cursor = db.cursor()
                cursor.execute("select * from package")
                data = cursor.fetchall()
                lst = []
                for i in data:
                    lst.append(i[1])
                if len(a) < 3:
                    msg = Message(frame, text="Insert Package name with minimum length of 3")
                    msg.config(width=500, bg="cadetblue")
                    msg.place(x=100, y=0)
                    msg.after(3000, lambda: msg.destroy())
                elif a in lst:
                    msg = Message(frame, text="Package name already have")
                    msg.config(width=500, bg="cadetblue")
                    msg.place(x=100, y=0)
                    msg.after(3000, lambda: msg.destroy())
                else:
                    f = int(f)
                    a = a.replace(" ", "*")
                    cursor.execute(
                        """insert into package (pkg_name,theme,guest,duration,functions,price) values ('%s','%s','%s','%s','%s',%s)""" % (
                        a, b, c, d, e, f))
                    db.commit()
                    msg = Message(frame, text="Added Succesfully")
                    msg.config(width=500, bg="cadetblue")
                    msg.place(x=100, y=0)
                    msg.after(3000, lambda: msg.destroy())
        except:
            msg = Message(frame, text="Enter Price in Integer")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())

    def deletep(self, a, frame):
        str(a)
        a = a.replace(" ", "*")
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from package")
        data = cursor.fetchall()
        lst = []
        for i in data:
            lst.append(i[1])
        if a in lst:
            cursor.execute("""delete from package where pkg_name='%s'""" % (a,))
            db.commit()
            msg = Message(frame, text="Delete Succesfully")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
        else:
            msg = Message(frame, text="Package name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())

    def updatep(self, a, b, c, d, e, f, frame):
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from package")
        data = cursor.fetchall()
        lst = []
        for i in data:
            lst.append(i[1])
        if a in lst:
            try:
                f = int(f)
                cursor.execute(
                    """update package set theme='%s',guest='%s',duration='%s',functions='%s',price=%s where pkg_name='%s'"""
                    % (b, c, d, e, f, a))
                db.commit()
                msg = Message(frame, text="Update Succesfully")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
            except:
                msg = Message(frame, text="Enter Price in Integer")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
        else:
            msg = Message(frame, text="Name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())

    def searchp(self, a, frame):
        str(a)
        a = a.replace(" ", "*")
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from package")
        data = cursor.fetchall()
        lst = []
        text = Text(frame, bd=5)
        for i in data:
            lst.append(i[1])
        if a in lst:
            for i in data:
                if a in i:
                    text.place(x=0, y=0, height=250, width=200)
                    ok = i[1].replace("*", " ")
                    a = "ID:\n-----%s\nPackage Name:\n-----%s\nTheme:\n-----%s\nNo. of Guests:\n-----%s\nDuration:\n-----%s\nFunction:\n-----%s\nPrice:\n-----%s" % (
                    i[0], ok, i[2], i[3], i[4], i[5], i[6])
                    text.insert(END, a)
                    text.after(10000, lambda: text.destroy())
                else:
                    pass
        else:
            self.entry7.delete(0, END)
            msg = Message(frame, text="Name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())





class Admin(Inventory, Package, Booking, Customer,Staff):
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("1920x1080+0+0")
        self.tk.title("Admin")
        self.tk.iconbitmap('Icon.ico')
        self.tk.configure(bg="cadetblue", bd=0)
        self.photo = PhotoImage(file="wed.gif")
        self.label = Label(self.tk, image=self.photo)
        self.label.grid(row=0, column=0)
        self.entry = Entry(self.tk, width=33, bg="cadetblue", bd=0, font=("times", 18))
        self.entry.place(x=610, y=388, height=40)
        self.entry1 = Entry(self.tk, width=33, bg="cadetblue",bd=0, font=("times", 18), show="*")
        self.entry1.place(x=610, y=644, height=40)
        self.button = Button(self.tk, text="Login", bg="cadetblue", bd=3, font=("Helvetica", 13),
                             command=lambda: self.__Login(self.entry.get(), self.entry1.get(), self.tk), width=20,
                             height=2)
        self.button.place(x=700, y=770)

    def __Login(self, a, b, frame):
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        cursor.execute("select * from admin")
        data = cursor.fetchall()
        g_msg = ""
        for i in data:
            if i[1] == a and i[2] == b:
                g_msg = "welcome"
                self.tk.destroy()
                self.new_win()
                break
            else:
                g_msg = "wrong pass"
                self.entry.delete(0, END)
                self.entry1.delete(0, END)
                msg = Message(frame, text="Invalid admin name or password")
                msg.config(width=500, bg="red")
                # msg.after(3000,lambda:msg.destroy())
                msg.place(x=700, y=250)
                msg.after(3000, msg.destroy)

    def new_win(self):
        tk1 = Tk()
        tk1.geometry("1920x1080+0+0")
        tk1.title("Menu")
        tk1.iconbitmap('Icon.ico')

        tk1.configure(bg="cadetblue")
        lab = Label(tk1, text="Banquet Management System", bg="cadetblue", font=("Helvetica", 30))
        lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        lgbutton = Button(tk1, text="Logout", width=5, height=1, bg="cadetblue", bd=5, font=("aerial", 15),
                          command=lambda: tk1.destroy())
        lgbutton.place(x=1435, y=0)
        frame5 = Frame(tk1, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame5.grid(row=2, column=0)
        frame6 = Frame(tk1, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame6.grid(row=2, column=1)
        frame7 = Frame(tk1, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame7.grid(row=3, column=0)
        frame8 = Frame(tk1, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame8.grid(row=3, column=1)
        label5 = Label(frame5, text="Admin", font=("times", 30), bg="honeydew3")
        label6 = Label(frame6, text="Customer/Booking", font=("times", 30), bg="honeydew3")
        label7 = Label(frame7, text="Supervise", font=("times", 30), bg="honeydew3")
        label8 = Label(frame8, text="Staff", font=("times", 30), bg="honeydew3")
        label5.place(x=270, y=0)
        label6.place(x=220, y=0)
        label7.place(x=250, y=0)
        label8.place(x=250, y=0)
        button1 = Button(frame5, text="Admin", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), self.new_win1()])
        button1.place(x=270, y=100)
        button1 = Button(frame7, text="Inventory", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), Inventory.__init__(self)])
        button1.place(x=190, y=100)
        button1 = Button(frame7, text="Package", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), Package.__init__(self)])
        button1.place(x=310, y=100)
        button1 = Button(frame6, text="Booking", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), Booking.__init__(self)])
        button1.place(x=190, y=100)
        button1 = Button(frame6, text="Customer", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), Customer.__init__(self)])
        button1.place(x=310, y=100)
        button1 = Button(frame8, text="Staff", width=10, height=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: [tk1.destroy(), Staff.__init__(self)])
        button1.place(x=270, y=100)

    def new_win1(self):
        tk2 = Tk()
        tk2.geometry("1920x1080+0+0")
        tk2.configure(bg="cadetblue")
        lab = Label(tk2, text="Admin", bg="cadetblue", font=("Helvetica", 30))
        lab.grid(row=0, column=0, rowspan=2, columnspan=2)
        lgbutton = Button(tk2, text="Logout", width=5, bg="cadetblue", bd=5, font=("aerial", 15),
                          command=lambda: tk2.destroy())
        lgbutton.place(x=1435, y=0)
        back = Button(tk2, text="Back <=", width=7, bg="cadetblue", bd=5, font=("aerial", 15),
                      command=lambda: [tk2.destroy(), self.new_win()])
        back.place(x=30, y=0)
        frame5 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame5.grid(row=2, column=0)
        frame6 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame6.grid(row=3, column=1)
        frame7 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame7.grid(row=3, column=0)
        frame8 = Frame(tk2, height=400, width=770, bg="honeydew3", highlightthickness=30, highlightcolor="cadetblue4",
                       highlightbackground="cadetblue")
        frame8.grid(row=2, column=1)
        label5 = Label(frame5, text="Add Admin", font=("times", 30), bg="honeydew3")
        label6 = Label(frame6, text="Delete Admin", font=("times", 30), bg="honeydew3")
        label7 = Label(frame7, text="Update Admin", font=("times", 30), bg="honeydew3")
        label8 = Label(frame8, text="Search Admin", font=("times", 30), bg="honeydew3")
        label5.place(x=250, y=0)
        label6.place(x=250, y=0)
        label7.place(x=250, y=0)
        label8.place(x=250, y=0)

        label9 = Label(frame5, text="Admin Name :", font=("times", 15), bg="honeydew3")
        label10 = Label(frame5, text="Password :", font=("times", 15), bg="honeydew3")
        label9.place(x=200, y=100)
        label10.place(x=200, y=150)
        self.entry9 = Entry(frame5, font=("times", 13))
        self.entry9.place(x=330, y=100, height=30)
        self.entry10 = Entry(frame5, font=("times", 13))
        self.entry10.place(x=330, y=150, height=30)
        button1 = Button(frame5, text="Add", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.add(self.entry9.get(), self.entry10.get(), frame5))
        button1.place(x=300, y=200)

        label13 = Label(frame6, text="Admin Name :", font=("times", 15), bg="honeydew3")
        label13.place(x=200, y=100)
        self.entry3 = Entry(frame6, font=("times", 13))
        self.entry3.place(x=330, y=100, height=30)
        button1 = Button(frame6, text="Delete", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.delete(self.entry3.get(), frame6))
        button1.place(x=300, y=200)

        label11 = Label(frame7, text="Admin Name :", font=("times", 15), bg="honeydew3")
        label12 = Label(frame7, text="Updated Password :", font=("times", 15), bg="honeydew3")
        label11.place(x=200, y=100)
        label12.place(x=168, y=150)
        self.entry5 = Entry(frame7, font=("times", 13))
        self.entry5.place(x=330, y=100, height=30)
        self.entry6 = Entry(frame7, font=("times", 13))
        self.entry6.place(x=330, y=150, height=30)
        button1 = Button(frame7, text="Update", width=10, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.update(self.entry5.get(), self.entry6.get(), frame7))
        button1.place(x=300, y=200)

        label14 = Label(frame8, text="Admin Name :", font=("times", 15), bg="honeydew3")
        label14.place(x=200, y=100)
        self.entry7 = Entry(frame8, font=("times", 13))
        self.entry7.place(x=330, y=100, height=30)
        button1 = Button(frame8, text="Search by Name", width=20, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.__search(self.entry7.get(), frame8))
        button1.place(x=300, y=180)
        button1 = Button(frame8, text="View all Admin", width=20, bg="cadetblue", bd=3, font=("Helvetica", 13),
                         command=lambda: self.__searchall(tk2))
        button1.place(x=300, y=230)

    def __searchall(self, tk):
        db = MySQLdb.connect("localhost", "root", "test123", "Banquet")
        cursor = db.cursor()
        sql = """select * from admin """
        try:
            cursor.execute(sql)
            cursor.fetchall()
        except:
            pass
        res = []
        for i in cursor:
            res.append(i)

        tk = Toplevel(tk)
        tk.geometry("400x500")
        tk.config(bg="grey")
        tk.title("Admin Database")
        f = Frame(tk)
        f.pack(side=LEFT, fill=Y)
        f.config(bg="white")
        c = Canvas(tk, width=400, height=500, bg="cadetblue")  # , yscrollcommand=s)

        fr = Frame(c, bg="cadetblue")
        fr.pack()
        c.pack()
        c.create_window(0, 0, window=fr, anchor='nw')
        lst = ["ID", "Admin Name", "Password"]
        for i in range(len(lst)):
            if i == 1:
                width = 15
            else:
                width = 10
            Label(fr, bg="black", fg="white", width=width, font=("Arial", 15), text=lst[i]).grid(row=0, column=i)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i % 2 == 0:
                    color = "honeydew3"
                else:
                    color = "white"
                if j == 1:
                    width = 15
                else:
                    width = 10
                Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
        tk.mainloop()

    def update(self, a, b, frame):
        str(a)
        str(b)
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from admin")
        data = cursor.fetchall()
        lst = []
        for i in data:
            lst.append(i[1])
        if a in lst:
            if len(b) < 5 or len(b) > 20:
                msg = Message(frame, text="Match password limit")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                print("Match password limit")
                self.entry6.delete(0, END)
            else:
                cursor.execute("""update admin set pass='%s' where admin_name='%s'""" % (b, a))
                db.commit()
                msg = Message(frame, text="Update succesfully")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                self.entry5.delete(0, END)
                self.entry6.delete(0, END)
                print("update successfully Succesfully")
        else:
            msg = Message(frame, text="Name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
            self.entry6.delete(0, END)
            print("Name doesn't present")

    def delete(self, a, frame):
        str(a)
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from admin")
        data = cursor.fetchall()
        lst = []
        for i in data:
            lst.append(i[1])
        if a in lst:
            cursor.execute("""delete from admin where admin_name='%s'""" % (a,))
            db.commit()
            msg = Message(frame, text="Delete Succesfully")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
            self.entry3.delete(0, END)
            print("Delete Succesfully")
        else:
            msg = Message(frame, text="Name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
            self.entry3.delete(0, END)
            print("Name doesn't present")

    def __search(self, a, frame):
        str(a)
        a = a.lower()
        db = MySQLdb.connect("localhost", "root", "test123", "banquet")
        cursor = db.cursor()
        cursor.execute("select * from admin")
        data = cursor.fetchall()
        lst = []
        text = Text(frame, bd=5)
        for i in data:
            lst.append(i[1])
        if a in lst:
            for i in data:
                if a in i:
                    text.place(x=0, y=0, height=200, width=200)
                    a = "ID:\n-----%s\nName:\n-----%s\nPassword:\n-----%s" % (i[0], i[1], i[2])
                    text.insert(END, a)
                    text.after(5000, lambda: text.destroy())
                    print(i)
                else:
                    pass
        else:
            self.entry7.delete(0, END)
            msg = Message(frame, text="Name doesn't present")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
            print("Name doesn't present")

    def add(self, a, b, frame):
        print(a)
        print(b)
        # str(a)
        str(b)
        try:
            a = int(a)
            msg = Message(frame, text="Name must contain Alphabet")
            msg.config(width=500, bg="cadetblue")
            msg.place(x=100, y=0)
            msg.after(3000, lambda: msg.destroy())
        except:
            a = a.lower()
            db = MySQLdb.connect("localhost", "root", "test123", "banquet")
            cursor = db.cursor()
            cursor.execute("select * from admin")
            data = cursor.fetchall()
            lst = []
            for i in data:
                lst.append(i[1])
            if len(lst) == 5:
                msg = Message(frame, text="Maximum limit of admin exceeds")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                print("Maximum limit of admin exceeds")
            elif len(a) < 3:
                msg = Message(frame, text="Insert Admin name with minimum length of 3")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                print("Insert Admin name with minimum length of 3")
                self.entry10.delete(0, END)
            elif a in lst:
                msg = Message(frame, text="Admin already have")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                print("Admin already have")
                self.entry10.delete(0, END)
            elif len(b) < 5 or len(b) > 20:
                msg = Message(frame, text="Match password limit")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                print("Length of password must be 5 to 20")
                self.entry10.delete(0, END)
            else:
                msg = Message(frame, text="Added Succesfully")
                msg.config(width=500, bg="cadetblue")
                msg.place(x=100, y=0)
                msg.after(3000, lambda: msg.destroy())
                cursor.execute("""insert into admin (admin_name,pass) values ('%s','%s')""" % (a, b))
                db.commit()
                self.entry9.delete(0, END)
                self.entry10.delete(0, END)
                print("Added Succesfully")



class Banquet:
    def __init__(self):
        self.w = Tk()
     # self.w.iconbitmap('Icon.ico')
        self.w.geometry("1920x1080+0+0")
        self.w.configure(bg="cadetblue", bd=-12)
        photobanquet = PhotoImage(file="wall1.png")
        labelbanquet = Label(self.w, image=photobanquet)
        labelbanquet.grid(row=0, column=0)
        self.w.after(1000, lambda: self.how())  # Destroy the widget after 30 seconds
        self.w.mainloop()

    def how(self):
        self.w.destroy()
        a = Admin()


a = Banquet()


