import copy
import random

result = []
score = []

def generateRandomSequence(n):
    sequence = []
    for i in range(n):
        sequence.append(i + 1)
    counter = n - 1
    while counter >= 0:
        index = random.randint(0, n - 1)
        sequence[index], sequence[counter] = sequence[counter], sequence[index]
        counter -= 1
    return sequence

def isSafe(board, row, col):
 
    if board[row][col] == 2:
        return False

    flag_a = 0
    i = col
    while i >= 0:
        if board[row][i] == 1 and flag_a == 0:
            return False
        elif board[row][i] == 2:
            flag_a = 1
        i -= 1

    i = row
    j = col
    flag_b = 0
    while i >= 0 and j >= 0:
        if board[i][j] == 1 and flag_b == 0:
            return False
        elif board[i][j] == 2:
            flag_b = 1
        i -= 1
        j -= 1

    i = row
    j = col
    flag_c = 0
    while j >= 0 and i < 8:
        if board[i][j] == 1 and flag_c == 0:
            return False
        elif board[i][j] == 2:
            flag_c = 1
        i += 1
        j -= 1
    
    i = row
    flag_d = 0
    while i < 8:
        if board[i][col] == 1 and flag_d == 0:
            return False
        elif board[i][col] == 2:
            flag_d = 1
        i += 1

    i = row
    flag_e = 0
    while i >= 0:
        if board[i][col] == 1 and flag_e == 0:
            return False
        elif board[i][col] == 2:
            flag_e = 1
        i -= 1

    return True
 
def check_obstacle(board, row, col):
    j = row + 1
    while j < 8:
        if board[j][col] == 2:
            return True
        j += 1
    return False

def check_reward(board, x, rewards):
    s = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                s += rewards[i][j]
    if s >= x:
        return True
    else:
        return False

def solveNQUtil(board, col, n, x, rewards):
    if (n == 0):
        boardc = copy.deepcopy(board)
        if check_reward(boardc, x, rewards):
            result.append(boardc)
        return True

    res = False
    for i in range(8):
        if (isSafe(board, i, col)):
            board[i][col] = 1
            if not check_obstacle(board, i, col):
                res = solveNQUtil(board, col + 1, n - 1, x, rewards) or res
            else:
                res = solveNQUtil(board, col + 1, n - 1, x, rewards) or res
                res = solveNQUtil(board, col, n - 1, x, rewards) or res
            board[i][col] = 0
    return res

def solveNQ(n, x):
    result.clear()
    board = [[0 for j in range(n)]
             for i in range(n)]
    rewards = [[0 for j in range(n)]
             for i in range(n)]
    sequence = generateRandomSequence(64)
    counter = 0
    for i in range(8):
        for j in range(8):
            rewards[i][j] = sequence[counter]
            counter += 1
    board[3][0] = 2
    board[3][3] = 2
    board[6][2] = 2
    solveNQUtil(board, 0, n, x, rewards)
    return result

n = 8
res = solveNQ(n, 300)
for i in range(len(res)):
    for j in range(8):
        for k in range(8):
            print(res[i][j][k], end = " ")
        print()
    print()
print(len(res))