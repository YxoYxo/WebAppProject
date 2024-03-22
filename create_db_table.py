import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to the database")

conn.execute('DROP TABLE USER_REGISTER')
print("USER_REG Table droped")

conn.execute('DROP TABLE AUDIT_LOG')
print("AUDIT_LOG Table droped")

conn.execute('CREATE TABLE USER_REGISTER (user_id INTEGER PRIMARY KEY AUTOINCREMENT, registration_date DATETIME DEFAULT CURRENT_TIMESTAMP, first_name VARCHAR(50), last_name VARCHAR(50), company VARCHAR(50), street_address VARCHAR(100), city VARCHAR(50), state VARCHAR(50), zip_code VARCHAR(20), country VARCHAR(50), email VARCHAR(100), contact_number VARCHAR(20)       )'
)
print("Table created")

conn.execute('CREATE TABLE AUDIT_LOG (log_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, activity_timestamp DATETIME, activity_type VARCHAR(50), FOREIGN KEY (user_id) REFERENCES USER_REGISTER(user_id))'
)
