from gui import *
import formulas

class Logic:
    def __init__(self, gui: Ui_Form) -> None:
        '''
        Returns Logic object
        '''
        self.gui: Ui_Form = gui

        self.status: bool = True

        self.value1: float = 0.0
        self.value2: float = 0.0
        self.operation: str = '+'
        self.last_screen: float = 0.0

        self.gui.zero.clicked.connect(self.zero)
        self.gui.one.clicked.connect(self.one)
        self.gui.two.clicked.connect(self.two)
        self.gui.three.clicked.connect(self.three)
        self.gui.four.clicked.connect(self.four)
        self.gui.five.clicked.connect(self.five)
        self.gui.six.clicked.connect(self.six)
        self.gui.seven.clicked.connect(self.seven)
        self.gui.eight.clicked.connect(self.eight)
        self.gui.nine.clicked.connect(self.nine)
        self.gui.subtract.clicked.connect(self.subtract)
        self.gui.add.clicked.connect(self.add)
        self.gui.multiply.clicked.connect(self.multiply)
        self.gui.divide.clicked.connect(self.divide)
        self.gui.period.clicked.connect(self.period)
        self.gui.clear.clicked.connect(self.clear)
        self.gui.power.clicked.connect(self.power)
        self.gui.enter.clicked.connect(self.enter)

    def zero(self) -> None:
        '''
        Adds zero to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '0')
    def one(self) -> None:
        '''
        Adds one to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '1')
    def two(self) -> None:
        '''
        Adds two to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '2')
    def three(self) -> None:
        '''
        Adds three to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '3')
    def four(self) -> None:
        '''
        Adds four to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '4')
    def five(self) -> None:
        '''
        Adds five to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '5')
    def six(self) -> None:
        '''
        Adds six to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '6')
    def seven(self) -> None:
        '''
        Adds seven to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '7')
    def eight(self) -> None:
        '''
        Adds eight to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '8')
    def nine(self) -> None:
        '''
        Adds nine to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '9')
    
    def period(self) -> None:
        '''
        Adds a decimal point to the display
        '''
        self.gui.answer_box.setText(self.gui.answer_box.toPlainText() + '.')

    def setNumpadStatus(self, numpad_status: bool) -> bool:
        '''
        Enables or Disables all numpad buttons based off of numpad_status.
        :param numpad_status: Bool to control the Enabled state of all numpad buttons
        :return: Bool state of all numpad buttons
        '''
        self.gui.zero.setEnabled(numpad_status)
        self.gui.one.setEnabled(numpad_status)
        self.gui.two.setEnabled(numpad_status)
        self.gui.three.setEnabled(numpad_status)
        self.gui.four.setEnabled(numpad_status)
        self.gui.five.setEnabled(numpad_status)
        self.gui.six.setEnabled(numpad_status)
        self.gui.seven.setEnabled(numpad_status)
        self.gui.eight.setEnabled(numpad_status)
        self.gui.nine.setEnabled(numpad_status)
        self.gui.period.setEnabled(numpad_status)

    def setAllButtonsStatus(self, buttons_status: bool) -> bool:
        '''
        Enables or Disables all button besides power based off of buttons_status.
        :param buttons_status: Bool to control the Enabled state of all buttons besides power
        :return: Bool state of all buttons besides power
        '''
        self.gui.answer_box.setEnabled(buttons_status)
        self.gui.zero.setEnabled(buttons_status)
        self.gui.two.setEnabled(buttons_status)
        self.gui.one.setEnabled(buttons_status)
        self.gui.three.setEnabled(buttons_status)
        self.gui.four.setEnabled(buttons_status)
        self.gui.five.setEnabled(buttons_status)
        self.gui.six.setEnabled(buttons_status)
        self.gui.seven.setEnabled(buttons_status)
        self.gui.eight.setEnabled(buttons_status)
        self.gui.nine.setEnabled(buttons_status)
        self.gui.subtract.setEnabled(buttons_status)
        self.gui.add.setEnabled(buttons_status)
        self.gui.multiply.setEnabled(buttons_status)
        self.gui.divide.setEnabled(buttons_status)
        self.gui.period.setEnabled(buttons_status)
        self.gui.clear.setEnabled(buttons_status)
        self.gui.enter.setEnabled(buttons_status)

    def multiply(self) -> None:
        '''
        Sets mulitply to be the next operation done on the two values. 
        '''
        self.value2 = self.gui.answer_box.toPlainText()
        self.show_answer()
        self.gui.answer_box.clear()
        self.operation = '*'
        self.setNumpadStatus(True)

    def add(self) -> None:
        '''
        Sets add to be the next operation done on the two values. 
        '''
        self.value2 = self.gui.answer_box.toPlainText()
        self.show_answer()
        self.gui.answer_box.clear()
        self.operation = '+'
        self.setNumpadStatus(True)

    def subtract(self) -> None:
        '''
        Sets subtract to be the next operation done on the two values. 
        '''
        self.value2 = self.gui.answer_box.toPlainText()
        self.show_answer()
        self.gui.answer_box.clear()
        self.operation = '-'
        self.setNumpadStatus(True)

    def divide(self) -> None:
        '''
        Sets divide to be the next operation done on the two values. 
        '''
        self.value2 = self.gui.answer_box.toPlainText()
        self.show_answer()
        self.gui.answer_box.clear()
        self.operation = '/'
        self.setNumpadStatus(True)

    def enter(self) -> None:
        '''
        Calculates the last calculation & displays final result if possible.
        '''
        if self.gui.answer_box.toPlainText().strip() == '':
            return
        self.value2 = self.gui.answer_box.toPlainText()
        self.show_answer()
        self.setNumpadStatus(False)


    def power(self) -> bool:
        '''
        Toggles the disabled state of all buttons except for power button. "Turns off the calculator"
        :return: Power state of the calculator
        '''

        if self.status:
            self.status = False
            self.last_screen = self.gui.answer_box.toPlainText()
            self.gui.answer_box.clear()
        else:
            self.status = True
            self.gui.answer_box.setText(str(self.last_screen))
        
        self.setAllButtonsStatus(self.status)

        return self.status 

    def clear(self) -> None:
        '''
        Clears the calculator's memory
        '''
        self.operation: str = '+'
        self.value1: float = 0.0
        self.value2: float = 0.0
        self.last_screen: str = ''
        self.gui.answer_box.setText('')
        self.setAllButtonsStatus(self.status)


    def show_answer(self) -> None:
        '''
        Calculates the formula and displays answers or error message.
        '''
        try:
            self.value1 = float(self.value1)
            self.value2 = float(self.value2)

            if self.operation == '+':
                result: float = formulas.add([self.value1, self.value2])
            elif self.operation == '-':
                result: float = formulas.subtract([self.value1, self.value2])
            elif self.operation == '*':
                result: float = formulas.multiply([self.value1, self.value2])
            elif self.operation == '/':
                result: float = formulas.divide([self.value1, self.value2])
            elif self.operation == '':
                return
            else:
                raise Exception(f"Unexpected operation: {self.operation}")

            # print(self.value1, self.operation, self.value2, '=', result)
        except Exception as e:
            self.gui.answer_box.setText(str(e))
            self.value1 = result
            self.operation = ''
            return
        
        if result.is_integer():
            self.gui.answer_box.setText(f"{int(result)}")
        else:
            self.gui.answer_box.setText(f"{result:.2f}")
        
        self.value1 = result
        self.operation = ''