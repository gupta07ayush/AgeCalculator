# Import some functions from tkinter module
from tkinter import Entry, Button, Tk, Label, END

# import messagebox  class from tkinter
from tkinter import messagebox

# import datetime module
from datetime import datetime

# create a object of TK class to create a GUI window
root = Tk()

# set the name of tkinter GUI window
root.title('Age Calculator')

# set the size of root window
root.geometry("700x580")

# set the background color of whole GUI window root
root.config(bg="#344e41")


def today():
    # When today button is pressed this button will fill presend date in the field.
    present = datetime.now()
    day = present.strftime('%d')
    month = present.strftime("%m")
    year = present.strftime("%Y")

    # sending the present day values into given entry field
    given_day_entry.insert(END, day)
    given_month_entry.insert(END, month)
    given_year_entry.insert(END, year)


def resultant():
    pass


def clearAll():
    # delete the value of date of birth entry
    day_entry.delete(0, END)
    month_entry.delete(0, END)
    year_entry.delete(0, END)

    # delete the value of given entry
    given_day_entry.delete(0, END)
    given_month_entry.delete(0, END)
    given_year_entry.delete(0, END)


# Heading Age calculator
heading = Label(root, text='Age Calculator', font=(
    'Times new roman', 50, 'bold'), bg="#3a5a40")
heading.place(x=20, y=20, width=660, height=100)

# frame1 which contains all user entry boxes
frame1 = Label(root, font=(
    'Times new roman', 50, 'bold'), bg="#4a4e69")
frame1.place(x=20, y=150, width=660, height=170)

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
               font=('Helvetica', 14), border=4, relief='raised', command=today)
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
day_entry = Entry(root, text="", font=('arial', 15), bg='#ffe5d9')
day_entry.place(x=120, y=210, height=25, width=120)

month_entry = Entry(root, font=('arial', 15), bg='#ffe5d9')
month_entry.place(x=120, y=240, height=25, width=120)

year_entry = Entry(root, font=('arial', 15), bg='#ffe5d9')
year_entry.place(x=120, y=270, height=25, width=120)


# Given date Label
given_day = Label(root, text="Given Day:", bg='#4a4e69', fg='black',
                  font=('lucida ', 15))
given_day.place(x=400, y=210, )

given_month = Label(root, text="Given Month:", bg='#4a4e69', fg='black',
                    font=('lucida ', 15))
given_month.place(x=400, y=240, )

# Year label
given_year = Label(root, text="Given Year:", bg='#4a4e69', fg='black',
                   font=('lucida ', 15))
given_year.place(x=400, y=270)


# Given date entry field
given_day_entry = Entry(root, font=('arial', 15), bg='#ffe5d9')
given_day_entry.place(x=540, y=210, height=25, width=120)

given_month_entry = Entry(root, font=('arial', 15), bg='#ffe5d9')
given_month_entry.place(x=540, y=240, height=25, width=120)

given_year_entry = Entry(root, font=('arial', 15), bg='#ffe5d9')
given_year_entry.place(x=540, y=270, height=25, width=120)

# frame2 which contains results
frame2 = Label(root, font=(
    'Times new roman', 50, 'bold'), bg="#4a4e69")
frame2.place(x=20, y=350, width=660, height=190)

# Resultant age button
resultant_age = Button(root, text="Resultant Age", command=resultant,
                       font=('arial', 15, 'bold'), bg='#22223b', fg='white')
resultant_age.place(x=40, y=360, width=495)

# Clear All Button
clear_all = Button(root, text="Clear All", command=clearAll,
                   font=('arial', 17, 'bold'), bg='#22223b', fg='red')
clear_all.place(x=545, y=360, width=115, height=40)

# Result Labels of years, months and days
years = Label(root, text="Years", bg='#0c1821', fg='white',
              font=('Helvetica', 14,))
years.place(x=200, y=420, width=80, height=35)

months = Label(root, text="Months", bg='#0c1821', fg='white',
               font=('Helvetica', 14,))
months.place(x=300, y=420, width=80, height=35)

days = Label(root, text="Days", bg='#0c1821', fg='white',
             font=('Helvetica', 14,))
days.place(x=400, y=420, width=80, height=35)

# Result values of years, months and days
years_value = Label(root, text="", bg='#4a4e69', fg='white',
                    font=('Helvetica', 35, 'bold'))
years_value.place(x=200, y=470, width=80, height=35)

months_value = Label(root, text="", bg='#4a4e69', fg='white',
                     font=('Helvetica', 35, 'bold'))
months_value.place(x=300, y=470, width=80, height=35)

days_value = Label(root, text="", bg='#4a4e69', fg='white',
                   font=('Helvetica', 35, 'bold'))
days_value.place(x=400, y=470, width=80, height=35)


# start the GUI
root.mainloop()
