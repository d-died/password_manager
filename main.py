from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for letter in range(randint(8, 10))]
    random_numbers = [choice(numbers) for number in range(randint(2, 4))]
    random_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = random_symbols + random_numbers + random_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showinfo(title="OOPS", message="Please don't leave fields blank!")
    else:
        save_details = messagebox.askokcancel(title=website, message=f"The details you entered are as follows: \n Email: {email} \n "
                                                      f"Password: {password} \n Would you like to save these details?")
        if save_details:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)

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

# Generate password button:
gen_pass_button = Button(text="Generate Password", highlightbackground="white", command=gen_password)
gen_pass_button.grid(row=3, column=2)

# Add entry to txt file:
add_button = Button(text="Add", width=36, highlightbackground="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()