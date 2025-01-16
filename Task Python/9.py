"""
swapping with 2 variable
Enter a number 1 :- 10
Enter a number 2 :- 20

Before swapping: num1 = 10
Before swapping: num2 = 20

After swapping: num1 = 20
After swapping: num2 = 10
"""

num1 = int(input("Enter a number 1 :- ")) # 10
num2 = int(input("Enter a number 2 :- ")) # 20
print()
print(f"Before swapping: num1 = {num1}")
print(f"Before swapping: num2 = {num2}")
print()
if num2 != 0:
    num1 = num1*num2   #  200 = 10*20
    num2 = num1//num2  #   10 = 200//20
    num1 = num1//num2  #   20 = 200//10
    print(f"After swapping: num1 = {num1}") # Ans = 20
    print(f"After swapping: num2 = {num2}") # Ans = 10
else:
    print("Error: Division by zero is not allowed.")    