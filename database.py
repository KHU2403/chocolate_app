import sqlite3
from models import engine, Base

def initialize_database():
    connection = sqlite3.connect('flavors.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flavors_of_the_season (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            is_available BOOLEAN NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            suggestion TEXT,
            allergy_info TEXT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    initialize_database()
    Base.metadata.create_all(engine)
