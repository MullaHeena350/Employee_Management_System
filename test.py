#!/usr/bin/python3

from tkinter import*
from tkinter import ttk #for stylish
from PIL import Image,ImageTk
from employee import employee

class Login_Page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15730x790+0+0")
        self.root.title("Home page for Employee Management System")
        #title image
        # img=Image.open("/home/student/Desktop/pic/20.jpeg")
        # img=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=450,y=0,width=500,height=130)

        #bg image
        img2=Image.open("/home/student/Desktop/Employee_Management_System/collage/e.jpg")
        img2=img2.resize((1530,700),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=8,width=1370,height=730)

        title_lbl=Label(bg_img,text="WELCOME TO EMPLOYEE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1380,height=50)
        #STUDENT Button
        # img3=Image.open("/home/student/Desktop/pic/37.jpeg")
        # img3=img3.resize((215,220),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)
        
        # b1=Button(bg_img,image=self.photoimg3, cursor="hand2")
        # b1.place(x=200,y=60,width=220,height=220)

        b1=Button(bg_img,text="CLICK HERE",command=self.employee_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=660,y=460,width=220,height=40)

    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=employee(self.new_window)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Login_Page(root)
    root.mainloop()












