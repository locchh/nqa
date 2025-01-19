# QnA App Documentation

## Code

```python

import random
import pytermgui as ptg


# Sample dataset
data = [
    {"question": "What is the capital of France?", "answer": "A", "A": "Paris", "B": "Berlin", "C": "Madrid", "D": "Rome"},
    {"question": "What is 2 + 2?", "answer": "C", "A": "3", "B": "5", "C": "4", "D": "6"},
    {"question": "What is the color of the sky?", "answer": "B", "A": "Green", "B": "Blue", "C": "Red", "D": "Yellow"},
]

# Shuffle the dataset for random question order
random.shuffle(data)


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

```

## Overview

The `QnAApp` is an interactive terminal-based quiz application that presents users with a series of multiple-choice questions. It leverages the `pytermgui` library for rendering the graphical user interface in the terminal. The app displays questions, allows users to select answers, and provides feedback on their selections. Upon completing the quiz, the app shows a summary of the user's score.

## Features

- Randomizes the order of questions each time the quiz is started.
- Displays multiple-choice questions with four options (A, B, C, D).
- Provides immediate feedback on whether the user's answer is correct or incorrect.
- Displays the correct answer if the user selects an incorrect option.
- Tracks the user's score and shows it at the end of the quiz.
- Simple and user-friendly terminal interface using `pytermgui`.

## Code Breakdown

### 1. **Import Libraries**

```python
import random
import pytermgui as ptg
```

- `random`: Used to shuffle the question dataset, ensuring a random order of questions each time the quiz is started.
- `pytermgui`: A terminal GUI library used to create interactive components such as buttons, labels, and windows.

### 2. **Sample Dataset**

```python
data = [
    {"question": "What is the capital of France?", "answer": "A", "A": "Paris", "B": "Berlin", "C": "Madrid", "D": "Rome"},
    {"question": "What is 2 + 2?", "answer": "C", "A": "3", "B": "5", "C": "4", "D": "6"},
    {"question": "What is the color of the sky?", "answer": "B", "A": "Green", "B": "Blue", "C": "Red", "D": "Yellow"},
]
```

The `data` list contains dictionaries representing individual quiz questions. Each dictionary holds:
- The `question` string.
- The `answer` key, which indicates the correct answer (e.g., "A", "B", "C", or "D").
- Options "A", "B", "C", and "D" provide the possible answers.

### 3. **Shuffling Questions**

```python
random.shuffle(data)
```

This line randomly shuffles the question list to ensure that questions appear in a different order every time the app is run.

### 4. **QnAApp Class**

The `QnAApp` class encapsulates the main logic of the quiz application.

#### Attributes:
- `index`: Keeps track of the current question.
- `score`: Tracks the user's score.
- `manager`: The `WindowManager` instance responsible for handling GUI windows.
- `main_window`: The window that displays the current question.
- `feedback_window`: The window that shows feedback after answering a question.

#### Methods:

- **`__init__(self)`**: Initializes the app by setting the starting question index to 0, score to 0, and preparing the `WindowManager`. It also loads the first question.
  
- **`load_question(self)`**: Loads the current question and displays the options. If all questions have been answered, it shows the summary screen.

- **`check_answer(self, selected)`**: Checks if the selected answer is correct. If correct, it increases the score. Displays feedback (either "Correct!" or "Incorrect!") based on the user's choice.

- **`show_feedback(self, feedback)`**: Displays a window with the feedback message and a "Next" button. Clicking "Next" takes the user to the next question.

- **`next_question(self)`**: Moves to the next question by incrementing the `index` and loading the next question.

- **`show_summary(self)`**: Displays the final score summary after the quiz is completed.

- **`run(self)`**: Runs the application and starts the event loop.

### 5. **Main Program Execution**

```python
if __name__ == "__main__":
    app = QnAApp()
    app.run()
```

This block ensures that the app runs when executed as the main script. It creates an instance of the `QnAApp` class and calls its `run()` method to start the application.

## Usage

### Requirements:
- Python 3.x
- `pytermgui` library (install via `pip install pytermgui`)

### Running the App:

1. Clone or download the script.
2. Install the required dependencies:
   ```bash
   pip install pytermgui
   ```
3. Run the script:
   ```bash
   python qna_app.py
   ```
4. The app will display the first question with multiple-choice options. Use the arrow keys or number keys to select an option.
5. After each question, feedback will be shown. Click "Next" to proceed to the next question.
6. At the end of the quiz, the app will display your score.

## Conclusion

The `QnAApp` provides a simple, interactive terminal-based quiz experience, making use of `pytermgui` for a graphical user interface. It supports randomized questions, answer checking, and provides a final score summary. This app can be easily extended by adding more questions to the dataset or modifying the interface for additional features.