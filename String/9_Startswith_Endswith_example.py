s1 = "Python Programming"

if s1.startswith("Python") and s1.endswith("Programming"):
    print("Valid string")
else:
    print("Invalid string")

s1 = "  Python Programming  "

if s1.startswith("Python") and s1.endswith("Programming"):
    print("Valid string")
else:
    print("Invalid string")