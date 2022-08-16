from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Saver")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightbackground="white")
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(95, 100, image=lock_pic)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white", fg="black")
website_label.grid(column=0, row=1)

website_input = Entry(width=35, bg="white", fg="black", highlightcolor="white")
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username: ", bg="white", fg="black")
email_label.grid(column=0, row=2)

email_input = Entry(width=35, bg="white", fg="black")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(column=0, row=3)

password_input = Entry(width=18, bg="white", fg="black")
password_input.grid(column=1, row=3)

def gen_pass():
    print("I generated a password hehe")

gen_pass_button = Button(text="Generate Password", highlightbackground="white", command=gen_pass)
gen_pass_button.grid(row=3, column=2)

def add_password():
    print("hehe I added the password bing bong")

add_button = Button(text="Add", width=36, highlightbackground="white", command=add_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()