
def get_file_name():
    return input(': ')
def get_table_name():
    return input('Table name: ').lower()

def get_id():
    return input('Enter id: ')

def get_col():
    return input("Change column: ").lower()

def get_value():
    return input('Value: ')

def get_table_choice():
    return input('''Enter show choice:
    1 - Show full database
    2 - Show a table
: ''')

def delete_confirm(record_id):
    return input(f'Are you sure you want to delete record with id {record_id}?(y/n): ').lower()



