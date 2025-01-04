money = int(input("How much money would you like to invest, Mr Frodo? "))
days = int(input("How many days would you like to invest this for? "))
compound_int = money * ((1 + 0.045/12)**(days//31))
print("After that time you will have: $" + str(compound_int))