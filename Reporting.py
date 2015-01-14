import sqlite3

conn = sqlite3.connect('brewery.db')
c = conn.cursor()


def show_all():
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT brew_number, name, state, brew_date, rack_date, bottle_date, drink_date, expiration_date FROM beer")

        all_rows = c.fetchall()

        print('{0:<8}{1:^16}{2:^16}{3:^16}{4:^16}{5:^16}{6:^16}{7:^16}'.format("Brew #", "Name", "State", "Brew Date", "Rack Date", "Bottle Date", "Drink Date", "Expiration Date"))
        print('-'*120)
        # Fetch all the rows in a list of lists.
        for row in all_rows:
            print('{0:<8}{1:^16}{2:^16}{3:^16}{4:^16}{5:^16}{6:^16}{7:^16}'.format(row["brew_number"],
                                                              row["name"],
                                                              row["state"],
                                                              row["brew_date"],
                                                              row["rack_date"],
                                                              row["bottle_date"],
                                                              row["drink_date"],
                                                              row["expiration_date"],))


def sql_version():
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        sql_version = cur.fetchone()

        return sql_version

        #print("SQLite version: ", sql_version)

def show_all_tracking():
    import sqlite3
    import sys
    con = sqlite3.connect('brewery.db')
    with con:
        c = con.cursor()
        rows = c.execute('SELECT * FROM tracking')


        #rows = c.fetchone()

        for row in rows:
            print(row)

def primary_state():
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT name FROM beer WHERE state='primary'")

        all_rows = c.fetchall()

        test = []
        for name in all_rows:
            test += name

        print("| Primary: ", ', '.join(x for x in test))

def secondary_state():
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT name FROM beer WHERE state='secondary'")

        all_rows = c.fetchall()

        test = []
        for name in all_rows:
            test += name

        print("| Secondary: ", ', '.join(x for x in test))

def bottled_state():
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT name FROM beer WHERE state='bottled'")

        all_rows = c.fetchall()

        test = []
        for name in all_rows:
            test += name

        print("| Bottled: ", ', '.join(x for x in test))

def ready_to_drink():

    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT name FROM beer WHERE state='drinkable'")

        all_rows = c.fetchall()

        test = []
        for name in all_rows:
            test += name

        print("| Ready to Drink: ", ', '.join(x for x in test))


def total_bottles(list):
    return len(list)*50


def expired():

    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()
        c.execute("SELECT name FROM beer WHERE state='expired'")

        all_rows = c.fetchall()

        test = []
        for name in all_rows:
            test += name

        tab = '\t'

        print("| Cashed: ", ', '.join(x for x in test), tab*10, '  Reused Bottles: ', total_bottles(test))





# Test
#show_all()
#show_all_tracking()
#primary_state()
#secondary_state()
#bottled_state()
#ready_to_drink()
#expired()
