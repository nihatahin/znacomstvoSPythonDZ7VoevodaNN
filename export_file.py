#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_records
from validation_file import add_or_write, is_return, file_path
from to_str_convertion import tel2str
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
file_name_path = './files/file_export_rules.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def print_intro():
    print("\n\nYou would like to export all records to file. Follow the promts, please.")
#----------------------------------------------------------------------------
def warning_type():
    with open (get_file_name_path(), 'r', encoding= 'utf-8') as f_name_file:
        print(f_name_file.read())
#----------------------------------------------------------------------------
def empty_record_list():
    print("Records list is empty. Nothing to export.")
#----------------------------------------------------------------------------
def file_write():
    f_mode = add_or_write()
    if is_return(f_mode):
        return
    f_path = file_path()
    if is_return(f_path):
        return
    if f_path[1] == 1:
        md_expo(f_path[0], f_mode)
    elif f_path[1] == 2:
        txt_expo(f_path[0], f_mode)
    print("Export procedure is finished.")
#----------------------------------------------------------------------------
def export_recs():
    print_intro()
    if len(get_records()) > 0:
        warning_type()
        file_write()
    else:
        empty_record_list()
#----------------------------------------------------------------------------
def get_file_name_path():
    return file_name_path
#----------------------------------------------------------------------------
def txt_expo(path, mode):
    with open (path, mode, encoding= 'utf-8') as f_name_file:
        buffer = get_records()
        for i in range(len(buffer)):
            f_name_file.write(buffer[i][0] + '\n')
            f_name_file.write(buffer[i][1] + '\n')
            f_name_file.write(tel2str(buffer[i][2]) + '\n')
            f_name_file.write(buffer[i][3] + '\n\n')
#----------------------------------------------------------------------------
def md_expo(path, mode):
    if mode == 'a':
        with open (path, 'r', encoding= 'utf-8') as f_name_file:
            base_add = len(f_name_file.readlines()) - 1
            if base_add <= 1:
                mode = 'w'
    

    with open (path, mode, encoding= 'utf-8') as f_name_file:
        if mode == 'w':
            base_add = 1
            f_name_file.write('|#|Name|Surename|Telephone number|Discription|\n')
            f_name_file.write('|-:|-:|-:|-:|:-|\n')
        buffer = get_records()
        for i in range(len(buffer)):
            f_name_file.write(f"|{i + base_add}|{buffer[i][0]}|{buffer[i][1]}|{tel2str(buffer[i][2])}|{buffer[i][3]}|\n")

