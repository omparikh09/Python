"""
* * * * * 
* * * * * 
* * $ * * 
* * * * * 
* * * * * 
"""
num = int(input("Enter a num :- "))
for row in range(1,num+1):
    for col in range(1,num+1):
        if row == 3 and col == 3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print() 