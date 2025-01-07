suspects = [("Max Zorin", "Kills with guns", "Chip Tycoon"), ("Hugo Drax",), ("Jaws", "Bites people", "Mutant"),
            ("Nick Nack", "Really short"), ("Le Chiffre", "Good at poker", "Really evil"),
            ("Francisco Scaramanga", "Has a Golden Gun", "Probably will melt"),
            ("Mr Big", "Also the name of a rock band", "Dictator of San Monique")]

# write your program here
culprit = int(input("WHO DID IT HUGO!? "))
if (culprit == 7):
    print("It was " + suspects[0][0])
    datalist = (suspects[0][1], suspects[0][2])
    print("Data:", datalist)

else:
    datalist = len(suspects[culprit])
    if (datalist == 1):
        print("It was " + suspects[culprit][0])
        data = ()
        print("Data:", data)
    elif (datalist == 2):
        print("It was " + suspects[culprit][0])
        data = (suspects[culprit][1])
        print("Data:", data)
    else:
        print("It was " + suspects[culprit][0])
        data = (suspects[culprit][1], suspects[culprit][2])
        print("Data:", data)