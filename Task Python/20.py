"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

rows = int(input("Enter the rows :- "))

for i in range(rows+1):
    for j in range(i):
        print(" ", end="")
    for k in range(rows - i):
        print("* ",end="")
    print()    