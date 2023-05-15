import Board
from Player import Adversaire

class UltimateBoard:
    def __init__(self):
        self.list = [Board.Board() for i in range(9)]
        self.ulti_board = Board.Board()
        
    def __str__(self):
        out = ""
        for i in range(0, 9, 3):
            if i % 3 == 0:
                out += " --------------------------------------------"
            rows = [str(ub).split("\n") for ub in self.list[i:i+3]]
            for j in range(len(rows[0])):
                out += "-".join([row[j] for row in rows])
                out += "\n"
        return out
    
    def Get(self, board, move = -1):
        if move == -1:
            return self.list[board].board
        else :
            return self.list[board].board[move]
    
    def Set(self, input, board, move = -1):
        if move == -1:
            self.list[board].board = input
        else :
            self.list[board].board[move] = input
    
    def TerminalTest(self):
        for i in range(9):
            self.ulti_board.board[i] = self.list[i].TerminalTest()
        return self.ulti_board.TerminalTest()
    
    def Evaluate(self,joueur):
        cpt = 0
        for board in self.list:
            cpt += board.Evaluate(joueur)
        cpt += self.ulti_board.Evaluate(joueur) * 9
        return cpt

# Se deporte sur le board concerné et applique lui MinMaxBoard au board joué
# Lorsque l'on est Max et qu'un jeton est placé, il calcul le Min uniquement sur la board où il est renvoyé (et inversement pour Min)
# Maximazing est False car la dernière etapes est différente et se fait donc dans IAPlay
def Deported(game : UltimateBoard, board : int, alpha, beta, joueur, maximazing = False) -> float:
    # Retourne l'évaluation du jeu du joueur à la fin du minmax    
    if game.TerminalTest() != 0:
        return game.Evaluate(joueur)
    
    # si personne n'a encore gagner le board, le board est encore active
    if game.list[board].winner == 0:
        return Minmax(game, board, alpha, beta, joueur, maximazing)
    
    # sinon prendre en compte les differents board active dans l'arborescence minmax
    # on ne change pas le maximazing car c'est un prolongement de l'étape en cours
    actif_board = list(filter(lambda idxBoard : game.list[idxBoard].winner == 0, range(9)))
    if maximazing:
        for board in actif_board:
            best_score = float('-inf')
            score = Minmax(game, board, alpha, beta, joueur, maximazing)
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    else :
        for board in actif_board:
            best_score = float('inf')
            score = Minmax(game, board, alpha, beta, joueur, maximazing)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta <= alpha:
                break
        return best_score

# Version alternative de Board.Minmax en remplacant "game.board" par "game.list[idxBoard]"
# Mais l'indice du jeton posé (idx) remplace l'indice de la porchaine board (idxBoard)
def Minmax(game : UltimateBoard, board : int, alpha, beta, joueur, maximazing) -> float:
    possible_move = list(filter(lambda idx : game.Get(board,idx) == 0, range(9))) #indexe possible
    if maximazing:
        best_score  = float('-inf')
        for move in possible_move:
            game.Set(joueur, board, move)
            score = Deported(game, move, alpha, beta, joueur, False) 
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    
    else:
        best_score=float('inf')
        for move in possible_move:
            game.Set(Adversaire(joueur), board, move)
            score = Deported(game, move, alpha, beta, joueur, True)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta<=alpha:
                break
        return best_score
    
def AIPlay(game : UltimateBoard, board : int, joueur):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    # si la board est active, on y applique le Minmax
    if board != -1 and game.list[board].winner == 0:
        possible_moves = list(filter(lambda move : game.Get(board, move) == 0, range(9)))
        for move in possible_moves:
            game.Set(joueur, board, move)
            score = Deported(game, board, alpha, beta, joueur)
            best_score = max(best_score,int(score))
            beta = max(beta,best_score)
            if score == best_score:
                best_move = move
            if beta<=alpha:
                break
        return (board, best_move)

    # else le board n'est plus actif donc applique le minmax à tout les board actif
    actif_board = list(filter(lambda idx : game.list[idx].winner == 0, range(9)))
    for board in actif_board:
        possible_moves = list(filter(lambda move : game.Get(board, move) == 0, range(9)))
        for move in possible_moves:
            game.Set(joueur, board, move)
            score = Deported(game, board, alpha, beta, joueur)
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if score == best_score:
                best_board = board
                best_move = move
            if beta <= alpha:
                break
    return (best_board, best_move)

def HumainPlay(game : UltimateBoard, board : int):
    # si la board renvoyer est active
    if game.Get(board) == 0 :
        print("Vous êtes board n°", board)

    # sinon    
    actif_board = list(filter(lambda idx : game.list[idx].winner == 0, range(9)))
    while board not in actif_board:
        board = int(input("La board n°", board, " est inactive veuillez rentrer une autre board"))
    move = Board.HumanPlay(game.Get(board))
    return (board, move ) 