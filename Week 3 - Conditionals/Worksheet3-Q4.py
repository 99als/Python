month = int(input("Enter the month (1-12): "))
if (month == 1 or month == 2 or month == 12):
    print("It's summer. Have fun in the sun!")
elif (3 <= month <= 5):
    print("It's autumn. Enjoy the beautiful sunsets!")
elif (6 <= month <= 8):
    print("It's winter. Go skiing!")
elif (9 <= month <= 11):
    print("It's spring. Check out the spring racing carnival!")
else:
    print("Invalid input. Please enter any number between 1 and 12.")