from cgitb import text
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter import font
from turtle import width

win = tk.Tk()
win.geometry('1350x200')
win.title("Laboratory Register")

win.config(bg="black")

title_label1 = tk.Label(win, text = "Laboratory Register", font=("Arial",30,"bold"),border=12,relief=tk.GROOVE, bg ="yellow",foreground="black") 
title_label1.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Enter Lab Record", font=("Arial,25"), bg="black",foreground="yellow",relief=tk.GROOVE)
detail_frame.place(x=20,y=150,width=450,height=550)

data_frame = tk.Frame(win,bd=12,bg = "black", relief = tk.GROOVE)
data_frame.place(x=475,y=90,width=1050,height=680)

"""Entry"""

expno_lb1 = tk.Label(detail_frame,text="Exp No",font=("Arial",17), bg = "yellow",)
expno_lb1.grid(row=0,column=0,padx=2,pady=2)

expno_ent1 = tk.Entry(detail_frame,bd=7,font=("Arial",17))
expno_ent1.grid(row=0,column=1,padx=2,pady=2)


batch_lb2 = tk.Label(detail_frame,text="Batch",font=("Arial",17), bg = "yellow",)
batch_lb2.grid(row=1,column=0,padx=2,pady=2)

batch_ent2 = tk.Entry(detail_frame,bd=7,font=("Arial",17))
batch_ent2.grid(row=1,column=1,padx=2,pady=2)

rollno_lb1 = tk.Label(detail_frame,text="Roll No",font=("Arial",17), bg = "yellow",)
rollno_lb1.grid(row=2,column=0,padx=2,pady=2)

rollno_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
rollno_ent.grid(row=2,column=1,padx=2,pady=2)

doec_lb1 = tk.Label(detail_frame,text="Date of Starting Exp",font=("Arial",17), bg = "yellow",)
doec_lb1.grid(row=3,column=0,padx=2,pady=2)

doec_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
doec_ent.grid(row=3,column=1,padx=2,pady=2)

doef_lb1 = tk.Label(detail_frame,text="Date of Completion of Exp",font=("Arial",17), bg = "yellow",)
doef_lb1.grid(row=4,column=0,padx=2,pady=2)

doef_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
doef_ent.grid(row=4,column=1,padx=2,pady=2)

edoef_lb1 = tk.Label(detail_frame,text="Expected Date of Exp Checking",font=("Arial",17), bg = "yellow",)
edoef_lb1.grid(row=5,column=0,padx=2,pady=2)

edoef_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
edoef_ent.grid(row=5,column=1,padx=2,pady=2)

doed_lb1 = tk.Label(detail_frame,text="Date of Exp Checked",font=("Arial",17), bg = "yellow",)
doed_lb1.grid(row=6,column=0,padx=2,pady=2)

doed_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
doed_ent.grid(row=6,column=1,padx=2,pady=2)

doed_lb1 = tk.Label(detail_frame,text="Marks",font=("Arial",17), bg = "yellow",)
doed_lb1.grid(row=7,column=0,padx=2,pady=2)

doed_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17))
doed_ent.grid(row=7,column=1,padx=2,pady=2)



"""********"""

"""BUTTON"""

btn_frame = tk.Frame(detail_frame,bg="yellow",bd="10",relief=tk.GROOVE)
btn_frame.place(x=50,y=400,width=370,height=110)

add_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Add",bd=7,font=("Arial",12),width=17)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Update",bd=7,font=("Arial",12),width=16)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Delete",bd=7,font=("Arial",11),width=17)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Clear",bd=7,font=("Arial",11),width=16)
clear_btn.grid(row=1,column=1,padx=2,pady=2)

"""DONE BUTTON"""

search_frame = tk.Frame(data_frame,bg="black",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lb1 = tk.Label(search_frame,text="Search",fg="yellow",bg="black",font=("Arial",14))
search_lb1.grid(row=0, column=0, padx=2, pady=2)

"""SEARCH"""



"""Search Done"""

win.mainloop()


