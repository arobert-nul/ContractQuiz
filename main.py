import tkinter as tk
from name_validation import validate_name
from question import Question
from storage import save_result, load_results
from tkinter import filedialog
import shutil

QUESTIONS = [
    Question("What is the age range for the TCIAG Contract?", ["13-18", "19-25", "19-45", "All adults"], "A"),
    Question("Would an under 18 be eligible for Connect to Work?", ["Yes", "No", "Yes, if they match certain elgibilty criteria", "Yes, if they are able to pay"], "C"),
    Question("Are courses funded by ASF open to under 18s?", ["Yes", "No", "Yes, but they must pay tuition fees", "Yes, as long as they are not working or in education"], "B"),
    Question("Can 18 year olds be seen on the National Careers Service?", ["Yes", "No", "Yes, but they must not be in employment or education", "Yes, but they must attend appointments with a parent or guardian"], "C"),
]

class QuizApp:
    """Quiz Application"""

    def __init__(self, window):
        """Set up the window, buttons and labels"""
        self.window = window
        self.window.title("Inspira Contract Quiz")
        self.window.geometry("1400x1024")

        tk.Label(window, text="Inspira Contract Quiz", font=("Arial", 60)).pack(pady=20)
        tk.Label(window, text="Your name:").pack()
        self.name_entry = tk.Entry(window, width=30)
        self.name_entry.pack()
        self.error_label = tk.Label(window, text="", fg="red")
        self.error_label.pack()
        tk.Button(window, text="Start", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        """Starts quiz"""
        name = self.name_entry.get()
        if not validate_name(name):
            self.error_label.config(text="Please enter your name.")
        else:
            self.name = name
            self.current = 0
            self.score = 0
            self.show_question()

    def clear_screen(self):
        """Remove everything from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_question(self):
        """Shows a question"""
        self.clear_screen()
        question = QUESTIONS[self.current]
        tk.Label(self.window, text=f"Question {self.current + 1} of {len(QUESTIONS)}").pack(pady=10)
        tk.Label(self.window, text=question.question_text, font=("Arial", 18)).pack(pady=20)
        self.choice = tk.StringVar()
        for letter, answer in zip(["A", "B", "C", "D"], question.answers):
            tk.Radiobutton(self.window, text=letter + ". " + answer,
                           variable=self.choice, value=letter).pack()
        self.feedback_label = tk.Label(self.window, text="")
        self.feedback_label.pack(pady=10)
        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        """Selected answer is checked against correct answer"""
        question = QUESTIONS[self.current]
        choice = self.choice.get()
        if choice == "":
            self.feedback_label.config(text="Please choose an answer.", fg="red")
            return
        elif question.is_correct(choice):
            self.score = self.score + 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect", fg="red")
        self.submit_button.config(state="disabled")
        tk.Button(self.window, text="Next", command=self.next_question).pack(pady=10)

    def next_question(self):
        """Brings up next question on window"""
        self.current = self.current + 1
        if self.current < len(QUESTIONS):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        """Clears questions and shows results"""
        self.clear_screen()
        tk.Label(self.window, text=f"{self.name}, you scored {self.score} out of {len(QUESTIONS)}",
                 font=("Arial", 24)).pack(pady=40)
        if not save_result("results.csv", self.name, self.score, len(QUESTIONS)):
            tk.Label(self.window, text="Your result could not be saved.", fg="red").pack()
        tk.Button(self.window, text="View all results", command=self.show_history).pack(pady=20)
    
    def show_history(self):
        """Show a history of all results"""
        self.clear_screen()
        tk.Label(self.window, text="All results", font=("Arial", 24)).pack(pady=20)
        results = load_results("results.csv")
        if results == []:
            tk.Label(self.window, text="No results saved yet.").pack()
        for row in results:
            tk.Label(self.window, text=row[0] + " " + row[1] + "/" + row[2]).pack()
        tk.Button(self.window, text="Export results", command=self.export_results).pack(pady=20)
        self.export_label = tk.Label(self.window, text="")
        self.export_label.pack()

    def export_results(self):
        """Exports results as a CSV"""
        destination = filedialog.asksaveasfilename(defaultextension=".csv",
                                                   filetypes=[("CSV files", "*.csv")])
        if destination == "":
            return
        try:
            shutil.copyfile("results.csv", destination)
            self.export_label.config(text="Results exported.", fg="green")
        except OSError:
            self.export_label.config(text="Export failed.", fg="red")


window = tk.Tk()
app = QuizApp(window)
window.mainloop()