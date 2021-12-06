from collections import defaultdict
with open("../Datasets/day6.txt") as file:
    vals = []
    for line in file:
        vals = line.split(',')

#Number of days
days = 256
values = defaultdict(int)
for v in vals:
    values[v] += 1

for day in range(days):
    result = defaultdict(int)
    for k in values.keys():
        if int(k) > 0:
            result[int(k)-1] = values[k]
    result[6] += values[0]
    result[8] += values[0]
    #Update our dictionary for each day
    values = result
print(sum(values.values()))







#print(len(vals))



