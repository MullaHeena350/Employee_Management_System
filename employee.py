#!/usr/bin/python3
'''import tkinter as tk
root=tk.Tk()
w=root.winfo_height
root.geometry("400x400+0+0")

lab1=tk.Label(root,text="hello")
lab1.pack()
root.mainloop()'''


from curses.ascii import isalpha
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import re
class employee:
    def __init__(self,root):# here instead root u can use anyother words like master .it just indicates window name
        self.root=root#initialisation
        self.root.geometry("1530x790+0+0")#1530 is fro width, 790 is for height
        self.root.title('Employee Management System')
        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcombo=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

       
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')# self.root means on which window does this happening means named as root(window name)   
       #fg=foreground for letters coloring
        lbl_title.place(x=0,y=0,width=1530,height=50)#to show this title on window
        img_logo=Image.open('/home/student/Desktop/Employee_Management_System/collage/logo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)# ANTIALIAS is for to convert high level image to low level image
        self.photo_logo=ImageTk.PhotoImage(img_logo)# the reason to keep self. to photo_logo attribut is if u want to use this attribute anywher within a class so u ahve to put self.(dot)
        # (above)i have installed separetely imagetk using sudo apt install python3-pip.imagetk
        #NOW I can use imagetk
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=40,height=40)
                #First_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')# This for to create frame
        img_frame.place(x=0,y=50,width=1530,height=115)
                    #1st_Image
        img1=Image.open('/home/student/Desktop/Employee_Management_System/collage/t1.jpeg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=110)
                #2nd_Image
        img2=Image.open('/home/student/Desktop/Employee_Management_System/collage/t2.jpeg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=110)
                #3rd_Image
        img3=Image.open('/home/student/Desktop/Employee_Management_System/collage/t3.jpeg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=810,y=0,width=540,height=110)
        #Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')# This for to create frame
        main_frame.place(x=7,y=167,width=1350,height=530)

            # upper_frame inside main_Frame
            #LabelFrame=we can give text inside the frame
            #Frame=we cannot give text inside the frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',13,'bold'),fg='red')# This for to create frame
        upper_frame.place(x=7,y=2,width=1330,height=230)


                #Labels and Enrty feilds inside upper_frame
                #For Department
        lb1_dep=Label(upper_frame,text="Department:",font=('arial',11,'bold'),bg='white')
        #We are not going to place here when we dont know where to palce or how to place then you can use place method but here 
        #you know where to place so use grid method 
        lb1_dep.grid(row=0,column=0,padx=2,sticky=W)#W stands for west , sticky means it stick the text what you written
                #making comboBox 
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arail',12,'bold'),width=17,state='readonly')#
                    #To set values in comboBox
        combo_dep['value']=('select Department','HR','Software Engineer','Manager','Tester','Developer')
            #this tuples start from zero so kepted 0 n current method
        combo_dep.current(0)
            #now grid it 
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
                  #Name
        lb1_name=Label(upper_frame,font=('arial',12,'bold'),text="Name:",bg='white')
        lb1_name.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arail',11,'bold'))
        txt_name.grid(row=1,column=3,padx=2,pady=7)#sticky=W)
                #lb1_Designation
        lb1_Designation=Label(upper_frame,width=10,font=('arail',12,'bold'),text="Designation:",bg='white')
        lb1_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=1,column=1,stick=W,padx=2,pady=7)
        #   Email
        lb1_email=Label(upper_frame,width=5,font=('arail',12,'bold'),text="Email:",bg='white')
        lb1_email.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=28,font=('arial',11,'bold'))
        txt_email.grid(row=0,column=3,padx=2,pady=7)
             #Address
        lb1_address=Label(upper_frame,width=7,font=('arail',12,'bold'),text="Address:",bg='white')
        lb1_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=26,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)
            #Married
        lb1_married_status=Label(upper_frame,width=13,font=('arail',12,'bold'),text='Married_Status:',bg='white')
        lb1_married_status.grid(row=2,column=2,stick=W,padx=2,pady=7)
        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",font=('arial',12,'bold'),width=23)
        com_txt_married['value']=('Married','Unmarried',"Other")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7)
                #DOB
        lb1_dob=Label(upper_frame,font=('arial',12,'bold'),text="DOB:",bg='white')
        lb1_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=26,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
        #DOJ
        lb1_doj=Label(upper_frame,font=('arial',12,'bold'),text="DOJ:",bg='white')
        lb1_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=28,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,padx=0,pady=7)

        #Id_Proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcombo,state="readonly",font=('arial',12,'bold'),width=18)
        com_txt_proof['value']=('select ID Proof','PAN CARD','ADHAR CARD','DRIVING LICENS')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=26,font=('arial',11,'bold'))
        txt_doj.grid(row=4,column=1,padx=2,pady=7)

        #GENDER
        lb1_gender=Label(upper_frame,font=('arail',12,'bold'),text="Gender:",bg='white')
        lb1_gender.grid(row=4,column=2,stick=W,padx=2,pady=7)

        com_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=('arial',12,'bold'),width=18)
        com_gender['value']=('Male','Female',"Other")
        com_gender.current(0)
        com_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone
        lb1_phone=Label(upper_frame,font=('arial',12,'bold'),text="Phone No:",bg='white')
        lb1_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #country
        lb1_country=Label(upper_frame,font=('arial',12,'bold'),text="Country:",bg='white')
        lb1_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=0,pady=7)

        #CTC
        lb1_ctc=Label(upper_frame,font=('arial',12,'bold'),text="Salary(CTC):",bg='white')
        lb1_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

                #Button_Frame
        button_frame=LabelFrame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1140,y=18,width=168,height=180)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=("arail",15,"bold"),width=13,bg='darkblue',fg='white')
        btn_add.grid(row=0,column=0,padx=0,pady=0)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=("arail",15,"bold"),width=13,bg='darkblue',fg='white')
        btn_update.grid(row=1,column=0,padx=0,pady=5)

        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=("arail",15,"bold"),width=13,bg='darkblue',fg='white')
        btn_delete.grid(row=2,column=0,padx=0,pady=5)

        btn_clear=Button(button_frame,text='Clear',command=self.reset_data,font=("arail",15,"bold"),width=13,bg='darkblue',fg='white')
        btn_clear.grid(row=3,column=0,padx=0,pady=5)



                #lower_frame inside Main_fram
        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',13,'bold'),fg='blue')
        lower_frame.place(x=7,y=233,width=1330,height=290)
                #search_frame inside lower_frame
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',12,'bold'),fg='blue')
        search_frame.place(x=4,y=0,width=1318,height=58)
        
        search_by=Label(search_frame,font=('arail',13,"bold"),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5,pady=3)

                 # forSearch
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=('arail',13,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","Id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5,pady=3)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arail",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5,pady=3)

        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("arail",11,"bold"),width=14,bg="darkblue",fg="white")
        btn_search.grid(row=0,column=3,padx=5,pady=3)

        btn_search=Button(search_frame,text="Show All",command=self.fetch_data,font=("arail",11,"bold"),width=14,bg="darkblue",fg="white")
        btn_search.grid(row=0,column=4,padx=5,pady=3)
        #**********Employee table***********

        table_frame=Frame(lower_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=66,width=1320,height=190)
        #scrollbar for horizontal(x) and vertical(y)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #now making tree view means table 
        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","doj","dob","idproofcombo","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #the above in column are dumy values original values will be given to below
        scroll_x.pack(side=BOTTOM,fill=X)# fill means fill in x axis
        scroll_y.pack(side=RIGHT,fill=Y)# fil means fill in y axis
        scroll_x.config(command=self.employee_table.xview)#You want to see ths in x view
        scroll_y.config(command=self.employee_table.yview)#you want to see this in y view
        #heading
        self.employee_table.heading('dep',text="Department")
        self.employee_table.heading('name',text="Name")
        self.employee_table.heading('degi',text="Designation")
        self.employee_table.heading('email',text="Email")
        self.employee_table.heading('address',text="Address")
        self.employee_table.heading('married',text="Married_Status")
        self.employee_table.heading('doj',text="DOJ")
        self.employee_table.heading('dob',text="DOB")
        self.employee_table.heading('idproofcombo',text="Id_proof_type")
        self.employee_table.heading('idproof',text="Id_proof")
        self.employee_table.heading('gender',text="Gender")
        self.employee_table.heading('phone',text="Phone")
        self.employee_table.heading('country',text="Country")
        self.employee_table.heading('salary',text="Salary")
        #Above gives uh the some view like gaps in between columns and we got first colum as empty so to overcome this bleow code is works 
       # self.employee_table['show']='headings'# to remove empty column
        self.employee_table['show']='headings' 
        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("idproofcombo",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
       #self.employee_table['show']='headings'

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor) #dont give paranthesis to get_cursor dont call

        self.fetch_data()
