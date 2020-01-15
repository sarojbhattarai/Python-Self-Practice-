import sys
import cmath
import math

def get_number(msg, boolvalue):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not boolvalue and x < sys.float_info.epsilon:
                print("OOPS!! Zero is not allowed!")
                x = None
        except ValueError as err:
            print(err)        
        return x

print("ax\N{SUPERSCRIPT TWO}+bx+c = 0")
a = get_number("Enter value of a ", False)
b = get_number("Enter value of b ", True)
c = get_number("Enter value of c ", True)

discriminant = (b ** 2)- 4 * a * c

x1 = None
x2 = None

if discriminant == 0:
    x1 = -b / (2 * a)
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
        x1 = (-b + root)/(2 * a)
        x2 = (-b - root)/(2 * a)
    else:
        root = cmath.sqrt(discriminant)
        x1 = (-b + root)/(2 * a)
        x2 = (-b - root)/(2 * a)
equation = ("{a}x\N{SUPERSCRIPT TWO} + {b}x + {b} \N{RIGHTWARDS ARROW} x {x1} ".format(**locals()))

if x2 is not None:
    equation += "Or x = {x2}".format(**locals()) 

print(equation)
