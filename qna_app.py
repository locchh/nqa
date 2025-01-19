import json
import random
import pytermgui as ptg


# Constants
TOTAL_QUESTIONS = 5
DATASET_PATH = "./assets/data.json"
DEFAULT_WINDOW_WIDTH = 80
WINDOW_HEIGHT = 5
WINDOW_PADDING = (2, 2)


class QnAApp:
    def __init__(self):
        self.index = 0
        self.score = 0
        self.manager = ptg.WindowManager()
        self.main_window = None
        self.feedback_window = None
        self.questions = self.load_questions()
        self.load_question()

    @staticmethod
    def load_questions():
        """Load and shuffle the dataset, returning the selected number of questions."""
        with open(DATASET_PATH, "r") as file:
            data = json.load(file)
        random.shuffle(data)
        return data[:TOTAL_QUESTIONS]

    def format_question(self, question):
        """Split long questions into multiple lines for better readability."""
        max_line_length = 60
        words = question.split()
        lines = []
        current_line = []

        for word in words:
            if sum(len(w) for w in current_line) + len(current_line) + len(word) <= max_line_length:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
        lines.append(" ".join(current_line))

        return "\n".join(lines)

    def load_question(self):
        """Load and display the current question."""
        if self.main_window:
            self.manager.remove(self.main_window)

        if self.index >= len(self.questions):
            self.show_summary()
            return

        question_data = self.questions[self.index]
        formatted_question = self.format_question(question_data["question"])

        self.main_window = ptg.Window(
            ptg.Label(f"[bold]{formatted_question}[/bold]"),
            *[
                ptg.Button(
                    f"{option}: {question_data[option]}",
                    lambda _, opt=option: self.check_answer(opt),
                )
                for option in ["A", "B", "C", "D"]
            ],
            box=ptg.widgets.boxes.SINGLE,
            title="Quiz Question",
            padding=WINDOW_PADDING,
            width=DEFAULT_WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.manager.add(self.main_window)

    def check_answer(self, selected_option):
        """Validate the selected answer and show feedback."""
        correct_answer = self.questions[self.index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            feedback = "[green]Correct![/green]"
        else:
            feedback = f"[red]Incorrect! The correct answer is: {correct_answer}[/red]"
        self.show_feedback(feedback)

    def show_feedback(self, feedback):
        """Display feedback after answering a question."""
        if self.feedback_window:
            self.manager.remove(self.feedback_window)

        self.feedback_window = ptg.Window(
            ptg.Label(feedback),
            ptg.Button("Next", lambda _: self.next_question()),
            box=ptg.widgets.boxes.SINGLE,
            title="Feedback",
            padding=WINDOW_PADDING,
            width=DEFAULT_WINDOW_WIDTH,
        )

        self.manager.add(self.feedback_window)

    def next_question(self):
        """Move to the next question."""
        if self.feedback_window:
            self.manager.remove(self.feedback_window)
            self.feedback_window = None
        self.index += 1
        self.load_question()

    def show_summary(self):
        """Display the quiz summary with the final score."""
        self.main_window = ptg.Window(
            ptg.Label(f"[bold]Quiz Completed! Your score: {self.score}/{len(self.questions)}[/bold]"),
            ptg.Button("Exit", lambda _: self.manager.stop()),
            box=ptg.widgets.boxes.SINGLE,
            title="Summary",
            padding=WINDOW_PADDING,
            width=DEFAULT_WINDOW_WIDTH,
        )
        self.manager.add(self.main_window)

    def run(self):
        """Start the quiz application."""
        self.manager.run()


if __name__ == "__main__":
    app = QnAApp()
    app.run()
