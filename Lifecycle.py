import sqlite3
import Scheduling
import Reporting

new_line = '\n'
conn = sqlite3.connect('brewery.db')
c = conn.cursor()

### Insert data into database. This will be moved to Update.py

def new_brew():
    '''
    Creates a new beer record in the 'beer' table.
    '''
    # Get information from the brewer about the newly created beer
    name = input('Name: ')
    state = 'primary'
    yeast = input('Yeast: ')
    brew_date = Scheduling.brew_date()
    rack_date = Scheduling.rack_date(int(input('How many days are needed in primary fermentation: ')))
    bottle_date = Scheduling.bottling_date(int(input('How many days are needed in secondary fermentation: ')))
    drink_date = Scheduling.drink_date(int(input('How many days of bottle conditioning are needed: ')))
    expiration_date = Scheduling.expiration_date(int(input('How many days can the beer stay fresh in the bottle: ')))

    # Insert the inputted data into the 'beer' table as long as it hasn't be inputted before.
    c.execute('INSERT OR IGNORE INTO beer VALUES(NULL,?,?,?,?,?,?,?,?)', (name,
                                                            state,
                                                            yeast,
                                                            brew_date,
                                                            rack_date,
                                                            bottle_date,
                                                            drink_date,
                                                            expiration_date))
    # Save the committed data to brewery.db
    conn.commit()

def racking():
    '''
    changes the state from primary to secondary.
    '''

    racked_brew_number = input('What is the brew_number that has been racked: ')
    c.execute("UPDATE beer SET state='secondary' WHERE brew_number=?", racked_brew_number)

    conn.commit()
"""
def bottling():

    bottled_brew_number - input('What is the brew_number that has been bottled: ')
    c.execute("UPDATE beer SET state='bottled' WHERE brew_number=?", (bottled_brew_number))

    conn.commit()
"""

def change_state():
    '''
    prints the current state and allows the user to change the state to what they want.
    '''
    # Print all the current brews so that the brewer can pick the one he/she needs to change.
    import sqlite3
    con = sqlite3.connect('brewery.db')
    with con:
        # Convert to dictionary cursor so that we can refer to the data by their column names.
        con.row_factory = sqlite3.Row

        c = con.cursor()

        Reporting.show_all()
        print(new_line)
        updated_brew_number = input('What is the brew # that has changed state: ')
        print(new_line)
        # Print the brew states to pick from
        states = ['primary', 'secondary', 'bottled', 'drinkable', 'expired']
        print("Choose one of the following states: ", ', '.join(x for x in states))
        print(new_line)
        # Get the new state of the brew from the brewer
        new_state = input('What is the new state that the beer has been moved to: ')
        print(new_line)
        # Verify the input
        if new_state not in states:
            print('Please type a state.')

        else:
            # Update the databank
            con.row_factory = sqlite3.Row
            c.execute("UPDATE beer SET state=? WHERE brew_number=?", (new_state, updated_brew_number))
            conn.commit()

            # Print out the updated brew
            c.execute("SELECT * from beer WHERE brew_number=?", updated_brew_number)
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
            print(new_line)










def observation():
    '''
    Creates a new record in the tracking table
    '''
    # Get information from the brewer about temp and activity
    brew_number = input('What beer are you observing: ')
    observation_date = Scheduling.brew_date()
    temperature = input('What is the wort temperature: ')
    bubbles_min = input('How many bubbles per minute are coming out of the airlock: ')

    # Insert the inputted data into the 'beer' table as long as it hasn't be inputted before.
    c.execute('INSERT OR IGNORE INTO tracking VALUES(NULL,?,?,?,?)', (brew_number,
                                                                      observation_date,
                                                                      temperature,
                                                                      bubbles_min))
    conn.commit()


def close():
    conn.commit()
    conn.close()


# Testing
#new_brew()
#racking()
#change_state()
#observation()
#close()