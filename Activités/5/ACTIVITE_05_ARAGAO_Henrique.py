#ARAGAO Henrique
#Activité 05 - Polynomes

#1 Partie Guidée : Polynômes
Polyn = List[int]
ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1, -1, 1, -1, 0]
ex3 : Polyn = [27]
ex4 : Polyn = []

#Question 1
def degre(n : List[int]) -> int:
    """Renvoie le degree d'un polynome n"""
    degre : int = 0
    i : int
    index : int = 0
    for i in n:
        if n[index] * 1**i != 0:
            if index > degre:
                degre = index
        index = index + 1
    return degre

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre(ex4) == 0
assert degre([0,0,0,0,0]) == 0

#Question 2
def somme(n1 : List[int], n2 : List[int]) -> List[int]:
    """Renvoie la somme de deux polynômes n1 et n2"""
    index : int = 0
    i : int
    j : int
    z : int
    somme : List[int] = []
    if len(n1) > len(n2):
        difference : int = len(n1) - len(n2)
        for i in range(0, difference):
            n2.append(int('0'))
    if len(n2) > len(n1):
        difference : int = len(n2) - len(n1)
        for j in range(0, difference):
            n1.append(int('0'))
        
    for z in range(0, len(n2)):
        somme_e : int = n1[index] + n2[index]
        somme.append(somme_e)
        index = index + 1
        
    return somme

assert somme(ex1, ex1) == [6, 0, 4]
assert somme(ex1, ex4) == [3, 0, 2]
assert somme(ex1, ex2) == [4, -1, 3, -1, 0]

#Question 3
def normalise(n : List[int]) -> List[int]:
    """Retourne la forme normale du polynome"""
    degre_n : int = degre(n)
    normale : List[int] = []
    i : int = degre_n
    index : int = 0
    if degre_n == 0:
        return []
    while i >= 0:
        normale.append(n[index])
        i = i - 1
        index = index + 1
    return normale

assert normalise(ex1) == [3, 0, 2]
assert normalise(ex2) == [1, -1, 1, -1]
assert normalise([0,0,0,0,0]) == []
assert normalise ([]) == []

#Question 4
def produit(a : List[int], b : List[int]) -> List[int]:
    """Renvoie le produit de deux polynomes a et b"""
    i : int = 0
    j : int = 0
    multiplication : int
    produit : List[int] = []
    if len(a) > len(b):
        while i <= len(a):
            while j <= len(b):
                multiplication = a[i] * b[j]
                produit.append(multiplication)
                j = j + 1
            i = i + 1
    if len(b) > len(a):
        while i <= len(b):
            while j <= len(a):
                multiplication = b[i] * a[j]
                produit.append(multiplication)
                j = j + 1
            i = i + 1
    elif len(a) == len(b):
        while i < len(b):
            while j < len(a):
                multiplication = b[i] * a[j]
                produit.append(multiplication)
                j = j + 1
            i = i + 1
    return produit

print(produit(ex1, ex1))
print(produit(ex1, ex2))

assert normalise(produit(ex1, ex4)) == []
print(normalise(produit(ex1, ex1))) #== [9, 0, 12, 0, 4]
print(normalise(produit(ex1, ex2))) #== [3, -3, 5, -5, 2, -2]
print(normalise(produit([1, 1], [1, 0, 1])))# == [1, 1, 1, 1]
