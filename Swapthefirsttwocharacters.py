# Write a Python program to get a single string from two given strings,
#     separated by a space and swap the first two characters of each string.


def swap_first_two_chars(str1, str2):
    # Swapping the first two characters of each string
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    
    result = swapped_str1 + ' ' + swapped_str2
    
    return result

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = swap_first_two_chars(string1, string2)
print("Result:", result)













