#TME 10 - 12.3 / 12.4 / 12.5 C
#ARAGAO Henrique 21304445

#Exercice 12.3
#Question 1

#Question 12.4
#Question 1
l0 : List[int] = [6, 1, 3, 2, 4, 5]
l1 : List[int] = [1, 0, 0, 1, 0, 1, 1]

def trier_bulles(l : List[int]) -> List[int]:
    """Trie une list d'entier selon la méthode du tri à bulles"""
    i : int; j : int
    temp : int
    l_f : List[int] = l
    for i in range(0, len(l)):
        for j in range(0, len(l) - 1):
            if l_f[j] > l_f[j + 1]:
                temp = l[j]
                l_f[j] = l_f[j + 1]
                l_f[j + 1] = temp
    return l_f

print(trier_bulles(l0))
print(trier_bulles(l1))

assert l0 == [1, 2, 3, 4, 5, 6]
assert l1 == [0, 0, 0, 1, 1, 1, 1]

#Question 2
def trie_bulles_optm(l : List[int]) -> List[int]:
    """Optime le triage en verifiant si la liste est deja trie"""
    i : int
    j : int
    echanges : bool = False
    for i in range(0, len(l)):
        for j in range(0, len(l) - 1):
            if l[j] > l[j + 1]:
                echanges = True
    if echanges == True:
        return trier_bulles(l)
    else:
        return l

l_o : List[int] = [6, 1, 3, 2, 4, 5]
print(trier_bulles(l_o))

#Exercice 12.5
#Question 1
def partitionner(l : List[int]) -> int:
    """Partitionne les elements d'uneliste et renvoie l'indice du pivot"""
    pivot : int = l[0]; i : int; indice : int
    trier_bulles(l)
    for i in range(0, len(l)):
        if l[i] == pivot:
            indice = i
    return indice

l2 : List[float] = [2, 1, 4, 0, 3]
print(partitionner(l2))

#Question 2
l3 : List[int] = [8, 5, 2, 1, 3, 0, 4, 6, 7]
l4 : List[int] = [2, 1, 3, 0, 4]

def partitionner_sl(l : List[int], i : int, j : int) -> int:
    """Efectue la meme operation que partitionner sur une sous-liste de la liste l"""
    l2 : List[int] = l
    i_sl : int = partitionner(l[i:j])
    sous_list : List[int] = l2[i:j]
    trier_bulles(sous_list)

    k : int = 0
    z : int
    for z in range(i, j):
        l2[z] = sous_list[k]
        k = k + 1
        
    indice : int
    i_l : int
    for i_l in range(0, len(l)):
        if l2[i_l] == sous_list[i_sl]:
            indice = i_l

    return indice

assert partitionner_sl(l3, 2, 7) == 4
print(partitionner_sl(l2, 0, 5))

#Question 3
def trier_rapide_sl(l: List[int], i: int, j: int) -> None:
    """***Procédure***
    Précondition : 0 <= i <= j < len(l)
    Trie la sous-liste de l allant de i (inclus) à j (exclu)"""
    ip : int # indice du pivot
    if i != j:
        ip = partitionner_sl(l, i, j)
        trier_rapide_sl(l, i, ip)
        trier_rapide_sl(l, ip + 1, j)

# Jeu de tests
l5 : List[int] = [8, 5, 2, 1, 3, 0, 4, 6, 7]
assert trier_rapide_sl(l5, 2, 7) == None
assert l5 == [8, 5, 0, 1, 2, 3, 4, 6, 7]

l6 : List[int] = [8, 5, 2, 1, 3, 0, 4, 6, 7]
assert trier_rapide_sl(l6, 0, 3) == None
assert l6 == [2, 5, 8, 1, 3, 0, 4, 6, 7]

l7 : List[int] = [8, 5, 2, 1, 3, 0, 4, 6, 7]
assert trier_rapide_sl(l7, 0, 9) == None
assert l7 == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def trier_rapide(l : List[int], gauche : int, droite : int) -> None:
    """Fait la triage d'une liste selon le principe du tri rapide"""
    if gauche < droite:
        pivot : int = partitionner_sl(l, gauche, droite)
        trier_rapide(l, gauche, pivot - 1)
        trier_rapide(l, pivot + 1, droite)
    
l8 : List[int]= [4, 2, 1, 5, 3, 6]
print(trier_rapide(l8, 0 , len(l8)))
assert l8 == [1, 2, 3, 4, 5, 6]
