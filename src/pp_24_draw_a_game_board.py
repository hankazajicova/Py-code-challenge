HORIZONTAL = " ---"
VERTICAL = "|   "


def get_board(range_board: int) -> None:
    """
    Args:
        range_board (int): user input size
    """
    for _ in range(range_board):
        print(HORIZONTAL * range_board)
        print(VERTICAL * (range_board + 1))
    print(HORIZONTAL * range_board)


if __name__ == "__main__":
    size = int(input("Give me size of the board: "))
    get_board(size)
