game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

print(game[0])
print(game[1])
print(game[2])

PLAYER_1 = 'x'
PLAYER_2 = 'o'

def player_move(player_input: str) -> dict:
    """input tranformation into indices

    Args:
        player_input (str): user input

    Returns:
        dict: row index, column index
    """
    player_split = player_input.split(",", 1)
    player_row = int(player_split[0]) - 1
    player_col = int(player_split[1]) - 1
    return {
        "row" : player_row,
        "column" : player_col
        }


def play_the_game(board: list):
    """game board filling

    Args:
        board (list): input board
    """
    number_of_moves = 0
    while True:
        if number_of_moves == 9:
            break
        print("Make your move as row number,column number")
        player_1 = input("Player 1, you are on - row/column: ")
        player_1_move = player_move(player_1)

        if board[player_1_move['row']][player_1_move['column']] == 0:
            board[player_1_move['row']][player_1_move['column']] = PLAYER_1
            number_of_moves += 1

        print(game[0])
        print(game[1])
        print(game[2])

        print("Make your move as row number,column number")
        player_2 = input("Player 2, you are on - row/column: ")
        player_2_move = player_move(player_2)

        if board[player_2_move['row']][player_2_move['column']] == 0:
            board[player_2_move['row']][player_2_move['column']] = PLAYER_2
            number_of_moves += 1

        print(game[0])
        print(game[1])
        print(game[2])


    print("Game over")


play_the_game(game)
