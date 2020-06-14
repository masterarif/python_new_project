

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
print(board)

board = [[EMPTY for i in range(8)] for j in range(8)]