
even_sum = 0
odd_sum = 0
for i in range(1,6):
    num = int(input("Enter a num : "))

    if num%2==0:
        even_sum += num
    else:
        odd_sum += num

print(f"even num = {even_sum}")
print(f"odd num = {odd_sum}")