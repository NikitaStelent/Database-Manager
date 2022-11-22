import sqlite3
from os import path
import user_input as usin
from company import views
from company.logger import make_log
from company.sql_tables import SQL_COLS

def create_db(file_name):
    """Creates database with a given name"""
    with sqlite3.connect(f'db/{file_name}.db') as db:
        create_tables(file_name)

def create_tables(file_name):
    """Creates tables inside database"""
    with sqlite3.connect(f'db/{file_name}.db') as db:
        table1 = f""" CREATE TABLE {'staff'}({SQL_COLS['staff']})"""
        table2 = f""" CREATE TABLE {'info'}({SQL_COLS['info']})"""
        db.execute(table1)
        db.execute(table2)
        db.commit()

@make_log
def add_record(file_name):
    """Adds a record to database"""
    add_more = True
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        while add_more:
            value = views.get_values()
            query1 = f""" INSERT INTO staff VALUES (NULL,?,?,?,?) """
            cursor.execute(query1, value[:4])
            query2 = f""" INSERT INTO info VALUES (NULL,?,?,?,?) """
            cursor.execute(query2, value[4:])
            db.commit()
            if input('Add another record?(y/n): ').lower() == 'y':
                continue
            add_more = False

@make_log
def delete_record(file_name):
    """Deletes a record from the database"""
    record_id = usin.get_id()
    with sqlite3.connect(f'db/{file_name}.db') as db:
        cursor = db.cursor()
        query1 = f""" DELETE FROM staff WHERE id = {record_id} """
        query2 = f""" DELETE FROM info WHERE id = {record_id} """
        confirm = usin.delete_confirm(record_id)
        if confirm == 'y':
            try:
                cursor.execute(query1)
                cursor.execute(query2)
                db.commit()
                views.delete_success(record_id)
            except Exception as e:
                views.delete_error(e)

@make_log
def change_table_record(file_name):
    """Changes a record in database"""
    views.show_tables(file_name)
    table_name = usin.get_table_name()
    views.show_cols(file_name, table_name)
    change_col = usin.get_col()
    new_value = usin.get_value()
    record_id = usin.get_id()
    views.show_cols(file_name, table_name)
    with sqlite3.connect(f'db/{file_name}.db') as db:
        try:
            cursor = db.cursor()
            cursor.execute(f' UPDATE {table_name} SET {change_col} = ? WHERE id = ?', (new_value, record_id))
            db.commit()
            views.change_record_success(record_id)
        except NameError:
            views.change_record_failure()


def file_exist(file_name):
    """
    Checks if a database with given name exists
    """
    return path.exists(f'db/{file_name}.db')

def set_file_name():
    """Sets file name you're working with"""
    file_name = usin.get_file_name()
    if file_name == '':
        FILEPATH = 'employees'
    else:
        FILEPATH = file_name
    return FILEPATH

