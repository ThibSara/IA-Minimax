# -*- coding: utf-8 -*-

init_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
board = init_board

# liste des tuples de toutes les combinaisons gagnantes rangé par ordre croissant
winning_combination = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6))

# impression du tableau du tic tac toe
def Print_Board():
    out = []
    for i in range(9):
        if (i%3 == 0) : out += "\n"
# on remplace les valeurs du tableau par des X et des O pour un effet visuel
        if (board[i]==0):
            out += ' '
        elif (board[i]==1):
            out+='X'
        else:
            out+='O'
    print(" | ".join(out)+' | ')
         

# vérifie que le joueur peut jouer sur la case désirée, renvoie vrai si le mvt à été effectué, faux sinon
def Result(joueur,mvt):
    mvt=mvt-1
    if (joueur == 1) and (mvt >= 0 and mvt < 9) and board[mvt] == 0:
        board[mvt] = joueur
        return True
    return False


#vérifie si un joueur à gagné la partie
def TerminalTest(joueur):
    for i in winning_combination:
        if i in Set_Joueur(joueur,3):
            return True
    return False


# retour le nombre de nombre de pair et singleton potentiellement gagnant
# pair vaut 3 fois plus que singleton pour pousser à jouer au deuxième coups
def evaluate(joueur=2):
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

# crée liste de toutes les combinaison du joueur de n jetons
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

def minimax(alpha,beta,is_maximizing):
    #retourne la valeur de la grille si la partie est finie
    if TerminalTest(0) or TerminalTest(1):
        return evaluate()
    
    #si c'est au tour de l'ordi de jouer on maximise
    if is_maximizing:
        best_score  = float('-inf')
        for i in range(9):
            if board[i]==0:
                board[i]=2
                score= minimax(alpha,beta,False)
                board[i]=0
                best_score=max(score,best_score)
                alpha=max(alpha,best_score)
                if beta<= alpha:
                    break
        return best_score
    
    #si c'est au tour du joueur on minimise
    else:
        best_score=float('inf')
        for i in range(9):
            if board[i]==0:
                board[i]=1
                score=minimax(alpha,beta,True)
                board[i]=0
                best_score = min(score, best_score)
                beta=min(beta,best_score)
                if beta<=alpha:
                    break
        return best_score
  
#fonction pour que l'ordinateur joue le meilleur coup     
def AiPlay():
    best_score=float('-inf')
    best_move=None
    alpha = float('-inf')
    beta = float('inf')
    for i in range(9):
        if board[i]==0:
            board[i]=2
            score =minimax(alpha,beta,False)
            board[i]=0
            if score>best_score:
                best_score=score
                best_move=i
            alpha=max(alpha,best_score)
    board[best_move]=2
    Print_Board()
         
    
if __name__ == '__main__':
    Print_Board()
    while not TerminalTest(2) and not TerminalTest(1) and 0 in board:
        
        isPosCorrect = False
        while isPosCorrect ==False:
            pos = input('entrer numéro case: ')
            isPosCorrect = Result(1,int(pos))
        Result(1,int(pos))
        Print_Board()
        AiPlay()
    if TerminalTest(2):
        print("L'ordinateur a gagné!")
    elif TerminalTest(1):
        print("Vous avez gagné!")
    else:
        print("égalité")
    

            


"""
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
  """  
  
"""
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
"""

'''
# renvoie une liste des actions possibles
def Actions():
    index=[]
    for i in range(len(board)):
        if board[i] == 0:
            index.append(i)
    return index
'''    

'''
# Fonction pour savoir qui à gagné
def evaluate():
    if TerminalTest(1):
        score = 1
    elif TerminalTest(2):
        score = 2
    else:
        score = 0
    return score
'''