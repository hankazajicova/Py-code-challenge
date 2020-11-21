from pp_26_check_tic_tac_toe import get_winner

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
    current_player = PLAYER_1
    while True:
        if number_of_moves >= 9:
            break

        print("Make your move as row number,column number")
        player_input = input(f"Player {current_player}, you are on - row/column: ")
        players_move = player_move(player_input)

        if board[players_move['row']][players_move['column']] == 0:
            board[players_move['row']][players_move['column']] = current_player
            number_of_moves += 1

        print(game[0])
        print(game[1])
        print(game[2])

        if get_winner(game) != 0:
            break

        if current_player == PLAYER_1:
            current_player = PLAYER_2
        else:
            current_player = PLAYER_1

    print("Game over")


play_the_game(game)
