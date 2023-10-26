
# Function to create a board of a given size
def create_board(board_size):
    return [[' ' for _ in range(board_size)] for _ in range(board_size)]

# Function to display the game board
def display_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * (4 * len(board) - 1))

# Function to handle player input and undo/redo
def take_player_input(board, player_symbol, game_history, current_turn):
    while True:
        move = input(f"Player {player_symbol}, enter your move (e.g., 'A1', 'B2', 'undo', 'redo'): ").lower()

        if move == 'undo' and current_turn > 0:
            # Undo the last move.
            current_turn -= 1
            board[:] = game_history[current_turn]  # Restore the previous board state.
            display_board(board)
        elif move == 'redo' and current_turn < len(game_history) - 1:
            # Redo the next move.
            current_turn += 1
            board[:] = game_history[current_turn]  # Restore the next board state.
            display_board(board)
        else:
            # Validate the move format and check if the chosen cell is empty
            if len(move) != 2:
                print("Invalid format! Please follow this example: A1 or B3.")
                continue

            row, col = ord(move[0]) - ord('a'), int(move[1]) - 1  # Convert input to row and column indices.

            if row < 0 or row >= len(board) or col < 0 or col >= len(board) or board[row][col] != ' ':
                print("This position is either out of bounds or already occupied! Choose another one.")
                continue

            # If the move is valid, update the board, the game history, and exit the loop.
            board[row][col] = player_symbol
            game_history.append([row[:] for row in board])  # Append a copy of the current board.
            current_turn = len(game_history) - 1  # Update the current turn.
            break

    return board, game_history, current_turn

# Function to check for a win or a tie
def check_game_result(board, num_to_win):
    def check_for_win(player_symbol):
        # Check rows for a win.
        for i in range(len(board)):
            for j in range(len(board) - num_to_win + 1):
                if all(board[i][k] == player_symbol for k in range(j, j + num_to_win)):
                    return True

        # Check columns for a win.
        for i in range(len(board) - num_to_win + 1):
            for j in range(len(board)):
                if all(board[k][j] == player_symbol for k in range(i, i + num_to_win)):
                    return True

        # Check diagonals.
        for i in range(len(board) - num_to_win + 1):
            for j in range(num_to_win - 1, len(board)):
                if all(board[i + k][j - k] == player_symbol for k in range(num_to_win)):
                    return True

        for i in range(len(board) - num_to_win + 1):
            for j in range(len(board) - num_to_win + 1):
                if all(board[i + k][j + k] == player_symbol for k in range(num_to_win)):
                    return True

        return False

    # Check for a win or a tie.
    for player in ['X', 'O']:
        if check_for_win(player):
            return f"Player {player} wins!"

    # Check for a tie.
    if all(all(cell != ' ' for cell in row) for row in board):
        return "It's a tie!"

    return "Game in progress..."

# Main function to run the game
def main():
    print("Welcome to Tic-Tac-Toe!")

    while True:
        board_size = int(input("Choose the board size (e.g., 3 for 3x3, 4 for 4x4): "))
        num_to_win = int(input("Enter the number of symbols in a row required to win: "))

        # Initialize the game board based on the chosen size.
        board = create_board(board_size)

        # Initialize player symbols.
        current_player = 'X'
        game_history = [board]  # Initialize with the initial board.
        current_turn = 0  # Keeps track of the current turn.

        while True:
            # Display the current state of the board.
            display_board(board)

            # Take the current player's input and update the board.
            board, game_history, current_turn = take_player_input(board, current_player, game_history, current_turn)

            # Check for a game result with the specified number to win.
            result = check_game_result(board, num_to_win)

            if result != "Game in progress...":
                display_board(board)
                print(result)
                break

            # Switch players for the next turn.
            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
