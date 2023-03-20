from interpreter import Interpreter

def sum(n1, n2):
    return n1 + n2

add_command = Interpreter.Command(
    'add',
    ['number1', 'number2'],
    [float, float],
    lambda x, y: x + y,
    'Returns the result of the sum of 2 numbers'
)

subtract_command = Interpreter.Command(
    'sub',
    ['number1', 'number2'],
    [float, float],
    lambda x, y: x - y,
    'Returns the result of the subtraction of 2 numbers'
)

divide_command = Interpreter.Command(
    'divide',
    ['number1', 'number2'],
    [float, float],
    lambda x, y: x / y,
    'Returns the result of the division of 2 numbers'
)

multiply_command = Interpreter.Command(
    'multiply',
    ['number1', 'number2'],
    [float, float],
    lambda x, y: x * y,
    'Returns the result of the multiplication of 2 numbers'
)

super_interpreter = Interpreter([
    add_command,
    subtract_command,
    divide_command,
    multiply_command
])

super_interpreter.start()