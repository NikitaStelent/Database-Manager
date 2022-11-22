import sqlite3
from tabulate import tabulate
from logger import make_log
import user_input as usin


EMPLOYEE_HEADERS = ['Name:', 'Last name:', 'Gender:', 'Department:', 'Position:', 'Birth date:', 'Phone number:', 'City:']
PERSONAL_HEADERS = ['id', 'name', 'l_name', 'gender', 'department']
INFO_HEADERS = ['id', 'position', 'birth_date', 'phone_num', 'city']


def welcome_msg():
    print('''
Welcome to database manage program.
* Import: To import a new file put it to company\db directory.
* Use\Create: To use an existing file or create a new one - just write file name down below.
* Default file: Leave input blank to use default db named - "employees.db"''')


def show_options():
    print(f'''
    Choose a number:
    1 - Show database
    2 - Add a record
    3 - Delete a record
    4 - Show table record
    5 - Change table record
    X - Exit
    ''')

def next_line():
    print()
    print()


def next_line():
    print()
    print()


@make_log
def show_table_info(file_name):
    """Shows info based on user's choice"""
    choice = usin.get_table_choice()
    if choice == '1':
        show_full_info(file_name)
    elif choice == '2':
        show_tables(file_name)
        table_name = usin.get_table_name()
        headers = PERSONAL_HEADERS if table_name == 'staff' else INFO_HEADERS
        with sqlite3.connect(f'db/{file_name}.db') as db:
            cursor = db.cursor()
            try:
                query = f""" SELECT * FROM {table_name}"""
                print(tabulate(cursor.execute(query), headers=headers, tablefmt='fancy_grid'))
            except sqlite3.OperationalError:
                print(f'No such table as <{table_name}>')


@make_log
def show_table_record(file_name):
    """Shows a table record by id"""
    show_tables(file_name)
    table_name = usin.get_table_name()
    headers = PERSONAL_HEADERS if table_name == 'staff' else INFO_HEADERS
    record_id = usin.get_id()
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        query = f""" SELECT * FROM {table_name} WHERE id = {record_id}"""
        print(tabulate(cursor.execute(query), headers=headers, tablefmt='fancy_grid'), end='')


def show_tables(file_name):
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sqlite_master where type='table'")
        available = cursor.fetchall()
        print("Available tables: ")
        for i in available:
            print(i[1], end=' ')
        next_line()


def show_cols(file_name, table_name):
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        available = cursor.fetchall()[1:]
        print("Available columns: ")
        for i in available:
            print(i[1], end=' ')
        next_line()

def create_db_success(file_name):
    print(f'Database "{file_name}" was created!')

def delete_success(record_id):
    print(f'Record with id {record_id} was deleted')

def delete_error(error):
    print(f'Error occured: {error}')

def change_record_success(record_id):
    print(f'Record with id {record_id} was updated')

def change_record_failure():
    print('You might have entered the wrong value')

def show_full_info(file_name):
    headers = PERSONAL_HEADERS + INFO_HEADERS
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        query = """SELECT l.id, l.name, l.l_name, l.gender, l.department, r.id, r.position, r.birth_date, r.phone_num, r.city
        FROM staff l
        LEFT JOIN info r
        ON l.id = r.id
        ORDER BY l.id;"""
        print(tabulate(cursor.execute(query), headers=headers, tablefmt='fancy_grid'))


def show_all_cols():
    print(*PERSONAL_HEADERS[1:] + INFO_HEADERS[1:])

def get_values():
    values = []
    for i in range(len(EMPLOYEE_HEADERS)):
        elem = EMPLOYEE_HEADERS[i]
        print(elem)
        values.append(input())
    return tuple(values)