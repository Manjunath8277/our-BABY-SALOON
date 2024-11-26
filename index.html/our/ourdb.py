# import sqlite3 

# def init_db():
#     conn = sqlite3.connect('our.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS user (
#             username varchr NOT NULL,
#             email varchar NOT NULL,
#             password int NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# import sqlite3

# conn = sqlite3.connect("our.db")
# print("opened database successfully")
# conn.execute("CREATE TABLE users (username varchar, email varchar, password int)")
# print("table created successfully")
# conn.close()


import sqlite3 as sql

def create_table():
    conn = sql.connect('our.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE  users (
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call create_table function to create the users table
create_table()
