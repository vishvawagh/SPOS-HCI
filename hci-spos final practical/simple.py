import tkinter as tk

# Create a function to be executed when the button is clicked
def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a label
label = tk.Label(window, text="Welcome to Tkinter", font=("Arial", 16))
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter main loop
window.mainloop()
