import Board
import Ultimate
from Player import Adversaire
from typing import List

"""
Attention à ne pas confondre :
    UtimateBoard.list[Board] renvoie la class Board
    UltimateBoard.Get(Board) renvoie une List[int] avec tt les jeton du board
"""

class UltimateBoard:
    def __init__(self, game : 'UltimateBoard' = None):
        if game is None:
            self.list = [Board.Board() for i in range(9)]
            self.ulti_board = Board.Board()
        else :
            self.list = game.list
            self.ulti_board = game.ulti_board
  
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
            self.ulti_board.board[i] = self.list[i].TerminalTest()
        return self.ulti_board.TerminalTest()
    
    def Evaluate(self,joueur):
        cpt = 0
        for board in self.list:
            cpt += board.Evaluate(joueur)
        cpt += self.ulti_board.Evaluate(joueur) * 9
        return cpt
    
    # Aléger l'écriture pour acceder aux valeurs
    def Get(self, board, move = None) :
        if move == None:
            return self.list[board].board
        else :
            return self.list[board].board[move]
    def Set(self, input, board, move = None):
        if move == None:
            self.list[board].board = input
        else :
            self.list[board].board[move] = input
    
    # Fait une list de tout les mouvements possible
    def PossibleBoard(self) -> List[Board.Board]:
        return [idx for idx in range(9) if self.list[idx].winner == 0]
    def PossibleMove(self, board : int) -> List[int]:
        return self.list[board].PossibleMove()

# Reporte le MinMax aux board où il doit s'appliquer
# Maximazing est False on commence Deported à l'étape 2 car la premère necessite un traitement différent opéré dans AIPlay
def Reported(game : 'UltimateBoard', board : 'int', alpha, beta, joueur, maximazing = False) -> float:
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
            # Fait le max des max de tout les board actifs donc on conserve maximazing
            score = Minmax(game, board, alpha, beta, joueur, maximazing)
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    else :
        for board in actif_board:
            best_score = float('inf')
            # Fait le min des min de tout les board actifs donc on conserve maximazing
            score = Minmax(game, board, alpha, beta, joueur, maximazing)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta <= alpha:
                break
        return best_score

# Version alternative de Board.Minmax qui prends en entre la board sur laquel elle s'applique
def Minmax(game : 'UltimateBoard', board : 'int', alpha, beta, joueur, maximazing) -> float:
    if maximazing:
        best_score  = float('-inf')
        for move in game.list[board].PossibleMove():
            game.Set(joueur, board, move)
            score = Reported(game, move, alpha, beta, joueur, False) 
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    
    else:
        best_score=float('inf')
        for move in game.list[board].PossibleMove():
            game.Set(Adversaire(joueur), board, move)
            score = Reported(game, move, alpha, beta, joueur, True)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta<=alpha:
                break
        return best_score
    
def AIPlay(temp : 'UltimateBoard', board : 'int', joueur):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    # si la board est active, on y applique le Minmax
    if board != -1 and temp.list[board].winner == 0:
        for move in temp.PossibleMove(board):
            temp.Set(joueur, board, move)
            score = Reported(temp, board, alpha, beta, joueur) #deported into minmax
            best_score = max(best_score,score)
            beta = max(beta,best_score)
            if score == best_score:
                best_move = move
            if beta<=alpha:
                break
        return (board, best_move)

    # else le board n'est plus actif donc applique le minmax à tout les board actif
    for board in temp.PossibleBoard():
        for move in temp.PossibleMove(board) :
            temp.Set(joueur, board, move)
            score = Reported(temp, board, alpha, beta, joueur)
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if score == best_score:
                best_board = board
                best_move = move
            if beta <= alpha:
                break
    return (best_board, best_move)

def HumainPlay(game : 'UltimateBoard', board : 'int'):
    # si c'est le premier tour et qu'il n'y a pas de board
    if board == -1 :
        while board < 0 or board >= 9:
            board = int(input("Entrez sur quel board commencer : "))
    
    # si la board renvoyer est active
    elif game.list[board].winner == 0 :
        print("Vous êtes board n°" + str(board))

    # si la board est inactive
    else :
        while board not in game.PossibleBoard():
            board = int(input("La board n°" + str(board) + " est inactive\nVEntrer une autre board : "))
    
    move = Board.HumanPlay(game.list[board])
    return (board, move)