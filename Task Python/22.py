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


rows = int(input("Enter your rows :- "))

for i in range(1,rows + 1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()          


"""
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1
"""

"""
rows = int(input("Enter your rows :- "))

for i in range(1,rows + 1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(i):
        print(f"{i} ",end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(i):
        print(f"{i} ",end="")
    print()    
"""          