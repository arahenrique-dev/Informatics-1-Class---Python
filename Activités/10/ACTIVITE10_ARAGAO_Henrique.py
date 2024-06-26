#21304445
#ARAGAO Henrique

CaseT = str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

#Question 1
def plateaut_vide() ->  PlateauT :
    """Renvoie un plateau de jeu vide pour tic tac toe"""
    e : CaseT = " "
    matrice3_3 : PlateauT = [[e,e,e],[e,e,e],[e,e,e]]
    return matrice3_3

pla1 : PlateauT = plateaut_vide()
assert pla1[1][1] == " "
assert pla1 [0][2] == " "

#Question 2
def videt(p : PlateauT, i : int, j : int) -> bool:
    """Decide si la case de coordonees 'i' et 'j' du plateau 'p' est vide"""
    return p[i][j] == " "

assert videt(pla1, 1, 1) == True
assert videt(pla1, 0, 2) == True

#Question 3
def jouex(pla : PlateauT, i : int, j : int) -> None:
    """La fonction inscrive le symbole X dans la case de coordonnées i et j"""
    pla[i][j] = "X"

def joueo(pla : PlateauT, i : int, j : int) -> None:
    """La fonction inscrive le symbole O dans la case de coordonnées i et j"""
    pla[i][j] = "O"

assert videt(pla1, 0, 2) == True
assert jouex(pla1, 1, 1) == None
assert joueo(pla1, 0, 2) == None
assert videt(pla1, 0, 2) == False

#Question 4
def dessine_plateaut(pla : PlateauT) -> str:
    dessin : str = "/---\\\n"
    ligne : str = ""
    i : List[str]
    for i in pla:
            ligne = "|" + str(i[2]) + str(i[1]) + str(i[0]) + "|"
            dessin = dessin + ligne + "\n"
    dessin = dessin + "\---/"
    return dessin
assert dessine_plateaut(pla1) == "/---\\\n|O  |\n| X |\n|   |\n\\---/"

#Question 5
def gagnet(pla : PlateauT, s : str) -> bool:
    """Decide si le plateau est gagnant pour s"""
    gagnant : bool = False
    i : List[CaseT]; j : List[CaseT]; k : List[CaseT]
    e : int; f : int; g : int
    lignes : List[List[CaseT]] = [[pla[0][0], pla[0][1], pla[0][2]], [pla[1][0], pla[1][1], pla[1][2]], [pla[2][0], pla[2][1], pla[2][2]]]
        
    colomnes : List[List[CaseT]] =[[pla[0][0], pla[1][0], pla[2][0]], [pla[0][1], pla[1][1], pla[2][1]], [pla[0][2], pla[1][2], pla[2][2]]]

    diagonel : List[List[CaseT]] =[[pla[0][0], pla[1][1], pla[2][2]], [pla[0][2], pla[1][1], pla[2][0]]]
    for i in lignes:
        for e in range(0, len(i) - 1):
            if i[e] == i[e + 1] and i[e] == s:
                gagnant = True
    for j in colomnes:
        for f in range(0, len(j) - 1):
            if j[f] == j[f + 1] and j[f] == s:
                gagnant = True
    for k in diagonel:
        for g in range(0, len(k) - 1):
            if k[g] == k[g + 1] and k[g] == s:
                gagnant = True
    return gagnant

assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
print(gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O"))
assert gagnet([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
print(gagnet([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X"))
assert gagnet([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True
