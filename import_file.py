#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import append_records
from validation_file import file_path, is_return
from validation_data import valid_name, valid_tel, disc_valid
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
file_name_path = './files/file_import_rules.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def print_intro():
    print("\n\nYou would like to import all records from file. Follow the promts, please.")
#----------------------------------------------------------------------------
def warning_type():
    with open (get_file_name_path(), 'r', encoding= 'utf-8') as f_name_file:
        print(f_name_file.read())
#----------------------------------------------------------------------------
def get_file_name_path():
    return file_name_path
#----------------------------------------------------------------------------
def print_invalid():
    print('Invalid file format!')
#----------------------------------------------------------------------------
def file2str_list(path):
    with open (path, 'r', encoding= 'utf-8') as f_name_file:
        lines = f_name_file.readlines()
    return lines
#----------------------------------------------------------------------------
def file_read():
    f_path = file_path()
    if is_return(f_path):
        return
    file_lines = file2str_list(f_path[0])
    if f_path[1] == 1:
        md_impo(file_lines)
    elif f_path[1] == 2:
        txt_impo(file_lines)
    print("Import procedure is finished.")
#----------------------------------------------------------------------------
def strs_to_recs(strs):
    for i in range(len(strs)):
        strs[i] = strs[i].split('|')[2 : 6]
        strs[i][0] = strs[i][0].strip()
        strs[i][1] = strs[i][1].strip()
        strs[i][2] = strs[i][2].strip().replace('\t', '').replace(' ', '')
        strs[i][3] = strs[i][3].strip().replace('\t', ' ')
    return(strs)
#----------------------------------------------------------------------------
def md_impo(lines):
    if (lines[0] == '|#|Name|Surename|Telephone number|Discription|\n') and (lines[1] == '|-:|-:|-:|-:|:-|\n'):
        lst = strs_to_recs(lines[2 : ])
        if content_check(lst):
            append_file_to_data(conver_telephone(lst))
        else:
            print_invalid()
    else:
        print_invalid()
#----------------------------------------------------------------------------
def txt_str_num_check(num):
    return num % 5 == 0
#----------------------------------------------------------------------------
def lines2moist_records(ln):
    dry = []
    for i in range(0, len(ln), 4):
        dry.append([ln[i], ln[i + 1], ln[i + 2], ln[i + 3]])
    return dry
#----------------------------------------------------------------------------
def content_check(data):
    for i in range(len(data)):
        if not((valid_name(data[i][0])) and (valid_name(data[i][1])) and 
        (type(valid_tel(data[i][2])) == tuple) and (disc_valid(data[i][3]))):
            print_invalid()
            return False
    else:
        return True
#----------------------------------------------------------------------------
def every_fifth_is_enter(data):
    for i in range(4, len(data), 5):
        if data[i] != '\n':
            return False
    else:
        return True
#----------------------------------------------------------------------------
def delete_enters_and_spaces(data):
    mod_data = []
    for i in range(4, len(data), 5):
        if data[i] == '\n':
            mod_data.append(data[i - 4].strip())
            mod_data.append(data[i - 3].strip())
            mod_data.append(data[i - 2].strip().replace('\t', '').replace(' ', ''))
            mod_data.append(data[i - 1].strip().replace('\t', ' '))
    else:
        return mod_data
#----------------------------------------------------------------------------
def conver_telephone(full_data):
    for i in range(len(full_data)):
        full_data[i][2] = valid_tel(full_data[i][2])
    return full_data
#----------------------------------------------------------------------------
def append_file_to_data(data):
    for i in range(len(data)):
        append_records(tuple(data[i]))
#----------------------------------------------------------------------------
def txt_impo(lines):
    length = len(lines)
    if txt_str_num_check(length) and (length > 0):
        if every_fifth_is_enter(lines):
            lines = delete_enters_and_spaces(lines)
            lst = lines2moist_records(lines)
            if content_check(lst):
                append_file_to_data(conver_telephone(lst))
            else:
                print_invalid()
        else:
            print_invalid()
    else:
        print_invalid()   
#----------------------------------------------------------------------------
def import_recs():
    print_intro()
    warning_type()
    file_read()

