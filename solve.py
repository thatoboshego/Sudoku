def extractFile(filename):
    with open(filename, 'r', errors='ignore') as f:
        contents = f.read()
    return contents


def createBoard(contents):
    board = [[]]
    count = 0

    for i in contents:
        if i == '\n' or i == " ":
            continue

        board[count].append(i)

        if len(board[count]) == 9 and count < 8:
            board.append([])
            count += 1

    return board


def getSubgrid(board, row, col):
    subgrid_values = []

    if row <= 2 and col <= 2:
        for i in range(0, 3):
            for j in range(0, 3):
                subgrid_values.append(board[i][j])

    elif row <= 2 and col <= 5:
        for i in range(0, 3):
            for j in range(3, 6):
                subgrid_values.append(board[i][j])

    elif row <= 2 and col <= 8:
        for i in range(0, 3):
            for j in range(6, 9):
                subgrid_values.append(board[i][j])

    elif row <= 5 and col <= 2:
        for i in range(3, 6):
            for j in range(0, 3):
                subgrid_values.append(board[i][j])

    elif row <= 5 and col <= 5:
        for i in range(3, 6):
            for j in range(3, 6):
                subgrid_values.append(board[i][j])

    elif row <= 5 and col <= 8:
        for i in range(3, 6):
            for j in range(6, 9):
                subgrid_values.append(board[i][j])

    elif row <= 8 and col <= 2:
        for i in range(6, 9):
            for j in range(0, 3):
                subgrid_values.append(board[i][j])

    elif row <= 8 and col <= 5:
        for i in range(6, 9):
            for j in range(3, 6):
                subgrid_values.append(board[i][j])

    else:
        for i in range(6, 9):
            for j in range(6, 9):
                subgrid_values.append(board[i][j])

    return subgrid_values


def checkMove(board, row, col):
    candidates = [str(i) for i in range(1, 10)]

    tempListH = []
    for j in board[row]:
        if j != "0":
            tempListH.append(j)

    for k in tempListH:
        for l in candidates:
            if k == l:
                candidates.remove(l)

    tempListV = []
    for r in range(9):
        value = board[r][col]
        if value != "0":
            tempListV.append(value)

    for k in tempListV:
        for l in candidates:
            if k == l:
                candidates.remove(l)

    tempListS = getSubgrid(board, row, col)

    for k in tempListS:
        for l in candidates:
            if k == l:
                candidates.remove(l)

    return candidates


def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == "0":
                return i, j
    return None


def solve(board):
    empty = findEmpty(board)
    if not empty:
        return True

    row, col = empty
    candidates = checkMove(board, row, col)

    for value in candidates:
        print("Trying", value, "at row", row, "col", col)
        board[row][col] = value

        if solve(board):
            print("Placed", value, "at row", row, "col", col)
            return True

        print("Backtracking from", value, "at row", row, "col", col)
        board[row][col] = "0"

    return False


def writeSolution(board, filename):
    with open(filename, 'w') as f:
        for row in board:
            line = ' '.join(row)
            f.write(line + '\n')

contents = extractFile("puzzle.txt")
board = createBoard(contents)

solve(board)

writeSolution(board, "solved_puzzle.txt")