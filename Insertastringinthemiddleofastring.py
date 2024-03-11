# Write a Python function to insert a string in the middle of a string.

def insert_in_middle(original_str, str_to_insert):
    middle_index = len(original_str) // 2
    return original_str[:middle_index] + str_to_insert + original_str[middle_index:]

# Example usage:
original_string = "Hello, world!"
string_to_insert = "beautiful "
result = insert_in_middle(original_string, string_to_insert)
print(result)
