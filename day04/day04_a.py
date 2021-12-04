from aocd import lines
from enum import Enum

# Get data
bingo_boards = []
numbers = lines[0].split(',')
board = []
board_size = len(lines[2].split())

# Build boards
for i in range(2, len(lines)) :
    
    if lines[i] != "":
        # pair_list = zip(lines[i].split(), [False] * board_size)
        pair_list = [list(a) for a in zip(lines[i].split(), [False] * board_size)]
        
        board.append(list(pair_list))
    else :
        bingo_boards.append(board)
        board = []

bingo_boards.append(board)
board_size = len(bingo_boards[0])


class BingoType(Enum):
    NONE        = 0
    HORIZONTAL  = 1,
    VERTICAL    = 2,
    LEFT_DIAGONAL   = 3,
    RIGHT_DIAGONAL  = 4,


def draw_number(nb, bingo_boards) :
    # print('Drawing number ', nb)
    for board in bingo_boards :
        for y in range(len(board)) :
            for x in range(board_size) :
                if board[y][x][0] == nb :
                    board[y][x][1] = True
                    break
    return bingo_boards


def check_vertical_bingo(board):
    for col in range(len(board)) :
        bingo = True
    
        # Check if it's bingo on this column
        for row in range(len(board[col])) :
            if board[row][col][1] == False :
                bingo = False
                break
        
        if bingo :
            return (BingoType.VERTICAL, col) # Bingo on this column

    return (BingoType.NONE, -1) # No bingo


def check_horizontal_bingo(board):
    for row in range(len(board)) :
        bingo = True
    
        # Check if it's bingo on this row
        for col in range(len(board[row])) :
            if board[row][col][1] == False :
                bingo = False
                break
        
        if bingo :
            return (BingoType.HORIZONTAL, row) # Bingo on this row

    return (BingoType.NONE, -1) # No bingo


def check_diagonal_bingo(board):
    bingo = True
    len_board = len(board)

    # Left to right
    for i in range(len_board) :       
        if board[i][i][1] == False:
            bingo = False
            break

    if bingo :
        return (BingoType.LEFT_DIAGONAL, -1)

    # Right To Left
    for i in range(len_board) :
        pos = len_board - 1 - i # Decreasing utmost right position

        if board[pos][pos][1] == False:
            bingo = False
            break

    if bingo:
        return (BingoType.RIGHT_DIAGONAL, -1)
    else:
        return (BingoType.NONE, -1)


def check_bingo(bingo_boards):
    for idx, board in enumerate(bingo_boards) :
        bingo = check_vertical_bingo(board)
        if not bingo[0] == BingoType.NONE :
            return bingo, idx

        bingo = check_horizontal_bingo(board)
        if not bingo[0] == BingoType.NONE :
            return bingo, idx

        bingo = check_diagonal_bingo(board)
        if not bingo[0] == BingoType.NONE :
            return bingo, idx
    return bingo, -1


def calc_unmarked_sum(board):
    return sum(int(spot[0]) for row in board for spot in row if spot[1] == False)


for nb in numbers:
    bingo_boards = draw_number(nb, bingo_boards)
    bingo, idx = check_bingo(bingo_boards)
    if bingo[0] != BingoType.NONE:
        unmarked_sum = calc_unmarked_sum(bingo_boards[idx])
        final_score = unmarked_sum * int(nb)
        print(final_score)
        exit(0)

print('No bingo')