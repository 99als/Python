name = input("Enter your name, soldier: ")
if ((name).isdigit() and 0 <= int(name) <=2):
    print("HAHA! You may not pass!!")
elif (name == ""):
    print("A luddite! GO AWAY AT ONCE!")
else:
    print("Welcome to the camp, " + name + ", if that really is your name.")
