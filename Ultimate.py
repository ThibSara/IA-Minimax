from Board import Board, Adversaire

class UltimateBoard:
    def __init__(self):
        self.list = [Board() for i in range(9)]
        self.ulti_board = Board()
        
    def __str__(self):
        for i in range(0, 9, 3):
            if i % 3 == 0:
                print(" ----------------------------------------------")
            rows = [str(ub).split("\n") for ub in self.list[i:i+3]]
            for j in range(len(rows[0])):
                row_str = "-".join([row[j] for row in rows])
                print(row_str)
    
    def TerminalTest(self):
        for i in range(9):
            self.ulti_board[i] = self.list[i].TerminalTest
        return self.ulti_board.TerminalTest

# Applique le MinMaxBoard au board joué (indiqué par idxBoard)
# Lorsque l'on est Max et qu'un jeton est placé, il calcul le Min uniquement sur la board où il est renvoyé (et inversement pour Min)
def Minmax(game : UltimateBoard, idxboard : int, alpha, beta, joueur, isPlaying = True):
    #retourne la valeur de la grille si la partie est finie    
    if game.TerminalTest != 0:
        return game.list[idxboard].Evaluate(game.ulti_board.winner)
    
    # si personne n'a encore gagner le board, le board est encore active
    if game.list[idxboard].winner == 0:
        board = game.list[idxboard]
        return MinmaxBoard(board, alpha, beta, joueur, isPlaying)
    
    # sinon prendre en compte les differents board active dans l'arborescence minmax
    elif isPlaying:
        for idx in range(9):
            if game.list[idx].winner == 0:
                score = MinmaxBoard(game, idx, alpha, beta, joueur, True)
                best_score = max(best_score,score)
                alpha = max(alpha,best_score)
                if beta <= alpha:
                    break       #possible erreur : est ce que le break stop bien le for 
        return best_score
    else :
        for idx in range(9):
            if game.list[idx].winner == 0:
                score = MinmaxBoard(game, idx, alpha, beta, joueur, False)
                best_score = min(best_score,score)
                beta = min(beta,best_score)
                if beta <= alpha:
                    break
        return best_score

# Version alternative de Board.Minmax en remplacant "game.board" par "game.list[idxBoard]"
# Mais l'indice du jeton posé (idx) remplace l'indice de la porchaine board (idxBoard)
def MinmaxBoard(game : UltimateBoard, idxBoard : int, alpha, beta, joueur, isPlaying):
    if isPlaying:
        best_score  = float('-inf')
        for idx in range(9):
            if game.list[idxBoard][idx] == 0:
                game.list[idxBoard][idx] = joueur
                score = Minmax(game, idx, alpha, beta, joueur, False) 
                best_score = max(best_score,score)
                alpha = max(alpha,best_score)
                if beta <= alpha:
                    break
        return best_score
    
    else:
        best_score=float('inf')
        for idx in range(9):
            if game.list[idxBoard][idx] == 0:
                game.list[idxBoard][idx] = Adversaire(joueur)
                score = Minmax(game, idx, alpha, beta, joueur, True)
                best_score = min(best_score,score)
                beta = min(beta,best_score)
                if beta<=alpha:
                    break
        return best_score