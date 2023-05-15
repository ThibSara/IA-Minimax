#TicTacToe Main
from Player import *
from Board import *
from Ultimate import UltimateBoard, HumainPlay, AIPlay

"""
def ClassiqueTicTacToe(j1 : Player, j2 : Player):
    game = Board()
    joueur = j1
    while(game.winner == 0):
        print(str(game) + "\n\n Tour joueur "+ joueur+ " : ")
        ClassiqueTour(game,joueur)
        joueur = Adversaire(int(joueur))
        game.TerminalTest
    print("Le gaganant est "+ game.winner)

def ClassiqueTour(game : Board, joueur : Player):
    if joueur.isIA:
        move = AIPlay(game, int(joueur))
        game.board[move] = joueur
        print("Joueur "+ joueur +" a joué sur la case "+ move)   
    else :
        move = HumanPlay(game)
        game.board[move] = joueur
"""

def UltimateTicTacToe(j1,j2):
    game = UltimateBoard()
    joueur = j1
    next_board = 4     # pour que à la première étapes, l'ordi sur la case du milieu (plus interessante)
    while(game.ulti_board.winner == 0):
        print(str(game) + "\n\nTour joueur "+ str(joueur) + " : ")
        next_board = UltimateTour(game, next_board, joueur)
        joueur = Adversaire(joueur)
        game.TerminalTest()
    print("Le gaganant est "+ str(game.ulti_board.winner))

def UltimateTour(game : UltimateBoard,move, joueur : Player):
    if joueur.isIA:
        board, move = AIPlay(game, move, int(joueur))
        game.Set(joueur, board, move)
        print("Joueur "+ str(joueur) +" a joué sur la case "+ str(move))
        return move   
    else :
        board,move = HumainPlay(game, move)
        game.Set(joueur, board, move)
        return move


if __name__ == '__main__':
    j1 = Player(1,True)
    j2 = Player(2,False)
    UltimateTicTacToe(j1,j2)
    
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