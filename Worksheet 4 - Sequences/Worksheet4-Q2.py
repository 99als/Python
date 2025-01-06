question = input("Question: ")
amount = int(question[13:16])
cents = (question[-3:-1])
dollars = (question[-6:-4])

if (int(cents) == 0):
    total = int(dollars)/amount
    print("$" + str(total) + '0')
else:
    total2 = int(dollars + cents)
    total2 = float(total2/100)
    total2 = total2/amount
    print("$" + str(total2))