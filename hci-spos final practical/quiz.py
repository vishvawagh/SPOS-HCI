import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Online Quiz")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_option": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_option": 0
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "correct_option": 2
            }
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(window, text="", wraplength=300, font=("Arial", 12))
        self.question_label.grid(row=0, padx=20, pady=10, columnspan=2)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(window, text="", variable=self.radio_var, value=i, font=("Arial", 12))
            self.radio_buttons.append(radio_button)
            radio_button.grid(row=i + 1, column=0, padx=20, sticky="w")

        self.next_button = tk.Button(window, text="Next", command=self.check_answer, font=("Arial", 12))
        self.next_button.grid(row=5, padx=20, pady=10, columnspan=2)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                if i < len(options):
                    self.radio_buttons[i].config(text=options[i], state="normal")
                else:
                    self.radio_buttons[i].config(text="", state="disabled")
            self.radio_var.set(-1)
        else:
            self.show_result()

    def check_answer(self):
        if self.radio_var.get() == self.questions[self.current_question]["correct_option"]:
            self.score += 1

        self.current_question += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}")
        self.window.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
