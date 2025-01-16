# prime number 
num = int(input("Enter a number :- "))

flag = True

for i in range(2,num):
    if num%i == 0:
        flag = False
        break
    else:
        flag = True

if flag:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a not prime number.")                