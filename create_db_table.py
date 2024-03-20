import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to the database man!")

conn.execute('CREATE TABLE USER_REGISTER (user_id INTEGER PRIMARY KEY AUTOINCREMENT, registration_date DATE, first_name VARCHAR(50), last_name VARCHAR(50), company VARCHAR(50), street_address VARCHAR(100), city VARCHAR(50), state VARCHAR(50), zip_code VARCHAR(20), country VARCHAR(50), email VARCHAR(100), contact_number VARCHAR(20)       )'
)
print("Table created")

conn.close()