# Write a Python program to find whether a given number is even or odd,
# print out an appropriate message to the user.

def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

num = int(input("Enter a number: "))


even_or_odd(num)