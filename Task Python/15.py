# Accept number from user and chack the number is perfect or not.
sum = 0
num = int(input("Enter your num :- ")) # 6,28,496,8128 is a perfect number.

for i in range(1,num):
    rem = num % i
    if rem == 0:
        sum += i

if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
