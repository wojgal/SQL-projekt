import sqlite3

con = sqlite3.connect('baza_danych.db')
cur = con.cursor()


def insert_row(table, values):
    cur.execute(f"""INSERT INTO {table} VALUES {values}""")



def select(table, columns='*'):
    if type(columns) == 'list':
        cols = columns[0]

        for x in range(2, len(columns)):
            cols += ', ' + columns[x]

    cur.execute(f"""SELECT {cols} FROM {table}""")



def delete_row(table, attribute, value):
    cur.execute(f"""DELETE FROM {table} WHERE {attribute}={value}""")



#Jest zle
def update_record(table, new_values, id):
    col_names = cur.execute(f"""SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME={table}""")




