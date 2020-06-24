import warnings
from math import sin, cos, tan, sqrt
import re


print('BASIC-SCIENTIFIC-CALCULATOR \n')
print('Hello Alien')
print("Enter 'Instruction' to view Instruction.")
print("Enter 'Example' to view some example.")
print("Enter 'clear' to reset", '\n')

previous = 0
go = True


def calc():
    """
    A basic scientific calculator that can perform basic mathematical operations,
    the three(3) basic trigonometric functions(sin, cos and tan) and also calculate the
    squared root of a number

    """

    # Making 'previous' and 'go' global variables so they can be accessed
    global previous
    global go
    try:
        # To remove syntax warning when dubious syntax is inserted e.g 3(2)
        warnings.filterwarnings(action='ignore', category=SyntaxWarning)
        if previous == 0:
            # Converts the user input to lowercase and strip the whitespace
            expression = input('Enter Expression: ').strip().lower()
        else:
            expression = input(str(previous))

        if expression == 'quit':  # To quit the program
            print('Bye Alien')
            print('Please contact oyemsamuel20@gmail.com or 08132927389 for difficulties, Thank you!.')
            go = False
        elif expression == 'example':  # To show some examples
            print('1+3+5 = 9')
            print('sin(0)+cos(0) = 1')
            print('2*(3-4) = -2')
            print('sqrt(4) = 2')
            print('2**3 = 8')
        elif expression == 'instruction':
            print("How to use")
            print("1. Basic maths: \n   2+2 = 4\n   the answer '4' can be used for further calculations\n   or"
                  " type 'clear' to reset the calculator and start again\n")
            print("2. Trig functions: \n   sin(1) =  \n   cos(1) =\n   tan(45) =\n")
            print("3. Squared root and Power: \n   sqrt(4) = 2\n   2**3 = 8\n")
        else:
            # To clear all calculations and start again
            if expression == 'clear':
                previous = 0
            else:
                # Using regex to manipulate the input to get desired outputs and avoid errors
                expression = re.sub('[^0-9+**sqrt/cos()tan.sin-]', '', expression)
                if previous == 0:
                    previous = eval(expression)
                else:
                    previous = float(eval(str(previous) + expression))
    # All exception blocks to tackle errors
    except ZeroDivisionError:
        print('Cannot Divide a Number by Zero')
    except SyntaxError:
        print('Please Enter Digits or Enter \'Example\'')
    except TypeError:
        print('Please Re-enter')
    except NameError:
        print('Invalid Input, Try Again')
    except Exception as error:
        print('Sorry', str(error.__class__).strip('<>').lstrip('class'), 'Please Re-enter')


while go:
    calc()
