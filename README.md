# Simple-Calculator-App

This code is a simple calculator application built using the Kivy framework in Python.

The program creates a GridLayout with four columns to arrange the buttons in the calculator interface. The first row of buttons includes digits 1-9, followed by the four basic arithmetic operations (+, -, *, /), then the decimal point and zero. The last row includes the Clear (C) and Equals (=) buttons.

When the user clicks on a number or an operator button, the button_press() method is called. This method updates the equation string and displays it in the result Label. The clear() method sets the equation to an empty string and sets the result Label to '0'. The calculate() method evaluates the equation string using the eval() function and displays the result in the result Label. If the user attempts to divide by zero or enters an invalid input, an error message is displayed in the result Label instead.

The CalculatorLayout class is a subclass of the Kivy GridLayout and serves as the main widget of the app. The CalculatorApp class is a subclass of the Kivy App and serves as the entry point for the app. The build() method of the CalculatorApp class returns an instance of the CalculatorLayout class.

To run the app, execute the main block at the end of the code, which creates an instance of the CalculatorApp class and calls its run() method.
