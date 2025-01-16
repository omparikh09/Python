# Write a program that prints all even numbers between 1 and 20 (inclusive).


for num in range(1,21):
    if num%2==0:
        if num <= 20:
            print(f"even num = {num}")

