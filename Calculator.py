from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.expression = ""
        layout = BoxLayout(orientation='vertical')

        # Display
        self.display = Button(text="0", font_size=50, halign='right', background_color=[0, 0, 0, 1],
                            background_normal='')
        layout.add_widget(self.display)

        # Buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.display.text

        # Clear the display if "=" is pressed
        if instance.text == '=':
            try:
                result = eval(self.expression)
                self.display.text = str(result)
            except Exception as e:
                self.display.text = "Error"
            self.expression = ""
        elif instance.text == 'C':
            self.display.text = '0'
            self.expression = ""
        else:
            if current_text == '0':
                self.display.text = instance.text
            else:
                self.display.text += instance.text

        # Build the expression to be evaluated
        self.expression = self.display.text


if __name__ == "__main__":
    CalculatorApp().run()
