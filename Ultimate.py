import Board

# Définition de la classe UltimateBoard

class UltimateBoard:
    def __init__(self):
        self.board_list = [Board() for i in range(9)]
        self.ulti_board = Board()
        
    def __str__(self):
        for i in range(0, 9, 3):
            if i % 3 == 0:
                print(" ----------------------------------------------")
            rows = [str(ub).split("\n") for ub in self.board_list[i:i+3]]
            for j in range(len(rows[0])):
                row_str = "-".join([row[j] for row in rows])
                print(row_str)
    
    def CheckUltimate(self):
        for i in range(9):
            self.ulti_board[i] = self.board_list[i].winner


def Minimax(game, alpha, beta, joueur, isPlaying = True):
    #retourne la valeur de la grille si la partie est finie
    if game.ulti_board.TerminalTest != 0:
        return (game.board.Evaluate(), -1)
    
    if isPlaying:
        best_score  = float('-inf')
        for i in range(9):
            if game.board[i] == 0:
                game.board[i] = joueur
                (score,idx) = game.Minimax(game, alpha, beta, joueur, False)
                best_score = max(score,best_score)
                alpha = max(alpha,best_score)
                if beta <= alpha:
                    break
        return (best_score,i)   #juste besoin du dernier idx pour savoir où jouer

    else:
        best_score=float('inf')
        for i in range(9):
            if game.board[i] == 0:
                game.board[i] = Board.Adversaire(joueur)
                (score,idx) = game.Minimax(game, alpha, beta, joueur, True)
                best_score = min(score, best_score)
                beta = min(beta,best_score)
                if beta<=alpha:
                    break
        return (best_score,i)


