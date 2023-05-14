import random

# Définition de la classe Board



# liste des tuples de toutes les combinaisons gagnantes rangé par ordre croissant
winning_combination = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6))

class Board:
    #definition d'un tableau de tic tac toe
    def __init__(self, board = None):
        if board is None:
            self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.board = board
        self.winner = 0

    # impression du tableau du tic tac toe
    def __str__ (self):
        out = []
        for i in range(9):
            if (i%3 == 0) : out += "\n"
        # on remplace les valeurs du tableau par des X et des O pour un effet visuel
            if (self.board[i]==0):
                out += ' '
            elif (self.board[i]==1):
                out+='X'
            else:
                out+='O'
        return (" | ".join(out)+' | ')

    # retour le nombre de nombre de pair et singleton potentiellement gagnant
    # pair vaut 3 fois plus que singleton pour pousser à jouer au deuxième coups
    def Evaluate(self, joueur):
        cpt = 0
        # utile pour la fonction evaluate, score à changer
        for trio in self.SetJoueur(joueur, n=3):
            for winning in winning_combination:
                if trio[0] in winning and trio[1] in winning and trio[2] in winning:
                    cpt += 9

        for pair in self.SetJoueur(joueur, n=2):
            for trio in winning_combination:
                #if (element de pair dans trio AND le troisème element de trio vide) : cpt +=3
                if pair[0] in trio and pair[1] in trio and self.board[trio[0]] * self.board[trio[1]] * self.board[trio[2]] == 0 :
                    #print(str(pair)+" in "+ str(trio))
                    cpt += 3
    
        for elem in self.SetJoueur(joueur, n=1):
            for trio in winning_combination:
                #if (singleton dans trio AND les 2 autres elements de trio vide) : cpt +=1
                if elem in trio and ( 
                        self.board[trio[0]] + self.board[trio[1]] == 0 or
                        self.board[trio[0]] + self.board[trio[2]] == 0 or
                        self.board[trio[1]] + self.board[trio[2]] == 0 ):
                    #print(str(elem)+" in "+ str(trio))
                    cpt += 1 
        return cpt 

    def TerminalTest(self):
        for i in winning_combination:
            if i in self.SetJoueur(1, 3):
                self.winner = 1
                return 1
            elif i in self.SetJoueur(2, 3):
                self.winner = 2
                return 2
        return 0

    # crée une liste de toutes les combinaison du joueur de n combinaisons
    def SetJoueur(self, joueur, n = 3):
        # recupère les position de tout les jeton du joueur
        idx = [i for i in range(9) if self.board[i] == joueur]
    
        # si le joueur n'a pas posé assez de combinaisons pour pouvoir gagner
        if len(idx) < n: 
            return ()       
    
        # cree un tuple pour tout les set d'indexe possible
        out = []
        if n == 3:
            for i in range(len(idx)-2):
                for j in range(1,len(idx)-i-1):
                    out.append((idx[i], idx[i+j], idx[i+j+1]))
        elif n == 2:
            for i in range(len(idx)-1):
                for j in range(1,len(idx)-i):
                    out.append((idx[i], idx[i+j]))
        else:
            out = idx
        return tuple(out)
    
      

# Pas dans class pour ne pas modifier le réel board
def Minimax(game, alpha, beta, joueur, isPlaying = True):
    #retourne la valeur de la grille si la partie est finie
    if game.TerminalTest != 0:
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
                game.board[i] = Adversaire(joueur)
                (score,idx) = game.Minimax(game, alpha, beta, joueur, True)
                best_score = min(score, best_score)
                beta = min(beta,best_score)
                if beta<=alpha:
                    break
        return (best_score,i)
    
def Adversaire(joueur):
    if joueur == 1:
        return 2
    return 1
