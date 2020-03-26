#Python Tkinter and Sqlite3 Login Form
#Made By Namah Jain Form Youtube Channel All About Code
#Please Subscribe To Our Youtube Channel.
#https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from user_specific import *
from user_data import user_record
from similarity_matrix import sim_matrix
from inverted_index import List_of_Courses

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

def cleanup(array,array2):
	for items in array:
		array2.append(items[:len(items)-1])
        
i,j=0,0        

class s(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self,bg="blue")
        
        container.pack(expand=True,fill="both")
        
        self.frame={}
        
        for F in (startpage,main,p1,cr,page2,logout):
            frame=F(container,self)
            
            self.frame[F]=frame
            
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(startpage)
        
    def show_frame(self,container):
        frame=self.frame[container]
        frame.tkraise()




class startpage(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="WELCOME!! CLICK BELOW TO GO TO LOGIN PAGE",font=("Ariel",24),bg="white",fg="blue")
        label.pack(padx=300,pady=100)
        
        button1=Button(self,text="Login",font=("Ariel",24),bg = "red",fg="black",command=
                       lambda: controller.show_frame(main))
        button1.pack(ipadx=200,pady=100)
        
class page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        button1=Button(self,text="Get recommendations",font=("Ariel",24),bg="white",fg="blue",command=
                       lambda: controller.show_frame(p1))
        button1.pack(padx=290,pady=20)
        
        button1=Button(self,text="Logout",font=("Ariel",24),bg = "red",fg="black",command=
                       lambda: controller.show_frame(logout))
        button1.pack(ipadx=250,pady=300)

class logout(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label1=Label(self,text="You have been successfully logged out",font=("Ariel",24),bg="white",fg="blue")
        label1.pack(padx=290,pady=20)
        
        button1=Button(self,text="Click here to go to login again",font=("Ariel",24),bg = "red",fg="black",command=
                       lambda: controller.show_frame(main))
        button1.pack(ipadx=250,pady=300)
    
class main(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.username = StringVar()
        self.password = StringVar()
        self.label1 = Label(self,text ='LOGIN',font = ('',35),pady = 10)
        self.label1.pack(padx=50,pady=50)
        self.label1=Label(self,text = 'Username: ',font = ('',20),pady=5,padx=5).pack()
        Entry(self,textvariable = self.username,bd = 5,font = ('',15)).pack()
        self.label3=Label(self,text = 'Password: ',font = ('',20),pady=5,padx=5).pack()
        Entry(self,textvariable = self.password,bd = 5,font = ('',15),show = '*').pack()
        self.log=Button(self,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).pack()
        self.create=Button(self,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=
                           lambda: controller.show_frame(cr)).pack()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.controller.show_frame(page2)
               
        else:
            ms.showerror('Oops!','Username Not Found.')
            
class cr(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.label1 = Label(self,text ='CREATE ACCOUNT',font = ('',35),pady = 10)
        self.label1.pack(padx=50,pady=50)
        Label(self,text = 'Username: ',font = ('',20),pady=5,padx=5).pack()
        Entry(self,textvariable = self.n_username,bd = 5,font = ('',15)).pack()
        Label(self,text = 'Password: ',font = ('',20),pady=5,padx=5).pack()
        Entry(self,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').pack()
        Button(self,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).pack()
        Button(self,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=
               lambda: controller.show_frame(main)).pack()

    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()
    
class p1(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.array=[]	
        self.text=StringVar()
        i,j=0,0
        self.items=StringVar()
        topics = open('Course-List.txt')
        self.array.extend(topics.readlines())
        self.topic_new=[]
        self.l=[]
        cleanup(self.array,self.topic_new)
        self.var = []
        self.var2 = []
        self.var3=StringVar()
        self.var4=StringVar()
        self.var5=StringVar()
        self.var8=StringVar()
        self.subject_rating={}
        self.sub=[]
        entry = Entry(self,textvariable = self.var8,justify = CENTER)
        entry.place(x=300,y=140)
        self.button1 = Button(self,bg = "blue",activebackground="pink",text="Back to Previous page",fg="black",font=("Ariel",18),command =
                             lambda: controller.show_frame(page2) )
        self.button1.place(x=700,y=10)
        label = Label(self,bg="white",fg="blue",font=("Ariel",30),textvariable=self.var5)
        self.var5.set("Course recommendation system")
        label.place(x=10,y=10)
        label2 = Label(self,bg="white",fg="black",font=("Ariel",18),textvariable=self.var4)
        self.var4.set("Please Enter your subjects")
        label2.place(x=10, y=100)
        self.var.append(StringVar())
        subject1 = OptionMenu(self,self.var[0],*list(self.topic_new))
        self.var[0].set("Enter The Subject")
        subject1.place(x=10,y=140)
        self.var2.append(StringVar())
        #Entry(root,textvariable = var2[0],justify = CENTER).place(x=300,y=140)
        Spinbox(self,textvariable = self.var2[0], from_=1, to=5).place(x=300,y=140)
        self.var2[0].set("")
        self.add = Button(self,bg = "blue",activebackground="pink",text="Add",fg="black",font=("Ariel",18),command =self.action)
        self.add.place(x=10,y=200)
        self.submit=Button(self,bg = "red",activebackground="pink",text="Submit",fg="black",font=("Ariel",18),command =self.action2)
        self.submit.place(x=100,y=200)
        self.submit1=Button(self,bg = "green",activebackground="black",text="Get recomendations",fg="black",font=("Ariel",18),command =self.action3)
        self.submit1.place(x=10,y=300)
        
        
    def action2(self):
        ms.showinfo('Success!','Ratings successfully submitted')
    
    
    def action(self):
        global i,j
        self.sub.append(self.var[i].get())
        self.subject_rating[self.sub[i]]=int(self.var2[i].get())
        i = i+1
        self.var.append(StringVar())
        self.var2.append(StringVar())
        OptionMenu(self,self.var[i],*list(self.topic_new)).place(x=10,y=180+j)
        self.var[i].set("Enter Subject")
        self.add.place(x=10,y=220+j)
        self.submit.place(x=100,y=220+j)
        self.submit1.place(x=10,y=320+j)
    	#Entry(root,textvariable = var2[i],justify = CENTER).place(x=300,y=180+j)
        Spinbox(self,textvariable = self.var2[i], from_=1, to=5).place(x=300,y=180+j)
        self.var2[i].set("")
        j=j+40
    
    def action3(self):
        global i,j
        self.sub.append(self.var[i].get())
        self.subject_rating[self.sub[i]]=int(self.var2[i].get())
        print(self.subject_rating)
        l = Course_recommendation(self.subject_rating,user_record)
        self.display = Label(self,bg="blue",fg="black",font=("Ariel",24),textvariable=self.text)
        self.display.place(x=500,y=300)
        self.text.set("You May Also Like")
        scrollbar=Scrollbar(self)
        scrollbar.pack(side="right")
        mylist=Listbox(self,bg="black",bd=5,fg="red",width=50,height=10,font=('',16),yscrollcommand=scrollbar.set)
        k=0
        for items in l:
            subject=StringVar()
            mylist.insert(END,items)
        mylist.place(x=500,y=350+k)
        scrollbar.config(command=mylist.yview)
    


app=s()
app.mainloop()





