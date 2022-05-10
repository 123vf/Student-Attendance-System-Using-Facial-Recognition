from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
#from numpy import meshgrid
import cv2


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")


        #============================ Variables ====================================

        
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        # first Image
        img=Image.open(r"college_images\shine.jpg")
        img=img.resize((400,150), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
 
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
 
        # Second Image
        img1=Image.open(r"college_images\shine.jpg")
        img1=img1.resize((400,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=400,height=130)
 
        # Third Image
        img2=Image.open(r"college_images\shine.jpg")
        img2=img2.resize((400,150), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
 
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=400,height=130)

        # fourth Image
        img_2=Image.open(r"college_images\shine.jpg")
        img_2=img_2.resize((400,150), Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
 
        f_lbl=Label(self.root,image=self.photoimg_2)
        f_lbl.place(x=1200,y=0,width=400,height=130)


        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=50)


        # bg Image
        img3=Image.open(r"college_images\back.jpg")
        img3=img3.resize((1540,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=710)
 
    
        # Left label frame
        Left_frame=LabelFrame(bg_img, bd=15,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame.place(x=30, y=60,width=770,height=585)

        dep_label_1=Label(Left_frame, text="Student Information", font=("times new roman", 20, "bold"),bg="cyan",fg="black")
        dep_label_1.place(x=280,y=0,width=250,height=50)

        # Current Course information
        current_course_frame=LabelFrame(Left_frame, bd=10, relief=RIDGE, text=" Current Course Information ", font=("times new roman",15,"bold"),bg="white",fg="black")
        current_course_frame.place(x=8, y=55,width=725,height=130)

        # Department
        dep_label=Label(current_course_frame, text="Department :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        dep_label.grid(row=0, column=0,padx=30,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep , font=("times new roman", 12, "bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame, text="Course :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        course_label.grid(row=0, column=2,padx=30,sticky=W)

        course_combo=ttk.Combobox(current_course_frame , textvariable=self.var_course , font=("times new roman", 12, "bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course", "FE", "SE", "TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame, text="Year :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        year_label.grid(row=1, column=0,padx=30,sticky=W)

        year_combo=ttk.Combobox(current_course_frame , textvariable=self.var_year , font=("times new roman", 12, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year", "2020-21", "2021-22", "2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame, text="Semester :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        semester_label.grid(row=1, column=2,padx=30,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame , textvariable=self.var_semester , font=("times new roman", 12, "bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester", "Semester-1", "Semester-2", "Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        
        # Class student information
        class_student_frame=LabelFrame(Left_frame, bd=10, relief=RIDGE, text=" Class Student Information ", font=("times new roman",15,"bold"),bg="white",fg="black")
        class_student_frame.place(x=8, y=195,width=725,height=278)

        # Student ID
        studentID_label=Label(class_student_frame, text="Student ID :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        studentID_label.grid(row=0, column=0,padx=10,pady=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame , textvariable=self.var_std_id , width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid (row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studenName_label=Label(class_student_frame, text="Student Name :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        studenName_label.grid(row=0, column=2,padx=10,pady=10,sticky=W)

        studenName_entry=ttk.Entry(class_student_frame , textvariable=self.var_std_name,width=20, font=("times new roman", 13, "bold"))
        studenName_entry.grid (row=0, column=3, padx=10, pady=5, sticky=W)


        # Class Division
        class_div_label=Label(class_student_frame, text="Class Division :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        class_div_label.grid(row=1, column=0,padx=10,pady=10,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame , textvariable=self.var_div,width=18, font=("times new roman", 13, "bold"),state="readonly")
        class_div_combo["values"]=("Select Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid (row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label=Label(class_student_frame, text="Roll No :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        roll_no_label.grid(row=1, column=2,padx=10,pady=10,sticky=W)
        roll_no_entry=ttk.Entry(class_student_frame , textvariable=self.var_roll,width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid (row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label=Label(class_student_frame, text="Gender :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        gender_label.grid(row=2, column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame , textvariable=self.var_gender,width=18, font=("times new roman", 13, "bold"),state="readonly")
        gender_combo["values"]=("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid (row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        DOB_label=Label(class_student_frame, text="DOB :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        DOB_label.grid(row=2, column=2,padx=10,pady=10,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame , textvariable=self.var_dob,width=20, font=("times new roman", 13, "bold"))
        DOB_entry.grid (row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label=Label(class_student_frame, text="Email :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        email_label.grid(row=3, column=0,padx=10,pady=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame , textvariable=self.var_email , width=20, font=("times new roman", 13, "bold"))
        email_entry.grid (row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_no_label=Label(class_student_frame, text="Phone No :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        phone_no_label.grid(row=3, column=2,padx=10,pady=10,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame , textvariable=self.var_phone,width=20, font=("times new roman", 13, "bold"))
        phone_no_entry.grid (row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label=Label(class_student_frame, text="Address :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        Address_label.grid(row=4, column=0,padx=10,pady=10,sticky=W)

        Address_entry=ttk.Entry(class_student_frame , textvariable=self.var_address,width=20, font=("times new roman", 13, "bold"))
        Address_entry.grid (row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_name_label=Label(class_student_frame, text="Teacher Name :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        teacher_name_label.grid(row=4, column=2,padx=10,pady=10,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame , textvariable=self.var_teacher,width=20, font=("times new roman", 13, "bold"))
        teacher_name_entry.grid (row=4, column=3, padx=10, pady=5, sticky=W)


         # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame , text="Take Photo Sample",variable=self.var_radio1 ,  value="Yes")
        radionbtn1.place(x=420,y=222,height=17)
        
        
        radionbtn2=ttk.Radiobutton(class_student_frame, text="No Photo Sample" , variable=self.var_radio1 , value="No")
        radionbtn2.place(x=570,y=222,height=17)

        # bbuttons frame

        save_btn=Button (Left_frame , command=self.add_data , text="Save",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        save_btn.place(x=8,y=486,width=181.25,height=33)

        update_btn=Button (Left_frame , command=self.update_data , text="Update",width=18, font=("times new roman", 13, "bold"), bg="green", fg="white")
        update_btn.place(x=189.25,y=486,width=181.5,height=33)

        delete_btn=Button (Left_frame , command=self.delete_data , text="Delete",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        delete_btn.place(x=370.5,y=486,width=181.25,height=33)

        reset_btn=Button (Left_frame , command=self.reset_data , text="Reset",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        reset_btn.place(x=551.75,y=486,width=181.25,height=33)


        # bbuttons frame1
      
        take_photo_btn=Button (Left_frame , command=self.generate_dataset , text="Take Photo Sample",width=36, font=("times new roman", 13, "bold"), bg="green", fg="white")
        take_photo_btn.place(x=8,y=519,width=362.5,height=33)

        update_photo_btn=Button (Left_frame, text="Update Photo Sample",width=36, font=("times new roman", 13, "bold"), bg="green", fg="white")
        update_photo_btn.place(x=370.5,y=519,width=362,height=33)



        # Right label frame
        Right_frame=LabelFrame(bg_img, bd=15,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Right_frame.place(x=815, y=60,width=675,height=590)

        dep_label_2=Label(Right_frame, text="Student Details", font=("times new roman", 20, "bold"),bg="cyan",fg="black")
        dep_label_2.place(x=220,y=0,width=250,height=50)

        #============================ Search System ================================

        search_frame=LabelFrame(Right_frame, bd=10,bg="white",fg="black", relief=RIDGE, text=" Search System ", font=("times new roman",15,"bold"))
        search_frame.place(x=8, y=55,width=630,height=85)

        search_label=Label(search_frame, text="Search By : ", font=("times new roman", 12, "bold"),bg="white",fg="black")
        search_label.place(x=8,y=12,width=90,height=25)

        search_combo=ttk.Combobox(search_frame, font=("times new roman", 12, "bold"),state="readonly",width=15)
        search_combo["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.place(x=110,y=12,width=120,height=25)

        search_entry=ttk.Entry(search_frame,width=15, font=("times new roman", 13, "bold"))
        search_entry.place(x=240,y=12,width=150,height=25)

        search_btn=Button (search_frame, text="Search",width=10, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        search_btn.place(x=410,y=12,width=90,height=25)

        showAll_btn=Button (search_frame, text="Show All",width=10, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        showAll_btn.place(x=510,y=12,width=90,height=25)

        #============================ Table Frame ================================

        table_frame=Frame(Right_frame, bd=10,bg="darkblue", relief=RIDGE)
        table_frame.place(x=8, y=150,width=630,height=400)

        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        
        self.student_table=ttk. Treeview (table_frame, column=("id", "name","dep","course", "year","sem", "div", "roll", "gender", "dob", "email" , "phone","address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading ("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading ("sem", text="Semester")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading ("dob", text="DOB")
        self.student_table.heading ("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

       
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column ("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column ("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column ("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #==================================Function Declaration======================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Fetch Data======================================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============================Get Cursor=========================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        
        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #==================================Update Function=======================================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this student details?",parent=self.root)

                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set  Name=%s , Dep=%s , course=%s , Year=%s , Semester=%s , Division=%s , Roll=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s , Address=%s , Teacher=%s , PhotoSample=%s where Student_id=%s",(
                                                                                                              
                                                                                                                                                                                
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                                                                                ))
                    messagebox.showinfo("Success","Student datails update Successfully Completed !",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()



                else:
                    if not update:
                        return

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Delete Function=======================================

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required!",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Student Data Delete Page","Do you want to delete this student datails?",parent=self.root)

                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Deleted Student Details!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Reset Function=======================================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #======================= Generate Dta set OR Take Photo Samples =========================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                print(myresult)
               
                my_cursor.execute("update student set  Name=%s , Dep=%s , course=%s , Year=%s , Semester=%s , Division=%s , Roll=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s , Address=%s , Teacher=%s , PhotoSample=%s where Student_id=%s",(
                                                                                                              
                                                                                                                                                                                
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                                                                                ))

                id=self.var_std_id.get()


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #============================== Load Predefine Data On Face frontals from OpenCV ===============================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3
                    # Minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+ str(id) +"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()