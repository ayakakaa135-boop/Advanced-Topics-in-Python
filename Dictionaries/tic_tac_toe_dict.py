from colorama import Fore, Style


board = {str(i): ' ' for i in range(1, 10)}


def print_board(b):
    print()
    print(f" {b['7']} | {b['8']} | {b['9']} ")
    print("---+---+---")
    print(f" {b['4']} | {b['5']} | {b['6']} ")
    print("---+---+---")
    print(f" {b['1']} | {b['2']} | {b['3']} ")
    print()


def check_winner(b):
    winning_combos = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],
        ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],
        ['7', '5', '3'], ['1', '5', '9']
    ]
    for combo in winning_combos:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return True
    return False


def reset_board(b):
    for k in b:
        b[k] = ' '


def game():
    turn = 'X'
    count = 0

    while True:
        print_board(board)
        move = input(f"Player {Fore.GREEN + turn + Style.RESET_ALL}, choose a position (1-9): ")


        if move not in board:
            print("❌ Invalid move! Try again.")
            continue

        if board[move] != ' ':
            print(" Spot already taken, choose another.")
            continue


        board[move] = Fore.GREEN + 'X' + Style.RESET_ALL if turn == 'X' else Fore.RED + 'O' + Style.RESET_ALL
        count += 1


        if count >= 5 and check_winner(board):
            print_board(board)
            print(f" Player {turn} wins! ")
            break


        if count == 9:
            print_board(board)
            print(" It's a tie!")
            break


        turn = 'O' if turn == 'X' else 'X'


if __name__ == "__main__":
    while True:
        game()
        again = input("\nPlay again? (y/n): ").lower()
        if again == 'y':
            reset_board(board)
        else:
            print(" Thanks for playing!")
            break
