#nom: PIRES ARAGAO
#prenom: Henrique
#Groupe: Scfo12.3-A

#THEME 1

#Exercice 1.1
#Question 1
def moyenne_trois_nb(nb1 : float, nb2 : float, nb3 : float) -> float:
    "Donne la moyenne arithmetique de trois nombres "
    return (nb1 + nb2 + nb3) / 3

assert moyenne_trois_nb(3, 6, -3) == 2
assert moyenne_trois_nb(-3, 0, 3) == 0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5/3

#Question 2
def moyenne_ponderee(a:float, b:float, c:float, pa:float, pb:float, pc:float) -> float:
    """Precondition: la somme des cofficients est different de 0
        Donne la moyenne ponderee de trois nombres a, b et c avec des coefficients de ponderation pa, pb, pc"""
    return (a * pa + b * pb + c * pc) / (pa + pb + pc)

assert moyenne_ponderee(6, 7, 5, 2, 5, 3) == 6.2
assert moyenne_ponderee(8, 9, 10, 5, -2, 5) == 9
assert moyenne_ponderee(7, 4, 5, 7, -2, -1) == 9

#Exercice 1.2
#Question 1
def prix_ttc(prix_ht: float, taux_tva: float) -> float:
    "Retourne le prix toutes taxes comprises a partir du prix hors taxe et du taux de TVA"
    return prix_ht + (prix_ht * (taux_tva / 100))

assert prix_ttc(100.0, 20.0) ==  120.0
assert prix_ttc(100, 0.0) == 100.0
assert prix_ttc(100, 100.0) == 200.0
assert prix_ttc(0, 20) == 0.0
assert prix_ttc(200, 5.5) == 211.0

#Question 2
def prix_ht(prix_ttc: float, taux_tva: float) -> float:
    """Retourne le prix hors taxe a partir du prix TTC et un taux de TVA"""
    return prix_ttc / ((taux_tva + 100) / 100)

assert prix_ht(120.0, 20.0) ==  100.0
assert prix_ht(100, 0.0) == 100.0
assert prix_ht(200, 100.0) == 100.0
assert prix_ht(0, 20) == 0.0
assert prix_ht(211, 5.5) == 200.0

#Exercice 1.3
#Question 1
def polynomiale(a : float, b : float, c : float, d : float, x : float) -> float:
    """Retourne la valeur du polynome axˆ3 + bxˆ2 + cx + d"""
    #On peut donner la definition de la fonction comme: (a * x*x*x) + (b * x*x) + (c * x) + d
    #mais c'est plus efficace utiliser l'operateur de puissance **
    #Cette fonction effectue 6 multiplications, considerant la puissance
    return (a * x**3) + (b * x**2) + (c * x) + d

assert polynomiale(1, 1, 1, 1, 2) == 15
assert polynomiale(1, 1, 1, 1, 3) == 40
assert polynomiale(5, 4, 3, 2, 2) == 64
assert polynomiale(3, 7, 5, 1, 2) == 63

#Question 2
def polynomiale_carre(a : float, b : float, c : float, x : float) -> float:
    """Retourne la valeur du polynome axˆ4 + bxˆ2 + c"""
    #Cette fonction effectue 6 multiplications, considerant la puissance
    return (a * x**4) + (b * x**2) + c

assert polynomiale_carre(1, 1, 1, 2) == 21
assert polynomiale_carre(1, 1, 1, 3) == 91
assert polynomiale_carre(4, 3, 2, 2) == 78
assert polynomiale_carre(2, 5, 3, 2) == 55

#Exercice 1.4
#Question 1
import math

def aire_disque(r : float) -> float:
    """Calcule et donne l'aire d'un disque 'de rayon r"""
    return math.pi * r**2

assert aire_disque(4) == 50.26548245743669
assert aire_disque(5) == 78.53981633974483
assert aire_disque(1) == 3.141592653589793

#Question 2
def aire_couronne(r1 : float, r2 : float) -> float:
    """Precondition: r1 <= r2
    Calcule et donne l'aire d'une couronne avec les rayons r1 et r2"""
    return (math.pi * r2**2) - (math.pi * r1**2)


assert aire_couronne(1, 2) == 9.42477796076938
assert aire_couronne(3, 6) == 84.82300164692441
assert aire_couronne(2, 4) == 37.69911184307752

#Exercice 1.5
#Question 1
def fahrenheit_vers_celsius(tF : float) -> float:
    """Calcule et donne la temperature en Celsius a partir d'une temperature tF en Fahrenheit"""
    return (tF - 32) * (5/9)

assert fahrenheit_vers_celsius(212) == 100
assert fahrenheit_vers_celsius(32) == 0
assert fahrenheit_vers_celsius(41) == 5

#Question 2
def celsius_vers_fahrenheit(tC : float) -> float:
    """Calcule et donne la temperature en Fahrenheit a partir d'une temperature tC en Celsius"""
    return ((tC * 9) / 5) + 32

assert celsius_vers_fahrenheit(100) == 212
assert celsius_vers_fahrenheit(0) == 32
assert celsius_vers_fahrenheit(5) == 41

#Exercice 1.6
#Question 1
def fermat(n : float) -> float:
    """Calcule la valeur de Fn, donné par 2ˆ(2ˆn) + 1"""
    return (2 ** (2 ** n)) + 1

assert fermat(0) == 3
assert fermat(1) == 5
assert fermat(2) == 17
assert fermat(5) == 4294967297

#Question 2
def divisible(f5 : int) -> bool:
    """Verifie si F5 est divisible par 641 et n'est pas premier"""
    return f5 % 641 != 0

assert divisible(5) == True

