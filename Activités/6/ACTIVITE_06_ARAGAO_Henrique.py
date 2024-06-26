#ARAGAO Henrique
#21304445
#Activité 06 - Fractales

#1 Partie guidée: Courbes
#Question 1
Point = Tuple[float, float]
Courbe = List[Point]

O : Point = (0.0, 0.0)
tri1 : Courbe = [O, (0.0,0.3), (0.4,0.0), O]

def longueur(a : Courbe) -> float:
    """Renvoie la longueur d'une courbe 'a'."""
    x1 : float; y1 : float
    x2 : float; y2 : float
    somme_x : float = 0
    somme_y : float = 0
    longueur : float = 0.0
    i : int
    for i in range(0, len(a) - 1):
        point1 : Tuple[float, float] = a[i]
        point2 : Tuple[float, float] = a[i + 1]
        x1, y1 = point1
        x2, y2 = point2
        longueur = longueur + ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
        i = i + 1
    return longueur

assert abs(longueur(tri1) - 1.2) < 10**(-12)

#Question 2
def segment(p1 : Tuple[float, float], p2 : Tuple[float, float]) -> Image:
    """Renvoie l'image correspondand au segment de deux points"""
    x1 : float; y1 : float
    x2 : float; y2 : float
    x1, y1 = p1
    x2, y2 = p2
    line : Image = draw_line(x1, y1, x2, y2)
    return line

print(show_image(segment((0.0,0.1), (1.0,0.5))))

#Question 3
def image_courbe(c : Courbe) -> Image:
    """Renvoie l'image correspondant a courbe"""
    f_image : Image
    image_base : Image
    s : Image
    i : int
    for i in range(0, len(c) - 1):
        s = segment(c[i], c[i + 1])
        if i == 0:
            image_base = s
        image_base = overlay(s, image_base)
        i = i + 1
    f_image = overlay(s, image_base)
    return f_image

print(show_image(image_courbe(tri1)))

#Question 4
def deplace(p : Point, c : str, di : float) -> Point:
    """Precondition: c == H or B or G or D. Renvoie le point obtenu en deplacant le point p dans la direction d de la distance d"""
    x : float; y : float
    x, y = p
    if c == "H":
        return (x, y + di)
    elif c == "B":
        return (x, y - di)
    elif c == "G":
        return (x - di, y)
    elif c == "D":
        return (x + di, y)

assert deplace(O, "G", 1) == (-1.0, 0.0)
assert deplace(O, "H", 0.5) == (0.0, 0.5)

#Question 5
def spirale(ori : Point, dec : float, n : int) -> Courbe:
    """Renvoie la spirale construite a partir d'un point d'origine, decalage et nombre d'etapes"""
    i : int
    deplacement : Point = ori
    x, y = deplacement
    f_courbe : Courbe = [deplacement]
    s : str = " "
    for i in range(1, n + 1):
        s = "D"
        if i % 4 == 2:
            s = "H"
        if i % 4 == 3:
            s = "G"
        if i % 4 == 0:  
            s = "B"
        deplacement = deplace(deplacement, s, dec * i)
        f_courbe.append(deplacement)
    return f_courbe

print(show_image(image_courbe(spirale(O, 0.01, 400))))

#Suggestion 3
def courbe_dragon(a : Point, b : Point, i : int) -> Courbe:
    f_courbe : Courbe = [a]
    s : Point = (0, 0)
    xs, ys = s
    xa,ya = a
    xb, yb = b
    l : float
    h : float
    for x in range(0, i):
        l = xa - xb
        xs = (l / 2) + xa
        ys = (3**1/2 * l) / 2
        
        xa = xb
        ya = yb
        
        xb = xs
        yb = ys
        
        p1 : Point = (xs, ys)
        p2 : Point = (xb, yb)
        f_courbe.append(p1)
        f_courbe.append(p2)
    return f_courbe

print(show_image(image_courbe(courbe_dragon((-0.5,0), (0.5,0), 5))))
