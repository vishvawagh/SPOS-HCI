import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def register_student():
    name = name_entry.get()
    roll_number = roll_entry.get()
    selected_courses = course_combobox.get()

    if not name or not roll_number or not selected_courses:
        messagebox.showerror("Error", "Please fill in all the required fields.")
    else:
        student_info = f"Name: {name}\nRoll Number: {roll_number}\nCourses: {selected_courses}"
        messagebox.showinfo("Registration Successful", student_info)

# Create the main window
window = tk.Tk()
window.title("Student Registration")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)

roll_label = tk.Label(window, text="Roll Number:")
roll_entry = tk.Entry(window)

course_label = tk.Label(window, text="Select Courses:")

# Create a dropdown (combobox) for course selection
courses = ["Math", "Science", "History", "English"]
course_combobox = ttk.Combobox(window, values=courses)

# Set the initial value for the combobox
course_combobox.set("Select Course")

# Create a Register button
register_button = tk.Button(window, text="Register", command=register_student)

# Place widgets on the window using the grid layout manager
name_label.grid(row=0, column=0, sticky='w')
name_entry.grid(row=0, column=1, columnspan=2)

roll_label.grid(row=1, column=0, sticky='w')
roll_entry.grid(row=1, column=1, columnspan=2)

course_label.grid(row=2, column=0, sticky='w')
course_combobox.grid(row=2, column=1, columnspan=2)

register_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter main loop
window.mainloop()