#dictionary literals use curly braces and have a list of key: value pairs
#you can make an empty dictionary using empty curly braces

'''
jjj = {'chack' : 1, 'fred': 42, 'jan': 100}
print(jjj)

ooo = {}
print(ooo)
'''

counts = dict()
names = ['caio', 'gus', 'caio', 'gus', 'thiago']
for name in names:
    if name not in counts:
        counts[name] = 1

    else:
        counts[name] = counts[name] + 1
print(counts)