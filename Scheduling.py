import datetime

def brew_date():
    global brew_date
    # Sets the brew_date variable to the current day
    brew_date = datetime.date.today()
    return brew_date.strftime("%m-%d-%Y")


def rack_date(primary_days):
    global rack_date
    # Calculates rack date given a brew date of today and how many days are needed in primary fermentation.
    rack_date = brew_date + datetime.timedelta(days=primary_days)
    return rack_date.strftime("%m-%d-%Y")

def bottling_date(secondary_days):
    global bottling_date
    # Calculates bottling date given the rack_date and how many days are needed in secondary fermentation.
    bottling_date = rack_date + datetime.timedelta(days=secondary_days)
    return bottling_date.strftime("%m-%d-%Y")

def drink_date(bottle_days):
    global drink_date
    drink_date = bottling_date + datetime.timedelta(days=bottle_days)
    return drink_date.strftime("%m-%d-%Y")

def expiration_date(shelf_life):
    global expiration_date
    expiration_date = drink_date + datetime.timedelta(days=shelf_life)
    return expiration_date.strftime("%m-%d-%Y")

# Testing
'''
print(brew_date())
print(rack_date(14))
print(bottling_date(36))
print(drink_date(14))
print(expiration_date(180))
'''