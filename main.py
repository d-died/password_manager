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
canvas.pack()



window.mainloop()