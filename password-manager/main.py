from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ------------------------------------Search ------------------------------------ #
def find_password():
    website = website_input.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There are no passwords saved!")
    else:
        if len(website) == 0:
            messagebox.showerror(title="Error", message="You haven't typed any info")
        elif website in data:
            email_info = data[website]["email"]
            password_info = data[website]["password"]
            messagebox.showinfo(title="Email/Password", message=f"Email : {email_info} \nPassword : {password_info}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You haven't typed any info")
    else:
        confirm = messagebox.askokcancel(title=website,
                                         message=f"Email : {email}\n Password: {password}\n Is it correct?")
        if confirm:
            try:
                with open("data.json", "r") as file:
                    # Read old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)

                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg="white")

# Canvas setup
canvas = Canvas(width=150, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(75, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "gleny4001@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", relief=GROOVE, bg="white", command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, relief=GROOVE, bg="white", command=add_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, relief=GROOVE, bg="white", command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
