from models import engine, Base
import sqlite3

def create_tables():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            is_available BOOLEAN NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            flavor_suggestion TEXT,
            allergy_concern TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    Base.metadata.create_all(engine)
