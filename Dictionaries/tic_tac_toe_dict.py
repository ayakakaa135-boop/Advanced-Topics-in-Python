from colorama import Fore, Style, init

init(autoreset=True)


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    print()
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print()


def resetBoard():
    for key in theBoard:
        theBoard[key] = ' '


def game(player1, player2):
    turn = 'X'
    count = 0
    current_player = player1

    for _ in range(9):
        printBoard(theBoard)
        print(f"{Fore.CYAN}{current_player} ({turn}){Style.RESET_ALL}, it's your turn.")
        move = input("Choose position (1–9): ").strip()

        if move not in theBoard:
            print("❌ Invalid move. Choose between 1–9.")
            continue

        if theBoard[move] == ' ':
            if turn == 'X':
                theBoard[move] = Fore.GREEN + 'X' + Style.RESET_ALL
            else:
                theBoard[move] = Fore.RED + 'O' + Style.RESET_ALL
            count += 1
        else:
            print(" That place is already filled. Try again.")
            continue


        if count >= 5:
            combos = [
                ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],
                ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],
                ['7', '5', '3'], ['1', '5', '9']
            ]
            for line in combos:
                if theBoard[line[0]] == theBoard[line[1]] == theBoard[line[2]] != ' ':
                    printBoard(theBoard)
                    print(f"\n Game Over — {Fore.YELLOW}{current_player}{Style.RESET_ALL} wins! \n")
                    return

        if count == 9:
            printBoard(theBoard)
            print("\n  Game Over — It's a Tie!\n")
            return


        if turn == 'X':
            turn = 'O'
            current_player = player2
        else:
            turn = 'X'
            current_player = player1


if __name__ == "__main__":
    print("🎮 Welcome to Tic-Tac-Toe!\n")
    player1 = input("Enter name for Player 1 (X): ").strip() or "Player 1"
    player2 = input("Enter name for Player 2 (O): ").strip() or "Player 2"

    while True:
        game(player1, player2)
        again = input("Play again? (y/n): ").lower()
        if again == 'y':
            resetBoard()
        else:
            print("👋 Thanks for playing!")
            break
