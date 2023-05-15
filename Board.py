from Player import Adversaire

class Board:
    def __init__(self, board = None):
        if board is None:
            self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.board = board
        self.winner = 0

    def __str__(self):
        out = []
        for i in range(9):
            if (i%3 == 0) : out += "\n"
            
            if (self.board[i]==0) :     out += ' '
            elif (self.board[i]==1) :   out += 'X'
            else :                      out += 'O'
        return (" | ".join(out)+' | ')

    # Trie les combinaisons potentiellement gagnant et retroune :
    #   +1pt pour chaque jeton potentiellement gagnant
    #   +3pt pour chaque pair potentiellement gagnant (ratio x3 jeton pour pousser à jouer un 2eme coups)
    #   +9pt pour chaque trio gagnant (ratio trouvé de façon itérative)
    # Une combinaison est considéré potentiellement gagant si : 
    #   -tout est élement sont compris dans l'un des winning_trio de winning_combinaison
    #   -ET si les autres cases du winning_trio sont vides
    def Evaluate(self, joueur):
        cpt = 0
        joueur = int(joueur)
        for trio in SetJoueur(self.board, joueur, n=3):
            for winning in winning_combination:
                if trio[0] in winning and trio[1] in winning and trio[2] in winning:
                    cpt += 9

        for pair in SetJoueur(self.board, joueur, n=2):
            for trio in winning_combination:
                #if (chaque element de pair dans trio) AND le troisème element du trio vide
                if pair[0] in trio and pair[1] in trio and self.board[trio[0]] * self.board[trio[1]] * self.board[trio[2]] == 0 :
                    cpt += 3
    
        for jeton in SetJoueur(self.board, joueur, n=1):
            for trio in winning_combination:
                #if (jeton dans trio) AND (les 2 autres elements de trio vide)
                if jeton in trio and ( 
                        self.board[trio[0]] + self.board[trio[1]] == 0 or
                        self.board[trio[0]] + self.board[trio[2]] == 0 or
                        self.board[trio[1]] + self.board[trio[2]] == 0 ):
                    cpt += 1 
        return cpt 
    
    # Verifie si la partie est fini et met à jour Boar.winner
    def TerminalTest(self):
        #retourne le gagnant si il existe
        for i in winning_combination:
            if i in SetJoueur(self.board, joueur = 1, n = 3):
                self.winner = 1
                return 1
            elif i in SetJoueur(self.board, joueur = 2, n = 3):
                self.winner = 2
                return 2

        #retourne -1 il c'est un match null
        if all(case != 0 for case in self.board):
            return -1
        
        #retourne 0 si la partie est encore en cours
        return 0
    
    # Fait une list de tout les mouvements possible
    def PossibleMove(self):
        return [idx for idx in range(9) if self.board[idx] == 0]
    

# Récupère la liste de tout les jetons du joueur placé en parametre
# Renvoie toutes les combinaisons possible de n-éléments de cette liste
def SetJoueur(board, joueur, n = 3):
    # recupère les position de tout les jeton du joueur
    idx = [i for i in range(9) if board[i] == joueur]

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

# Calcul de l'interet à joueur sur une case des cases du board
# Fonction mise en dehors du boar pour éviter toute moification du véritable board
# Initialisé à False car la dernière étapes est différentes et se fait dans le Board.IAPlay
def Minmax(game : Board, alpha, beta, joueur, maximazing = False):
    # Retourne l'évaluation du jeu du joueur à la fin du minmax  
    if game.TerminalTest != 0:
        return game.Evaluate(joueur)
    
    if maximazing:
        best_score  = float('-inf')
        for move in game.PossibleMove():
            game.board[move] = joueur
            score = Minmax(game, alpha, beta, joueur, False) 
            best_score = max(best_score,score)
            alpha = max(alpha,best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score=float('inf')
        for move in game.PossibleMove():
            game.board[move] = Adversaire(joueur)
            score = Minmax(game, alpha, beta, joueur, True)
            best_score = min(best_score,score)
            beta = min(beta,best_score)
            if beta<=alpha:
                break
        return best_score

# Renvoie le mouvement choisi par le joueur si c'est une IA
def AIPlay(game : Board, joueur):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    temp_board = game
    
    for move in temp_board.PossibleMove():
        temp_board.board[move] = joueur
        score = Minmax(temp_board, alpha, beta, joueur)
        best_score = max(best_score,score)
        beta = max(beta,best_score)
        if score == best_score:
            best_move = move
        if beta<=alpha:
            break
    return best_move

# Demande le prochain mouvement à un joueur Humain
def HumanPlay(game : Board):
    move = int(input("Poser un jeton : "))
    while move not in game.PossibleMove():
        move = int(input("Donner une case encore vierge : "))
    return move

# Liste de toutes les combinaisons gagnantes rangé par ordre croissant
winning_combination = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6))