from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Sample quiz questions and answers
quiz_data = [
    {
        'question': 'What is the capital of India?',
        'options': ['Mumbai', 'Delhi', 'Kolkata', 'Pune'],
        'answer': 'Delhi'
    },

    {
        'question': 'Which is the largest planet in our solar system?',
        'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Jupiter'
    },
    {
        'question': 'Who wrote the Ramayana"?',
        'options': ['Kalidasa', 'Valmiki', 'Vyasa', 'Tulsidas'],
        'answer': 'Valmiki'
    },
    {
        'question': 'Who is the father of the computer"?',
        'options': ['Douglas Engelbart', 'René Sommer', 'Albert Newton', 'Charles Babbage'],
        'answer': 'Valmiki'
    },
    {
        'question': 'who wrote the mahabharata"?',
        'options': ['Kalidasa', 'Valmiki', 'Vyasa', 'Tulsidas'],
        'answer': 'Vyasa'
    },
    # Add more questions here...
]

class QuizApp(App):
    def build(self):
        self.score = 0
        self.current_question = 0

        layout = BoxLayout(orientation='vertical')

        # Question label
        self.question_label = Label(text=quiz_data[self.current_question]['question'],
                                    font_size=20, size_hint_y=0.5)
        layout.add_widget(self.question_label)

        # Option buttons
        self.option_buttons = []
        for option in quiz_data[self.current_question]['options']:
            button = Button(text=option, size_hint_y=None, height=50)
            button.bind(on_press=self.check_answer)
            self.option_buttons.append(button)
            layout.add_widget(button)

        return layout

    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = quiz_data[self.current_question]['answer']

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(quiz_data):
            # Update the question and options
            self.question_label.text = quiz_data[self.current_question]['question']
            for i in range(len(self.option_buttons)):
                self.option_buttons[i].text = quiz_data[self.current_question]['options'][i]
        else:
            # Quiz completed, show the result
            self.show_result()

    def show_result(self):
        result_layout = BoxLayout(orientation='vertical')
        result_label = Label(text=f"You scored {self.score}/{len(quiz_data)}",
                            font_size=30, size_hint_y=0.7)
        result_layout.add_widget(result_label)

        restart_button = Button(text="Restart Quiz", size_hint_y=0.3)
        restart_button.bind(on_press=self.restart_quiz)
        result_layout.add_widget(restart_button)

        self.root.clear_widgets()
        self.root.add_widget(result_layout)

    def restart_quiz(self, instance):
        # Reset quiz state and show the first question
        self.score = 0
        self.current_question = 0
        self.question_label.text = quiz_data[self.current_question]['question']
        for i in range(len(self.option_buttons)):
            self.option_buttons[i].text = quiz_data[self.current_question]['options'][i]
        self.root.clear_widgets()
        self.root.add_widget(self.build())


if __name__ == "__main__":
    QuizApp().run()
