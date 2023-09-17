board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
game = True
def check_win():
    # Überprüfe Zeilen
    for row in range(1, 10, 3):
        if board[str(row)] == board[str(row + 1)] == board[str(row + 2)]:
            return board[str(row)]
    # Überprüfe Spalten
    for col in range(1, 4):
        if board[str(col)] == board[str(col + 3)] == board[str(col + 6)]:
            return board[str(col)]
    # Überprüfe Diagonalen
    if board['1'] == board['5'] == board['9']:
        return board['1']
    if board['3'] == board['5'] == board['7']:
        return board['3']
    # Kein Gewinner
    return None
def print_board():
    print(f' {board["1"]} | {board["2"]} | {board["3"]} ')
    print('---------')
    print(f' {board["4"]} | {board["5"]} | {board["6"]} ')
    print('---------')
    print(f' {board["7"]} | {board["8"]} | {board["9"]} ')
while game == True:
    print_board()
    order = input("Welches Feld?")
    if order in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if board[order] not in ['x', 'o']:
            board[order] = "x"
            winner = check_win()
            if winner:
                print_board()
                print(f"{winner} hat gewonnen!")
                game = False
                break
        else:
            print("Dieses Feld ist bereits belegt. Bitte wähle ein anderes Feld.")
            continue
    else:
        print("Fehler kein richtiger Input!")
        print("NOch Mal von Vorn!")
        continue
    
    print_board()
    order = input("Welches Feld?")
    if order in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if board[order] not in ['x', 'o']:
            board[order] = "o"
            winner = check_win()
            if winner:
                print_board()
                print(f"{winner} hat gewonnen!")
                game = False
                break
        else:
            print("Dieses Feld ist bereits belegt. Bitte wähle ein anderes Feld.")
            continue
    else:
        print("Fehler kein richtiger Input!")
        print("NOch Mal von Vorn!")
        continue