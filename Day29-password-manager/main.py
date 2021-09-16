from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password.delete(0, 'end')
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)] \
                    + [random.choice(symbols) for i in range(nr_symbols)] \
                    + [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)
    random_password = "".join(password_list)
    password.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {website.get(): {"email": user.get(), "password": password.get()}}
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Error", message="Oops. Please complete all fields.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
                website.delete(0, 'end')
                password.delete(0, 'end')


def search_website():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_data = data[website.get()]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for this website exist.")
    else:
        messagebox.showinfo(title=website.get(), message=f"Username: {website_data['email']}\n"
                                                         f"Password: {website_data['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/ Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website = Entry(width=32)
website.grid(column=1, row=1)
website.focus()
user = Entry(width=51)
user.grid(column=1, row=2, columnspan=2)
user.insert(END, "lynnlubelihle@hotmail.co.uk")
password = Entry(width=32)
password.grid(column=1, row=3)

# Buttons
add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)
search = Button(text="Search", width=14, command=search_website)
search.grid(column=2, row=1)

window.mainloop()