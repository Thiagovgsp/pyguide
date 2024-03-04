'''Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].'''

def capital_indexes(input_strings):

    indexes = []

    for index, char in enumerate(input_strings):

        if char.isupper():
            indexes.append(index)

    return indexes

print(capital_indexes('HeLlO'))