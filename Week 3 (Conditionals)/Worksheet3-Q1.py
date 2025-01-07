dollars = float(input("How much does it cost? "))
total = dollars * 100
lastDigit = ((total%100)%10)
if ((0 <= lastDigit < 3) or (5 <= lastDigit <= 7)):
    print("The price didn't change or was rounded down! Pay cash!")
else:
    print("The price was rounded up! Pay card.")