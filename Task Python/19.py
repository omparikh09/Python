"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# Define the number of rows
rows = int(input("Enter the rows can you print :- "))

# Generate the pyramid pattern
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print() 