import math

"""--- To print multiplication tables up to 10 of any number."""
print("Give a number and I will give you its multiplication table up to 10.")
user_input = int(input("Number: "))

for i in range(1, 11):
    count = user_input
    count *= i
    print(user_input, "x", i, "=", count)
