def read_data(f):
    list = []
    with open(f) as file:
        for line in file:
            list.append(line)
    return list

def count_direction(data):
    hor = 0
    ver = 0
    for val in data:
        splitted = val.split()
        if splitted[0] == 'forward':
            hor += int(splitted[1])
        if splitted[0] == 'down':
            ver += int(splitted[1])
        if splitted[0] == 'up':
            ver -= int(splitted[1])
    print(hor*ver)


def count_aim(data):
    hor = 0
    ver = 0
    aim = 0
    for val in data:
        splitted = val.split()
        if splitted[0] == 'forward':
            hor += int(splitted[1])
            ver += aim * int(splitted[1])
        if splitted[0] == 'down':
            aim += int(splitted[1])
        if splitted[0] == 'up':
            aim -= int(splitted[1])

    print(ver*hor)

f = "../Datasets/data2.txt"
data = read_data(f)
#count_direction(data)
count_aim(data)
