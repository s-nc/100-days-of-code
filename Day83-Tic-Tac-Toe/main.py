from board import Board

game_board = Board()

n = 1
winner = False
print(game_board.board)

while not winner:

    if n % 2 == 0:
        player = 2
        symbol = "_O_"
    else:
        player = 1
        symbol = "_X_"
    move = input(f"Player {player}, please enter a co-ordinate (e.g. 11 for top left): ")

    if move[0] == '1':
        row_to_change = game_board.top
    if move[0] == '2':
        row_to_change = game_board.middle
    if move[0] == '3':
        row_to_change = game_board.bottom

    row_to_change[int(move[1])-1] = symbol

    game_board.update()

    print(game_board.board)
    winner = game_board.check_for_winner()
    if winner:
        print(f"Player {player} wins!")
        if input("Would you like to play again? Y or N: ") == "Y":
            winner = False
            n = 0
            game_board = Board()
            print(game_board.board)

    n += 1
