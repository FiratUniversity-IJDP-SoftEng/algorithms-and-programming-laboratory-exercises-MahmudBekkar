# Your Student ID: 220543602
# Your Name and Surname: Mahmud Bekkar
numbers = list(range(1, 11))
print("Original list:\n", numbers)
numbers.reverse()
print("Reversed the list:\n", numbers)
numbers.extend([11, 12, 13])
print("Adding 11,12,and 13:\n", numbers)
print("List's length:\n", len(numbers))
numbers.pop(0) 
numbers.pop(-1) 
print("List to first :\n", numbers)
even_numbers = sorted([num for num in numbers if num % 2 == 0])
print("list of even numbers:\n", even_numbers)
