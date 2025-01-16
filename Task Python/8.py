# find the large number.

num1 = int(input("Enter a number 1 :- "))
num2 = int(input("Enter a number 2 :- "))

if num1 > num2:
    print(f"{num1} is large {num2}")
elif num2 > num1:
    print(f"{num2} is large {num1}")
else:
    print(f"{num1} = {num2}")        
