import tkinter as tk
import random

# Sample quiz questions - Add more questions here
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Venus", "Mars", "Jupiter", "Neptune"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")
        self.score = 0
        self.current_question = None
        self.create_widgets()
        self.load_next_question()

    def create_widgets(self):
        self.welcome_label = tk.Label(self, text="Welcome to the Quiz Game!")
        self.welcome_label.pack(pady=10)

        self.question_label = tk.Label(self, text="")
        self.question_label.pack(pady=10)

        self.choices_var = tk.StringVar()
        self.choices_var.set("")
        self.choices_label = tk.Label(self, textvariable=self.choices_var)
        self.choices_label.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self, textvariable=self.answer_var)
        self.answer_entry.pack(pady=10)

        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def load_next_question(self):
        if quiz_questions:
            self.current_question = random.choice(quiz_questions)
            self.question_label.config(text=self.current_question["question"])
            self.choices_var.set("\n".join(self.current_question["choices"]))
            self.feedback_label.config(text="")
            self.answer_var.set("")
        else:
            self.display_final_results()

    def check_answer(self):
        user_answer = self.answer_var.get()

        if user_answer.lower() == self.current_question["correct_answer"].lower():
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is: {self.current_question['correct_answer']}", fg="red")

        quiz_questions.remove(self.current_question)
        self.after(1500, self.load_next_question)  # Display feedback for 1.5 seconds and load the next question

    def display_final_results(self):
        self.question_label.config(text=f"Quiz completed!\nYour score: {self.score}/{len(quiz_questions) + self.score}")
        self.choices_var.set("")
        self.answer_entry.pack_forget()
        self.feedback_label.pack_forget()
        self.submit_button.pack_forget()

        if self.score == len(quiz_questions):
            performance_message = "Congratulations! You got all the questions right!"
        else:
            performance_message = "Keep practicing to improve your score!"

        self.performance_label = tk.Label(self, text=performance_message)
        self.performance_label.pack(pady=10)

        self.play_again_button = tk.Button(self, text="Play Again", command=self.restart_quiz)
        self.play_again_button.pack(pady=10)

    def restart_quiz(self):
        quiz_questions.extend(self.used_questions)
        self.score = 0
        self.current_question = None
        self.performance_label.pack_forget()
        self.play_again_button.pack_forget()
        self.answer_entry.pack(pady=10)
        self.feedback_label.pack(pady=10)
        self.submit_button.pack(pady=10)
        self.load_next_question()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
