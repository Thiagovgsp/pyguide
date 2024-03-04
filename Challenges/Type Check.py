def only_ints(param1, param2):

    return type(param1) == int and type(param2) == int


print(only_ints(1, 2)) 
print(only_ints("a", 1))

'''

Type check
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.
For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

'''