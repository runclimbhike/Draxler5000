
import sqlite3
conn = sqlite3.connect('brewery.db')

c = conn.cursor()

# Print entire database contents

for row in c.execute('SELECT * FROM beer ORDER BY name WHERE '):
    print(row)


# Print out dates

