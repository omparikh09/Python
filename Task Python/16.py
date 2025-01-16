# accept num from user and print palindrom number.

rem = 0

num = int(input("Enter your number :- "))

copy = num
rev = 0

while num > 0:
    rem = num % 10 # rem = 12.1
    rev = (rev*10) + rem
    num //= 10

print(f"original number = {copy}")
print(f"reversed number = {rev}")

if copy == rev:
    print(f"This is a palindrom number = {copy}")
else:
    print(f"This is a not palindrom number = {copy}")   