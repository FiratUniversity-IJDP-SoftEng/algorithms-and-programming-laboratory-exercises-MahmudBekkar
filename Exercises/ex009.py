# Your Student ID: 220543602
# Your Name and Surname: Mahmud Bekkar
X = input("Enter conversion type (C to F or F to C): ").strip().lower()
temperature = float(input("Enter the temperature value: "))
if X == "1":
    result = (temperature * 9/5) + 32
    print(f"{temperature} Celsius is {result} Fahrenheit")
elif X == "2":
    result = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit is {result} Celsius")
else:
    print("Invalid conversion type")
