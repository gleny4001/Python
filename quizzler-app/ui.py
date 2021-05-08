from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR, pady=20)
        self.score_label.grid(column=1, row=0)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Buttons
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_check_answer)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_check_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        # text
        self.question_text = self.canvas.create_text(150, 125, font=("Ariel", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)
        else:
            self.canvas.itemconfig(self.question_text, text="The end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check_answer(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_check_answer(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

