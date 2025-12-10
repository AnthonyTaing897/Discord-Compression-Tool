import sqlite3

#initalise the database connection and cursor
connection = sqlite3.connect('Discord_Bot\DB\database.db')
cursor = connection.cursor()



table = """CREATE TABLE IF NOT EXISTS sessions (session_id TEXT PRIMARY KEY, session_code TEXT UNIQUE, user_id TEXT, start_time TIMESTAMP)"""

#clear session database

#Fetch all records from the sessions table
FetchALL = cursor.execute("SELECT * FROM sessions")
#get first record
print(FetchALL.fetchone()[1])

connection.commit()
cursor.close()
connection.close()
