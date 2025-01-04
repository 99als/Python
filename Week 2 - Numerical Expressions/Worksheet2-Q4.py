days = int(input("How many days have you lived? "))
years = days//365
print("You are", years, "years young!")
daysLeft = 365 - (days - 365 * years)
print("You have", daysLeft, "days until you next get to boogie down.")