#Exercice 1.8
#Question 1
print(type(42))
print(type(2.3))
print(type(True))
print(type("chaine de caractères"))
print(type(3+2))
print(type(6*2))
print(type(6**2))
print(type(10 > 23))

#Question 2
"""
"essai" == "essai"
    c'est true car les deux chaines de caractères sont identiques
"essai" == "essai "
    cést false car il y a un espace dans la seconde chaine de caractères
"3" == 3
    c'est false car le premier est de type str and le seconde est un entier int
4 == 5
    c'est false car les deux valeurs sont différents
4 == 4
    c'est true car les valeurs de deux entier sont pareils
4 == 2*2
    c'est true car l'expression algebrique de 2*2 donne la meme valeurs de 4
"""

#Question 3
assert 42 / 5 == 8.4
assert 42 // 5 == 8
assert 42 % 5 == 2
assert 6 == 2*3
expression = (2 * 3**3) / (5 - 2)
assert expression == 18
print(type(expression))
#J'attendais un entier et pas un float
def max(nb : float) -> float:
    """Retourne le nombre maximum entre le paramètre et 10"""
    if nb > 10:
        return nb
    else:
        return 10
assert max(14) == 14
assert max(9) == 10

#Question 4
def perimetre(largeur : int, longueur : int) -> int:
    """Précondition : (largeur >= 0) and (longueur >= 0)
    Précondition : longueur >= largeur
    Retourne le périmètre du rectangle défini par sa largeur et sa longueur. """
    return 2 * (largeur + longueur)

assert perimetre(4, 5) == 18
assert perimetre(2, 5) == 14
assert perimetre(5, 8) == 26

def surface(larg : float, long : float) -> float:
    """Precondition: la largueur et longueur sont >= 0 et la largueur <= longueur
    Retourne la surface d'un rectangle a partir de sa largueur et longueur"""
    return larg * long

assert surface(1, 4) == 4
assert surface(2, 0) == 0
assert surface(3, 4) == 12
assert surface(3, 6) == 18


#THEME 2

#Exercice 2.5
#Question 1
import math
def volume_tetraedre(a : float, b : float, c : float, d : float, e : float, f : float) -> float:
    """Calcule le volume d'un tétraèdre a partir de ces paramètres"""
    x = a**2 + b**2 - d**2
    y = b**2 + c**2 -e**2
    z = a**2 + c**2 - f**2

    p = 4*(a**2)*(b**2)*(c**2)
    q = (a**2)*(y**2) + (b**2)*(z**2) + (c**2)*(x**2)
    r = x*y*z

    return (1 / 12) * math.sqrt(p - q + r)

assert volume_tetraedre(1, 1, 1, 1, 1, 1) == 0.11785113019775792
assert volume_tetraedre(2, 2, 2, 2, 2, 2) == 0.9428090415820634
assert volume_tetraedre(5, 4, 3, 2, 4, 5) == 3.491060010942235

def volume_tetraedre_regulier(a) -> float:
    """Calcule le volume d'un tétraèdre regulier a partir de ce paramètre"""
    x = a**2 + a**2 - a**2
    y = a**2 + a**2 -a**2
    z = a**2 + a**2 - a**2

    p = 4*(a**2)*(a**2)*(a**2)
    q = (a**2)*(y**2) + (a**2)*(z**2) + (a**2)*(x**2)
    r = x*y*z

    return (1 / 12) * math.sqrt(p - q + r)

assert volume_tetraedre_regulier(1) == 0.11785113019775792
assert volume_tetraedre_regulier(2) == 0.9428090415820634

#Exercice 2.6
#Question 1
def ou(p : bool, q : bool) -> bool:
    """Retourne la disjonction de p et q."""
    if p == True:
        return True
    elif q == True:
        return True
    else:
        return False
    
def et(p : bool, q : bool) -> bool:
    """Retourne la conjonction de p et q."""
    if p == True:
        if q == True:
            return True
        else:
            return False
    else:
        return False
    
def non(p : bool) -> bool:
    """Retourne la négation de p."""
    if p == True:
        return False
    else:
        return True

assert ou(True, False) == True
assert ou(et(True, False), False) == False
assert et(ou(False, True), non(False)) == True
assert non(non(3 == 1 + 2)) == True

#Question 2
"""
ou(3 == 3, 5 // 0 == 2)
    Si on passe cette fonction, elle nous donne un erreur car il fait une division par zéro

(3==3) or (5//0==2)
    Elle va retourner true avant d'évaluer la deuxieme expression
    
(3 == 4) and (5 // 0 == 2)
    Elle va nous retourner false parce que elle a evalué false pour la première expression

et(3 == 4, 5 // 0 == 2)
    elle fait une division par zéro et nous donne un erreur
"""

#Question 3
def implique(p : bool, q : bool) -> bool:
    """Retourne le résultat de 'p implique q'."""
    return ou(non(p), q)
    
def ou_exclusif(p : bool, q : bool) -> bool:
    """Retourne le résultat de 'p xor q'."""
    return ou(et(p, non(q)), et(non(p), q))

assert implique(False, False) == True
assert implique(True, False) == False
assert implique(True, 3 == 3) == True
assert ou_exclusif(True, False) == True
assert ou_exclusif(3 == 2, 3 == 3) == True
assert ou_exclusif(2 == 2, 3 == 3) == False

#Question 4
def equivalent(p : bool, q : bool) -> bool:
    """Retourne True si et seulement si p et q sont équivalents."""
    return et(implique(p, q), implique(q, p))

assert equivalent(True, 3 == 3) == True
assert equivalent(True, 3 == 4) == False
assert equivalent(3 == 2, 3 == 8) == True