#we have to write function to save data
    #***********Function declarations**************
    

    def  add_data(self):
            count=0
            #i want to put conditions like some validation required while entering data by user
            if self.var_dep.get()=="" or self.var_email.get()=="":#get()method is used to get data
                    messagebox.showerror('Error','All field are required')# if either one is true then i have to show a message through showerror
                    
            elif True:
                    flag = 0
                    data = self.var_phone.get()
                    if len(str(data)) == 10:
                            if str(data).isnumeric():
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            flag = 0
                    if not flag:
                        count=1
                        messagebox.showerror('Invalid', 'Phone Number is Invalid')
                    flag1 = 0
                    pat = "^[a-zA-z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
                    mail = self.var_email.get()
                    if re.match(pat, mail):
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'Email is Invalid')
                    ctc = self.var_salary.get()
                    if ctc.isnumeric():
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'CTC is Invalid')
                    
                    country = self.var_country.get()
                    if country.isalpha():
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'Country Name is Invalid')
                    flag = 0
                    data = self.var_idproof.get()
                    val = self.var_idproofcombo.get()
                    if val == 'PAN CARD':
                            if len(str(data)) == 10:
                                    if str(data).isalpha():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'PAN is Invalid')
                    flag = 0
                    if val == "ADHAR CARD":
                            if len(str(data)) == 12:
                                    if str(data).isalnum():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'Adhar is Invalid')
                    flag = 0
                    if val == "DRIVING LICENS":
                            if len(str(data)) == 16:
                                    if str(data).isalpha():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'Driving License is Invalid')
                    dob = self.var_dob.get()
                    ls = dob.split("/")
                    dates = ['01', '02', '03', '04', '05', '06', '07', '08','09']
                    tone = ['01','03','05','07','08','10','12']
                    tzero = ['04','06','11']
                    flag = 0
                    if ls[1] == '02':
                            if ls[0] in dates or 10 <= int(ls[0] <=29):
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tone:
                            if ls[0]in dates or 10<= int(ls[0]) <= 31:
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tzero:
                            if ls[0] in dates or 10 <= int(ls[0]) <= 30:
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            count=1
                            messagebox.showerror("Invalid", "Invalid Month")
                    
                    if flag == 0:
                            count=1
                            messagebox.showerror("Invalid", "Invalid date")

                    doj = self.var_doj.get()
                    ls = doj.split("/")
                    dates = ['01', '02', '03', '04', '05', '06', '07', '08','09']
                    tone = ['01','03','05','07','08','10','12']
                    tzero = ['04','06','11']
                    flag = 0
                    if ls[1] == '02':
                            if ls[0] in dates or 10 <= int(ls[0] <=29):
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tone:
                            if ls[0]in dates or 10<= int(ls[0]) <= 31:
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tzero:
                            if ls[0] in dates or 10 <= int(ls[0]) <= 30:
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            count=1
                            messagebox.showerror("Invalid", "Invalid Month")
                    
                    if flag == 0:
                            count=1
                            messagebox.showerror("Invalid", "Invalid date")       
            
                    #if i get any error then this try block will understand how to run
                    
                    if(count==0):
                        try:

                            #now we have to estabilish a connection with database
                                conn=mysql.connector.connect(host='localhost',user='root',password='iiits123',database='mydat')
                                my_cursor=conn.cursor()# need to creat a cursor
                                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_designation.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_married.get(),
                                                                                                        self.var_doj.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_idproofcombo.get(),
                                                                                                        self.var_idproof.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_country.get(),
                                                                                                        self.var_salary.get()))#this execute command is bolongs to mysql %s can be called as holding place
                                conn.commit()
                                self.fetch_data()#this is required because when we give data in middle circumstance then it should also add into database
                                conn.close()
                                messagebox.showinfo('success','Employee has been added!',parent=self.root)
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                    else:
                        messagebox.showerror('Error',"invalid details cannot save data")

        #Fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host='localhost',user='root',password='iiits123',database='mydat')
            my_cursor=conn.cursor()
            #now give command
            my_cursor.execute('select * from employee1')
            data=my_cursor.fetchall()#i am storing in variable called data 
            #i need to present this data into table
            if len(data)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    #now insert
                    for i in data:
                            self.employee_table.insert("",END,values=i)
                    conn.commit() #commit means it will update data
            conn.close()
    #get cursor
    #when i click on the data i need to get this data on above labels 
    def get_cursor(self,event=""):
            cursor_row=self.employee_table.focus()
            content=self.employee_table.item(cursor_row)
            data=content['values']

            self.var_dep.set(data[0])
            self.var_name.set(data[1])
            self.var_designation.set(data[2])
            self.var_email.set(data[3])
            self.var_address.set(data[4])
            self.var_married.set(data[5])
            self.var_doj.set(data[6])
            self.var_dob.set(data[7])
            self.var_idproofcombo.set(data[8])
            self.var_idproof.set(data[9])
            self.var_gender.set(data[10])
            self.var_phone.set(data[11])
            self.var_country.set(data[12])
            self.var_salary.set(data[13]) #after this we need to this at table soo go to table(above it is)
    def update_data(self):
            count=0
            if self.var_dep.get()=="" or self.var_email.get()=="":#get()method is used to get data
                    messagebox.showerror('Error','All field are required')# if either one is true then i have to show a message through showerror
            
            else:
                    flag = 0
                    data = self.var_phone.get()
                    if len(str(data)) == 10:
                            if str(data).isnumeric():
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            flag = 0
                    if not flag:
                        count=1
                        messagebox.showerror('Invalid', 'Phone Number is Invalid')
                    flag1 = 0
                    pat = "^[a-zA-z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
                    mail = self.var_email.get()
                    if re.match(pat, mail):
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'Email is Invalid')
                    ctc = self.var_salary.get()
                    if ctc.isnumeric():
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'CTC is Invalid')
                    
                    country = self.var_country.get()
                    if country.isalpha():
                        pass
                    else:
                        count=1
                        messagebox.showerror('Invalid', 'Country Name is Invalid')
                    flag = 0
                    data = self.var_idproof.get()
                    val = self.var_idproofcombo.get()
                    if val == 'PAN CARD':
                            if len(str(data)) == 10:
                                    if str(data).isalpha():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'PAN is Invalid')
                    flag = 0
                    if val == "ADHAR CARD":
                            if len(str(data)) == 12:
                                    if str(data).isalnum():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'Adhar is Invalid')
                    flag = 0
                    if val == "DRIVING LICENS":
                            if len(str(data)) == 16:
                                    if str(data).isalpha():
                                            flag = 1
                                    else:
                                            flag = 0
                            else:
                                    flag = 0
                            if not flag:
                                    count=1
                                    messagebox.showerror('Invalid', 'Driving License is Invalid')
                    dob = self.var_dob.get()
                    ls = dob.split("/")
                    dates = ['01', '02', '03', '04', '05', '06', '07', '08','09']
                    tone = ['01','03','05','07','08','10','12']
                    tzero = ['04','06','11']
                    flag = 0
                    if ls[1] == '02':
                            if ls[0] in dates or 10 <= int(ls[0] <=29):
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tone:
                            if ls[0]in dates or 10<= int(ls[0]) <= 31:
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tzero:
                            if ls[0] in dates or 10 <= int(ls[0]) <= 30:
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            count=1
                            messagebox.showerror("Invalid", "Invalid Month")
                    
                    if flag == 0:
                            count=1
                            messagebox.showerror("Invalid", "Invalid date")

                    doj = self.var_doj.get()
                    ls = doj.split("/")
                    dates = ['01', '02', '03', '04', '05', '06', '07', '08','09']
                    tone = ['01','03','05','07','08','10','12']
                    tzero = ['04','06','11']
                    flag = 0
                    if ls[1] == '02':
                            if ls[0] in dates or 10 <= int(ls[0] <=29):
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tone:
                            if ls[0]in dates or 10<= int(ls[0]) <= 31:
                                    flag = 1
                            else:
                                    flag =0
                    elif ls[1] in tzero:
                            if ls[0] in dates or 10 <= int(ls[0]) <= 30:
                                    flag = 1
                            else:
                                    flag = 0
                    else:
                            count=1
                            messagebox.showerror("Invalid", "Invalid Month")
                    
                    if flag == 0:
                            count=1
                            messagebox.showerror("Invalid", "Invalid date")       
            
                    #if i get any error then this try block will understand how to run
                    
                    if(count==0):
                    #if i get any error then this try block will understand how to run
                        try:



                                update=messagebox.askyesno('Update','Are you sure to update this employee data')
                                if update>0:

                                        #now we have to estabilish a connection with database
                                        conn=mysql.connector.connect(host='localhost',user='root',password='iiits123',database='mydat')
                                        my_cursor=conn.cursor()
                                        my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_Status=%s,DOJ=%s,DOB=%s,Id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(self.var_dep.get(),
                                                                                                                                                                                                                                              self.var_name.get(),
                                                                                                                                                                                                                                             self.var_designation.get(),
                                                                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                                            self.var_married.get(),
                                                                                                                                                                                                                                            self.var_doj.get(),
                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                            self.var_idproofcombo.get(),
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                            self.var_country.get(),
                                                                                                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                                                                                                            self.var_idproof.get()))
                                else:
                                
                                        if not update:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('success','Employee successfully updated',parent=self.root)
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root) 
                    else:
                        messagebox.showerror('Error','invalid data cannot be updated')      

                #Delete
    def delete_data(self):
            if self.var_idproof.get()=="":
                    messagebox.showerror('Error','All are required')
            else:
                    try:
                            Delete=messagebox.askyesno('Delete','Are you sure to delete this employee')
                            if Delete>0:
                                    conn=mysql.connector.connect(host='localhost',user='root',password='iiits123',database='mydat')
                                    my_cursor=conn.cursor()
                                    sql='delete from employee1 where id_proof=%s'
                                    value=(self.var_idproof.get(),)#entry proof means it takes value from id_proof.get and we ahve to give comma 
                                    my_cursor.execute(sql,value)
                            else:
                                    if not Delete:
                                            return
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo('Delete','Employee successfully deleted',parent=self.root)
                    except Exception as es:
                            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
        #Reset
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_name.set("")
            self.var_designation.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.var_married.set("")
            self.var_dob.set("")
            self.var_doj.set("")
            self.var_idproofcombo.set("Select ID proof")
            self.var_idproof.set("")
            self.var_gender.set("")
            self.var_phone.set("")
            self.var_country.set("")
            self.var_salary.set("")
#Search
    def search_data(self):
            if self.var_com_search.get()=='' or self.var_search.get()=='':
                    messagebox.showerror('Error','Please select option')
            else:
                    try:
                        conn=mysql.connector.connect(host='localhost',user='root',password='iiits123',database='mydat')
                        my_cursor=conn.cursor()
                        my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))#this query related to search so u have to follow as it is.
                        rows=my_cursor.fetchall()
                        if len(rows)!=0:
                                self.employee_table.delete(*self.employee_table.get_children())
                                for i in rows:
                                        self.employee_table.insert("",END,values=i)
                        conn.commit()
                        conn.close()
                    except Exception as es:
                            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                    












#SO now window is ready so to close or to pack window we need to do code below 
if __name__=="__main__":
    root=Tk()
    obj=employee(root)
    root.mainloop()



