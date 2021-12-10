from collections import defaultdict
with open("../Datasets/day7.txt") as file:
    vals = []
    for line in file:
        vals = line.split(',')

ints = list(map(int, list(vals)))
dic = defaultdict(float)

for i in range(max(ints)):
    count = 0
    steps = 0
    for val in ints:
        steps = abs(val-i)
        count += ((steps*steps) + steps) / 2
    dic[i] = count

print(min(dic.values()))
