import tkinter
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
class classconnection:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host='localhost', database='PYTHONSQL', user='root', password='root')
            self.cur = self.mydb.cursor()
        except Exception as ex:
            print(ex)

class Bachat_gat(classconnection):
    def __init__(self):
        super().__init__()
    def ownpg(self):
        qry = "SELECT * FROM Owner"
        self.cur.execute(qry)
    def nextt1(self):
        qry = "SELECT * FROM Next"
        self.cur.execute(qry)
    def nextt3(self):
        if(self.opt.get()==1):
            self.staff_login()
        elif(self.opt.get()==2):
            self.owner_login()
        else:
            print("Invalid")
    def homepage(self):
        self.homepg=tkinter.Toplevel()
        self.homepg.geometry('500x500')
        self.homepg.title('HOMEPAGE')
        self.title123=tkinter.Label(self.homepg, text="Welcome to Signin Page", bd=10, relief="groove", font=("times new roman", 40, "bold"), bg="black", fg="blue")
        self.title123.grid(row=0,column=4)
        self.opt=tkinter.IntVar()
        self.Task_No=tkinter.StringVar()
        self.Name_var=tkinter.StringVar()
        self.Name_var1=tkinter.StringVar()
        self.workdesc_var=tkinter.StringVar()
        self.stat_var=tkinter.StringVar()
        self.Sno_var=tkinter.StringVar()
        self.groupno=tkinter.StringVar()
        self.duedt=tkinter.StringVar()
        self.stl=tkinter.Radiobutton(self.homepg, text="Staff Login", variable=self.opt, value=1).grid(row=5, column=4)
        self.owl=tkinter.Radiobutton(self.homepg, text="Owner Login", variable=self.opt, value=2).grid(row=6, column=4)
        self.b1=tkinter.Button(self.homepg, text="Next", command=self.nextt3)
        self.b1.grid(row=8,column=4)
    
    def staff_login(self):
        self.opt1=tkinter.IntVar()
        self.stafflg=tkinter.Toplevel()
        self.stafflg.geometry('500x500')
        self.stafflg.title(' Staff LOGIN')
        self.title1234=tkinter.Label(self.stafflg, text="Welcome Staff", bd=10, relief="groove", font=("times new roman", 40, "bold"), bg="red", fg="white")
        self.title1234.grid(row=0,column=7)
        contact_no=tkinter.Label(self.stafflg, text="Sno.No")
        contact_no.grid(row=4,column=4)
        self.ctno=tkinter.Entry(self.stafflg)
        self.ctno.grid(row=4,column=5)
        self.password=tkinter.Label(self.stafflg, text="Password")
        self.password.grid(row=5,column=4)
        self.psswd=tkinter.Entry(self.stafflg)
        self.psswd.grid(row=5,column=5)
        self.username=tkinter.Label(self.stafflg, text="Username")
        self.username.grid(row=6,column=4)
        self.unm=tkinter.Entry(self.stafflg)
        self.unm.grid(row=6,column=5)
        self.b1=tkinter.Button(self.stafflg, text="Next", command=self.nextt1)
        self.b1.grid(row=7,column=4)
        
    def nextt1(self):
        qry="select * from staff_cred where Sec_no='%s' and password='%s'"%(self.ctno.get(),self.psswd.get())
        self.cur.execute(qry)
        rs=self.cur.fetchall()
        print(rs)
        if len(rs)==0:
            messagebox.showinfo('','Invalid S_no/Password')
        else:
            self.rec=tkinter.Radiobutton(self.stafflg, text="Insert new women records", variable=self.opt1, value=1).grid(row=5, column=3)
            self.tsk=tkinter.Radiobutton(self.stafflg, text="Insert new Tasks", variable=self.opt1, value=2).grid(row=6, column=3)
            self.updt=tkinter.Radiobutton(self.stafflg, text="Update Tasks", variable=self.opt1, value=3).grid(row=7, column=3)
            self.b1=tkinter.Button(self.stafflg, text="submit", command=self.nextt2)
            self.b1.grid(row=8,column=3)
    def nextt2(self):
        if(self.opt1.get()==1):
            self.women_reg()
        elif(self.opt1.get()==2):
            self.task_reg()
        elif(self.opt1.get()==3):
            self.page2()
        else:
            print("Invalid")
        
    def task_reg(self):
        self.tskreg=tkinter.Toplevel()
        Task_no=tkinter.Label(self.tskreg, text="Task No.:")
        Task_no.grid(row=0,column=0)
        self.tskno=tkinter.Entry(self.tskreg)
        self.tskno.grid(row=0,column=1)
        self.name=tkinter.Label(self.tskreg, text=" Company Name: ")
        self.name.grid(row=1,column=0)
        self.nm=tkinter.Entry(self.tskreg)
        self.nm.grid(row=1,column=1)
        self.sts=tkinter.Label(self.tskreg, text="Status: ")
        self.sts.grid(row=2,column=0)
        self.st=tkinter.Entry(self.tskreg)
        self.st.grid(row=2,column=1)
        self.workdesc=tkinter.Label(self.tskreg, text="Work description ")
        self.workdesc.grid(row=3,column=0)
        self.desc=tkinter.Entry(self.tskreg)
        self.desc.grid(row=3,column=1)
        self.b5=tkinter.Button(self.tskreg, text="Save Info", command=self.saveinfo1)
        self.b5.grid(row=4,column=1)
    def saveinfo1(self):
        qry="insert into task values ('%d','%s','%s','%s','%s')"%(self.tskno.get(),self.nm.get(),self.st.get(),self.desc.get())
        print(qry)
        self.cur.execute(qry)
        self.mydb.commit()
        messagebox.showinfo('','Task registered successfully')
        self.tskreg.destroy()
    def women_reg(self):
        self.wmreg=tkinter.Toplevel()
        Reg_no=tkinter.Label(self.wmreg, text="Reg.No")
        Reg_no.grid(row=0,column=0)
        self.rgno=tkinter.Entry(self.wmreg)
        self.rgno.grid(row=0,column=1)
        self.name=tkinter.Label(self.wmreg, text="Name: ")
        self.name.grid(row=1,column=0)
        self.nm=tkinter.Entry(self.wmreg)
        self.nm.grid(row=1,column=1)
        self.adhr=tkinter.Label(self.wmreg, text="Aadhar No.")
        self.adhr.grid(row=2,column=0)
        self.ad=tkinter.Entry(self.wmreg)
        self.ad.grid(row=2,column=1)
        self.addd=tkinter.Label(self.wmreg, text="Address No.")
        self.addd.grid(row=3,column=0)
        self.addr=tkinter.Entry(self.wmreg)
        self.addr.grid(row=3,column=1)
        self.joindt=tkinter.Label(self.wmreg, text="Join date(yyyy/mm/dd): ")
        self.joindt.grid(row=4,column=0)
        self.dt=tkinter.Entry(self.wmreg)
        self.dt.grid(row=4,column=1)
        self.b5=tkinter.Button(self.wmreg, text="Save Info", command=self.saveinfo)
        self.b5.grid(row=5,column=1)

    def saveinfo(self):
        qry="insert into women values ('%s','%s','%s','%s','%s')"%(self.rgno.get(),self.nm.get(),self.ad.get(),self.addr.get(),self.dt.get())
        self.cur.execute(qry)
        self.mydb.commit()
        messagebox.showinfo('','Record of Women is inserted')
        self.wmreg.destroy()
        
    def owner_login(self):
        self.ownlg=tkinter.Toplevel()
        self.ownlg.geometry('500x500')
        self.ownlg.title(' Owner LOGIN')
        self.username=tkinter.Label(self.ownlg, text="Username")
        self.username.grid(row=1,column=0)
        self.unm=tkinter.Entry(self.ownlg)
        self.unm.grid(row=1,column=1)
        self.password=tkinter.Label(self.ownlg, text="Password")
        self.password.grid(row=2,column=0)
        self.psswd=tkinter.Entry(self.ownlg)
        self.psswd.grid(row=2,column=1)
        self.secno=tkinter.Label(self.ownlg, text="Security No. ")
        self.secno.grid(row=3,column=0)
        self.ssno=tkinter.Entry(self.ownlg)
        self.ssno.grid(row=3,column=1)
        b1=tkinter.Button(self.ownlg, text="Submit", command=self.ownpg)
        b1.grid(row=4,column=3)

    def ownpg(self):
        qry="select * from owner where usernm='%s' and password='%s' and sec_no='%s'"%(self.unm.get(),self.psswd.get(),self.ssno.get())
        print(qry)
        self.cur.execute(qry)
        rs=self.cur.fetchall()
        print(rs)
        if len(rs)==0:
            messagebox.showinfo('','Invalid Username/Password')
        else:
            self.ownerr1()
    def clear1(self):
        self.Task_No.set(" ")
        self.charg.set(" ")
        self.Sno_var.set(" ")
        self.groupno.set(" ")

    def get_cursor2(self):
        cursor_row=self.student_table1.focus()
        contents=self.student_table1.item(cursor_row)
        row=contents['values']
        self.Task_No.set(row[2])
        self.Sno_var.set(row[0])
        self.groupno.set(row[1])
        self.charg.set(row[3])
        
    def fetch_cursor2(self):
        self.student_table1.bind("<ButtonRelease-1>",self.get_cursor2())

    
    def fetch_data2(self):
            self.cur.execute(" select O.S_no,O.groupLeaderNo,O.Task_No,O.charges,G.NoOfLadieswithHer from owner_tb O join groupleader G on O.groupLeaderNo=G.groupLeaderNo; ")
            rows=self.cur.fetchall()
            if len(rows)!=0:
                self.student_table1.delete(*self.student_table1.get_children())
                for row in rows:
                    self.student_table1.insert('', tkinter.END, values=row)
                self.mydb.commit()
    def update_data1(self):
        self.cur=self.mydb.cursor()
        self.cur.execute("update owner_tb set charges='%s' where Task_No='%s'"%(self.charg.get(),self.Task_No.get()));
        self.mydb.commit()
        self.cur.execute("call conver_1()");
        self.mydb.commit();
        self.clear1()
        messagebox.showinfo("Success", "Record has been updated and inserted successfully !")
    def delete_data1(self):
        self.cur.execute("delete from owner_tb where Task_no='%s'"%(self.Task_No.get()))
        self.mydb.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully !")

    def ownerr1(self):
        self.own11=tkinter.Toplevel()
        self.own11.geometry('500x500')
        self.Task_No=tkinter.StringVar()
        self.Sno_var=tkinter.StringVar()
        self.groupno=tkinter.StringVar()
        self.duedt=tkinter.StringVar()
        self.charg=tkinter.IntVar()
        self.own11.title('WELCOME TO BACHAT GAT SYSTEM')
        title=tkinter.Label(self.own11, text="Welcome to Svadhyay Bachat Gat", bd=10, relief="groove", font=("times new roman", 40, "bold"), bg="brown", fg="white")
        title.pack(side=tkinter.TOP, fill=tkinter.X)
        manage_frame1 = tkinter.Frame(self.own11, bd=4, relief="ridge", bg="brown")
        manage_frame1.place(x=20,y=100,width=470,height=650)
        lbl_roll=tkinter.Label(manage_frame1, text="Sno: ", font=("times new roman", 15, "bold"), bg="brown", fg="white")
        lbl_roll.grid(row=1,column=0,padx=10,pady=20,sticky="w")

        txt_roll=tkinter.Entry(manage_frame1, textvariable=self.Sno_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_roll.grid(row=1,column=1,padx=10,pady=20,sticky="w")
        
        lbl_name=tkinter.Label(manage_frame1, text="Group Leader No :", font=("times new roman", 15, "bold"), bg="brown", fg="white")
        lbl_name.grid(row=2,column=0,padx=10,pady=20,sticky="w")

        txt_name=tkinter.Entry(manage_frame1, textvariable=self.groupno, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_name.grid(row=2,column=1,padx=10,pady=20,sticky="w")
                
        lbl_email=tkinter.Label(manage_frame1, text="Task No :", font=("times new roman", 15, "bold"), bg="brown", fg="white")
        lbl_email.grid(row=3,column=0,padx=10,pady=20,sticky="w")

        txt_email=tkinter.Entry(manage_frame1, textvariable=self.Task_No, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_email.grid(row=3,column=1,padx=10,pady=20,sticky="w")
        

        lbl_gender=tkinter.Label(manage_frame1, text="Charges: ", font=("times new roman", 15, "bold"), bg="brown", fg="white")
        lbl_gender.grid(row=4,column=0,padx=10,pady=20,sticky="w")

        txt_gen=tkinter.Entry(manage_frame1, textvariable=self.charg, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_gen.grid(row=4,column=1,padx=20,pady=10)


        btn_frame = tkinter.Frame(manage_frame1, bd=4, relief="ridge", bg="brown")
        btn_frame.place(x=15,y=600,width=400,height=38)
        updatebtn=tkinter.Button(btn_frame, text="Update Charges", width=15, command=self.update_data1).grid(row=0, column=1)
        deletebtn=tkinter.Button(btn_frame, text="Delete Record", width=10, command=self.delete_data1).grid(row=0, column=2)
        clearbtn=tkinter.Button(btn_frame, text="Clear Data", width=10, command=self.clear1).grid(row=0, column=3)
        fetchcursor=tkinter.Button(btn_frame, text="Fetch Data", width=15, command=self.fetch_cursor2).grid(row=0, column=4)


        detail_frame = tkinter.Frame(self.own11, bd=4, relief="ridge", bg="brown")
        detail_frame.place(x=500,y=100,width=830,height=590)

        table_frame1 = tkinter.Frame(detail_frame, bd=4, relief="ridge", bg="brown")
        table_frame1.place(x=10,y=40,width=800,height=230)
        
        self.scroll_x1=tkinter.Scrollbar(table_frame1, orient=tkinter.HORIZONTAL)
        self.scroll_y1=tkinter.Scrollbar(table_frame1, orient=tkinter.VERTICAL)
        self.student_table1=ttk.Treeview(table_frame1,columns=("Roll No","Name","Email","Gender"),xscrollcommand=self.scroll_x1.set,yscrollcommand=self.scroll_y1.set)
        self.scroll_x1.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.scroll_y1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll_x1.config(command=self.student_table1.xview)
        self.scroll_y1.config(command=self.student_table1.yview)
        self.student_table1.heading("Roll No",text="S.no: ")
        self.student_table1.heading("Name",text="Group leader No. :")
        self.student_table1.heading("Email",text="Task No: ")
        self.student_table1.heading("Gender",text="Charges: ")
        #self.student_table1.heading("Total",text="Total Ladies ")
        self.student_table1['show']='headings'
        self.student_table1.column("Roll No",width=100)
        self.student_table1.column("Name",width=100)
        self.student_table1.column("Email",width=100)
        self.student_table1.column("Gender",width=100)
        #self.student_table1.column("Group",width=100)
        self.student_table1.pack(fill=tkinter.BOTH, expand=1)
        self.fetch_data2()
        
        
        
    def clear(self):
        self.Task_No.set(" ")
        self.Name_var.set(" ")
        self.workdesc_var.set(" ")
        self.stat_var.set(" ")
        self.Sno_var.set(" ")
        self.groupno.set(" ")
        self.duedt.set(" ")
    def update_data(self):
        self.cur=self.mydb.cursor()
        self.cur.execute("update task set Status='%s' where Task_No='%s'"%(self.stat_var.get(),self.Task_No.get()));
        self.cur.execute("insert into assignedgroup(due_date,S_no,groupLeaderNo,Task_No) values ('%s','%s','%s','%s')"%(self.duedt.get(),self.Sno_var.get(),self.groupno.get(),self.Task_No.get()))
        self.mydb.commit()
        self.clear()
        messagebox.showinfo("Success", "Record has been updated and inserted successfully !")
    
    def fetch_cursor(self):
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor())
    def fetch_cursor1(self):
        self.student_table1.bind("<ButtonRelease-1>",self.get_cursor1())
    def get_cursor(self):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Task_No.set(row[0])
        self.Name_var.set(row[1])
        self.workdesc_var.set(row[3])
        self.stat_var.set(row[2])

    def fetch_data(self):
            self.cur.execute("select * from task where status='unassigned' or status='assigned' ")
            rows=self.cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', tkinter.END, values=row)
                self.mydb.commit()

    def fetch_data1(self):
            self.cur=self.mydb.cursor()
            self.cur.execute("select * from groupleader")
            rows=self.cur.fetchall()
            if len(rows)!=0:
                self.student_table1.delete(*self.student_table1.get_children())
                for row in rows:
                    self.student_table1.insert('', tkinter.END, values=row)
                self.mydb.commit()
                
    def fetch_cursor1(self):
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor1())
    def get_cursor1(self):
        cursor_row=self.student_table1.focus()
        contents=self.student_table1.item(cursor_row)
        row=contents['values']
        self.Name_var1.set(row[1])
        self.Sno_var.set(row[2])
        self.groupno.set(row[0])

            
        
    def delete_data(self):
        self.cur.execute("delete from Task where Task_no='%s'"%(self.Task_No.get()))
        self.mydb.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully !")
    def nextt(self):
        self.cur.execute("update task set Status='%s' where Task_No='%s'"%(self.stat_var.get(),self.Task_No.get()));
        self.mydb.commit()
        self.cur.execute("delete from assignedgroup where Task_No='%s'"%(self.Task_No.get()));
        self.mydb.commit();

                         
        
        
    def page2(self):
        window=tkinter.Toplevel()
        title=tkinter.Label(window, text="Bachat Gat Management System", bd=10, relief="groove", font=("times new roman", 40, "bold"), bg="red", fg="yellow")
        title.pack(side=tkinter.TOP, fill=tkinter.X)
        self.Task_No=tkinter.StringVar()
        self.Name_var=tkinter.StringVar()
        self.Name_var1=tkinter.StringVar()
        self.workdesc_var=tkinter.StringVar()
        self.stat_var=tkinter.StringVar()
        self.Sno_var=tkinter.StringVar()
        self.groupno=tkinter.StringVar()
        self.duedt=tkinter.StringVar()
        manage_frame = tkinter.Frame(window, bd=4, relief="ridge", bg="crimson")
        manage_frame.place(x=20,y=100,width=470,height=650)
        lbl_roll=tkinter.Label(manage_frame, text="Task no. :", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1,column=0,padx=10,pady=20,sticky="w")

        txt_roll=tkinter.Entry(manage_frame, textvariable=self.Task_No, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_roll.grid(row=1,column=1,padx=10,pady=20,sticky="w")
        
        lbl_name=tkinter.Label(manage_frame, text="Company Name :", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2,column=0,padx=10,pady=20,sticky="w")

        txt_name=tkinter.Entry(manage_frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_name.grid(row=2,column=1,padx=10,pady=20,sticky="w")
                
        lbl_email=tkinter.Label(manage_frame, text="Work Description :", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_email.grid(row=4,column=0,padx=10,pady=20,sticky="w")

        txt_email=tkinter.Entry(manage_frame, textvariable=self.workdesc_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_email.grid(row=4,column=1,padx=10,pady=20,sticky="w")

        lbl_gender=tkinter.Label(manage_frame, text="Status: ", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=3,column=0,padx=10,pady=20,sticky="w")

        txt_gen=tkinter.Entry(manage_frame, textvariable=self.stat_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_gen.grid(row=3,column=1,padx=20,pady=10)

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.stat_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Assigned","Unassigned","Completed")
        combo_gender.grid(row=3,column=1,padx=20,pady=10)

        lbl_groups=tkinter.Label(manage_frame, text="Sno(Group leader): ", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_groups.grid(row=7,column=0,padx=10,pady=20,sticky="w")

        txt_groupsno=tkinter.Entry(manage_frame, textvariable=self.Sno_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_groupsno.grid(row=7,column=1,padx=10,pady=20,sticky="w")

        lbl_name1=tkinter.Label(manage_frame, text="Name of Women :", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_name1.grid(row=6,column=0,padx=10,pady=20,sticky="w")

        txt_name1=tkinter.Entry(manage_frame, textvariable=self.Name_var1, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_name1.grid(row=6,column=1,padx=10,pady=20,sticky="w")
        
        lbl_grp=tkinter.Label(manage_frame, text="Group Number: ", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_grp.grid(row=5,column=0,padx=10,pady=20,sticky="w")

        txt_grpno=tkinter.Entry(manage_frame, textvariable=self.groupno, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_grpno.grid(row=5,column=1,padx=10,pady=20,sticky="w")

        lbl_duedate=tkinter.Label(manage_frame, text="Due date(yyyy/mm/dd): ", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_duedate.grid(row=8,column=0,padx=10,pady=20,sticky="w")

        txt_dt=tkinter.Entry(manage_frame, textvariable=self.duedt, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        txt_dt.grid(row=8,column=1,padx=10,pady=20,sticky="w")



        btn_frame = tkinter.Frame(manage_frame, bd=4, relief="ridge", bg="crimson")
        btn_frame.place(x=15,y=600,width=440,height=38)
        updatebtn=tkinter.Button(btn_frame, text="Update unassigned Status", width=20, command=self.update_data).grid(row=0, column=1)
        deletebtn=tkinter.Button(btn_frame, text="Delete", width=6, command=self.delete_data).grid(row=0, column=2)
        clearbtn=tkinter.Button(btn_frame, text="Clear", width=5, command=self.clear).grid(row=0, column=3)
        fetchcursor=tkinter.Button(btn_frame, text="Fetch task Data", width=12, command=self.fetch_cursor).grid(row=0, column=4)
        fetchcursor1=tkinter.Button(btn_frame, text="Fetch GRP Data", width=14, command=self.fetch_cursor1).grid(row=0, column=5)

        detail_frame = tkinter.Frame(window, bd=4, relief="ridge", bg="crimson")
        detail_frame.place(x=500,y=100,width=830,height=590)

        table_frame = tkinter.Frame(detail_frame, bd=4, relief="ridge", bg="crimson")
        table_frame.place(x=10,y=40,width=800,height=230)

        self.scroll_x=tkinter.Scrollbar(table_frame, orient=tkinter.HORIZONTAL)
        self.scroll_y=tkinter.Scrollbar(table_frame, orient=tkinter.VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Roll No","Name","Email","Gender"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.scroll_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No",text="Task No :")
        self.student_table.heading("Name",text="Comapny Name :")
        self.student_table.heading("Email",text="Work Desc :")
        self.student_table.heading("Gender",text="Status:")
        self.student_table['show']='headings'
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.pack(fill=tkinter.BOTH, expand=1)
        self.fetch_data()




        table_frame1 = tkinter.Frame(detail_frame, bd=4, relief="ridge", bg="crimson")
        table_frame1.place(x=15,y=280,width=800,height=230)

        self.scroll_x1=tkinter.Scrollbar(table_frame1, orient=tkinter.HORIZONTAL)
        self.scroll_y1=tkinter.Scrollbar(table_frame1, orient=tkinter.VERTICAL)
        self.student_table1=ttk.Treeview(table_frame1,columns=("Roll No","Name","Email","Gender"),xscrollcommand=self.scroll_x1.set,yscrollcommand=self.scroll_y1.set)
        self.scroll_x1.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.scroll_y1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll_x1.config(command=self.student_table1.xview)
        self.scroll_y1.config(command=self.student_table1.yview)
        self.student_table1.heading("Roll No",text="GroupNo.. :")
        self.student_table1.heading("Name",text="Group leader Name. :")
        self.student_table1.heading("Email",text="Ssno:")
        self.student_table1.heading("Gender",text="No.of members:")
        self.student_table1['show']='headings'
        self.student_table1.column("Roll No",width=100)
        self.student_table1.column("Name",width=100)
        self.student_table1.column("Email",width=100)
        self.student_table1.column("Gender",width=100)
        self.student_table1.pack(fill=tkinter.BOTH, expand=1)
        bttns=tkinter.Button(detail_frame, text="Update Status(Completed)", width=25, command=self.nextt).place(x=410, y=550)
        self.fetch_data1()
        window.title("Student Database Record")
        window.geometry("1350x700+0+0")
        window.mainloop()



page=tkinter.Tk()
B=Bachat_gat()
B.homepage()
