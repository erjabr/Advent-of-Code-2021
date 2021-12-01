
data_test = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]
def read_data(f):
    list = []
    with open(f) as file:
        for line in file:
            list.append(int(line))
    return list

def count_depth(list):
    depth = 0
    j = 0
    for i in range(1,len(list)):
        if(list[i] > list[j]):
            depth += 1
        j += 1
    return depth
def sliding_window(list,window_size):
    windows = []
    for i in range(len(list)-window_size + 1):
        windows.append([list[i],list[i+1],list[i+2]])
    return windows

def sum_windows(l):
    sum = []
    for array in l:
        sum_val = 0
        for val in array:
            sum_val += val
        sum.append(sum_val)
    return sum

f = "../Datasets/data1.py"
data = read_data(f)
windows = sliding_window(data,window_size=3)
#c_part_one = count_depth(data)
c_part_two = count_depth(sum_windows(windows))
print(c_part_two)