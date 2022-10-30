#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import append_records
from validation_data import is_return, disc_valid, valid_name, valid_tel
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def add_rec():
    print_start()
    cur_name = add_name('name')
    if is_return(cur_name):
        return
    cur_sur = add_name('surename')
    if is_return(cur_sur):
        return
    cur_tel = add_tel()
    if is_return(cur_tel):
        return
    cur_dis = add_disc()
    if is_return(cur_dis):
        return

    append_records((cur_name, cur_sur, cur_tel, cur_dis))
#----------------------------------------------------------------------------
def print_start():
    print("\n\nYou would like to add new record to TELEBUG. Follow the promts, please.")
#----------------------------------------------------------------------------
def promt(ent_obj, tg= 'valid'):
    if tg == 'valid':
        match ent_obj:
            case "name":
                print(f"Enter person {ent_obj} (for examle, Alex) or '/return' to stop add procedure. Use only letters, spacebar and symbols '\'', '-': ", end= '')
            case "surename":
                print(f"Enter person {ent_obj} (for examle, Kipaev) or '/return' to stop add procedure. Use only letters, spacebar and symbols '\'', '-': ", end= '')
            case "phone number":
                print(f"Enter person {ent_obj}. Use correct data format (for examle, +7(999)888-77-66) or '/return' to stop add procedure: ", end= '')
            case "discription":
                print(f"Enter person {ent_obj} (for examle, Cool body!) or '/return' to stop add procedure. Don't use symbol '|': ", end= '')
            case _:
                print('Wrong configuration!')
    elif tg == 'invalid':
        print(f"Invalid {ent_obj} was entered. Try again.")
    else:
        print(f"Wrong state!")
#----------------------------------------------------------------------------
def add_name(ent_obj):
    while True:
        promt(ent_obj)
        not_filtered_string = input().strip()

        if is_return(not_filtered_string) or valid_name(not_filtered_string.replace('\t', ' ')):
            return not_filtered_string
        else:
            promt(ent_obj, 'invalid')
#----------------------------------------------------------------------------
def disc_check():
    while True:
        promt('discription')
        discrip = input().strip()

        if disc_valid(discrip):
            return discrip        
        else:
            promt('discription', 'invalid')   
#----------------------------------------------------------------------------
def add_disc():
    not_filtered_string = disc_check()

    if is_return(not_filtered_string):
        return not_filtered_string
    else:
        return not_filtered_string.replace('\t', ' ')
#----------------------------------------------------------------------------
def add_tel():
    while True:
        promt("phone number")
        not_filtered_string = input().replace('\t', '').replace(' ', '')
        if is_return(not_filtered_string):
            return not_filtered_string
        else:
            tele_tup = valid_tel(not_filtered_string)
            if type(tele_tup) == tuple:
                return tele_tup
            else:
                promt("phone number", 'invalid')
#----------------------------------------------------------------------------