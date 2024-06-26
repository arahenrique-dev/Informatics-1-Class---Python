#TME 6
#ARAGAO Henrique 21304445
#AMRANE Sami 21105270
#7.4, 7.5, 8.4, 8.5

#Exercice 7.4 : Fractions
#Question 1
def pgcd(a : float, b : float) -> int:
    """Precondition: b > 0 et a >= b
    Retourne le plus grand diviseur de a et b"""
    quotient : int = int(a)
    diviseur : int = int(b)
    temp : int = 0
    while diviseur != 0:
        temp = quotient % diviseur
        quotient = diviseur
        diviseur = temp
    return int(quotient)

assert pgcd(9, 3) == 3
assert pgcd(15, 15) == 15
assert pgcd(56, 42) == 14
assert pgcd(4199, 1530) == 17
    
def fraction(a : float, b : float) -> Tuple[float, float]:
    """Retourne la fraction canonique de a / b"""
    diviseur : int
    if a > b:
        diviseur = pgcd(a, b)
    else:
        diviseur = pgcd(b,a)
    
    return a / diviseur, b / diviseur

assert fraction(9, 12) == (3, 4)
assert fraction(12, 9) == (4,3)
assert fraction(180, 240) == (3, 4)
assert fraction(121, 187) == (11,17)

#Question 2
def frac_mult(a : Tuple[int, int], b : Tuple[int, int]) -> Tuple[float, float]:
    """Retourne la forme canonique de la multiplication de deux fractions a et b"""
    a0, a1 = a
    b0, b1 = b
    multiplie0 : int = a0 * b0
    multiplie1 : int =  a1 * b1
    return fraction(multiplie0, multiplie1)

assert frac_mult( (3, 4), (8, 4) ) == (3, 2)
assert frac_mult( (3, 4), (4, 3) ) == (1, 1)
assert frac_mult( (3, 4), (1, 1) ) == (3, 4)
assert frac_mult( (3, 4), (0, 2) ) == (0, 1)

#Question 3
def frac_div(a : Tuple[int, int], b : Tuple[int, int]) -> Tuple[float, float]:
    """Retourne la forme canonique de la division de deux fractions a et b"""
    a0, a1 = a
    b0, b1 = b
    div0 : int = a0 * b1
    div1 : int =  a1 * b0
    return fraction(div0, div1)

assert frac_div((3, 4), (8, 4)) == (3, 8)
assert frac_div((3, 4), (4, 3)) == (9, 16)
assert frac_div((3, 4), (1, 1)) == (3, 4)
assert frac_div((3, 4), (0, 2)) == (1, 0)

#Question 4
def ppcm(a : int, b : int) -> float:
    """Précondition : (a != 0) and (b != 0)
    Retourne le plus petit commun multiple de a et b.
    """
    # pgcd de a et b
    p : int = 0
    if a >= b:
        p = pgcd(a, b)
    else:
        p = pgcd(b, a)
    return abs(a * b) / p

assert ppcm(3, 4) == 12
assert ppcm(4, 3) == 12
assert ppcm(11, 17) == 187
assert ppcm(15, 9) == 45

def frac_add(a : Tuple[int, int], b : Tuple[int, int]) -> Tuple[int, int]:
    """Renvoie la fraction canonique correspondant a la somme de deux fractions a et b"""
    n1, d1 = a
    n2, d2 = b
    p : float = ppcm(d1,d2)
    numerateur : float = n1 * (p / d1) + n2 * (p / d2)
    n3, d3 = fraction(numerateur, p)
    return int(n3), int(d3)

assert frac_add( (8, 4), (1, 4) ) == (9, 4)
assert frac_add( (9, 4), (5, 4) ) == (7, 2)
assert frac_add( (1, 3), (1, 2) ) == (5, 6)
    
#EXERCICE 7.5:
#Question 1:
Point=Tuple[int,int]
def vecteur(p1:Point,p2:Point)->Point:
    """ renvoie le couple de coordonnÃ©es du vecteur formÃ© par les points p1 et p2."""
    x,y=p1
    m,n=p2
    return(m-x,n-y)

assert vecteur((1,2),(3,2))==(2, 0)
assert vecteur((1,3),(1,2))==(0, -1)
assert vecteur((3,2),(2,2))==(-1, 0)

#Question 2:
def alignes(p1:Point, p2:Point, p3:Point)->bool:
    """Renvoie le boolÃ©en True si les 3 points sont alignÃ©s et False sinon."""
    n:Point=vecteur(p1,p2)
    m:Point=vecteur(p2,p3)
    x,y=n
    o,p=m
    produit_scalaire:int=x*o+y*p
    if produit_scalaire==0:
        return False
    else:
        return True
    
assert alignes((0,0), (1,1), (5,5))== True

