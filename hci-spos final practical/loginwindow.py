import tkinter as tk
from tkinter import messagebox

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # You can implement your login logic here
    # For simplicity, we'll assume a successful login for demonstration
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Login Successful", "Login was successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
window = tk.Tk()
window.title("Login Window")

# Create labels
username_label = tk.Label(window, text="Username:")
password_label = tk.Label(window, text="Password:")

# Create entry widgets for user input
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")  # The "show" attribute hides the password characters

# Create a login button
login_button = tk.Button(window, text="Login", command=check_login)

# Place widgets on the window using the grid layout manager
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
