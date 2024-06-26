#TME 2
#PIRES_ARAGAO

#Thème 3
#Ex(3.1)
#Question 1
def somme_impairs_inf(n : int) -> int:
    """Retourne la somme des entiers impairs inferieurs ou égaux au paramètre n"""
    somme : int  = 0
    i : int = 0
    while i < n:
        if n % 2 != 0:
            somme = somme + i
        i = i + 1
    return somme

print(somme_impairs_inf(2))

#Ex(3.5)
#Question 1
def fibonacci(n : int) -> int:
    """Retourne le terme en n-ieme position de la sequence de fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


assert fibonacci(3) == 2
assert fibonacci(5) == 5
assert fibonacci(8) == 21

#Question 2
print(fibonacci(8))
#La valeur de fibonacci(8) est 21

#Question 3
def fibo_diff(k : int) -> float:
    """Retourne le k-ieme terme a partir de la division entre elements consecutifs a partir de Fibonacci"""
    if k >= 2:
        return fibonacci(k) / fibonacci(k - 1)

assert fibo_diff(5) == 1.6666666666666667
assert fibo_diff(10) == 1.6176470588235294
assert fibo_diff(41) == 1.618033988749895

#Ex(3.8)
#Question 1
import random

def lancer_de6() -> float:
    """Retourne un nombre aleatoire entre 1 et 6"""
    return int(6 * random.random() + 1)

print(lancer_de6())
assert 1 <= lancer_de6() <= 6

#Question 2
def lancer_de6_seed(grain : int) -> float:
    """Retourne les nombres aleatoires en sequence a partir de la graine grain."""
    random.seed(grain)
    return int(6 * random.random() + 1)

print(lancer_de6_grain(3))

#Ex(4.4)
#Question 1
def somme_cubes(n : int) -> int:
    """ Calcule et retourne la somme de cubes
    """
    
    # S est la variable de la somme des elements
    s : int = 0
    k : int = 0
    while k <= n:
        s = s + (k**3)
        k = k + 1
    return s

assert somme_cubes(0) == 0
assert somme_cubes(1) == 1
assert somme_cubes(2) == 9
assert somme_cubes(3) == 36
assert somme_cubes(4) == 100

#Question 2
def somme_cubes_invariant(n : int) -> int:
    """ Calcule et retourne la somme de cubes en utilisant une autre type de boucle
    """
    
    # S est la variable de la somme des elements
    s : int = 0
    k : int = 0
    for i in range(k, n + 1):
        s = s + (k**3)
        k = k + 1
    return s

assert somme_cubes_invariant(4) == 100
#Elle est utile quand on veut faire l'evaluation a la fin d'execution de la boucle et pas avant.

#Question 3
#Il faut faire 2 multiplications et deux additions fois la valeur de n

#Question 4
def somme_cubes_invariant2(n : int) -> float:
    """ Calcule et retourne la somme de cubes avec une autre expression
    """
    
    # S est la variable de la somme des elements
    s : float = 0
    k : int = 0
    while k <= n:
        s = s + ((k * (k - 1)) / 2)**2
        k = k + 1
    return s

assert somme_cubes_invariant2(4) == 46 #l'expression est 46
