from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #from pillow module
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')


        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_desig=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        



        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='navy blue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        # logo
        img_logo=Image.open('emp_imgs/emplogo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='red')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st
        img1=Image.open('emp_imgs/emp1.png')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        # 2nd
        img2=Image.open('emp_imgs/emp2.png')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        # 3rd
        img3=Image.open('emp_imgs/emp3.png')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)


        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='yellow')
        Main_frame.place(x=15,y=220,width=1500,height=560)

        # Upper_frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='light grey',text='Employee Information',font=('times new roman',12,'bold'),fg='red')
        upper_frame.place(x=15,y=10,width=1470,height=270)

        # Label and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',13,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','Accounts and Finance','HR','Sales and Marketing','Research and Development','IT services','Security and Transport','Product Development')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(upper_frame,text='Name',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_designation
        lbl_desig=Label(upper_frame,text='Designation',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_desig.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_desig,width=22,font=("arial",11,"bold"))
        txt_desig.grid(row=1,column=1,padx=2,pady=7)

        # Email
        lbl_email=Label(upper_frame,text='Email',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # AdDress
        lbl_address=Label(upper_frame,text='Address',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # MArried
        lbl_married_status=Label(upper_frame,text='Married Status',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',13,'bold'),width=18,state='readonly')
        com_txt_married['value']=("Married","UnMarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB
        lbl_dob=Label(upper_frame,text='DOB',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #DOJ
        lbl_doj=Label(upper_frame,text='DOJ',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        #Id Proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',13,'bold'),width=18,state='readonly')
        com_txt_proof['value']=("Select ID Proof","Pancard","Adhar Card","Driving license")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,text='Gender',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',13,'bold'),width=18,state='readonly')
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #Phone
        lbl_phone=Label(upper_frame,text='Phone No',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,text='Country',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # CTC
        lbl_ctc=Label(upper_frame,text='Salary(CTC)',font=('arial',12,'bold'),fg='black',bg='lightgrey')
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        # Center Picture
        img_cen=Image.open('emp_imgs/apsit_logo.png')
        img_cen=img_cen.resize((245,245),Image.ANTIALIAS)
        self.photocen=ImageTk.PhotoImage(img_cen)

        self.img_cen=Label(upper_frame,image=self.photocen)
        self.img_cen.place(x=1000,y=0,width=245,height=245)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='lightgrey')
        button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text='Clear',command=self.reset_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)


        #=================Lower_frame====================
        lower_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='yellow',text='Employee Information table',font=('times new roman',12,'bold'),fg='red')
        lower_frame.place(x=15,y=280,width=1470,height=270)

        # Search frame
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='lightgrey',text='Search Employee Information',font=('times new roman',12,'bold'),fg='navyblue')
        search_frame.place(x=0,y=0,width=1465,height=60)

        search_by=Label(search_frame,font=('arial',12,'bold'),text='Search by :',fg='black',bg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        
        
        # Search
        self.var_com_search=StringVar()
       
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=18,state='readonly')
        com_txt_search['value']=("Select Option","Phone","Id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)



        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text='Search',command=self.search_data,font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text='Display ALL',command=self.fetch_data,font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)

        msg_text=Label(search_frame,font=('time new roman',30,'bold'),text="APSIT WE BuiLd DreAms",fg='red',bg='white')
        msg_text.place(x=860,y=0,width=600,height=30)

        msg_logo=Image.open(r'emp_imgs/msg_logo.png')
        msg_logo=msg_logo.resize((50,50),Image.ANTIALIAS)
        self.pmsg_logo=ImageTk.PhotoImage(msg_logo)

        self.logo=Label(search_frame,image=self.pmsg_logo)
        self.logo.place(x=840,y=0,width=50,height=30)

        # ================Employee Table==================
        # Table Frame
        table_frame=Frame(lower_frame,bd=2,relief=RIDGE,bg='black')
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desig','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='MArital Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID PRoof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')



        self.employee_table['show']='headings'



        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("desig",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)



        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #*************Function Declarations***********

    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Kamlakar123@',database='management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                    self.var_dep.get(),
                                    self.var_name.get(),
                                    self.var_desig.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_married.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_idproofcomb.get(),
                                    self.var_idproof.get(),
                                    self.var_gender.get(),
                                    self.var_phone.get(),
                                    self.var_country.get(),
                                    self.var_salary.get(),
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Kamlakar123@',database='management_system')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    # Get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']


        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_desig.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update',"Are you Sure update this Employee Data")
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Kamlakar123@',database='management_system')
                    my_cursor=conn.cursor()
                    my_cursor.execute('Update Employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                                                                                    self.var_dep.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_desig.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_married.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_doj.get(),
                                                                                    self.var_idproofcomb.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_country.get(),
                                                                                    self.var_salary.get(),
                                                                                    self.var_idproof.get()
                                                                                 ))
                
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Data Successfully Updated',parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



    # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error',"All Fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete',"Are you sure to delete this data")
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Kamlakar123@',database='management_system')
                    my_cursor=conn.cursor()
                    sql='delete from employee where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Data Successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_desig.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select Id Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select an Option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Kamlakar123@',database='management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()


