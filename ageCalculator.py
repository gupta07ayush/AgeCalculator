# Import some functions from tkinter module
from tkinter import Entry, Button, Tk, Label

# import messagebox  class from tkinter
from tkinter import messagebox

# create a object of TK class to create a GUI window
root = Tk()

# set the name of tkinter GUI window
root.title('Age Calculator')

# set the size of root window
root.geometry("700x400")

# set the background color of whole GUI window root
root.config(bg="#344e41")

# Heading Age calculator
heading = Label(root, text='Age Calculator', font=(
    'Times new roman', 50, 'bold'), bg="#3a5a40")
heading.place(x=20, y=20, width=660, height=100)

# frame which contains all user entry boxes
frame = Label(root, font=(
    'Times new roman', 50, 'bold'), bg="#4a4e69")
frame.place(x=20, y=150, width=660, height=200)

# Date of birth heading label
dob = Label(root, text="Date of Birth", bg='#283618', fg='white',
            font=('Helvetica', 15, 'bold'))
dob.place(x=40, y=170, width=200, height=30)

# given date heading label
given_date = Label(root, text="Given Date", bg='#283618', fg='white',
                   font=('Helvetica', 15, 'bold'))
given_date.place(x=400, y=170, width=160, height=30)

# button to display today's date
today = Button(root, text="Today", bg='#283618', fg='#f1faee',
               font=('Helvetica', 14), border=3, relief='raised')
today.place(x=570, y=170, width=90, height=30)

# day label
day = Label(root, text="Day:", bg='#4a4e69', fg='black',
            font=('lucida ', 15))
day.place(x=40, y=210, )

# month label
month = Label(root, text="Month:", bg='#4a4e69', fg='black',
              font=('lucida ', 15))
month.place(x=40, y=240, )

# Year label
year = Label(root, text="Year:", bg='#4a4e69', fg='black',
             font=('lucida ', 15))
year.place(x=40, y=270)

# Date of birth Entry Field
given_day_entry = Entry(root, font=('arial', 15))
given_day_entry.place(x=120, y=210, height=25, width=120)

given_month_entry = Entry(root, font=('arial', 15))
given_month_entry.place(x=120, y=240, height=25, width=120)

given_year_entry = Entry(root, font=('arial', 15))
given_year_entry.place(x=120, y=270, height=25, width=120)


# Given date label


# Given date entry field
given_day_entry = Entry(root, font=('arial', 15))
given_day_entry.place(x=540, y=210, height=25, width=120)

given_month_entry = Entry(root, font=('arial', 15))
given_month_entry.place(x=540, y=240, height=25, width=120)

given_year_entry = Entry(root, font=('arial', 15))
given_year_entry.place(x=540, y=270, height=25, width=120)


# start the GUI
root.mainloop()
