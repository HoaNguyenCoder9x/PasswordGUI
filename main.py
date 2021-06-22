from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for p in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for q in range(random.randint(8, 10))]
    random.shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    website = entry_website.get()
    password = entry_password.get()
    # is_empty = messagebox.askyesno(title='Confirm information', message='Do you want to add this information?')

    if website == '' or password == '':
        messagebox.showerror(title='Warning', message='You must fill all information')

    else:
        is_ok = messagebox.askokcancel(title='Warning Messege', message=f'website: {website}\nemail: {email}\n'        
                                                                f'password: {password} \n')
        if is_ok:
            with open('data.txt', mode='a') as data:
                data.write(f'{website} | {email} | {password} \n')
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.maxsize(width=200, height=200)
window.title('Password GUI')
window.config(pady=50, padx=50, bg='pink')

canvas = Canvas(width=210, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(105, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2)

#label website
label_website = Label(text='Website: ', bg='pink', font=('Arial', 10, 'bold'))
label_website.grid(column=0, row=1)

#label email
label_email = Label(text='Email: ', bg='pink', font=('Arial', 10, 'bold'))
label_email.grid(column=0, row=2)

#label Password
label_password = Label(text='Password: ', bg='pink', font=('Arial', 10, 'bold'))
label_password.grid(column=0, row=3)

#entry website
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

#Entry_email
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, 'hoa.ntt5224@sinhvien.hoasen.edu.vn')
email = entry_email.get()

#Entry password
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, columnspan=1)
password = entry_password.get()

#Button_generatePw
button_generate_pw = Button(width=11, text='Generate', height=1, command= generate_pw)
button_generate_pw.grid(column=2, row=3)

#button add
button_generate_pw = Button(width=30, text='Add', command=save_pw)
button_generate_pw.grid(column=1, row=4, columnspan=2)



window.mainloop()
