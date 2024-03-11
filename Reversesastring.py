# Write a Python function to reverses a string if its length is a multiple of 4.

def reverse_string_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

# Example usage:
input_string = "abcdefgh"
output_string = reverse_string_if_multiple_of_4(input_string)
print("Input:", input_string)
print("Output:", output_string)





