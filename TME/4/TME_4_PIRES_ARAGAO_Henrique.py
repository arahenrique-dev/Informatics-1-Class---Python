#TME 4
#ARAGAO Henrique

#Exercice 5.5
#Question 1
def est_voyelle(c : str) -> bool:
    """Précondition : len(c) == 1
    Retourne True si et seulement si c est une voyelle miniscule ou majuscule.
    """
    return (c == 'a') or (c == 'A') \
           or (c == 'e') or (c == 'E') \
           or (c == 'i') or (c == 'I') \
           or (c == 'o') or (c == 'O') \
           or (c == 'u') or (c == 'U') \
           or (c == 'y') or (c == 'Y')

def nb_voyelles(s : str) -> int:
    """Renvoie la quantité des voyelles existentes dans une chaîne de characteres"""
    i : int
    nb : int = 0
    for i in range(0, len(s)):
        if est_voyelle(s[i]) == True:
            nb = nb + 1
    return nb
        
assert nb_voyelles('la maman du petit enfant le console') == 12
assert nb_voyelles('mr brrxcx') == 0
assert nb_voyelles('ai al o ents') == 5

#Question 2
def nb_voyelles_accents(s : str) -> int:
    """Renvoie le nombres de characteres qui sont voyelles et voyelles avec l'accent grave"""
    i : int
    nb : int = 0
    for i in range(0, len(s)):
        if est_voyelle(s[i]) or (s[i] == 'á') or (s[i] == 'Á') \
            or (s[i] == 'é') or (s[i] == 'É') \
            or (s[i] == 'í') or (s[i] == 'Ó') \
            or (s[i] == 'ú') or (s[i] == 'Ú') == True:
            nb = nb + 1
    return nb

assert nb_voyelles_accents('la maman du bébé le réconforte') == 11
assert nb_voyelles_accents("L'été j'aime pas boire du café") == 12

#Question 3
def sans_voyelle(s : str) -> str:
    """Renvoie une chaine de characteres d'une phrase sans les voyelles"""
    nouvelle_chaine : str = ""
    i : int
    for i in range(0, len(s)):
        if est_voyelle(s[i]) == False:
            nouvelle_chaine = nouvelle_chaine + s[i]            
    return nouvelle_chaine

assert sans_voyelle('aeiouy') == ''
assert sans_voyelle('la balle au bond rebondit') == 'l bll  bnd rbndt'
assert sans_voyelle('mr brrxcx') == 'mr brrxcx'

#Question 4
def mot_mystere(s : str) -> str:
    """Renvoie une chaine de characteres d'une phrase en remplacent les voyelles par des symboles soulignés"""
    chaine_souligne : str = ""
    i : int
    for i in range(0, len(s)):
        if est_voyelle(s[i]) == False:
            chaine_souligne = chaine_souligne + s[i]
        else:
            chaine_souligne = chaine_souligne + '_'
    return chaine_souligne

assert mot_mystere('aeiouy') == '______'
assert mot_mystere('la balle au bond rebondit bien') == 'l_ b_ll_ __ b_nd r_b_nd_t b__n'
assert mot_mystere('mr brrxcx') == 'mr brrxcx'

#Exercice 5.7
#Question 1
#La fonction ord doit avoir un parametre s de len(s) == 1.
def chiffre(s : str) -> int:
    """Retourne le chiffre entier equivalent au character unicode"""
    if ord(s) <=57 and ord(s) >= 48:
        return int(s)

assert chiffre('5') == 5
assert chiffre('8') == 8

#Question 2
def entier(s : str) -> int :
    """Retourne l'entier represente par la chaine s"""
    return int(s)

assert entier('9') == 9
assert entier('42') == 42
assert entier('0') == 0
assert entier('0012') == 12

#Question 3
#Retourne le caractere equivalant a son code unicode.
def caractere(n : int) -> str:
    """Retourne le caractere qui represente un chiffre"""
    return str(n)

assert caractere(8) == '8'
assert caractere(4) == '4'

#Question 4
def chaine(n : int) -> str:
    """Retourne la chaine de caracteres qui represente un chiffre"""
    return str(n)

assert chaine(9) == '9'
assert chaine(122) == '122'

#Exercice 5.8
#Question 1
def est_chiffre(c : str) -> bool:
    """Précondition : len(c) == 1
    Retourne True si et seulement si c est un chiffre. """
    return ('0' <= c) and (c <= '9')

def decompression(s : str) -> str:
    """Cette fonction fait une decompression d'une chaine de characteres"""
    i : int
    chaine_decompresse : str = ""
    for i in range(1, len(s)):
        if est_chiffre(s[i]) == True:
            fois_ch : int = int(s[i])
            j : int = 0
            while j <= fois_ch:
                chaine_decompresse = chaine_decompresse + s[i + 1] 
        else:
            chaine_decompresse = chaine_decompresse + s[i]
    return chaine_decompresse

#Question 2
def compression(s : str) -> str:
    """Cette fonction fait une compression d'une chaine de characteres"""
    i : int
    nb_lettres : int = 1
    s_compresse : str = ""
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            nb_lettres = nb_lettres + 1
        else:
            s_compresse = s_compresse + s[i - 1]
            if nb_lettres > 1:
                s_compresse = s_compresse + str(nb_lettres)
            nb_lettres = 1
    s_compresse = s_compresse + s[-1]
    if nb_lettres > 1:
        s_compresse = s_compresse + str(nb_lettres)
    return s_compresse
