# Write a Python function that takes a list of words and returns the length of the longest one.


def longest_word_length(words):
    if not words:
        return 0  

    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

# Example usage:
word_list = ["apple", "banana", "orange", "strawberry"]
print("Length of the longest word:", longest_word_length(word_list))
