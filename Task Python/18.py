"""
A 
A B 
A B C 
A B C D 
A B C D E
"""
limit = int(input("Enter your limit :- "))

for row in range(1,limit+1):
    for col in range(1,row+1):
        print(chr(64 + col),end=" ") # chr(65) = 'A', so 64 + j give latters
    print()    