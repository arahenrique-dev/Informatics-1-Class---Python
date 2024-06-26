#Henrique ARAGAO
#21304445

#Ecercice 4.6
#Question 1
def factorielle_compte(n : int) -> int:
    """Retourne le nombres de multiplications effectuées par une factorielle"""
    k : int = 1
    f : int = 1
    nb_ops : int = 0

    while k < n:
        f = f * k
        k = k + 1
        nb_ops = nb_ops + 1
    print("Nombre d'operations = ", nb_ops)
    return nb_ops

assert factorielle_compte(5) == 4
assert factorielle_compte(7) == 6
