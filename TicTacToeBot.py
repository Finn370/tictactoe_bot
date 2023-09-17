board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
game = True

def check_win(board):
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

    # Überprüfe auf Unentschieden
    if all(value in ['x', 'o'] for value in board.values()):
        return "Niemand"

    # Kein Gewinner
    return None

# Macht das Spielfeld
def print_board():
    print(f' {board["1"]} | {board["2"]} | {board["3"]} ')
    print('----------')
    print(f' {board["4"]} | {board["5"]} | {board["6"]} ')
    print('----------')
    print(f' {board["7"]} | {board["8"]} | {board["9"]} ')

def minimax(position, depth, maximizing_player):
    if depth == 0 or check_win(position):
        return evaluate(position)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(position):
            new_position = make_move(position, move, 'o')
            eval = minimax(new_position, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(position):
            new_position = make_move(position, move, 'x')
            eval = minimax(new_position, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def evaluate(position):
    winner = check_win(position)
    if winner == 'o':
        return 1
    elif winner == 'x':
        return -1
    else:
        return 0

def get_possible_moves(position):
    return [key for key, value in position.items() if value not in ['x', 'o']]

def make_move(position, move, player):
    new_position = position.copy()
    new_position[move] = player
    return new_position

# Spieler nimmt seinen Zug
while game == True:
    print_board()
    order = input("Welches Feld?")
    if order in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if board[order] not in ['x', 'o']:
            board[order] = "x"
            winner = check_win(board)
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
        print("Nochmal von Vorn!")
        continue
    
    # Computer macht seinen Zug mit Minimax-Algorithmus
    best_score = float('-inf')
    best_move = None
    for key in board.keys():
        if board[key] not in ['x', 'o']:
            board[key] = "o"
            score = minimax(board, 5, False)
            board[key] = key
            if score > best_score:
                best_score = score
                best_move = key
    if best_move:
        board[best_move] = "o"
    
    # Gewinner wird angezeigt
    winner = check_win(board)
    if winner:
        print_board()
        print(f"{winner} hat gewonnen!")
        game = False
        if input("Nochmal? Ja (j), Nein (n)") == "j":
            board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
            game = True

input("Drücke irgeneine Taste zum beenden")