# -*- coding: utf-8 -*-
import random
# liste des tuples de toutes les combinaisons gagnantes rangé par ordre croissant
winning_combination = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6))

# création de la classe d'un tableau de tic tac toe
class Board:
    #definition d'un tableau de tic tac toe
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def set_board(self,x,i):
        self.board[i] = x

    # impression du tableau du tic tac toe
    def Print_Board(self):
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
         
    # vérifie si le joueur peut jouer sur la case désirée, renvoie vrai si le mvt à été effectué, faux sinon
    def Result(self,mvt):
        if self.board[mvt] == 0:
            self.board[mvt] = 1
            return True
        return False


    # vérifie si un joueur à gagné la partie
    def TerminalTest(self,joueur):
        for i in winning_combination:
            if i in self.Set_Joueur(joueur,3):
                return True
        return False


    # retour le nombre de nombre de pair et singleton potentiellement gagnant
    # pair vaut 3 fois plus que singleton pour pousser à jouer au deuxième coups
    def evaluate(self,joueur=2):
        cpt = 0
        for pair in self.Set_Joueur(joueur, n=2):
            for trio in winning_combination:
                #if (element de pair dans trio AND le troisème element de trio vide) : cpt +=3
                if pair[0] in trio and pair[1] in trio and self.board[trio[0]] * self.board[trio[1]] * self.board[trio[2]] == 0 :
                    #print(str(pair)+" in "+ str(trio))
                    cpt += 3
    
        for elem in self.Set_Joueur(joueur, n=1):
            for trio in winning_combination:
                #if (singleton dans trio AND les 2 autres elements de trio vide) : cpt +=1
                if elem in trio and ( 
                        self.board[trio[0]] + self.board[trio[1]] == 0 or
                        self.board[trio[0]] + self.board[trio[2]] == 0 or
                        self.board[trio[1]] + self.board[trio[2]] == 0 ):
                    #print(str(elem)+" in "+ str(trio))
                    cpt += 1
        return cpt 

    # crée une liste de toutes les combinaison du joueur de n combinaisons
    def Set_Joueur(self,joueur, n = 3):
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

    # fonction minimax avec elagage alpha beta
    def minimax(self,alpha,beta,is_maximizing):
        #retourne la valeur de la grille si la partie est finie
        if self.TerminalTest(0) or self.TerminalTest(1):
            return self.evaluate()
    
        #si c'est au tour de l'ordi de jouer on maximise
        if is_maximizing:
            best_score  = float('-inf')
            for i in range(9):
                if self.board[i]==0:
                    self.board[i]=2
                    score= self.minimax(alpha,beta,False)
                    self.board[i]=0
                    best_score=max(score,best_score)
                    alpha=max(alpha,best_score)
                    if beta<= alpha:
                        break
            return best_score
    
        #si c'est au tour du joueur on minimise
        else:
            best_score=float('inf')
            for i in range(9):
                if self.board[i]==0:
                    self.board[i]=1
                    score= self.minimax(alpha,beta,True)
                    self.board[i]=0
                    best_score = min(score, best_score)
                    beta=min(beta,best_score)
                    if beta<=alpha:
                        break
            return best_score
  
    #fonction pour que l'ordinateur joue le meilleur coup     
    def AiPlay(self):
        best_score=float('-inf')
        best_move=None
        alpha = float('-inf')
        beta = float('inf')
        for i in range(9):
            if self.board[i]==0:
                self.board[i]=2
                score =self.minimax(alpha,beta,False)
                self.board[i]=0
                if score>best_score:
                    best_score=score
                    best_move=i
                alpha=max(alpha,best_score)
        if best_move is not None:
            self.board[best_move]=2
            return best_move # renvoie le coup joué
        else:
        # Aucun coup possible
            return random.randint(0,8) # Ou une autre valeur spéciale
#fin des fonctions de la classe Board
 
