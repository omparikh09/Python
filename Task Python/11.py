"""
A 
B C
D E F
G H I J
K L M N O
"""
char = 65  

num = 5

for row in range(1,num+1):
    for col in range(row):
        print(chr(char), end=" ")
        char += 1 
    print()
