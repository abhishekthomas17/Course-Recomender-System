import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
from user_specific import *
from user_data import user_record
from similarity_matrix import sim_matrix
from inverted_index import List_of_Courses
import sqlite3

i,j=0,0
def cleanup(array,array2):
	for items in array:
		array2.append(items[:len(items)-1])



class s(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self,bg="blue")
        
        container.pack(expand=True,fill="both")
        
        self.frame={}
        
        for F in (startpage,p1):
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
        label.pack(padx=290,pady=20)
        
        button1=Button(self,text="Login",font=("Ariel",24),bg = "red",fg="black",command=
                       lambda: controller.show_frame(p1))
        button1.pack(ipadx=250,pady=300)

class p1(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.array=[]	
        self.text=StringVar()
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
        self.display = Label(self,bg="white",fg="black",font=("Ariel",24),textvariable=self.text)
        self.display.place(x=10,y=260+j)
        self.text.set("You May Also Like")
        k=0
        for items in l:
            subject=StringVar()
            Label(self,bg="white",fg="black",font=("Ariel",18),textvariable=subject).place(x=10,y=320+j+k)
            subject.set(items)
            k=k+40
        
    
app=s()
app.mainloop()