class Player:
    def __init__(self,J1_is_AI = False, J2_is_AI = True):
        self.J1 = J1_is_AI
        self.J2 = J2_is_AI
        self.currentPlayer = 1
        
    def __str__(self):
        return str(self.currentPlayer)
    
    def __int__(self):
        return int(self.currentPlayer)
    
    def NextTurn(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        else :
            self.currentPlayer = 1
    
    def isAI(self):
        if self.currentPlayer == 1:
            return self.J1
        return self.J2

# Renvoie le int du joueur adverse
def Adversaire(joueur):
    if joueur == 1:
        return 2
    return 1