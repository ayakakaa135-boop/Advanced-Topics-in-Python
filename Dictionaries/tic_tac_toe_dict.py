from colorama import Fore, Style

# ===== Constants =====
PLAYER_X = 'X'
PLAYER_O = 'O'
WIN_COMBOS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# ===== Functions =====
def printBoard(board):
    print(f"\n {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} \n")

def resetBoard():
    return {i: str(i) for i in range(1, 10)}

def checkWin(board, symbol):
    return any(all(board[pos] == symbol for pos in combo) for combo in WIN_COMBOS)

def game(players_data):
    board = resetBoard()
    printBoard(board)
    turn = PLAYER_X

    for _ in range(9):
        player = players_data[turn]
        move = input(f"{player['color']}{player['name']} ({turn}) choose position (1-9): {Style.RESET_ALL}")

        if not move.isdigit() or int(move) not in range(1, 10):
            print(Fore.YELLOW + "❌ Invalid input. Enter number 1–9." + Style.RESET_ALL)
            continue

        move = int(move)
        if board[move] in [PLAYER_X, PLAYER_O]:
            print(Fore.RED + "⚠️ Spot already taken!" + Style.RESET_ALL)
            continue

        board[move] = turn
        printBoard(board)

        if checkWin(board, turn):
            print(player['color'] + f"🏆 {player['name']} wins!" + Style.RESET_ALL)
            break

        turn = PLAYER_O if turn == PLAYER_X else PLAYER_X  # ternary switch

    else:
        print(Fore.CYAN + "🤝 It's a draw!" + Style.RESET_ALL)


# ===== Main =====
if __name__ == "__main__":
    p1_name = input("Enter Player 1 name: ")
    p2_name = input("Enter Player 2 name: ")

    players_data = {
        PLAYER_X: {'name': p1_name, 'color': Fore.GREEN},
        PLAYER_O: {'name': p2_name, 'color': Fore.RED}
    }

    while True:
        game(players_data)
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print(Fore.MAGENTA + "👋 Thanks for playing!" + Style.RESET_ALL)
            break
