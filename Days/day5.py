
import numpy as np
zeros = np.zeros((1000, 1000))

def read_data(f):
    c = 0
    with open(f) as file:
        for line in file:
            first,last = line.split('->')
            x1,y1 = first.split(',')
            x2,y2 = last.split(',')
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            #Needed to know which direction we go in, for our diagonal part
            dx = 1 if x2 >= x1 else -1
            dy = 1 if y2 >= y1 else -1

            if x1 == x2:
                for y in range(y1,y2 + dy, dy):
                    zeros[x1][y] = zeros[x1][y] + 1
            elif y1 == y2:
                for x in range(x1,x2+dx,dx):
                    zeros[x][y1] = zeros[x][y1] + 1
            # check for cases such as (9,7) -> (7,9) or (1,1) -> (3,3)
            elif abs(x2-x1) == abs(y2-y1):
                x = x1
                for y in range(y1, y2 + dy, dy):
                    zeros[x][y] += 1
                    #Reduce or increase the value of depending on the direction
                    x += dx

    for x in range(1000):
        for y in range(1000):
            if zeros[x][y] > 1:
                c += 1
    print(c)
import time
t_start = time.perf_counter_ns()
f = "../Datasets/data5.txt"
read_data(f)
t_end = time.perf_counter_ns()
print((t_end-t_start)/1000000)