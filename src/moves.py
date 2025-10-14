def move_left(board):
    new_board = [row[:] for row in board]
    for i in range(len(new_board)):
        new_row = [tile for tile in new_board[i] if tile != 0]
        merged_row = []
        skip = False
        for j in range(len(new_row)):
            if skip:
                skip = False
                continue
            if j < len(new_row) - 1 and new_row[j] == new_row[j + 1]:
                merged_row.append(new_row[j] * 2)
                skip = True
            else:
                merged_row.append(new_row[j])
        merged_row += [0] * (len(board) - len(merged_row))
        new_board[i] = merged_row
    return new_board

def move_right(board):
    new_board = [row[:] for row in board]
    for i in range(len(new_board)):
        new_row = [tile for tile in new_board[i] if tile != 0][::-1]
        merged_row = []
        skip = False
        for j in range(len(new_row)):
            if skip:
                skip = False
                continue
            if j < len(new_row) - 1 and new_row[j] == new_row[j + 1]:
                merged_row.append(new_row[j] * 2)
                skip = True
            else:
                merged_row.append(new_row[j])
        merged_row = [0] * (len(board) - len(merged_row)) + merged_row[::-1]
        new_board[i] = merged_row
    return new_board

def move_up(board):
    new_board = [list(row) for row in zip(*board)]
    new_board = move_left(new_board)
    return [list(row) for row in zip(*new_board)]

def move_down(board):
    new_board = [list(row) for row in zip(*board)]
    new_board = move_right(new_board)
    return [list(row) for row in zip(*new_board)]