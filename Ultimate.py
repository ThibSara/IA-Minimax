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
    
    def TerminalTest(self):
        for i in range(9):
            self.ulti_board[i] = self.list[i].TerminalTest
        return self.ulti_board.TerminalTest
    
    def Evaluate(self,joueur):
        cpt = 0
        for board in self.list:
            cpt += board.Evaluate(joueur)
        cpt += self.ulti_board.Evaluate(joueur) * 9

# Applique le MinMaxBoard au board joué (indiqué par idxBoard)
# Lorsque l'on est Max et qu'un jeton est placé, il calcul le Min uniquement sur la board où il est renvoyé (et inversement pour Min)
# Maximazing est False car la dernière etapes est différente et se fait donc dans IAPlay
def Minmax(game : UltimateBoard, idxboard : int, alpha, beta, joueur, maximazing = False):
    # Retourne l'évaluation du jeu du joueur à la fin du minmax    
    if game.TerminalTest != 0:
        return game.Evaluate(joueur)
    
    # si personne n'a encore gagner le board, le board est encore active
    if game.list[idxboard].winner == 0:
        return MinmaxBoard(game, idxboard, alpha, beta, joueur, maximazing)
    
    # sinon prendre en compte les differents board active dans l'arborescence minmax
    actif_board = filter(lambda idx : game.list[idx].winner == 0, range(9))
    if maximazing:
        for idxboard in actif_board:
            score = MinmaxBoard(game, idxboard, alpha, beta, joueur, True)
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    else :
        for idxboard in actif_board:
            score = MinmaxBoard(game, idxboard, alpha, beta, joueur, False)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta <= alpha:
                break
        return best_score

# Version alternative de Board.Minmax en remplacant "game.board" par "game.list[idxBoard]"
# Mais l'indice du jeton posé (idx) remplace l'indice de la porchaine board (idxBoard)
def MinmaxBoard(game : UltimateBoard, idxBoard : int, alpha, beta, joueur, maximazing):
    possible_move = filter(lambda idx : game.list[idxBoard][idx] == 0, range(9)) #indexe possible
    if maximazing:
        best_score  = float('-inf')
        for move in possible_move:
            game.list[idxBoard][move] = joueur
            score = Minmax(game, move, alpha, beta, joueur, False) 
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    
    else:
        best_score=float('inf')
        for move in possible_move:
            game.list[idxBoard][move] = Adversaire(joueur)
            score = Minmax(game, move, alpha, beta, joueur, True)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta<=alpha:
                break
        return best_score
    
def AIPlay(game : UltimateBoard, idxBoard : int, joueur):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    # si la board est active, on y applique le Minmax
    if idxBoard != -1 and game.list[idxBoard].winner == 0:
        possible_moves = filter(lambda move : game.list[idxBoard][move] == 0, range(9)) 
        for move in possible_moves:
            game.list[idxBoard][move] = joueur
            score = Minmax(game, idxBoard, alpha, beta, joueur)
            best_score = max(best_score,score)
            beta = max(beta,best_score)
            if score == best_score:
                best_move = move
            if beta<=alpha:
                break
        return best_move

    # else le board n'est plus actif donc applique le minmax à tout les board actif
    actif_board = filter(lambda idx : game.list[idx].winner == 0, range(9))
    for idxboard in actif_board:
        score = Minmax(game, idxboard, alpha, beta, joueur)
        best_score = max(best_score,score)
        alpha = max(alpha,best_score)
        if score == best_score:
                best_move = move
        if beta <= alpha:
            break
    return best_move

def HumainPlay(game : UltimateBoard, idxBoard : int):
    # si la board renvoyer est active
    if game.list[idxBoard] == 0 :
        print("Vous êtes board n°", idxBoard)

    # sinon    
    actif_board = filter(lambda idx : game.list[idx].winner == 0, range(9))
    while idxBoard not in actif_board:
        idxBoard = int(input("La board n°", idxBoard, " est inactive veuillez rentrer une autre board"))
    return Board.HumanPlay(game.list[idxBoard]) 