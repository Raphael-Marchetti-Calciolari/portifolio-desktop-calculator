import inspect
from typing import Callable, Any

class Interpreter:
    def __init__(self, commands : list = None) -> None:
        self.commands = [
            self.Command(
                command_name='exit',
                params=[],
                param_types=[],
                behaviour=lambda: quit(),
                description='Closes the interpreter'
            )
        ]
        self.commands.extend(command for command in commands)

    def __show_command_list(self):
        for command in self.commands:
            print(f'{command.name} - {command.description}')

    def __read_user_input(self):
        self.user_input = str(input('> '))

    def __interpret_command(self):
        parsed_input = self.user_input.split(' ')
        command_found = False
        error_flag = False
        for command in self.commands:
            if (parsed_input[0] == command.name):
                command_found = True
                n_params = len(command.params)
                if (len(parsed_input) != 1 + n_params):
                    print(f">> Syntax error, the command is called as: > {command.name}", end=' ')
                    for param in command.params:
                        print(f'{param}', end=' ')
                    print()
                    error_flag = True
                    break
                param_values = []
                for param in range(len(command.params)):
                    try:
                        input_value = parsed_input[param + 1]
                        value = command.param_types[param](input_value)
                        param_values.append(value)
                    except:
                        print(f'>> Error, the value "{input_value}" cannot be assigned to {command.params[param]} of type {command.param_types[param].__name__}')
                        error_flag = True
                        break

                if (not error_flag):
                    result = command.behaviour(*param_values)
                    print(f">> {result}")

        if (not command_found): print(f'>> Command "{parsed_input[0]}" not recognized')

    def start(self):
        while(True):
            self.__show_command_list()
            self.__read_user_input()
            self.__interpret_command()

    class Command:
        def __init__(self, command_name:str, params:list, param_types:list, behaviour:Callable[..., Any] = None, description:str = None) -> None:
            self.name = command_name
            self.params = params
            self.param_types = param_types
            self.behaviour = behaviour if (self.__check_behaviour(behaviour)) else None
            self.description = description

        def __check_behaviour(self, behaviour):
            params = inspect.signature(behaviour).parameters
            param_names = [param.name for param in params.values()]
            check = (len(self.params) == len(param_names))
            if (not check): print(f'>> WARNING: the behaviour attributed to the command {self.name} is invalid, check if the params are matching')
            return (len(self.params) == len(param_names))
