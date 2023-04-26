
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