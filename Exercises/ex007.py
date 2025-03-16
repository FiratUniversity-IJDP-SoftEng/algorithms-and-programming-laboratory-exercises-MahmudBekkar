# Your Student ID: 220543602
# Your Name and Surname: Mahmud Bekkar
user = input("Enter a string : ")
y = {}
for i in user:
    y[i] = y.get(i, 0) + 1
print("Character frequencies :")
for i in sorted(y):
    print(f"{i}: {y[i]}")
