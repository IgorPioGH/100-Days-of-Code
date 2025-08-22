from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip
# o * não importa o messagebox, pq ele não é uma classe

# ---------------------------- SEARCH FUNCTION ----------------------------------- #
def find_password():
    user_entry = website_entry.get()
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            try:
                website = data[user_entry]
            except KeyError:
                # Website nao cadastrado
                messagebox.showwarning(title="Website not founded!", message="Make sure you cadastred this website.")
            else:
                # mensagem de senha copiada
                pyperclip.copy(data[user_entry]["password"])
                messagebox.showinfo(title="Password Copied", message=f"Copied your password from the site: {user_entry}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Founded")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8,10)
    nr_symbols = randint(3,4)
    nr_numbers = randint(3,4)

    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_letters = [choice(letters) for _ in range(nr_letters)]
    # Gerar uma lista com todos caracteres
    generated_password = password_letters + password_symbols + password_numbers
    # Embaralhar a lista
    shuffle(generated_password)
    # Passar a lista para string
    string_password = "".join(generated_password)
    # Sobrescrever o campo de senha
    password_entry.delete(0, END)
    password_entry.insert(0, string_password)
    # Copiar para o clipboard
    password_entry.clipboard_clear()
    password_entry.clipboard_append(string_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_file(update_data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(update_data, file, indent=4)


def save_password():
    e_mail = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": e_mail,
            "password": password,
        }
    }

    # Satandard dialogs -> MessageBoxe
    if website == "" or password == "":
        messagebox.showwarning(title="Empty Entry", message="Make sure you wrote a password or a website")
    else:
        try:
            with open("data.json", "r", encoding='utf-8') as file:
                # reading all data
                data = json.load(file)
                # update all data with new_data
                data.update(new_data)
        except json.decoder.JSONDecodeError:
            # insert the first item
            update_file(new_data)
        except FileNotFoundError:
            # insert the first item
            update_file(new_data)
        else:
            update_file(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# criando a tela
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# pegando a imagem
canva = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file='logo.png')
canva.create_image(100, 100, image=logo_image)
canva.grid(column=1, row=0)

# Criando widgets
# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2,sticky="EW")
email_entry.insert(END, "email_teste@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3,sticky="EW")

# Buttons
generate_button = Button(text='Generate Password', command=create_password)
generate_button.grid(column= 2, row=3, sticky="EW")

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1 , row=4, columnspan=2,sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()