

import sqlite3

# Create databank named brewery.db
conn = sqlite3.connect('brewery.db')
c = conn.cursor()

# Create main table 'beer' to keep track of the beer catalog, state and dates.

c.execute('''CREATE TABLE IF NOT EXISTS beer
                (brew_number INTEGER PRIMARY KEY,
                name varchar(32),
                state TEXT NOT NULL,
                yeast varchar NOT NULL,
                brew_date int,
                rack_date int,
                bottle_date int,
                drink_date int,
                expiration_date int)''')

### Create table 'tracking' to keep track of temperature and air lock activity ie. bubbles/min.

c.execute('''CREATE TABLE IF NOT EXISTS tracking
                (observation_number INTEGER PRIMARY KEY,
                brew_number int,
                observation_date int,
                temperature CHAR(3),
                bubbles_min int)''')


conn.commit()







