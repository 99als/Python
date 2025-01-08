# import the `randint` function
from random import randint

def luck_tester(lucky_number, max_rolls, die_size):
    count = 0
    while count < max_rolls:
        if randint(1, die_size) == lucky_number:
            return 'Off to Mordor!'
        count += 1
    return 'Back to the Shire!'
