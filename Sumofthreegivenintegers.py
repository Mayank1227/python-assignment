# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# Define a function 'sum_three' that takes three integer inputs: x, y, and z.
def sum_three(x, y, z):
    
    if x == y or y == z or x == z:
        sum = 0
    else:
      
        sum = x + y + z
   
    return sum

print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))
print(sum_three(3,5,7))
