#ARAGAO Henrique
#6.6 / 6.7 / 6.8 / 6.9

#Exercice 6.6
#Question 1
def somme(n : List[float]) -> float:
    """Renvoie la somme des éléments de la liste n"""
    somme : float = 0
    i : float
    index : int = 0
    for i in n:
        somme = somme + n[index] 
        index = index + 1
    return somme

assert somme([1, 2, 3, 4, 5]) == 15
assert somme([1, 2.5, 3.2, 4, 5]) == 15.7
assert somme([1, 2.5, 3.5, 4, 5]) == 16.0
assert somme([]) == 0

#Question 2
def moyenne(n : List[float]) -> float:
    """Retourne la moyenne d'une liste de nombres."""
    return somme(n) / len(n)

assert moyenne([1, 2, 3, 4, 5]) == 3.0
assert moyenne([1, 2.5, 3.5, 4, 5]) == 3.2
assert moyenne([5]) == 5.0

def carres(l : List[float]) -> List[float]:
    """Renvoie la liste des carrés des elements de l"""
    l_carres : List[float] = []
    i : float
    index : int = 0
    for i in l:
        l_carres.append(l[index]**2)
        index = index + 1
    return l_carres

assert carres([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert carres([1, -2, -3, 4, 5]) == [1, 4, 9, 16, 25]
assert carres([]) == []
assert carres([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert carres([-5, -1, 2]) == [25, 1, 4]
assert carres([]) == []
assert carres([10, 0.5]) == [100, 0.25]

#Question 4
def variance(n : List[float]) -> float:
    """Renvoie la variance de la liste n en vue que la variance est la difference entre la moyenne des carres des elements et le carre de la moyenne des elements de la liste"""
    variance : float = moyenne(carres(n)) - moyenne(n) ** 2
    return variance

assert variance([10, 10, 10, 10]) == 0.0
assert variance([20, 0, 20, 0]) == 100.0

#Question 5
def ecart_type(n : List[float]) -> float:
    """Renvoie l'ecart-type d'une liste de nombres"""
    ecart_type : float = variance(n) ** (1/2)
    return ecart_type

assert ecart_type([10, 10, 10, 10]) == 0.0
assert ecart_type([20, 0, 20, 0]) == 10.0
assert ecart_type([15, 15, 5, 5]) == 5.0
assert ecart_type([12, 11, 10, 12, 11]) == 0.7483314773547993


#Ecercice 6.7
#Question 1
def liste_mult(l : List[int], k : int) -> List[int]:
    """Retourne la liste obtenue de la liste l multiplié par k"""
    list_nouvelle : List[int] = []
    index : int = 0
    i : int
    for i in l:
        list_nouvelle.append(l[index]*k)
        index = index + 1
    return list_nouvelle

assert liste_mult([3, 5, 9, 4], 2) == [6, 10, 18, 8]
assert liste_mult([], 2) == []

#Question 2
def liste_div(l : List[int], k : int) -> List[int]:
    """Precondition: k != 0
    Retourne la liste obtenue en divisent les elements de la liste n par k"""
    list_nouvelle : List[int] = []
    index : int = 0
    i : int
    for i in l:
        if l[index] % k == 0: 
            list_nouvelle.append(int(l[index] / k))
        index = index + 1
    return list_nouvelle

assert liste_div([2, 7, 9, 24, 6], 2) == [1, 12, 3]
assert liste_div([2, 7, 9, 24, 6], 3) == [3, 8, 2]
assert liste_div([2, 7, 9, 24, 6], 5) == []
assert liste_div([2, 7, 9, -24, 6], -3) == [-3, 8, -2]
assert liste_div([], 3) == []

#Exercice 6.8
#Question 1
def entrelacement(l1 : List[float], l2 : List[float]) -> List[float]:
    """"Precondition: Les 2 listes ont le meme type et meme longueur
    Retourne une liste en intercalant les elements de l1 et l2"""
    nouvelle_liste : List[float] = []
    i : float
    index : int = 0
    for i in l1:
        nouvelle_liste.append(l1[index])
        nouvelle_liste.append(l2[index])
        index = index + 1
    return nouvelle_liste

assert entrelacement([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]

#Question 2
def entrelacement_general(l1 : List[float], l2 : List[float]) -> List[float]:
    """"Precondition: Les 2 listes ont le meme type
    Retourne une liste en intercalant les elements de l1 et l2"""
    nouvelle_liste : List[float] = []
    i : float
    j : float
    z : float
    index : int = 0
    if len(l2) == len(l1):
        for i in l1:
            nouvelle_liste.append(l1[index])
            nouvelle_liste.append(l2[index])
            index = index + 1
        
    elif len(l2) > len(l1):
        for j in l1:
            nouvelle_liste.append(l1[index])
            nouvelle_liste.append(l2[index])
            index = index + 1
        while index < len(l2):
            nouvelle_liste.append(l2[index])
            index = index + 1
    elif len(l1) > len(l2):
        for z in l2:
            nouvelle_liste.append(l1[index])
            nouvelle_liste.append(l2[index])
            index = index + 1
        while index < len(l1):
            nouvelle_liste.append(l1[index])
            index = index + 1
            
    return nouvelle_liste

assert entrelacement_general([1,2,3],[4,5,6]) == [1, 4, 2, 5, 3, 6]
assert entrelacement_general([1,2,3],[4,5,6,7,8]) == [1, 4, 2, 5, 3, 6, 7, 8]
assert entrelacement_general([1,2,3,4,5],[6,7,8]) == [1, 6, 2, 7, 3, 8, 4, 5]

#Exercice 6.9
#Question 1
def jonction(l : List[str], c : str) -> str:
    """Précondition : len(c) = 1
    Retourne la chaîne composée de la jonction des chaîne de L séparées deux-à-deux par le caractère séparateur c."""
    i : int
    index : int = 0
    chaine : str = ''
    for i in range(0, len(l)):
        chaine = chaine + l[index]
        if index < len(l) - 1:
            chaine = chaine + c
        index = index + 1
    return chaine

assert jonction(['un', 'deux', 'trois', 'quatre'], '.') == 'un.deux.trois.quatre'
assert jonction(['les', 'mots', 'de', 'cette', 'phrase'], ' ') == 'les mots de cette phrase'
assert jonction(['un'], '+') == 'un'
assert jonction([], '+') == ''

#Question 2
def separation(s : str, c :str) -> List[str]:
    """Précondition : len(c) = 1
    Retourne la liste de chaînes composées des sous-chaînes de s séparées par le caractère séparateur c. Le séparateur c n'est pas présent dans la chaîne résultat."""
    i : int
    index : int = 0
    liste : List[str] = []
    mot : str = ''
    s_copie : str = s + c
    if len(s) == 0:
        return []
    else:
        for i in range(0, len(s_copie)):
            if s_copie[index] != c:
                mot = mot + s_copie[index]
            else:
                liste.append(mot)
                mot = ''
            index = index + 1
        return liste

assert separation('un.deux.trois.quatre', '.') == ['un', 'deux', 'trois', 'quatre']
assert separation('les mots de cette phrase', ' ') == ['les', 'mots', 'de', 'cette', 'phrase']
assert separation('les mots de cette phrase', '.') == ['les mots de cette phrase']
assert separation('', '+') == []
