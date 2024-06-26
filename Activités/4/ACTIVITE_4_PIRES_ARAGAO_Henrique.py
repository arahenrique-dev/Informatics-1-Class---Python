#Activité 4 - Chiffres
#ARAGAO Henrique

#1 Preliminaires
def identite(s : str) -> str :
    """ Renvoie la chaine s telle quelle """
    return s

assert identite("LU1IN011") == "LU1IN011"
assert identite("") == ""

def identite_texte(nom : str) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-copie.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-copie.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(identite(ligne))

#2 Partie Guidée: Chiffre de César
#Question 1
def est_minuscule(s : str) -> bool:
    """Évaluation d'un charactere si il est une lettre minuscule"""
    i : int
    for i in range(len(s) + 1):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            return True
        return False

assert est_minuscule("a") == True
assert est_minuscule("z") == True
assert est_minuscule("g") == True
assert est_minuscule("A") == False
assert est_minuscule("Z") == False
assert est_minuscule("G") == False
assert est_minuscule("100") == False
assert not est_minuscule("C")
assert not est_minuscule(" ")

def est_majuscule(s : str) -> bool:
    """Évaluation d'un charactere si il est une lettre majuscule"""
    i : int
    for i in range(len(s) + 1):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            return True
        return False

assert est_majuscule("A") == True
assert est_majuscule("Z") == True
assert est_majuscule("G") == True
assert est_majuscule("a") == False
assert est_majuscule("z") == False
assert est_majuscule("g") == False
assert est_majuscule("100") == False
assert not est_majuscule("c")
assert not est_majuscule(" ")

#Question 2
def caractere_decale(s : str, n : int) -> str:
    """Precondition: len(s) == 1
    Decale et renvoie un caractère par n places si c'est une lettre romaine. Sinon, le caractère ne change pas"""
    lettre_code : int
    lettre_decale : str
    if est_minuscule(s):
        if ord(s) + n > 122:
            lettre_code = n + ord(s) - 26
        else:
            lettre_code = ord(s) + n
    elif est_majuscule(s):
        if ord(s) + n > 90:
            lettre_code = n + ord(s) - 26
        else:
            lettre_code = ord(s) + n
    else:
        lettre_code = ord(s)
    lettre_decale = chr(lettre_code)
    return lettre_decale

assert caractere_decale("a", 0) == "a"
assert caractere_decale("a", 3) == "d"
assert caractere_decale("A", 3) == "D"
assert caractere_decale("V", 8) == "D"
assert caractere_decale(" ", 3) == " "

#Question 3
def ligne_chiffre_cesar(s : str, n : int) -> str:
    """Renvoie une chaine de caracteres chiffrée avec une clef en appliquant le chiffrement de César"""
    chaine : str = ""
    i : int
    for i in range(0, len(s)):
        chaine = chaine + caractere_decale(s[i], n)
    return chaine

assert ligne_chiffre_cesar("Bonjour LU1IN011", 3) == "Erqmrxu OX1LQ011"
assert ligne_chiffre_cesar("Bonjour LU1IN011", 0) == "Bonjour LU1IN011"

def ligne_dechiffre_cesar(s : str, n : int) -> str:
    """Renvoie une chaine de caracteres dechiffrée avec une clef en appliquant le déchiffrement de César"""
    lettre_code : int
    lettre_dechiffree : str
    chaine : str = ""
    i : int
    for i in range(0, len(s)):
        if est_minuscule(s[i]):
            if ord(s[i]) - n < 97:
                lettre_code = ord(s[i]) - n + 26
            else:
                lettre_code = ord(s[i]) - n
        elif est_majuscule(s[i]):
            if ord(s[i]) - n < 65:
                lettre_code = ord(s[i]) - n + 26
            else:
                lettre_code = ord(s[i]) - n
        else:
            lettre_code = ord(s[i])
        lettre_dechiffree = chr(lettre_code)
        chaine = chaine + lettre_dechiffree
    return chaine

assert ligne_dechiffre_cesar("Erqmrxu OX1LQ011", 3) == "Bonjour LU1IN011"
assert ligne_dechiffre_cesar("Bonjour LU1IN011", 0) == 'Bonjour LU1IN011'
beaute1 : str = "Je suis belle, o mortels ! comme un reve de pierre,"
assert ligne_dechiffre_cesar(ligne_chiffre_cesar(beaute1, 12), 12) == beaute1

#Question 4
def chiffre_fichier_cesar(nom : str, n : int) -> None:
    """Chiffre le texte d'un fichier a partir d'une clef n et cree un nouveaux fichier respective"""
    identite_texte(nom)
    with open(nom + '.txt', "r") as fichier:
        with open(nom + "-copie.txt", "w") as chiffree_fichier:
            s : str
            for s in fichier.readlines():
                s = ligne_chiffre_cesar(identite(s), n)
                chiffree_fichier.write(s)

print(chiffre_fichier_cesar('/Users/Henrique/Documents/Sorbonne/Info/Activités/4/bovary', 3))
    
def dechiffre_fichier_cesar(nom : str, n : int) -> None:
    """Dechiffre le texte d'un fichier a partir d'une clef n et cree un nouveaux fichier respective"""
    identite_texte(nom)
    with open(nom + '.txt', "r") as fichier:
        with open(nom + "-copie.txt", "w") as dechiffree_fichier:
            s : str
            for s in fichier.readlines():
                s = ligne_dechiffre_cesar(identite(s), n)
                dechiffree_fichier.write(s)
    

print(dechiffre_fichier_cesar('/Users/Henrique/Documents/Sorbonne/Info/Activités/4/bovary-cesar', 3))

#3 Suggestion : Attaque
def attaque_cesar(nom : str) -> None:
    """Decale un extrait d'un texte d'un fichier en toutes les possibilités et 
ecrit le resultat dans un nouveau fichier"""
    i : int = 0
    identite_texte(nom)
    with open(nom + '.txt', "r") as fichier:
        with open(nom + "-copie.txt", "w") as attaque_fichier:
            f : str = fichier.read()
            s : str
            while i <= 25:
                s = ligne_dechiffre_cesar(f, i)
                attaque_fichier.write('\n==========================\n')
                attaque_fichier.write('Decalage de : ' + str(i) + '\n\n')
                attaque_fichier.write(s)
                attaque_fichier.write('\n')
                i = i + 1

print(attaque_cesar('/Users/Henrique/Documents/Sorbonne/Info/Activités/4/bovary-cesar-attaque'))

