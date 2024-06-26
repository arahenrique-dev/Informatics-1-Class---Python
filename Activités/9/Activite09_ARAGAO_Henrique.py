#Activite 09 - Frequence dans des textes

#1 - Partie Guidée: Occurence des mots
def ouvre_fichier(nom : str) -> List[str]:
    """ renvoie la liste des lignes du fichier texte ./nom.txt """
    with open("/"+nom+".txt", "r", encoding = "utf −8") as f:
        return f. readlines ()

exemple1 : List[str] = ouvre_fichier("Users/Henrique/Documents/Sorbonne/Info/Activités/9/beaute")

#Question 1
def decompose_ligne(li : str, sep : Set[str]) -> List[str]:
    """Renvoie une liste de chaines de caractreres correspondant au decoupage de li selon le caractere sep"""
    i : str; s : str
    list_c : List[str] = []
    mot : str = ""
    for i in li:
        if i != "\n" and i != "":
            mot = mot + i
            for s in sep:
                if i == s:
                    mot = mot[:-1]
                    if len(mot) != 0:
                        list_c.append(mot)
                    mot = ""
                
    return list_c


ponctuation : Set[str] = {" ", ",", ";", "'", "(", ")", ".", "!", "?", ":"}

print( decompose_ligne(exemple1[0], ponctuation))# == ['Je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre']
print(decompose_ligne(exemple1[8], ponctuation)) #== ['Et', 'jamais', 'je', 'ne', 'pleure', 'et', 'jamais', 'je', 'ne', 'ris']
print(decompose_ligne(exemple1[2], ponctuation))
#Question 2
def minusculise(m : str) -> str:
    """Renvoie le mot m en sa forme minuscule"""
    mot : str = ""
    c : str
    for c in m:
        if ord(c) >= 65 and ord(c) <= 90:
            mot = mot + chr(ord(c) + 32)
        else:
            mot = mot + c
    return mot

assert minusculise("bonjour") == "bonjour"
assert minusculise("BONJOUR") == "bonjour"
assert minusculise("Bonjour") == "bonjour"

#Question 3
def mots(lis : List[str], sep : Set[str]) -> List[str]:
    """Renvoie la liste de mots (separes par sep) de lis converties en minuscules"""
    li_decomp : List[str] = []
    m : str
    for m in lis:
        li_decomp = li_decomp + decompose_ligne(minusculise(m), sep)
    return li_decomp

#assert mots(exemple1 , ponctuation)[:15] == ['je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre', 'et', 'mon', 'sein', 'où', 'chacun']

#Question 4
def dictionnaire_occ_mots(ms : List[str]) -> Dict[str, int]:
    """Renvoie le dictionnaire referent a liste de ms ou les clefs sont les mots et ses valeurs son le nombre d'occurences de ce mot dans ms"""
    fois : int = 0
    i : int
    dico : Dict[str, int] = {}
    m : str
    for m in ms:
        for i in range(0, len(ms)):
            if m == ms[i]:
                fois = fois + 1
        dico[m] = fois
        fois = 0
    return dico

dico1 : Dict[str, int] = dictionnaire_occ_mots(mots(exemple1, ponctuation ))

print(exemple1)
print(mots(exemple1, ponctuation ))
print(dico1)
assert dico1["je"] == 5
assert dico1["belle"] == 1
assert dico1["jamais"] == 2

#Question 5
def hapax(d : Dict[str, int]) -> Set[str]:
    """Renvoie l'emsemble des hapax du dictionnaire d"""
    return {i for i in d if d[i] == 1}

print(len(hapax(dico1)))
print(("sphinx" in hapax(dico1 )))
print(("jamais" in hapax(dico1 )))
