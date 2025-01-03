import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    """)
    connection.commit()
initiate_db()

cursor.execute("DELETE FROM Products")
for i in range(1, 5):
    cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                   (f"Product: {i}", f"Описание: {i}", i*100))
def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


connection.commit()
