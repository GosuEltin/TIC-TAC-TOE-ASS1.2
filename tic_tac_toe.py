# Tic-Tac-Toe game in Python (console-based)

def draw_board(board):
    """Draws the Tic-Tac-Toe board."""
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(f"{idx} {' '.join(row)}")


def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    """Main function to play the game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Tic-Tac-Toe Game")
    print("Player 1: X | Player 2: O")
    
    while True:
        draw_board(board)
        print(f"Player {current_player}'s turn.")

        try:
            row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid coordinates. Try again.")
                continue
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
            board[row][col] = current_player
        except ValueError:
            print("Invalid input. Enter two numbers separated by space.")
            continue

        if check_winner(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            draw_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
