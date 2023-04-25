# -*- coding: utf-8 -*-
"""
Created on Sat Mai 01 18:24:07 2023

@author: Ruben LEON TD°S
Alog MinMax
"""


init_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
board = init_board

# liste des tuples de toutes les combinaisons gagnantes rangé par ordre croissant
winning_combination = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6))

def Print_Board():
    out = []
    for i in range(9):
        if (i%3 == 0) : out += "\n"
        out += str(board[i])
    print(" ".join(out) )
        
       
# renvoie une liste des actions possibles
def Actions():
    index=[]
    for i in range(len(board)):
        if board[i] == 0:
            index.append(i+1)
    return index
    
def Result(joueur,mvt):
    if (joueur == 1 or joueur == 2) and (mvt >= 0 and mvt < 9) and board[mvt] == 0:
        board[mvt] = joueur
        return True
    return False

# retour le nombre de nombre de pair et singleton potentielement gagnant
# pair vaut 3 fois plus que singleton pour pousser à jouer au deuxième coups
def Utility(joueur):
    cpt = 0
    for pair in Set_Joueur(joueur, n=2):
        for trio in winning_combination:
            #if (element de pair dans trio AND le troisème element de trio vide) : cpt +=3
            if pair[0] in trio and pair[1] in trio and board[trio[0]] * board[trio[1]] * board[trio[2]] == 0 :
                #print(str(pair)+" in "+ str(trio))
                cpt += 3
    
    for elem in Set_Joueur(joueur, n=1):
        for trio in winning_combination:
            #if (singleton dans trio AND les 2 autres elements de trio vide) : cpt +=1
            if elem in trio and ( 
                    board[trio[0]] + board[trio[1]] == 0 or
                    board[trio[0]] + board[trio[2]] == 0 or
                    board[trio[1]] + board[trio[2]] == 0 ):
                #print(str(elem)+" in "+ str(trio))
                cpt += 1
    return cpt 
 

def TerminalTest():
    for i in winning_combination:
        if i in Set_Joueur(1,3) or i in Set_Joueur(2,3):
            return True
    return False


# cree liste de toutes les combinaison du joueur de n jetons
def Set_Joueur(joueur, n = 3):
    # recupère les position de tout les jeton du joueur
    idx = [i for i in range(9) if board[i] == joueur]
    
    # si le joueur n'a pas posé assez de jeton pour pouvoir gagner
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


def minimax(depth,maximizingJoueur):
    if depth==0 or TerminalTest()==False:
        return Utility(maximizingJoueur)
    if maximizingJoueur:
        maxEval = float('-inf')
        for a in Actions():
            eval = minimax(a,depth-1,False)
            maxEval = max(maxEval,eval)
        return  maxEval
    else:
        minEval = float('inf')
        for a in Actions():
            eval = minimax(a,depth-1,True)
            minEval = min(minEval,eval)
        return  minEval
