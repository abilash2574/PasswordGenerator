from tkinter import *
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

global data

def get_pass():
    password_feild.delete(0, END)
    if(length_feild.get() == ''):
        data = (3,3,2)
    else:
        tem_len = int(length_feild.get())
        tem_dig = int(digit_feild.get())
        tem_spe = int(special_feild.get())
        data = ((tem_len-(tem_dig+tem_spe), tem_dig, tem_spe))
    length_feild.delete(0, END)
    digit_feild.delete(0, END)
    special_feild.delete(0, END)
    generate = Setup(data)
    pass_word = generate.get_password()
    password_feild.insert(0, pass_word)
    pyperclip.copy(pass_word)
    copied_status = Label(root, text="The password is copied to the clipboard", bg="yellow", fg="black")
    copied_status.grid(row=5)



submit_button = Button(root, text="Enter", command=get_pass)
submit_button.grid(row=3)


# ----------------------------------------------------------------------------

# generate = Setup([3,3,2])
# pass_word = generate.get_password()
# ----------------------------------------------------------------------------

root.mainloop()
