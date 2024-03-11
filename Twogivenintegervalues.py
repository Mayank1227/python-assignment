# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

def check_values(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

print(check_values(7, 2))  
print(check_values(3, 8)) 
print(check_values(4, 4))  
print(check_values(2, 3))  
print(check_values(10, 15))