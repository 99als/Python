amount = int(input("Enter number: "))

if amount < 8:
    print("Cold!")
elif 8 <= amount < 20:
    print("Getting warmer ...")
elif 20 <= amount < 100:
    print("Hot!")
elif amount >= 100:
    print("BOILING!!!")