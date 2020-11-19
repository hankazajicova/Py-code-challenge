board_1 = [[1, 1, 0],
         [2, 1, 0],
         [2, 2, 2]]


def row_check(board: list) -> int:
    """check for same values in row

    Args:
        board (list): input board list

    Returns:
        int: won player
    """
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            print("won in row")
            return row[0]

    print("not in row")
    return None


def column_check(board: list) -> int:
    """check for same values in column

    Args:
        board (list): input board list

    Returns:
        int: won player
    """
    new_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0])-1,-1,-1)]
    for column in new_board:
        if len(set(column)) == 1 and column[0] != 0:
            print("won in column")
            return column[0]

    print("not in column")
    return None


def diagonale_check(board: list) -> int:
    """check for same values in diagonale

    Args:
        board (list): input board list

    Returns:
        int: won player
    """
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
        if board[0][0] != 0:
            print("won in diagonale")
            return board[0][0]

    print("not in diagonale")
    return None


def get_winner(board: list) -> int:
    """winner evaluation

    Args:
        board (list): input board list

    Returns:
        int: winner
    """
    win_type = [row_check, column_check, diagonale_check]
    for won in win_type:
        winner = won(board)
        if winner is not None:
            print("The winner is player:")
            return winner

    return 0

tic_tac_toe = get_winner(board_1)
print(tic_tac_toe)
