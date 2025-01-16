"""
Enter your number :- 20
Do you want to continue press 'y' for yes and 'n' for no :- y
Enter your number :- 14
Do you want to continue press 'y' for yes and 'n' for no :- y  
Enter your number :- 58
Do you want to continue press 'y' for yes and 'n' for no :- n
"""
status = True 

while status:
    num = int(input("Enter your number :- "))

    choice = input("Do you want to continue press 'y' for yes and 'n' for no :- ").lower()

    if choice == 'y':
        status = True
    else:
        status = False    