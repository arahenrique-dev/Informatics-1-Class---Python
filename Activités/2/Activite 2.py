#ARAGAO Henrique
#21304445
#Activite 02 - Approximation de pi

#1 Partie Guidée : S ́erie alternée de Leibniz
#Question 1
import math as math
def terme_leibniz(n : int) -> float:
    """"Retourne le terme a l'indice n du terme leibniz"""
    return ((-1)**n) / (2*n + 1)

assert terme_leibniz(0) == 1
assert terme_leibniz(10) == 1 / 21
assert terme_leibniz(1) == -1 / 3

#Question 2
def somme_leibniz(n : int) -> float:
    """Retourne la somme des termes jusqu'au n"""
    somme : float = 0
    i : int
    for i in range(n + 1):
        somme = somme + terme_leibniz(i)
    return somme

assert somme_leibniz(0) == 1
assert somme_leibniz(1) == 1 - (1/3)
assert somme_leibniz(4) == 1 - (1/3) + (1/5) +- (1/7) + (1/9)

#Question 3
def approx_leibniz(n : int) -> float:
    """Retourne l'approximation de pi a partir de la série alternée de Leibniz"""
    return somme_leibniz(n) * 4

assert approx_leibniz(10) == 3.232315809405594
assert approx_leibniz(100) == 3.1514934010709914

#Question 4
assert abs(approx_leibniz(1) - math.pi) < 10**2
assert abs(approx_leibniz(100) - math.pi) < 10**10

#2 Suggestion : Formule des frères Chudovsky
def factorielle(n : int) -> float:
    """Retourne la factorielle d'un nombre n"""
    factorielle : float = 1
    i : int
    for i in range(1, n + 1):
        factorielle = factorielle * (i)
    return factorielle

assert factorielle(5) == 120
assert factorielle(4) == 24

def Mq(q : int) -> float:
    """Retourne le terme multinomel de la formule de Chudovsky"""
    return factorielle(6 * q) / (factorielle(3 * q) * factorielle(q)**3)

assert Mq(1) == 120.0
assert Mq(2) == 83160.0

def Lq(q : int) -> float:
    """Retourne le terme lineaire de la formule de Chudovsky"""
    return (545140134 * q) + 13591409

assert Lq(3) == 1649011811
assert Lq(6) == 3284432213

def Xq(q : int) -> float:
    """Retourne le terme exponentiel de la formule de Chudovsky"""
    return (-262537412640768000)**q

assert Xq(4) == 4750778730825123872882070905368780411780329837430598270976000000000000
assert Xq(5) == -1247257156019619631959228850474915324796444794921068388944443347008749568000000000000000

def approx_chudovsky(n : int) -> float:
    """Retourne la approximation de pi a partir de la formule de Chudovsky"""
    c : float = 426880 * math.sqrt(10005)
    terme : float= (Mq(n) * Lq(n)) / Xq(n)
    somme : float = 0
    i : int
    for i in range(n + 1):
        somme = somme + ((Mq(i) * Lq(i)) / Xq(i))
    return c * somme**(-1)

assert approx_chudovsky(1) == 3.141592653589793

#3 Suggestion : Optimisation de Chudovsky
def approx_chudovsky_optim(n : int) -> float:
    """Retourne la approximation de pi a partir de la formule de Chudovsky"""
    c : float = 426880 * math.sqrt(10005)
    terme : float= (Mq(n) * Lq(n)) / Xq(n)
    somme : float = 0
    i : int
    for i in range(n + 1):
        somme = somme + ((Mq(n - i) * Lq(n - i)) / Xq(n - i))
    return c * somme**(-1)

assert approx_chudovsky_optim(1) == 3.141592653589793
