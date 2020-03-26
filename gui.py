import os,tkinter,json
from tkinter import *
from tkinter import messagebox as ms
from user_specific import *
from user_data import user_record
from similarity_matrix import sim_matrix
from inverted_index import List_of_Courses


root = Tk()
root.title('Course Recommender System')
root.geometry("750x750")
array=[]	
i,j=0,0
topics = open('Course-List.txt')
array.extend(topics.readlines())
def cleanup(array,array2):
	for items in array:
		array2.append(items[:len(items)-2])
        
def action():
    global i,j
    sub.append(var[i].get())
    subject_rating[sub[i]]=int(var2[i].get())
    i = i+1
    var.append(StringVar())
    var2.append(StringVar())
    OptionMenu(root,var[i],*list(topic_new)).place(x=10,y=180+j)
    var[i].set("Enter Subject")	
    add.place(x=10,y=220+j)
    submit1.place(x=10,y=320+j)
    submit.place(x=100,y=220+j)
    #Entry(root,textvariable = var2[i],justify = CENTER).place(x=300,y=180+j)
    Spinbox(root,textvariable = var2[i], from_=1, to=5).place(x=300,y=180+j)
    var2[i].set("")
    j=j+40

def action2():
    ms.showinfo('Success!','Ratings successfully submitted')
    
	
def action3():
    sub.append(var[i].get())
    subject_rating[sub[i]]=int(var2[i].get())
    print(subject_rating)
    l = Course_recommendation(subject_rating,user_record)
    # l contans a list of top 10 courses to be recommended
    text = StringVar()	
    display = Label(bg="white",fg="black",font=("Ariel",24),textvariable=text)
    display.place(x=10,y=360+j)
    text.set("Recommended Courses For you")
    k=0
    for items in l:
        subject = StringVar()
        Label(bg="white",fg="black",font=("Ariel",18),textvariable=subject).place(x=10,y=420+j+k)
        subject.set(items)
        k=k+40
	


topic_new=[]
cleanup(array,topic_new)
var = []
var2 = []
var3=StringVar()
var4=StringVar()
var5=StringVar()
var8=StringVar()
subject_rating={}
sub=[]

entry = Entry(root,textvariable = var8,justify = CENTER)
entry.place(x=300,y=140)
label = Label(bg="white",fg="blue",font=("Ariel",30),textvariable=var5)
var5.set("Course Recommender System")
label.place(x=10,y=10)
root.configure(background = "white")
label2 = Label(bg="white",fg="black",font=("Ariel",18),textvariable=var4)
var4.set("Please Enter your subjects")
label2.place(x=10, y=100)
var.append(StringVar())
subject1 = OptionMenu(root,var[0],*list(topic_new))
var[0].set("Enter The Subject")
subject1.place(x=10,y=140)
var2.append(StringVar())
#Entry(root,textvariable = var2[0],justify = CENTER).place(x=300,y=140)
Spinbox(root,textvariable = var2[0], from_=1, to=5).place(x=300,y=140)
var2[0].set("")
add = Button(root,bg = "red",activebackground="black",text="Add",fg="black",font=("Ariel",18),command = action)
add.place(x=10,y=200)
submit=Button(root,bg = "green",activebackground="black",text="Submit",fg="black",font=("Ariel",18),command = action2)
submit.place(x=100,y=200)
submit1=Button(root,bg = "blue",activebackground="black",text="Get recomendations",fg="black",font=("Ariel",18),command = action3)
submit1.place(x=10,y=300)
root.mainloop()
