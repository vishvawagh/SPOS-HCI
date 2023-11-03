import tkinter as tk
from tkinter import messagebox

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    if not username or not password or not email or not phone:
        messagebox.showerror("Error", "Please fill in all the required fields.")
    else:
        # You can implement your signup logic here, such as storing data in a database
        messagebox.showinfo("Signup Successful", "Signup was successful!")

# Create the main window
window = tk.Tk()
window.title("Signup Window")

# Create labels and entry fields
username_label = tk.Label(window, text="Username:")
username_entry = tk.Entry(window)

password_label = tk.Label(window, text="Password:")
password_entry = tk.Entry(window, show="*")  # Hide password characters

email_label = tk.Label(window, text="Email:")
email_entry = tk.Entry(window)

phone_label = tk.Label(window, text="Phone:")
phone_entry = tk.Entry(window)

# Create a signup button
signup_button = tk.Button(window, text="Sign Up", command=sign_up)

# Place widgets on the window using the grid layout manager
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)

phone_label.grid(row=3, column=0)
phone_entry.grid(row=3, column=1)

signup_button.grid(row=4, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
