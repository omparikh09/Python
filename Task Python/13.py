"""
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9
"""
num = int(input("Enter num of rows :- "))

for row in range(1,num+1):
    num = row
    for col in range(1,row+1):
        print(num,end=" ")
        num += 1
    print()    