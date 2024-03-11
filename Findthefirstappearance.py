# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.


def replace_not_poor(string):
    # Find the index of 'not' and 'poor'
    index_not = string.find('not')
    index_poor = string.find('poor')
    
    if index_not != -1 and index_poor != -1 and index_not < index_poor:
       
        return string[:index_not] + 'good' + string[index_poor + 4:]
    else:
        return string

# Test the function
test_string = "The weather is not so poor today."
result = replace_not_poor(test_string)
print(result)
