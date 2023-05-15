#TicTacToe Main
from Player import *
from Board import *
from Ultimate import *

"""
Problème irrésolue :
Ligne 39, lorsque j'appelle AIPlay, il modifie game alors que ce n'est même pas en paramètre
Classique TicTacToe pas debuggé
"""


"""
def ClassiqueTicTacToe(j1 : Player, j2 : Player):
    game = Board()
    joueur = j1
    while(game.winner == 0):
        print(str(game) + "\n\n Tour joueur "+ joueur+ " : ")
        
        if joueur.isIA:
            move = AIPlay(game, int(joueur))
            game.board[move] = joueur
            print("Joueur "+ joueur +" a joué sur la case "+ move)   
        else :
            move = HumanPlay(game)
            game.board[move] = joueur
        
        joueur = Adversaire(int(joueur))
        game.TerminalTest
    print("Le gaganant est "+ game.winner)
"""

def UltimateTicTacToe(joueur : Player):
    game = UltimateBoard()
    move = -1     # pour donner le choix du board au premier tour au premier tour
    while(game.ulti_board.winner == 0):
        print(str(game) + "\n\nTour joueur "+ str(joueur) + " : ")
        
        if joueur.isAI():
            temp = UltimateBoard(game)                          # game temporaire pour ne pas modifier la veritable game
            board, move = AIPlay(temp, move, int(joueur))       # le parametre board de l'IA est le move de jeton précédent
            game.Set(int(joueur), board, move)                  # update le veritable game
            print("Joueur "+ str(joueur) +" a joué dans la board "+ str(board) +" sur la case "+ str(move))
        else :
            board,move = HumainPlay(game, move)                 # demande au joueur son mouvement
            game.Set(int(joueur), board, move)                  # update le veritable game
        
        joueur.NextTurn()                                       # changement de tour
        game.TerminalTest()                                     # verifie si la game est fini
    print("Le gagnant est "+ str(game.ulti_board.winner))

if __name__ == '__main__':
    joueur = Player(J1_is_AI = False, J2_is_AI = True)
    UltimateTicTacToe(joueur)
    
    """
    exo = input("~~~~ ULTIMATE TIC TAC TOE ~~~~\n\n"
          "Type de Tic Tac Toe : \n"
          "\t1 : Classique\n"
          "\t2 : Ultimate\n"
          "Choisir un type : ")
    print("\nSelectioner qui controle joueur :\n"
          "\t1 : Human\n"
          "\t2 : IA")
    j1 = input("Joueur 1 : ")
    #while j1 not in (1,2):
    #    j1 = input("Tapez 1, 2 : ")
    Player(1, j1 == "2")

    j2 = input("Joueur 2 : ")
    #while j2 != 1 and j2 != 2:
    #    j2 = input("Tapez 1, 2 : ")
    j2 = Player(1, j2 == "2")
    
    if exo == "1":
        ClassiqueTicTacToe(j1,j2)

    else :
        print("pb")
        #UltimateTicTacToe(j1,j2)
    """