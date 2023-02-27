from tkinter import *
from tkinter import ttk
import mysql.connector

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")

        title = Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)


        #===============All Variables==============
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()



        #===============Manage Frame===============
        manage_frame = Frame(self.root,bg="crimson",bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=100,width=450,height=640)

        m_title = Label(manage_frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,padx=100,pady=20)



        lbl_roll = Label(manage_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll = Entry(manage_frame,textvariable=self.Roll_No_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")



        lbl_name = Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name = Entry(manage_frame,textvariable=self.name_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")



        lbl_email = Label(manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email = Entry(manage_frame,textvariable=self.email_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")



        lbl_gender = Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender = ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state='readonly')
        combo_gender['values'] = ('male','female','others')
        combo_gender.grid(row=4,column=1,padx=20,pady=10)



        lbl_contact = Label(manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact = Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")



        lbl_dob = Label(manage_frame,text="DOB",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob = Entry(manage_frame,textvariable=self.dob_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")



        lbl_address = Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address = Text(manage_frame,width=21,height=5,font=("",15))
        self.txt_address.grid(row=7,column=1,padx=20,pady=10,sticky='w')

        #===============Button Frame===============
        btn_frame = Frame(manage_frame,bg="crimson",bd=4,relief=RIDGE)
        btn_frame.place(x=10,y=565,width=420)

        addbtn = Button(btn_frame,command=self.add_students,text="Add",width=5).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,command=self.update_data,text="Update",width=5).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,command=self.delete_data,text="Delete",width=5).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_frame,command=self.clear,text="Clear",width=5).grid(row=0,column=3,padx=10,pady=10)

        #===============Detail Frame=============== 
        detail_frame = Frame(self.root,bg="crimson",bd=4,relief=RIDGE)
        detail_frame.place(x=500,y=100,width=830,height=640)

        lbl_search = Label(detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=20,padx=20,sticky="w")

        combo_search = ttk.Combobox(detail_frame,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values'] = ('Roll no.','Name','Contact')
        combo_search.grid(row=0,column=1,padx=20,pady=20)

        txt_search = Entry(detail_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(detail_frame,text="Search",width=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(detail_frame,text="Show all",width=5).grid(row=0,column=4,padx=10,pady=10)

        #================Table Frame================
        table_frame = Frame(detail_frame,bg="crimson",bd=4,relief=RIDGE)
        table_frame.place(x=10,y=70,width=800,height=550)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(table_frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show'] = 'headings'

        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=150)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.Student_table.pack(fill=BOTH,expand=1) 

        self.fetch_data()

    def add_students(self):
        con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost',database='student')
    
        cur = con.cursor()

        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END)
                                                                        ))

        con.commit()

        self.fetch_data()
        self.clear()

        con.close()

    def fetch_data(self):
        con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost',database='student')
    
        cur = con.cursor()

        cur.execute("select * from students")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("") 
        self.name_var.set("")
        self.email_var.set("") 
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row) 
        row=contents['values']

        #here row will give the values in a list form

        self.Roll_No_var.set(row[0]) 
        self.name_var.set(row[1])
        self.email_var.set(row[2]) 
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost',database='student')
    
        cur = con.cursor()

        cur.execute("update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s , address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))

        con.commit()

        self.fetch_data()
        self.clear()

        con.close()

    def delete_data(self):
        con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost',database='student')
    
        cur = con.cursor()

        cur.execute("delete from students where roll_no=%s",(self.Roll_No_var.get(),))

        con.commit()
        
        con.close()

        self.fetch_data()
        self.clear()


root = Tk()
ob = Student(root) 
root.mainloop()