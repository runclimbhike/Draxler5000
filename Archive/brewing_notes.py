import sqlite3
# Connect to my hardcoded brewery database
conn = sqlite3.connect('brewery.db')
# Create a cursor instance in order to execute SQL statements.
c = conn.cursor()


# Create table
c.execute('''CREATE TABLE brewing_notes
               (name, date, temp, notes)''')