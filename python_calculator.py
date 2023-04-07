import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 4
        self.equation = ''
        self.result = Label(text='0', font_size=40, size_hint_y=None, height=100)
        self.add_widget(self.result)

        # Add number buttons
        for i in range(1, 10):
            self.add_widget(Button(text=str(i), font_size=40, on_press=self.button_press))

        # Add operator buttons
        self.add_widget(Button(text='+', font_size=40, on_press=self.button_press))
        self.add_widget(Button(text='-', font_size=40, on_press=self.button_press))
        self.add_widget(Button(text='*', font_size=40, on_press=self.button_press))
        self.add_widget(Button(text='/', font_size=40, on_press=self.button_press))

        # Add decimal and zero buttons
        self.add_widget(Button(text='.', font_size=40, on_press=self.button_press))
        self.add_widget(Button(text='0', font_size=40, on_press=self.button_press))

        # Add clear and equals buttons
        self.add_widget(Button(text='C', font_size=40, on_press=self.clear))
        self.add_widget(Button(text='=', font_size=40, on_press=self.calculate))

    def button_press(self, button):
        if button.text == '.':
            if '.' in self.equation:
                return
        self.equation += button.text
        self.result.text = self.equation

    def clear(self, button):
        self.equation = ''
        self.result.text = '0'

    def calculate(self, button):
        if self.equation:
            try:
                self.equation = str(eval(self.equation))
                self.result.text = self.equation
            except ZeroDivisionError:
                self.result.text = "Can't divide by zero"
            except SyntaxError:
                self.result.text = 'Invalid input'
        else:
            self.result.text = '0'


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()



