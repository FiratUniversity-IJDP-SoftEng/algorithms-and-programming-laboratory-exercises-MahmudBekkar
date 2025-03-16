# Your Student ID: 220543602
# Your Name and Surname: Mahmud Bekkar
bekkar = int(input("Number Of Rows: "))
for i in range(1, bekkar + 1):
    x = " " * (bekkar - i) 
    y = "*" * (2 * i - 1)  
    print(x + y)

