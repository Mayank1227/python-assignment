
#  Write python program that swap two number with temp variable and
# without temp variable.

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))

print("Numbers before swapping:", num1, num2)

num1, num2 = swap_without_temp(num1, num2)

print("Numbers after swapping:", num1, num2)
