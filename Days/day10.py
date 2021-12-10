
with open("../Datasets/day10.txt") as file:
    s = []
    for line in file:
        line = line.rstrip()
        s.append(line)
open_list = ["[","{","(","<"]
close_list = ["]","}",")",">"]




def count_brack(s):
    results = []
    scores = []
    counter = 0
    for line in s:
        corr = False
        index = []
        res = []
        for c in line:
            if c in open_list:
                index.append(c)
            elif c in close_list:
                pos = close_list.index(c)
                if ((len(index) > 0) and
                        (open_list[pos] == index[len(index) - 1])):
                    index.pop()
                else:
                    corr = True
                    break
        if len(index) == 0:
            print("Balanced")
        else:

            if not corr:
                index.reverse()
                for val in index:
                    if val == '(':
                        counter = counter * 5 + 1
                    if val == '[':
                        counter = counter * 5 + 2
                    if val == '{':
                        counter = counter * 5 + 3
                    if val == '<':
                        counter = counter * 5 + 4
                scores.append(counter)
                counter = 0
    scores.sort()
    print(scores[int(len(scores)/2)])

















count_brack(s)

