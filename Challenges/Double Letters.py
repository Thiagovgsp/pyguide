'''
Challenge
Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

'''

def double_letters(string):
    # Loop through the string by index
    for i in range(len(string) - 1):
        # Check if the current character is the same as the next character
        if string[i] == string[i + 1]:
            return True
    return False

# Example usage
print(double_letters("hello"))  # Output: True
print(double_letters("nono"))  # Output: False
