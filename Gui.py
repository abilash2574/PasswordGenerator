from tkinter import *
from tkinter import messagebox
from setup import Setup
import pyperclip


root = Tk()
root.title("Password Generator")


length_label = Label(root, text="Enter the length of the Password")
length_feild = Entry(root, width=5)
length_label.grid(row=0, column=0)
length_feild.grid(row=0, column=1)

digit_label = Label(root, text="Enter the number of digits to include")
digit_feild = Entry(root, width=5)
digit_label.grid(row=1, column=0)
digit_feild.grid(row=1, column=1)

special_label = Label(root, text="Enter the number of special characters to include")
special_feild = Entry(root, width=5)
special_label.grid(row=2, column=0)
special_feild.grid(row=2, column=1)

password_feild = Entry(root, width=30, borderwidth=5)
password_feild.grid(row=4, column=0)

# This function gets all the password from the Values it gets from the GUI



def get_pass():
    password_feild.delete(0, END)
    if(length_feild.get() == ''):
        messagebox.showerror("No value Entered", "Please Fill the Entry Feilds")       # This is to make a default password, this must be changed
    else:
        try:
            tem_len = int(length_feild.get())
            tem_spe = int(special_feild.get())
            tem_dig = int(digit_feild.get())
        except ValueError as e:
            messagebox.showerror("Input Error","Please enter an Number")
        else:
            data = ((tem_len-(tem_dig+tem_spe), tem_dig, tem_spe))      # Doing the calculation and porcessing
            length_feild.delete(0, END)
            digit_feild.delete(0, END)
            special_feild.delete(0, END)
            generate = Setup(data)          # This is from the Class Setup which is imported and an instance is created
            pass_word = generate.get_password()     # Calling the method
            password_feild.insert(0, pass_word)
            pyperclip.copy(pass_word)           # This is for copying the password directly into the clipboard
            copied_status = Label(root, text="The password is copied to the clipboard", bg="yellow", fg="black")
            copied_status.grid(row=5)



submit_button = Button(root, text="Enter", command=get_pass)
submit_button.grid(row=3)

root.mainloop()
