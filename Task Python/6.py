# Write a program to find the sum of all odd numbers from 1 to 100

odd_sum = 0

for num in range(1,101):
    if num%2!=0:
       odd_sum += num

print(f"The sum of all odd numbers from 1 to 100 is: {odd_sum}")