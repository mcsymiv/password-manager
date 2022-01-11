from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def grid(row, column):
    """
    :return: dictionary {"row": r, "column": c}
    """
    return {"row": row, "column": column}


def add_password():
    web = website_input.get()
    email = email_input.get()
    key = password_input.get()
    data = {}
    new_key_entry = {
        web: {
            "email": email,
            "key": key
        }
    }

    if web == "" or key == "":
        messagebox.showerror(title="Error", message="Empty password")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading existing data
                data = json.load(fp=data_file)
        except FileNotFoundError:
            data = new_key_entry
        else:
            # Update data with new data_entry
            data.update(new_key_entry)
        finally:
            with open("data.json", mode="w") as data_file:
                json.dump(obj=data, fp=data_file, indent=4)
                website_input.delete(0, "end")
                password_input.delete(0, "end")


def generate_password():
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)


def search_website():
    website = website_input.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                key = data[website]["key"]
                messagebox.showinfo(title="Your entry", message=f"Email: {email}\nPassword: {key}")
            else:
                messagebox.showerror(title="Oops", message=f"No {website} entry is present")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There are no data")


# window
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=20)

# canvas
canvas = Canvas(width=148, height=128)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(10, 128, image=lock_img)
canvas.grid(row=0, column=0, rowspan=4)

# -------- Labels --------- #
# website label
website_label = Label(text="Website", justify="left")
website_label.grid(row=0, column=1)

# email label
email_label = Label(text="Email/Username")
email_label.grid(row=1, column=1)

# password label
password_label = Label(text="Password")
password_label.grid(row=2, column=1)

# -------- Entries --------- #
# website text input
website_input = Entry(width=20)
website_input.grid(row=0, column=2)
website_input.focus()
# email text input
email_input = Entry(width=30)
email_input.insert(0, string="s.mcsymiv@gmail.com")
email_input.grid(row=1, column=2, columnspan=2)
# password text input
password_input = Entry(width=20)
password_input.grid(row=2, column=2)

# -------- Buttons --------- #
# password generate button
password_generate_button = Button(text="Generate", command=generate_password)
password_generate_button.grid(row=2, column=3)

# add password button
add_password_button = Button(text="Add", width=20, command=add_password)
add_password_button.grid(row=3, column=1, columnspan=3)

website_search = Button(text="Search", command=search_website)
website_search.grid(row=0, column=3)

root.mainloop()