#Exercice 8.4
#Question 1
def moyenne(a : List[float]) -> float:
    """Renvoie la moyenne d'une liste de nombres"""
    elements : int = 0
    somme : float = 0
    i : float
    for i in a:
        somme = somme + i
        elements = elements + 1
    moyenne : float = somme / elements
    return moyenne

assert moyenne([0,10,20]) == 10.0
assert moyenne([0, 10, 20]) == 10.0
assert moyenne([1,2]) == 1.5

#Question 2
def ecart_nombre(a : List[float], b : float) -> List[float]:
    """Renvoie une liste des valeurs absolues de la différence entre les dombres de a avec b"""
    i : float
    ecart_nombre : List[float] = []
    for i in a:
        ecart_nombre.append(abs(i - b))
    return ecart_nombre

assert ecart_nombre([10,10,10],10) == [0,0,0]
assert ecart_nombre([0,10,20], 10) == [10,0,10]
assert ecart_nombre([1,2],1.5) == [0.5,0.5]

#Question 3
def liste_carre(l : List[float]) -> List[float]:
    """Renvoie la liste des carres des elements de la liste l"""
    carres : List[float] = []
    i : float
    for i in l:
        carres.append(i**2)
    return carres

assert liste_carre([0,0,0]) == [0, 0, 0]
assert liste_carre([10,0,10]) == [100, 0, 100]
assert liste_carre([0.5,0.5]) == [0.25, 0.25]

#Question 4
def variance(l : List[float]) -> float:
    """Renvoie la variance associe a une liste l"""
    nb_moyenne : float = moyenne(l)
    nb_elements : int = 0
    variance : float = 0
    i : float
    for i in l:
        variance = variance + (i - nb_moyenne)**2
        nb_elements = nb_elements + 1
    variance = variance / nb_elements
    return variance

assert variance([10,10,10]) == 0.0
assert variance([0,10,20]) == 66.66666666666667
assert variance([1,2]) == 0.25

#Question 5
def variance_ter(l : List[float]) -> float:
    """Retourne la variance associée à l"""
    # moyenne des valeurs de L
    m : float = moyenne(l)
    return moyenne([abs(m-e)**2 for e in l])

assert variance_ter([10,10,10]) == 0.0
assert variance_ter([0,10,20]) == 66.66666666666667
assert variance_ter([1,2]) == 0.25

# Exercice 8.5 :
# Question 1:
def liste_caractere(s:str)->List[str]:
    """ renvoie les elements de la chane de caractere s caracteres par caractères dans une liste."""
    return [c for c in s]

assert liste_caractere("les carottes")==['l', 'e', 's', ' ', 'c', 'a', 'r', 'o', 't', 't', 'e', 's']
assert liste_caractere(" ")==[" "]

# Question 2:

def chaine_de(L:List[str])->str:
    """ renvoie les caracteres d'une liste pour former une chaine de caractères res."""
    res:str=""
    c:str
    for c in L:
        res=res+c
    return res

assert chaine_de(["s","a","l","u","t"])=="salut"
assert chaine_de(["a","u"," ","r","e","v","o","i","r"])=="au revoir"
assert chaine_de(liste_caractere("les carottes"))=="les carottes"

# Question 3:        
def num_car(s:str)->int:
    """ renvoie l'ord unicode de la lettre demandée"""
    if ord(s)<97 or ord(s)>122:
        return ord(s)
    else:
        return ord(s)-97

assert num_car("a")==0
assert num_car("b")==1
assert num_car("z")==25

# Question 4:
def car_num(n:int)->str:
    """ renvoie a partir d'un numero le caractere correspondant."""
    l:List[str]=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i:int
    for i in range(len(l)):
        if i == n:
            return l[i]

assert car_num(num_car("n"))=="n"
assert car_num(0)=="a"
assert car_num(2)=="c"

# Question 5:
def rot13(s:str)->str:
    """ renvoie via un codage une lettre pour une letrre rentrée."""
    if num_car(s)>= 12 and num_car(s)<26:
        return car_num((num_car(s)+13)%26)
    elif num_car(s)< 12 and num_car(s)<26:
        return car_num(num_car(s)+13)
    else:
        return s
assert rot13('o')=='b'
assert rot13('z')=='m'
assert rot13('8')=='8'
assert rot13(rot13("o"))=="o"

# Question 6:
def codage_rot13(s:str)->str:
    """ renvoie un code secret de la chainne de caractere s à partir de la fonction rot13()."""
    c:str
    res:str=""
    for c in s:
        res=res+rot13(c)
    return res

assert codage_rot13("les carottes sont cuites")=="yrf pnebggrf fbag phvgrf"
assert codage_rot13("yrf pnebggrf fbag phvgrf")=="les carottes sont cuites"
secret : str = codage_rot13("les carottes sont cuites")
assert codage_rot13(secret)=="les carottes sont cuites"

