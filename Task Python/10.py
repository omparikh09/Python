"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

num = int(input("Enter your number :- "))

for row in range(1,num+1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

for row in range(num-1,0,-1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()        