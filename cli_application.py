import os
import sys
import hashlib
from random import randint

class CliApplication:
    def __init__(self, application_name = '') -> None:
        if (application_name == ''): application_name = 'CliApplication'
        self.unique_name = application_name + "__" + self.__get_nbit_hex_name(application_name)
        os.system(f'title {self.unique_name}')

        try:
            application_type = sys.argv[1]
            # Execute program in new cmd window
            self.__close_terminal()

        except:
            file_name = os.path.basename(__file__)
            os.system(f'start cmd /c python {file_name} cli_program')

    def __get_nbit_hex_name(self, name: str, nbits = int(8)):
        name = name + str(randint(0, 1024))
        name = name.encode('utf-8')
        hash = hashlib.sha3_512()
        hash.update(name)
        hash = hash.hexdigest()
        cut_position = randint(0, len(hash)-9)
        return hash[ cut_position : cut_position + nbits ]

    def __close_terminal(self):
        os.system(f'taskkill /f /fi "WINDOWTITLE eq {self.unique_name}"')