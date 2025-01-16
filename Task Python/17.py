# accept principal amount and find the compound interest of year 

principal = int(input("Enter your principal amount :- ")) # Enter your parincipal amount
rate = int(input("Enter the annual interest rate (in %) :- ")) # Enter your interest
year = int(input("Enter the year :- ")) # Enter the year


amount = principal * pow((1 + rate / 100),year) #amount find 
compoundInterest = amount - principal # find compound interest

print(f"The total amount after {year} year is :- {amount}")
print(f"The compound interest is :- {compoundInterest}")
