import os
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from unicodedata import name
from PIL import ImageTk, Image

root = Tk()  
root.geometry("500x400")
# root.configure(bg="#87CEEB")      #To change the background color of wwindow
root.title("USA Cars Data")

def open_file():
    global file_1,name_1
    file_1 = tk.filedialog.askopenfilenames(filetypes=(('CSV Files', '*.csv'),))
    print(file_1)
    name_1 = os.path.basename(file_1[0])[:-4]
    file.set(name_1)

def find():
    global cars
    data = pd.read_csv(file_1[0])
    cars = len(data[(data['brand']==brand.get()) & (data['state']==state.get()) & (data['color']==color.get())])
    x = f"The number of {color.get()} {brand.get()} cars in {state.get()} are: {cars}"
    result.set(x)
    


label_0 = Label(master=root,text = 'USA Cars Data',font=("Georgia 13 bold",20,"bold")).place(x=150,y=20)
label_1 = Label(master=root,text = 'Select CSV File:',font=("Georgia 13",14)).place(x=30,y=60)

file= StringVar()
Entry_label = Entry(master=root,textvariable = file).place(x=30,y=90,width=250,height=27)

button1 = Button(master=root,relief = "groove", text="Browse", command=open_file).place(x=300,y=90,width=84,height=27)

label_2 = Label(master=root,text = '--------------------------------------------------------------',font=("Georgia 13",17)).place(x=0,y=120)
label_3 = Label(master=root,text = 'Features',font=("Georgia 13 bold",20,"bold")).place(x=180,y=140)
label_4 = Label(master=root,text = 'State: ',font=("Georgia 13",14)).place(x=30,y=180)
label_5 = Label(master=root,text = 'Color: ',font=("Georgia 13",14)).place(x=30,y=220)
label_5 = Label(master=root,text = 'Brand: ',font=("Georgia 13",14)).place(x=30,y=260)

state= StringVar()
Entry_label = Entry(master=root,textvariable = state).place(x=150,y=180,width=150,height=27)
color= StringVar()
Entry_label = Entry(master=root,textvariable = color).place(x=150,y=220,width=150,height=27)
brand= StringVar()
Entry_label = Entry(master=root,textvariable = brand).place(x=150,y=260,width=150,height=27)

label_6 = Label(master=root,text = '--------------------------------------------------------------',font=("Georgia 13",17)).place(x=0,y=300)

button2 = Button(master=root,relief = "groove", text="Find Cars", command=find).place(x=180,y=330,width=150,height=27)

result = StringVar()
label_7 = Label(master=root,textvariable = result,font=("Georgia 13",12)).place(x=30,y=360)

mainloop()