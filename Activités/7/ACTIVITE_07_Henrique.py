#Activite 7
#ARAGAO Henrique
#21304445

#Partie guidée: Chemins et Labyrinthes
#Question 1

Coord = Tuple[int, int]
Dir = str

ori : Coord = (0, 0)
p1 : Coord = (3, 3)
p2 : Coord = (0, 2)

def deplace(c : Coord, d : Dir) -> Coord:
    """Renvoie les coordonnes de la case apres un deplacement vers une direction"""
    x, y = c
    if d == "N":
        return (x, y + 1)
    elif d == "E":
        return (x + 1, y)
    elif d == "S":
        return (x, y - 1)
    elif d == "O":
        return (x - 1, y)

assert deplace(ori, "N") == (0,1)
assert deplace(p1, "E") == (4,3)
assert deplace(deplace(p2, "N"), "S") == p2

#Question 2
Chemin = List[Dir]
def deplace_chemin(c : Coord, ch : Chemin) -> Coord:
    """Renvoie les coordonnes de la case apres avoir suivi toutes les directions de ch en ordre"""
    coordonnes : Coord = c
    i : str
    for i in ch:
        coordonnes = deplace(coordonnes, i)
    return coordonnes

assert deplace_chemin(ori, ["N", "N"]) == p2
assert deplace_chemin(ori, ["N", "E", "S", "O"]) == ori
assert deplace_chemin(ori, []) == ori

#Question 3
#n, e, s, o , nat
Case = Tuple[bool,bool,bool,bool,str]
Laby = List[List[Case]]

laby1 : Laby = [[(True, True, False, False, ""), (False, False, True, False, "ENTREE")], [(True, False, False, True, ""), (False, False, True, False, "SORTIE")]]
laby2 : Laby = [[(True, False, False, False, ""),(False, True, True, False, ""),(True, True, False, False, ""),(False, False, True, False, "ENTREE")],[(False, False, False, False, ""), (True, True, False, True, ""), (True, False, True, True, ""),(False, True, True, False, "")],[(True, False, False, False, ""), (False, False, True, True, ""), (True, True, False, False, ""), (False, False, True, True, "")],[(True, False, False, False, "SORTIE"), (True, False, True, False, ""),(True, False, True, True, ""),(False, False, True, False, "")]]

def deplace_possible(la: Laby, c: Coord, d: Dir) -> bool:
    """Decide si le deplacement est possible"""
    x, y = c
    position: Case = la[x][y]
    n, e, s, o, na = position

    if d == "N":
        return n
    elif d == "E":
        return e
    elif d == "S":
        return s
    elif d == "O":
        return o

    return False

assert deplace_possible(laby1, (0, 1), "S")
assert not deplace_possible(laby1, (0, 1), "E")
assert not deplace_possible(laby1, (0, 1), "N")

#Question 4
def chemin_possible(la : Laby, c : Coord, ch : Chemin) -> bool:
    """Decide si l'itineraire par le chemin ch a partir de c est possible dans le labyrinthe la"""
    if len(ch) == 0:
        return True
    direction : str = ch[0]
    if deplace_possible(la, c, direction):
        return chemin_possible(la, deplace(c,direction), ch[1:])
    return False

assert chemin_possible(laby1, (0, 1), ["S", "E", "N"])
assert chemin_possible(laby1, (0, 1), ["S", "N", "S", "E", "N"])
assert not chemin_possible(laby1, (0, 1), ["S", "O"])
assert not chemin_possible(laby1, (0, 1), ["S", "E", "N", "O"])

#Question 5
def est_solution(la : Laby, c : Coord, ch : Chemin) -> bool:
    """Decice si le couple (c, ch) est une solution du labyrinthe la"""
    x, y = c
    position : Case = la[x][y]
    n, ea, s, o, na = position
    
    cf : Coord = deplace_chemin(c, ch)
    xf,yf = cf
    position_f : Case = la[xf][yf]
    nf,ef,sf,of,naf = position_f
    return chemin_possible(la, c, ch) and na == "ENTREE" and naf == "SORTIE"

assert est_solution(laby1, (0, 1), ["S", "E", "N"])
assert est_solution(laby1, (0, 1), ["S", "E", "O", "E", "N"])
assert not est_solution(laby1, (0, 0), ["E", "N"])
assert not est_solution(laby1, (0, 1), ["E"])
assert not est_solution(laby1, (0, 1), ["S", "E"])

#Suggestion 2 : Marche Aléatoire
def main_droite(la : Laby,  c : Coord, d : Dir) -> Chemin:
    """Tourne le labyrinthe toujours a droite"""
    i : str
    cn: Coord = c
    directions: List[str] = ['N', 'E', 'S', 'O']
    if deplace_possible(la, cn, 'N'):
        cn = deplace(cn, 'N')
        return main_droite(la, cn, d)
    if deplace_possible(la, cn, 'E'):
        cn = deplace(cn, 'E')
        return main_droite(la, cn, d)
    if deplace_possible(la, cn, 'S'):
        cn = deplace(cn, 'S')
        return main_droite(la, cn, d)
    if deplace_possible(la, cn, 'O'):
        cn = deplace(cn, 'O')
        return main_droite(la, cn, d)
    
    return []


print(main_droite(laby1, (0,0), 'S'))
