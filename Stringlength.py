# Write a Python program to get a string made of the first 2 and the last
#   2 chars from a given a string. If the string length is less than 2, return
#     instead of the empty string


def get_first_and_last_two_chars(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

# Test the function
input_string = input("Enter a string: ")
result = get_first_and_last_two_chars(input_string)
print("Result:", result)