# impression du tableau d'ultimate tic tac toe      
def print_ultimate_board(ultimate_board):
    for i in range(0, 9, 3):
        if i % 3 == 0:
            print(" ----------------------------------------------")
        rows = [ub.Print_Board().split("\n") for ub in ultimate_board[i:i+3]]
        for j in range(len(rows[0])):
            row_str = "-".join([row[j] for row in rows])
            print(row_str)
        
 
# vérifie si l'un des joueurs à gagné l'ultimate tic tac toe
def ultimate_Terminal_Test(joueur,ultimate_board):
    ultimate_res_board = Board() # crée un sous tableau de ultimate board avec sur chaque case la valeur du gagnant ou 0 si nul
    for i in range(9):
        if ultimate_board[i].TerminalTest(joueur):
            ultimate_board[i].set_board(1,i)
    if ultimate_res_board.TerminalTest(joueur): # on regarde si un des joueurs à une combinaison gagnante
        return True
    return False
            
# boucle de jeu   
if __name__ == '__main__':
    ultimate_board = [Board() for i in range(9)]
    print_ultimate_board(ultimate_board)
    #boardPos c'est la position dans le tableau ultimate
    boardPos= 4 # choix que l'ia fait par défaut à chaque fois 
    premier_tour = True
    premier_joueur = input('taper 1 si le joueur commence ou 2 si l\'ordinateur commence: ')
    
    #cas ou le joueur commence
    if premier_joueur=='1':
        while not ultimate_Terminal_Test(1,ultimate_board) and not ultimate_Terminal_Test(2,ultimate_board):            
            
            # permet au joueur de choisir la position dans le tableau ultimate au premier tour et vérifie que la position est correcte
            if premier_tour:
                premier_tour=False
                isPosCorrect = False
                while isPosCorrect==False:
                    boardPos = int(input('entrer numéro board: '))
                    if boardPos>0 and boardPos<10:
                        isPosCorrect=True
                boardPos-=1
        
            #permet au joueur de choisir la position dans le tableau vérifie que la position entrée dans le sous tableau est correcte également
            #pos représente la position dans le sous tableau
            isPosCorrect=False
            while isPosCorrect ==False:
                pos = int(input('entrer numéro case: '))
                if pos>0  and pos<10 and ultimate_board[boardPos].Result(pos-1)==True:
                    isPosCorrect=True
            pos-=1
        
            #imprime le tableau avec la nouvelle entrée
            ultimate_board[boardPos].Result(pos)
            print_ultimate_board(ultimate_board)
        
            # l'ia joue en fonction de la derniere position de la case (pos)
            print(" \n Au tour de l'ordinateur: \n")
            boardPos = ultimate_board[pos].AiPlay()
            print_ultimate_board(ultimate_board)
     
     
    #cas ou l'ordinateur commence
    else:
        while not ultimate_Terminal_Test(1,ultimate_board) and not ultimate_Terminal_Test(2,ultimate_board):       
            
            #l'ia joue en fonction de la derniere position de la case
            print(" \n Au tour de l'ordinateur: \n")
            boardPos= ultimate_board[boardPos].AiPlay() # on récupère la position (pos) choisie par l'ia
            print_ultimate_board(ultimate_board)
            
            #vérifie que la position entrée par le joueur dans le sous tableau est correcte
            isPosCorrect=False
            while isPosCorrect ==False:
                pos = int(input('entrer numéro case: '))
                if pos>0  and pos<10 and ultimate_board[boardPos].Result(pos-1)==True:
                    isPosCorrect=True
            pos-=1
        
            #imprime le tableau avec la nouvelle entrée
            ultimate_board[boardPos].Result(pos)
            print_ultimate_board(ultimate_board)
            boardPos=pos 
        
        
    if ultimate_Terminal_Test(2,ultimate_board):
        print("L'ordinateur a gagné!")
    elif ultimate_Terminal_Test(1,ultimate_board):
        print("Vous avez gagné!")
    else:
        print("égalité")
