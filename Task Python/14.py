"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
k = 1
num = int(input("Enter a number :- "))
for row in range(1,num+1):
    for col in range(1,row+1):
        print(f"{k}",end=" ")
        k += 1
    print()    