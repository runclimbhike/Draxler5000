import datetime
import Reporting
import Lifecycle
import os
import time

# Set console size
os.system("mode con: cols=124 lines=55")
# Define some whitespace functions
tab = '\t'
pounds = '#'*4
space = ' '
new_line = '\n'
side = '|'
# Display a program initialization splash screen.

# Create the program header
def ProgramHeader():
    '''
    This is the program header that clears the console and then prints the current status.
    '''
    # Clear the console.
    os.system('cls')
    # Print the header
    print(pounds*31)
    print((tab*6), 'Current Brewery Status')
    print((tab*5),tab,'      ',  datetime.date.today().strftime("%m-%d-%Y"))
    print(new_line)

    # Show all brews currently in primary fermentation.
    Reporting.primary_state()
    # Show all brews currently in secondary fermentation.
    Reporting.secondary_state()
    # Show all brews currently in bottle conditioning.
    #Reporting.bottled_state()
    Reporting.ready_to_drink()
    Reporting.expired()

    print(pounds*31)

# Create a list of the possible options for the Main Control Console so that user input can be verified.
options = ['1', '2', '3', '4', '0']
prompt = 'Select a number: '
while True:
    # Call the Program Header to print it out.
    ProgramHeader()
    # Print the console options.
    print(tab*6, ' MAIN CONTROL CONSOLE')
    print(pounds*31)
    print(tab*3, '1. VIEW & SEARCH\t2. CREATE & UPDATE\t3. SYSTEM SETTINGS\t0. EXIT')
    # Get user selection
    inp = input(prompt)
    # Verify user input
    if inp not in options:
        print('Select a number: ')
        continue
### View & Search ###
    if inp == '1':
        ProgramHeader()

        while True:
            print(tab*6, '*** VIEW & SEARCH MENU ***')
            print(tab*3, '1. Beers in Primary\t2. All Beers\t0. Back to Main Control Console')
            data_requested = input('Select a number: ')

            if data_requested == '2':
                print(new_line)
                Reporting.show_all()
                print(new_line)

            elif data_requested == '0':
                #print(new_line*66)
                break


### Create & Update ###
    if inp == '2':
        ProgramHeader()
        while True:
            tab = '\t'
            space = ' '

            print(tab*6, '*** CREATE & UPDATE MENU ***')
            print(space*3, '1.Create new beer\t2.Update beer state\t0.Back to Main Control Console')
            data_requested = input('Select a number: ')

            if data_requested == '1':
                Lifecycle.new_brew()

            elif data_requested == '2':
                print(new_line)
                Lifecycle.change_state()

            elif data_requested == '3':
                Lifecycle.bottling()




            elif data_requested == '0':
                break

### System Settings ###
    if inp == '3':
        ProgramHeader()
        while True:
            tab = '\t'
            print(tab*6, '*** SYSTEM SETTINGS MENU***')
            print(tab*3, '1. Placeholder\t2. Placeholder\t0. Back to Main Control Console')
            data_requested = input('Select a number: ')

            if data_requested == '0':
                break


### Exit ###

    if inp == '0':

        Lifecycle.close()
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console.')
        time.sleep(.5)
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console..')
        time.sleep(.5)
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console...')
        time.sleep(.5)
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console....')
        time.sleep(.5)
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console.....')
        time.sleep(.5)
        ProgramHeader()
        print('Saving changes, closing database connection and exiting the console.....DONE')
        exit()

