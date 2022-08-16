from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Saver")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightbackground="white")
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(95, 100, image=lock_pic)
canvas.grid(row=0, column=1)

# Website field:
website_label = Label(text="Website: ", bg="white", fg="black")
website_label.grid(column=0, row=1)
website_input = Entry(width=35, bg="white", fg="black", highlightcolor="white")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/User field:
email_label = Label(text="Email/Username: ", bg="white", fg="black")
email_label.grid(column=0, row=2)
email_input = Entry(width=35, bg="white", fg="black")
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, string="dsumpmann@gmail.com")

# Password field:
password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(column=0, row=3)
password_input = Entry(width=18, bg="white", fg="black")
password_input.grid(column=1, row=3)

def gen_pass():
    print("I generated a password hehe")

gen_pass_button = Button(text="Generate Password", highlightbackground="white", command=gen_pass)
gen_pass_button.grid(row=3, column=2)

# Add entry:
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    data = open("data.txt", "a")
    data.write(f"{website} | {email} | {password} \n")
    website_input.delete(0, END)
    password_input.delete(0, END)

add_button = Button(text="Add", width=36, highlightbackground="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()