from models import engine, Base  # Ensure these are correct
import sqlite3

def create_tables():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()

    # Create table for seasonal flavors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            is_available BOOLEAN NOT NULL
        )
    ''')

    # Create table for ingredient inventory
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    ''')

    # Create table for customer suggestions and allergy concerns
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

if __name__ == '_main_':
    create_tables()  # Create SQLite tables
    Base.metadata.create_all(engine)  # Create all SQLAlchemy tables