def printBoard(xState, yState):
    # Creating a 3x3 board
    board = [' ' for _ in range(9)]
    for i in range(9):
        if xState[i] == 1:
            board[i] = 'X'
        elif yState[i] == 1:
            board[i] = 'O'

    # Printing the board
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def checkWin(state):
    # Winning combinations
    winCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winCombos:
        if state[combo[0]] == state[combo[1]] == state[combo[2]] == 1:
            return True
    return False

def main():
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    moves = 0

    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, yState)
        if turn == 1:
            print("X's turn")
            value = int(input("Enter a position from 1 to 9: ")) - 1
            if xState[value] == 0 and yState[value] == 0:
                xState[value] = 1
                turn = 0
                moves += 1
        else:
            print("O's turn")
            value = int(input("Enter a position from 1 to 9: ")) - 1
            if xState[value] == 0 and yState[value] == 0:
                yState[value] = 1
                turn = 1
                moves += 1

        if checkWin(xState):
            printBoard(xState, yState)
            print("X wins!")
            break
        if checkWin(yState):
            printBoard(xState, yState)
            print("O wins!")
            break
        if moves == 9:
            printBoard(xState, yState)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
