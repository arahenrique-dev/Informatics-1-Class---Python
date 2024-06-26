#Henrique PIRES ARAGAO
#Numero Étudiant: 21304445

#Activite 01 - Cadavres Exquis
#1 Partie Guidée : Cadavre exquis basique.
#Question 1
def sujet(n : int) -> str:
    """Precondition: le nombre doit etre entre 1 et 6
    Retourne le sujet à partir du nombre choisi"""
    if n == 1:
        return "Henrique"
    elif n == 2:
        return "Maria"
    elif n == 3:
        return "Pierre"
    elif n == 4:
        return "Pauline"
    elif n == 5:
        return "Chaves"
    elif n == 6:
        return "Chiquinha"

assert sujet(3) == "Pierre"
assert sujet(5) == "Chaves"

#Question 2
def verbe(n : int) -> str:
    """Precondition: le nombre doit etre entre 1 et 6
    Retourne le verbe d'action à partir du nombre choisi"""
    if n == 1:
        return "joue"
    elif n == 2:
        return "mange"
    elif n == 3:
        return "visite"
    elif n == 4:
        return "achete"
    elif n == 5:
        return "écoute"
    elif n == 6:
        return "bois"

def cod(n : int) -> str:
    """Precondition: le nombre doit etre entre 1 et 6
    Retourne le complement d'objet direct à partir du nombre choisi"""
    if n == 1:
        return "le foot"
    elif n == 2:
        return "du chocolat"
    elif n == 3:
        return "le musée"
    elif n == 4:
        return "une chemise"
    elif n == 5:
        return "une chanson"
    elif n == 6:
        return "du café"

def lieu(n : int) -> str:
    """Precondition: le nombre doit etre entre 1 et 6
    Retourne le lieu où une action se passe à partir du nombre choisi"""
    if n == 1:
        return "au stade"
    elif n == 2:
        return "chez-soi"
    elif n == 3:
        return "à Paris"
    elif n == 4:
        return "au magasin"
    elif n == 5:
        return "au concert"
    elif n == 6:
        return "dans un restaurant"

assert verbe(2) == "mange"
assert verbe(4) == "achete"
assert cod(3) == "le musée"
assert cod(6) == "du café"
assert lieu(1) == "au stade"
assert lieu(5) == "au concert"



#Question 3
def phrase(nb_sujet : int, nb_verbe : int, nb_cod : int, nb_lieu : int) -> str:
    """Precondition: le nombres doivent etre entre 1 et 6
    Retourne une phrase avec les mots a partir des nombres choisis"""
    return sujet(nb_sujet) + " " + verbe(nb_verbe) + " " + cod(nb_cod) + " " + lieu(nb_lieu)

assert phrase(2, 2, 2, 2) == "Maria mange du chocolat chez-soi"
assert phrase(3, 6, 1, 2) == "Pierre bois le foot chez-soi"

#Question 4
import random

def de6() -> int:
    """Renvoie un nombre entier aléatoire parmi 1 et 6"""
    return int(6*random.random() + 1)

assert de6() >= 1 and de6() <= 6

#Question 5
def phrase_aleatoire() -> str:
    """Donne une phrase aleatoire composant des valeurs mis aux autres fonctions sujet, verbe, cod et lieu"""
    return sujet(de6()) + " " + verbe(de6()) + " " +  cod(de6()) + " " + lieu(de6())

print(phrase_aleatoire())

#Suggestion : Cadavre exquis plus riches.
def conj(n : int) -> str:
    """Precondition: le nombre doit etre entre 1 et 6
    Retourne une conjunction à partir du nombre choisi"""
    if n == 1:
        return "mais"
    elif n == 2:
        return "et"
    elif n == 3:
        return "donc"
    elif n == 4:
        return "au magasin"
    elif n == 5:
        return "car"
    elif n == 6:
        return "ou"

def phrase_suggestion(nb_sujet : int, nb_verbe : int, nb_cod : int, nb_lieu : int, nb_conj : int) -> str:
    """Precondition: le nombres doivent etre entre 1 et 6
    Retourne une phrase avec les mots a partir des nombres choisis"""
    return sujet(nb_sujet) + " " + verbe(nb_verbe) + " " + cod(nb_cod) + " " + lieu(nb_lieu) + " " + conj(nb_conj) + " " + sujet(nb_sujet) + " " + verbe(nb_verbe) + " " + cod(nb_cod)

print(phrase_suggestion(2, 4, 5, 6, 4))
