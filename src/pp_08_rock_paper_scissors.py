moves = ["rock", "paper", "scissors"]

## For version 1
results_paper = {
    'paper': 'even',
    'rock': 'paper',
    'scissors' : 'scissors'
}

results_rock = {
    'paper': 'paper',
    'rock': 'even',
    'scissors' : 'rock'
}

results_scissors = {
    'paper': 'scissors',
    'rock': 'rock',
    'scissors' : 'even'
}

results = {
    'paper' : results_paper,
    'rock' : results_rock,
    'scissors' : results_scissors
}
##

def validate_move(move: str) -> bool:
    """user input validation

    Args:
        move (str): user input

    Returns:
        bool: validation
    """
    if move in moves:
        return True

    return False


def play_game(player1: str, player2: str) -> bool:
    """
    logic for rock-paper-scissors game

    Args:
        player1 (str): move of player 1
        player2 (str): move of player 2

    print(:)
        str: win/even statement

    Returns:
        bool: validation
    """
    validate_player1 = validate_move(player1)
    validate_player2 = validate_move(player2)

    if not validate_player1 or not validate_player2:
        print("moves can be only: rock, scissors, paper")
        return False

    # version 1 with dictionary matrices

    result = results[player1][player2]
    winner = None

    if result == "even":
        print("game is even, start again")
        return False

    if result == player1:
        winner = "Player 1"
    elif result == player2:
        winner = "Player 2"

    print("Stronger is {result}. {winner} is the winner".format(result=result, winner=winner))
    return True

    # version 2 with explicit conditions

    # if player1 == player2:
    #     print("game is even, start again")
    #     return False

    # if player1 == "rock" and player2 == "paper":
    #     print("paper beats rock, player 2 won")
    # elif player1 == "paper" and player2 == "rock":
    #     print("paper beats rock, player 1 won")
    # elif player1 == "paper" and player2 == "scissors":
    #     print("scissors cuts paper, player 2 won")
    # elif player1 == "scissors" and player2 == "paper":
    #     print("scissors cuts paper, player 1 won")
    # elif player1 == "rock" and player2 == "scissors":
    #     print("rock blunts scissors, player 1 won")
    # elif player1 == "scissors" and player2 == "rock":
    #     print("rock blunts scissors, player 2 won")

    # return True


def run_game():
    """
    starter of the rock-scissors-paper game
    """
    while True:
        player_1 = input("Player 1: Give me rock, paper or scissors: ")
        player_2 = input("Player 2: Give me rock, paper or scissors: ")
        game_status = play_game(player_1.lower(), player_2.lower())
        if game_status is False:
            continue

        continue_game = input("Do you want to continue? ")
        if continue_game.lower() == "no":
            break

    print("I hope you enjoyed your game.")

run_game()
