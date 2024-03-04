'''
Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.
'''

def online_count(statuses):
    # Use a generator expression to count how many people are online
    count_online = sum(1 for status in statuses.values() if status == "online")
    return count_online

# Example usage
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))  # Output: 2

'''
This function works by iterating over the values of the statuses dictionary with a generator expression. 
It checks each value to see if it is equal to "online". 
For each case where the condition is true, it generates a 1, effectively counting the number of people who are online. 
The sum() function then adds up all the 1s to get the total count of people who are online, and this count is returned.
'''