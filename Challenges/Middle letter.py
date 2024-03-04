'''
Middle letter
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(input_string):
    
    length = len(input_string)

    if length % 2 == 0:
        return ''
    
    else:
        mid_index = length // 2
        return input_string[mid_index]
    
print(mid('abc'))
print(mid('aaaa'))

'''
% Operator: Modulo
The % operator is known as the modulo or modulus operator. 
It is used to find the remainder of the division of two numbers. 
It essentially tells you what remains after dividing the first number by the second number.
In this example, 10 % 3 returns 1 because when you divide 10 by 3, the quotient is 3 and the remainder is 1.
'''
'''
// Operator: Floor Division
The // operator performs floor division. 
It divides two numbers and rounds the result down to the nearest whole number, effectively "flooring" the result to the closest (and not greater than the result) integer.
Here, 10 // 3 returns 3. When you divide 10 by 3, you get 3.3333..., but floor division truncates the decimal part (without rounding), resulting in the integer 3.
'''