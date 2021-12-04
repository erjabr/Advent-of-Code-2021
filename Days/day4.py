def read_data(f):
    s = []
    with open(f) as file:
        for line in file:
            s.append(line)
    return s
import numpy as np
def check_bingo(board,input):
    tracker = np.zeros((len(board),len(board[0])),dtype=bool)
    boolean = False
    for i in range(len(board)):
        counter = 0
        for j in range(len(board[i])):
            if int(board[i][j]) in input:
                counter += 1
                tracker[i][j] = True
            if counter == 5:
                boolean = True

    for i in range(len(board)):
        counter = 0
        for j in range(len(board[i])):
            if int(board[j][i]) in input:
                counter += 1
                tracker[j][i] = True
            if counter == 5:
                boolean = True

    counter = 0
    for i in range(len(board)):
        if int(board[i][i]) in input:
            counter += 1
            tracker[i][i] = True
        if counter == 5:
            boolean = True
    counter = 0

    for i in range(len(board)):
        if int((board[i][len(board) - i - 1])) in input:
            counter += 1
            tracker[i][len(board) - i - 1] = True
        if counter == 5:
           boolean = True

    if(boolean):
        #("Bingo")
        #Sum the values that are not visited:
        sum = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if tracker[i][j] == False:
                    sum += int(board[i][j])
        print(sum*input[-1])
        return True
    return False

def bingo(data,input):
    for i in range(5,len(input)-1):
        vals = input[:i]
        for idx,board in enumerate(data):
            if(check_bingo(board,vals)):
                data.pop(idx)

def fix_boards(string):
    boards = []
    list = []
    for i in range(1,len(string)):
        if string[i] == '' or string[i] == '\n':
            continue
        if len(list) == 5:
            boards.append(list)
            list = []
        list.append(string[i].split())
    return boards

f = "../Datasets/day4.txt"
data = read_data(f)
input = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]
boards = fix_boards(data)
bingo(boards,input)


