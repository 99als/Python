height = int(input("Enter triangle height: "))
for i in range (height, 0, -1):
    print(f"{i*'*':<}{(height - i) * ' '}{i*'*':>{height}}")
for i in range(2,height+1):
    print(f"{i*'*':<}{(height - i) * ' '}{i*'*':>{height}}")
