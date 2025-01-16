# break example in game implementation 

lives = 3

count = True

while count:
    num = int(input("Enter a number :- "))
    lives -= 1
    if lives < 1:
        break