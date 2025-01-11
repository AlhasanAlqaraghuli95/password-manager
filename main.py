import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    # I am joining all the elements in the list with no separation

    password = "".join([char for char in password_list])

    # Delete anything in that field before adding this password
    delete_field(password_entry)

    # Insert the password into the field and also copy it to clipboard
    password_entry.insert(0, password)
    copy_text_to_clipboard(password)

def delete_field(field):
    field.delete(0, tk.END)

def copy_text_to_clipboard(to_copy):
    pyperclip.copy(to_copy)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    fields_filled = check_empty_fields()

    if fields_filled:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        confirm = show_confirmation_message()

        if confirm:
            with open("data.txt", "a") as file:
                file.write(f"{website} \n {email} \n {password}\n\n")

    clear_entry()

# Clear the fields
def clear_entry():
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Setting pop-up message
def show_confirmation_message():

    confirmation = messagebox.askyesno("Confirm details", f"Are the details correct to save? \n\nWebsite: {website_entry.get()} \nEmail: {email_entry.get()} \nPassword: {password_entry.get()}")
    return confirmation

# Ensuring validity of data
def check_empty_fields():

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror("Empty fields", "Please fill in all of the fields before submitting")
        return False
    else:
        return True

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating the image

canvas = tk.Canvas(width = 200, height = 200)
canvas.grid(column = 1, row = 0)

logo_image = tk.PhotoImage(file="logo.png")

# The tuple for create image specifies the x and y coordinates of the center of the image.
# setting it to half the canvas size will center the image
canvas.create_image(100, 100, image=logo_image)

# Labels
website_label = tk.Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = tk.Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = tk.Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# Entries
website_entry = tk.Entry(width = 35)
website_entry.grid(column=1, row=1, columnspan=2, sticky = "EW")
website_entry.focus_set() # Focus the cursor here

email_entry = tk.Entry(width = 35)
email_entry.insert(0, "alhasan.alqaraghuli@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky = "EW")

password_entry = tk.Entry(width = 17)
password_entry.grid(column=1, row=3, sticky = "EW")

# Buttons
password_button = tk.Button(text="Generate Password", command = generate_password)
password_button.grid(column=2, row=3, sticky = "EW")

add_button = tk.Button(text="Add", width = 36, command = save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky = "EW")

window.mainloop()