class Player:
    def __init__(self,joueur, isIA):
        self.joueur = joueur
        self.isIA = isIA
        #composante isIA uniquement utilisé dans Main car classe crée tardivement
    
    def __str__(self):
        return str(self.joueur)
    
    def __int__(self):
        return int(self.joueur)
    
    def ChgmtTour(self, j1, j2):
        if self.joueur == j1 :
            return j2
        return j1




# Renvoie le nombre de l'adversaire du joueur en parametre
def Adversaire(joueur):
    if joueur == 1:
        return 2
    return 1