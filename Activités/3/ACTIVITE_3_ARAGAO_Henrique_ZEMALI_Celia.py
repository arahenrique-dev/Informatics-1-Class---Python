#ARAGAÃO Henrique
#ZEMALI Célia

import math as math

#1 Partie Guidée: Simulation
def divise(k : int, n : int) -> bool:
    """Pre:k> 0andn>=0
    Decide si k divise n """
    return n % k == 0

assert divise(2, 4) == True
assert divise(6, 30) == True
assert divise(6,20) == False
assert divise(7,15) == False

def est_parfait(n : int) -> bool:
    """ Pre : n >= 1
    Decide si n est un nombre parfait."""
    s : int = 0
    i : int = 1
    while i != n:
        if divise(i, n):
            s=s+i
        i=i+1
    return n == s

assert est_parfait(6) == True
assert est_parfait(28) == True
assert est_parfait(4) == False
assert est_parfait(15) == False

def eqt_parfait_simulee(n : int) -> None:
    """Pre : n >= 1
    Renvoie la même r éesultat que est parfait et qui affiche la valeur des variables i et s en     entrée de boucle, et à la fin de chaque tour de boucle."""
    s : int = 0
    i : int = 1
    tour : int = 0
    print("=== Evaluation de : ’est parfait simulee(" + str(n) + ")’ ===")
    print("debut de boucle, s =", s)
    print("debut de boucle, s =", i)
    while i != n:
        if divise(i, n):
            s=s+i
        i=i+1
        tour = tour + 1
        print("====================")
        print("fin du tour ", tour, "s=", s)
        print("fin du tour ", tour, "i=", i)
    print("====================")
    print("sortie de boucle, s =", s, "et n =", n)
    print(n == s)
    print("=================================================")
print(eqt_parfait_simulee(6))

#2 Suggestion : Test
def test_parfait(n : int) -> bool:
    """Verifie si le nombre est dans la liste des nombres parfaits"""
    k : int
    i : int = 0
    liste_nombres_parfaits : List[int] = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]
    for k in range(n + 1):
        if k == liste_nombres_parfaits[i]:
            i = i + 1
            return True
    return False

print(test_parfait(5))
print(test_parfait(29))
print(test_parfait(137438691329))

#Suggestion 3 Invariant
#Question 1 et Question 2 
def est_parfait_invariant(n : int) -> bool :
    """ Pre : n > = 1
    Decide si n est un nombre parfait ."""
    i : int = 1
    s : int = 0

    while i != n :
        print("Valeur de l'invariant",s,"dans le début du boucle")
        print("========================================")
        if divise(i, n):
            s = s + i
        i = i + 1

    print("Valeur de l'invariant", s,"aprés le boucle")
    print("========================================")

    return n == s

#Suggestion 4
#Question 1
def eqt_parfait_fichier(n : int) -> None:
    """Pre : n >= 1
    Ecrire un fichier avec les memes instructions de la fonction est_parfait_simulee"""
    s : int = 0
    i : int = 1
    tour : int = 0
    with open('fichier', 'w') as fichier:
        fichier.write("=== Evaluation de : ’est parfait simulee(6)’ ===\n")
        fichier.write("debut de boucle, s =" + str(s) + "\n")
        fichier.write("debut de boucle, s =" + str(i) + "\n")
        while i != n:
            if divise(i, n):
                s=s+i
            i=i+1
            tour = tour + 1
            fichier.write("====================\n")
            fichier.write("fin du tour " + str(tour) + " s=" + str(s) + "\n")
            fichier.write("fin du tour " + str(tour) + " i=" + str(i) + "\n")
        fichier.write("====================\n")
        fichier.write("sortie de boucle, s = " + str(s) + " et n = " +  str(n) + "\n")
        fichier.write(str(n == s))
        fichier.write("=================================================\n")

print(eqt_parfait_fichier(6))

#Question 2
def est_parfait_tableau(n : int) -> None:
    """ Pre : n >= 1
    Decide si n est un nombre parfait."""
    with open('tableau', 'w') as tableau:
        s : int = 0
        i : int = 1
        tableau.write('==================================================\n')
        tableau.write('|         tour       |     i     |       s       |\n')
        tableau.write('==================================================\n')
        '''entree : str = '| {:19}|{:>10} |{:>14} |'
        tableau.write('| ' + '{:19}' + '|' + '{:>10}' + ' |' + '{:>14}' + ' |'.format(entree, i, s))'''
        while i != n:
            if divise(i, n):
                s=s+i
                tableau.write('i=' + str(i) + ' s=' + str(s) + '\n')
            else:
                tableau.write('i=' + str(i) + ' s=' + str(s) + '\n')
            i=i+1
        tableau.write('Sortie i=' + str(i) + ' s=' + str(s) + '\n')

print(est_parfait_tableau(100))

#Suggestion 5
#Question 1
def est_parfait_appels(n : int) -> bool:
    """ Renvoie le resultat de est_parfait et calcule et affiche le nombre de fois ù la fonction divise a été appelé."""
    s : int = 0
    i : int = 1
    fois_divise : int = 0
    while i != n:
        if divise(i, n):
            s=s+i
        fois_divise = fois_divise + 1
        i=i+1
    print(str(fois_divise) + " appels a la function divise (est_parfait_appels)")
    return n == s

#Question 2
def est_parfait_opti_appels(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """
    s : int = 1
    i : int = 2
    fois_divise : int = 0
    if i == 1 : 
        return False
    while i != int(math.sqrt(n)) + 1 :
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        fois_divise = fois_divise + 1
        i = i + 1
    print(str(fois_divise) + " appels a la function divise (est_parfait_opti_appels)")
    return n == s

#Question 3
print(est_parfait_appels(100))
print(est_parfait_opti_appels(100))
