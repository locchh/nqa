import json
import random
import pytermgui as ptg


# Load dataset
with open("./assets/data.json","r") as f:
    data = json.load(f)

# Shuffle the dataset for random question order
random.shuffle(data)

# Select 5 questions
data = data[:5]

class QnAApp:
    def __init__(self):
        self.index = 0
        self.score = 0
        self.manager = ptg.WindowManager()
        self.main_window = None
        self.feedback_window = None
        self.load_question()

    def load_question(self):
        if self.main_window:
            self.manager.remove(self.main_window)

        if self.index >= len(data):
            self.show_summary()
            return

        question_data = data[self.index]
        self.main_window = ptg.Window(
            ptg.Label(f"[bold]{question_data['question']}[/bold]"),
            *[ptg.Button(f"{option}: {question_data[option]}", lambda _, opt=option: self.check_answer(opt)) for option in ["A", "B", "C", "D"]],
            box=ptg.widgets.boxes.SINGLE,
            title="Quiz Question",
        )

        self.manager.add(self.main_window)

    def check_answer(self, selected):
        correct_answer = data[self.index]["answer"]
        if selected == correct_answer:
            self.score += 1
            feedback = "[green]Correct![/green]"
        else:
            feedback = f"[red]Incorrect! The correct answer is: {correct_answer}[/red]"

        self.show_feedback(feedback)

    def show_feedback(self, feedback):
        if self.feedback_window:
            self.manager.remove(self.feedback_window)

        self.feedback_window = ptg.Window(
            ptg.Label(feedback),
            ptg.Button("Next", lambda *_: self.next_question()),  # Use lambda to avoid extra args
            box=ptg.widgets.boxes.SINGLE,
            title="Feedback",
        )

        self.manager.add(self.feedback_window)

    def next_question(self):
        self.manager.remove(self.feedback_window)
        self.feedback_window = None
        self.index += 1
        self.load_question()

    def show_summary(self):
        self.main_window = ptg.Window(
            ptg.Label(f"[bold]Quiz Completed! Your score: {self.score}/{len(data)}[/bold]"),
            ptg.Button("Exit", lambda *_: self.manager.stop()),  # Use lambda to avoid extra args
            box=ptg.widgets.boxes.SINGLE,
            title="Summary",
        )
        self.manager.add(self.main_window)

    def run(self):
        self.manager.run()


if __name__ == "__main__":
    app = QnAApp()
    app.run()