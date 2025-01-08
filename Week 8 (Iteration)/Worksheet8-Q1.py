num = input("Enter the number for 'num': ")
n = input("Enter the number for 'N': ")
if (num.isdigit() and n.isdigit() and int(num) != 0):
    num = int(num)
    n = int(n)
    count = 1
    while count <= n:
        print(f"{count} ** {num} = {count ** num}")
        count += 1
else:
    print("Invalid input")