import re

file = input('enter: ')
if not file:
    file = 'romeo.txt'

try:
    with open(file, 'r') as handle:
        content = handle.read()
        print(content)

except FileNotFoundError:
    print(f"The file {file} does not exist.")


"""
import re

file = input('enter: ')
if not file:
    file = 'romeo.txt'

try:
    with open(file, 'r') as handle:
        content = handle.read()
        print(content)

except FileNotFoundError:
    print(f"The file {file} was not found")
"""