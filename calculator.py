from cli_application import CliApplication

class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

    def inputNumbers(self, operation):
        print(f"...\t{operation}\t...")
        n1 = float(input('Choose the first number: '))
        print(f"{n1}\t{operation}\t...")
        n2 = float(input('Choose the second number: '))
        print(f"{n1}\t{operation}\t{n2}")
        return [n1, n2]

    def run(self):
        option = ''
        command_list = ['A', 'S', 'D', 'M', 'Q']

        while (True):

            print(f'''Choose an operation
            ({command_list[0]}) - addition
            ({command_list[1]}) - subtraction
            ({command_list[2]}) - division
            ({command_list[3]}) - multiply
            ({command_list[4]}) - quit''')

            option = str(input('Command: '))

            if (option not in command_list):
                print('Command not recognized, please try again')
                continue
            
            if (option == command_list[0]):
                (n1, n2) = self.inputNumbers('+')
                result = self.add(n1, n2)
                print(f'The result is: {result}')
            
            if (option == command_list[1]):
                (n1, n2) = self.inputNumbers('-')
                result = self.subtract(n1, n2)
                print(f'The result is: {result}')

            if (option == command_list[2]):
                (n1, n2) = self.inputNumbers('/')
                result = self.divide(n1, n2)
                print(f'The result is: {result}')

            if (option == command_list[3]):
                (n1, n2) = self.inputNumbers('*')
                result = self.multiply(n1, n2)
                print(f'The result is: {result}')

            if (option == command_list[4]):
                return
