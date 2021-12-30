from tkinter import *
from datetime import date
import datetime 
from tkinter import messagebox

today = date.today()
current_time = datetime.datetime.now() 


# print (current_time.year) 
    
# print (current_time.month) 

# print (current_time.day) 


root = Tk()


def test():
    what_year = int(year_entry.get())
    if what_year > current_time.year:
        error = messagebox.askokcancel("Name Error ", "Please Enter an valid year")
    what_month = int(month_entry.get())
    print(current_time.year - what_year)
    difference = 1 -4
    print(current_time.month - what_month)



dob = Label(root, text="Enter you Date of Birth creditials below :- ")
dob.grid(row=0, column=0, columnspan=3)

year_label = Label(root, text="Year: -- ").grid(row=1, column=0)
year_entry = Entry(root)
year_entry.grid(row=1, column=1)


month_label = Label(root, text="Month: -- ").grid(row=2, column=0)
month_entry = Entry(root)
month_entry.grid(row=2, column=1)


day_label = Label(root, text="Day: -- ").grid(row=3, column=0)
day_entry = Entry(root)
day_entry.grid(row=3, column=1)

calculate = Button(root, text='Calculate age', command=test).grid(row=4, column=1)

root.mainloop()