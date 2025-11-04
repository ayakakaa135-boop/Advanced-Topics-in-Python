theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

def printBoard(board):
    print()
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print()

def game():
    turn = 'X'
    count = 0

    for i in range(9):
        printBoard(theBoard)
        move = input(f"Player {turn}, choose a position (1-9): ")


        if move not in theBoard:
            print("Invalid move, try again.")
            continue


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already taken!")
            continue


        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or \
               theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or \
               theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ' or \
               theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ' or \
               theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ' or \
               theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ' or \
               theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or \
               theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print(f" Player {turn} wins! ")
                break


        if count == 9:
            printBoard(theBoard)
            print("It's a tie!")
            break

        # تبديل الدور
        turn = 'O' if turn == 'X' else 'X'

if __name__ == "__main__":
    game()
