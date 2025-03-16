# Your Student ID: 220543602
# Your Name and Surname: Mahmud Bekkar
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
operation = input("INPUT (+, -, *, /) : ")
if operation == "+":
    SUM = x + y
elif operation == "-":
    SUM = x - y
elif operation == "*":
    SUM = x * y
else:
    if y == 0:
        SUM = ""
        print("Error! Division by Zero")
    else:
        SUM = x / y
print(SUM)
