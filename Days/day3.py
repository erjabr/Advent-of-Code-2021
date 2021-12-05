from collections import defaultdict


def read_data(f):
    list = []
    with open(f) as file:
        for line in file:
            list.append(line)
    return list

def count_bits(converted_list):
    col = defaultdict(int)
    #dic = {i:counter, i:counter}
    for val in converted_list:
        for idx, c in enumerate(val):
            col[idx] += int(c)
    list = []
    for k, value in col.items():
        if value >= 500:
            list.append(1)
        else:
            list.append(0)

    return list
def bit_crit_co2(array,idx):
    c = 0
    zeros = []
    ones = []

    if len(array) == 1:
        return array

    for a in array:
        c += int(a[idx])
        if int(a[idx]) == 1:
            ones.append(a)
        else:
            zeros.append(a)

    if len(array) == 2 and c == 1:
        return zeros

    if len(array) - c <= c:
        return zeros
    else:
        return ones

def bit_crit_oxy(array,idx):
    c = 0
    zeros = []
    ones = []

    if len(array) == 1:
        return array

    for a in array:
        c += int(a[idx])
        if int(a[idx]) == 1:
            ones.append(a)
        else:
            zeros.append(a)

    if len(array) == 2 and c == 1:
        return ones

    if c >= len(array) - c:
        return ones
    else:
        return zeros

def co2(array):
    list_oxy = array
    list_co2 = array
    for i in range(len(array)):
        if(len(list_oxy) == 1):
            break
        list_oxy = bit_crit_oxy(list_oxy,i)
        list_co2 = bit_crit_co2(list_co2,i)
        #print(list_co2)

    print(list_oxy)
    print(list_co2)

#def part2(array):


f = "../Datasets/data3.txt"
data = read_data(f)
converted_list = []

for element in data:
    converted_list.append(element.strip())

import time
t_start = time.perf_counter_ns()
co2(converted_list)
t_stop = time.perf_counter_ns()
print(t_stop-t_start)
