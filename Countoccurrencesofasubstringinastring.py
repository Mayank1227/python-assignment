# Write a Python program to count occurrences of a substring in a string.

  
ini_str =(input("Enter a string:"))
sub_str =(input("Enter a string:"))
 
count = 0
n = len(ini_str)
m = len(sub_str)
 
for i in range(n - m + 1):
    if ini_str[i:i+m] == sub_str:
        count += 1
 
print("Number of substrings:", count)