sum = 0

flag = True

while flag:
    num = int(input("Enter the number :- "))
    sum += num

    choice = input("Do you went enter more number perss n for no ")

    if choice == 'n' or choice == 'no':
        status = False