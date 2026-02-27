import tkinter as tk
from tkinter import messagebox

def displayData():
    first = entFirst.get().strip()
    last = entLast.get().strip()
    email = entEmail.get().strip()
    phone = entPhone.get().strip()

    # first and last plus other information
    if not first or not last:
        messagebox.showwarning("Missing Info", "Please enter your First Name and Last Name.")
        return

    msg = (
        f"Welcome to tkinter, {first}\n"
        f"You entered:\n"
        f"Name: {first} {last}\n"
        f"Email: {email}\n"
        f"Phone: {phone}"
    )

    messagebox.showinfo("tkinter Form", msg)

def Clear():
    # clears out entry boxes
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)
    entFirst.focus_set()

# main form
root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")

# label frame
lblFrPerson = tk.LabelFrame(root, text="Personal Information")
lblFrPerson.pack(padx=20, pady=20, fill="x")

# labels + entries
brand_bg = "blue"
brand_fg = "white"

lblFirst = tk.Label(lblFrPerson, text="First Name:", bg=brand_bg, fg=brand_fg)
lblFirst.grid(column=0, row=0, padx=8, pady=6, sticky="e")

entFirst = tk.Entry(lblFrPerson)
entFirst.grid(column=1, row=0, padx=8, pady=6, sticky="w")

lblLast = tk.Label(lblFrPerson, text="Last Name:", bg=brand_bg, fg=brand_fg)
lblLast.grid(column=0, row=1, padx=8, pady=6, sticky="e")

entLast = tk.Entry(lblFrPerson)
entLast.grid(column=1, row=1, padx=8, pady=6, sticky="w")

lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column=0, row=2, padx=8, pady=6, sticky="e")

entEmail = tk.Entry(lblFrPerson)
entEmail.grid(column=1, row=2, padx=8, pady=6, sticky="w")

lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column=0, row=3, padx=8, pady=6, sticky="e")

entPhone = tk.Entry(lblFrPerson)
entPhone.grid(column=1, row=3, padx=8, pady=6, sticky="w")

# button frame
fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)

btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=6)

btnR = tk.Button(fraButtons, text="Reset", width=5, command=Clear)
btnR.pack(side=tk.LEFT, padx=6)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=6)

entFirst.focus_set()
root.mainloop()