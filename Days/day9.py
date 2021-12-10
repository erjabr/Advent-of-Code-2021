with open("../Datasets/day9.txt") as file:
    s = []
    for line in file:
        line = line.rstrip()
        s.append(line)
import numpy as np
def adj_list(map,start,tracker):
    adj = []
    for pos in start:
        i,j = pos
        if i - 1 in range(len(map)):
            if int(map[i - 1][j]) != 9 and not(tracker[i-i][j]):
                adj.append([i-1,j])
                tracker[i-1][j] = True

        if i + 1 in range(len(map)):
            if int(map[i + 1][j]) != 9 and not(tracker[i+1][j]):
                adj.append([i + 1, j])
                tracker[i+1][j] = True

        if j - 1 in range(len(map[i])):
            if int(map[i][j-1]) != 9 and not(tracker[i][j-1]):
                adj.append([i,j-1])
                tracker[i][j-1] = True

        if j + 1 in range(len(map[i])):
            if int(map[i][j+1]) != 9 and not(tracker[i][j+1]):
                adj.append([i,j+1])
                tracker[i][j+1] = True
    return adj
from collections.abc import Iterable
def flatten(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def fix_list(l):
    unique = []
    for v in l:
        if v not in unique:
            unique.append(v)
    return unique

def basis_map(map,low_points):
    basis = []
    for i in range(len(low_points)):
        tracker = np.zeros((len(s), len(s[0])), dtype=bool)
        adj = [low_points[i]]
        big_list = []
        while len(adj) > 0:
            adj = adj_list(map, adj,tracker)
            big_list.append(adj)

        flat = fix_list(flatten(big_list))
        basis.append(len(flat))
    basis.sort(reverse=True)
    print(basis[0]*basis[1]*basis[2])


def height_map(map):
    sum = 0
    list = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            mark = 0
            adj = 0
            #Ner
            if i-1 in range(len(map)):
                adj += 1
                if int(map[i][j]) < int(map[i-1][j]):
                    mark += 1

            if i+1 in range(len(map)):
                adj += 1
                if int(map[i][j]) < int(map[i+1][j]):

                    mark += 1
            if j-1 in range(len(map[i])):
                adj += 1
                if int(map[i][j]) < int(map[i][j-1]):
                    mark += 1
            if j+1 in range(len(map[i])):
                adj += 1
                if int(map[i][j]) < int(map[i][j+1]):
                    mark += 1
            #We have a winnner

            if mark == adj:
                list.append([i,j])
                sum += int(map[i][j]) + 1
    return sum,list



sum,list = height_map(s)
basis_map(s,list)
#print(list)