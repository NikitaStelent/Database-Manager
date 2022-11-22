import model
import views

FILEPATH = ''

def menu():
    is_on = True
    while is_on:
        views.show_options()
        option = input(': ').upper()
        if option == '1':
            views.show_table_info(FILEPATH)
        elif option == '2':
            model.add_record(FILEPATH)
        elif option == '3':
            model.delete_record(FILEPATH)
        elif option == '4':
            views.show_table_record(FILEPATH)
        elif option == '5':
            model.change_table_record(FILEPATH)
        elif option == 'X':
            is_on = False

def run():
    global FILEPATH
    views.welcome_msg()
    FILEPATH = model.set_file_name()

    if model.file_exist(FILEPATH):
        print(f'Using <{FILEPATH}> database')
    elif not model.file_exist(FILEPATH):
        model.create_db(FILEPATH)
        views.create_db_success(FILEPATH)

    menu()
