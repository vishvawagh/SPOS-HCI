import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c")
    if feedback:
        # You can process the feedback here (e.g., store it in a database)
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        clear_feedback()
    else:
        messagebox.showerror("Error", "Please provide your feedback before submitting.")

def clear_feedback():
    feedback_text.delete("1.0", "end")

# Create the main window
window = tk.Tk()
window.title("Hotel Feedback Form")

# Create a label for the title
title_label = tk.Label(window, text="Customer Feedback Form", font=("Arial", 16))
title_label.pack(pady=10)

# Create a label for the feedback field
feedback_label = tk.Label(window, text="Your Feedback:")
feedback_label.pack()

# Create a text widget for entering feedback
feedback_text = tk.Text(window, height=5, width=40)
feedback_text.pack()

# Create a Submit button
submit_button = tk.Button(window, text="Submit Feedback", command=submit_feedback)
submit_button.pack(pady=10)

# Create a Clear button
clear_button = tk.Button(window, text="Clear Feedback", command=clear_feedback)
clear_button.pack()

# Start the Tkinter main loop
window.mainloop()
