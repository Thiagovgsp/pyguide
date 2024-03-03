#simplified counting with get()
counts = dict()
names = ['caio', 'gus', 'caio', 'gus', 'thiago']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

