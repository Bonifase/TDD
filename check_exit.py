import sys


def check_exit(value):
    if value == 'exit':
        print('Quiting the program...\n')
        print('Bye!\n')
        return sys.exit()
