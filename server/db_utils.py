import sqlite3
import time  # for timestamping
import os


def setup(db_name):
    # THIS FILE WILL EXECUTE THIS FUNCTION WHEN RUN
    print(f'creating database {db_name}...')

    try:  # creating file time
        if not os.path.exists(db_name + '.db'):
            with open(db_name + '.db', "w") as f:
                pass
    except Exception as err:
        return print(err)

    current_time = time.strftime("%H:%M:%S", time.localtime())
    try:
        conn = sqlite3.connect(db_name + '.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS creation_timestamp (Time TEXT)')
        c.execute(f'INSERT INTO creation_timestamp ({current_time})')
        print(f'Success creating {db_name}.db @ {current_time}!')
        return True
    except sqlite3.OperationalError as err:
        print(f'Error creating \'{db_name}.db\' @ \'{current_time}\' ')


def create_table(db_name, table_name, columns):  # TODO REPLACE f STRINGS BC SQL INJECTION
    """
    Create a sqlite3 table of your choosing.

    Parameters:
    db_name (str): The name of the database.
    table_name (str): The name of the table to be created.
    columns (dict): A dictionary of column names and their types.
    """

    columns_with_types = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})"

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table_sql)

        conn.commit()
        conn.close()

        print(f"Table '{table_name}' created successfully in database '{db_name}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def insert_data(db_name, table_name, columns, values):
    """
    Insert a new row of data
    :param db_name:
    :param table_name:
    :param columns:
    :param values:
    :return:
    """


if __name__ == "__main__":
    print('Executed db_utils file, running setup function')
    setup('prerelease')
