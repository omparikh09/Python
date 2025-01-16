# Accept number form user and chack the number is Amstrong number or not.

n = 0
result = 0

num = int(input("Enter the number :- "))

ornum = num

while ornum != 0:
    ornum //= 10
    n += 1
    
ornum = num     

while ornum != 0:
    rem = ornum%10
    result += pow(rem,n)
    ornum //= 10    

if result == num:
    print(f"{num} is an Amstrong number.") 
else:
    print(f"{num} is not an Amstrong number.")       