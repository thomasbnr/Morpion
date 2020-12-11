# Bonnerot Thomas 
#N° 18906646

import time
from math import inf as infinity
from random import choice


humain = -1
Ia = + 1

tableau = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Va afficher le tableau (et/ou grille)

# j1 = IA
#j2 = humain

def returns(etat, choix_j1, choix_j2) : 

    print('----------------')
    for row in etat :
        print('\n----------------')
        for cell in row:
            if cell == +1:
                print('|', choix_j1, '|', end='')
            elif cell == -1:
                print('|', choix_j2, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------')

#Verifie les cas de victoires

def victoire(etat, joueur ) : 
    victoire_etat = [

        [etat[0][0], etat[0][1], etat[0][2]],
        [etat[1][0], etat[1][1], etat[1][2]],
        [etat[2][0], etat[2][1], etat[2][2]],
        [etat[0][0], etat[1][0], etat[2][0]],
        [etat[0][1], etat[1][1], etat[2][1]],
        [etat[0][2], etat[1][2], etat[2][2]],
        [etat[0][0], etat[1][1], etat[2][2]],
        [etat[2][0], etat[1][1], etat[0][2]],
    ]
    if [joueur, joueur, joueur] in victoire_etat:
        return True
    else:
        return False

#heuristique 

def heuristique(etat) : 
    if victoire(etat, Ia):
        score = +1
    elif victoire(etat, humain):
        score = -1
    else:
        score = 0

    return score

#Vainqueur 

def vainqueur(etat):

    return victoire(etat, humain) or victoire(etat, Ia)


def empty_cells(etat):
 
    cells = []

    for x, row in enumerate(etat):
        for y, cell in enumerate(row):
            if cell == 0: cells.append([x, y])
    return cells


# Position possible

def mouv_possible(x, y):

    if [x, y] in empty_cells(tableau):
        return True
    else:
        return False

def set_move(x, y, joueur):

    if mouv_possible(x, y):
        tableau[x][y] = joueur
        return True
    else:
        return False


#fonction minimax, renvois la meilleure solution
def minimax(etat, profondeur, joueur):

    if joueur == Ia:
        meilleur = [-1, -1, -infinity]
    else:
        meilleur = [-1, -1, +infinity]

    if profondeur == 0 or vainqueur(etat):
        score = heuristique(etat)
        return [-1, -1, score]

    for cell in empty_cells(etat):
        x, y = cell[0], cell[1]
        etat[x][y] = joueur
        score = minimax(etat, profondeur - 1, -joueur)
        etat[x][y] = 0
        score[0], score[1] = x, y

        if joueur == Ia:
            if score[2] > meilleur[2]:
                meilleur = score  
        else:
            if score[2] < meilleur[2]:
                meilleur = score  

    return meilleur



def tour_ia(choix_j1, choix_j2):

    profondeur = len(empty_cells(tableau))
    if profondeur == 0 or vainqueur(tableau):
        return

    print('Ordinateur '.format(choix_j1))
    returns(tableau, choix_j1, choix_j2)

    if profondeur == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(tableau, profondeur, Ia)
        x, y = move[0], move[1]

    set_move(x, y, Ia)
    time.sleep(1)


def tour_humain(choix_j1, choix_j2):
 
    profondeur = len(empty_cells(tableau))
    if profondeur == 0 or vainqueur(tableau):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    print('A votre tour [{}]'.format(choix_j2))
    returns(tableau, choix_j1, choix_j2)

    while (move < 1 or move > 9):
            move = int(input('Choose (1_9): '))
            coordonnes = moves[move]
            essai = set_move(coordonnes[0], coordonnes[1], humain)
            if essai == False:
                print('Reessai')
                move = -1



def main():
 
    choix_j2 = 'X'
    choix_j1 = 'O' 
    premier = ''  

    while premier != 'Y' and premier != 'N':
        premier = input('Prêt? y/n : ').upper()
        
    while len(empty_cells(tableau)) > 0 and not vainqueur(tableau):
        if premier == 'N':
            tour_ia(choix_j1, choix_j2)
            premier = ''

        tour_humain(choix_j1, choix_j2)
        tour_ia(choix_j1, choix_j2)


    if victoire(tableau, humain):
        print('Vous '.format(choix_j2))
        returns(tableau, choix_j1, choix_j2)
        print('Vainqueur')
    elif victoire(tableau, Ia):
        print('Ordinateur '.format(choix_j1))
        returns(tableau, choix_j1, choix_j2)
        print('Looser :/')
    else:
        returns(tableau, choix_j1, choix_j2)
        print('Egalité. On en refait une ? ')

    exit()


if __name__ == '__main__':
    main()