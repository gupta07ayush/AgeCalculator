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
    'Times new roman', 50, 'bold'), bg="#005f73")
frame.place(x=20, y=150, width=660, height=200)

# start the GUI
root.mainloop()
