#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_records
from help import show_help
from add import add_rec
from show import show_rec
from export_file import export_recs
from import_file import import_recs
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

logo_path = './files/logo.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def show_hello():
    with open (get_logo_path(), 'r', encoding= 'utf-8') as logo_file:
        print(logo_file.read())
    print('Hello. Welcome to telephone directory main menu.')
#----------------------------------------------------------------------------
def enter_cmd(is_valid):
    if is_valid:
        print('Enter command', end=' ')
    else:
        print('Invalid command was entered. Please, Try again', end=' ')
    return input('(or ' + "print '/help' + Enter to show command list" + '): ')
#----------------------------------------------------------------------------
def exit_print():
    print('It is pity, but you leave TELBUG! We will look foward to meet you again!')
#----------------------------------------------------------------------------
def basement():
    valid = True
    while True:
        cmd = enter_cmd(valid)
        valid = lambda valid: True if not valid else valid
        match cmd:
            case '/show':
                show_rec(get_records())
            case '/add':
                add_rec()
            case '/expo':
                export_recs()
            case '/impo':
                import_recs()
            case '/exit':
                exit_print()
                break
            case '/help':
                show_help()
            case _:
                valid= False
#----------------------------------------------------------------------------
def get_logo_path():
    return logo_path