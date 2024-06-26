#ACTIVITE_08_ARAGAO_Henrique

def ouvre_fichier(nom : str) -> List[str]:
    """ renvoie la liste des lignes du fichier texte ./nom.csv """
    with open("./"+nom+".csv", "r") as f:
        return f.readlines()

exemple1 : List[str] = ['"sport";"date";"participants";"vainqueur"\n',
                        '"boxe";2021-09-18;12;"Alice"\n','"boxe";2021-09-25;10;"Alice"\n',
                        '"karate";2021-09-26;19;"Carole"\n','"boxe";2021-10-02;8;"Bob"\n',
                        '"karate";2021-10-03;20;"Carole"\n','"tennis";2021-10-04;3;"Alice"\n',
                        '"boxe";2021-10-09;5;"Alice"\n','"karate";2021-10-10;20;"Damien"\n',
                        '"boxe";2021-10-16;6;"Carole"\n', '"echecs";2021-09-17;120;"Bob"\n',
                        '"echecs";2021-09-24;120;"Bob"\n', '"echecs";2021-10-01;120;"Carole"\n']

#Question 1
def decompose_ligne(li : str, sep : str)-> List[str]:
    """Separe les sous-chaines de la ligne li qui sont entre le separateur sep"""
    li1 : str = li + sep
    nl : List[str] = []
    mot : str = ""
    mot_s : str = ""
    ch : str
    for ch in li1:
        if ch!="\n":
            mot_s = mot_s + ch
            if ch == sep:
                mot = mot_s[:-1]
                nl.append(mot)
                mot_s = ""
    return nl

assert decompose_ligne(exemple1[0], ';') == ['"sport"', '"date"', '"participants"', '"vainqueur"']
assert decompose_ligne(exemple1[3], ";") == ['"karate"', '2021-09-26', '19', '"Carole"']
assert decompose_ligne(exemple1[3], ",") == ['"karate";2021-09-26;19;"Carole"']

#Question 2
def enleve_guillemets(s : str) -> str:
    """Envele les guillemets si s commence et finit par les doubles guillemets '"' et retourne l'interieur de la chaine"""
    ns : str = ""
    i : str
    for i in s:
        if i != '"':
            ns = ns + i
    return ns

assert enleve_guillemets('"sport"') == 'sport'
assert enleve_guillemets('sport') == 'sport'

#Question 3
def enleve_guillemets_ligne(li : List[str]) -> List[str]:
    """Enleve les guillemets doubles des elements de la liste li"""
    return [enleve_guillemets(i) for i in li]

assert enleve_guillemets_ligne(['"sport"', '"date"','"participants"', '"vainqueur"']) == ['sport', 'date', 'participants', 'vainqueur']
assert enleve_guillemets_ligne(['"karate"', '2021−09−26', '19', '"Carole"']) == ['karate', '2021−09−26', '19', 'Carole']

#Question 4
def lignes_propres(lis : List[str], sep : str) -> List[List[str]]:
    """Renvoie une liste de liste de chaines de caracteres correspondants a la decomposition des lignes de lis en elevant les guillemets doubles"""
    z : str;
    li : List[List[str]] = []
    return [[enleve_guillemets(mot) for mot in decompose_ligne(z, sep)] for z in lis]

assert lignes_propres(exemple1, ";") == [['sport', 'date', 'participants', 'vainqueur'], ['boxe', '2021-09-18', '12', 'Alice'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole'], ['echecs', '2021-09-17', '120', 'Bob'], ['echecs', '2021-09-24', '120', 'Bob'], ['echecs', '2021-10-01', '120', 'Carole']]

def cherche_indice(e : str, li : List[str]) -> int:
    """Renvoie le premier indice de li du element e si il apparait dans la liste et None sinon"""
    i : int
    for i in range(0, len(li)):
        if e == li[i]:
            return i

assert cherche_indice("sport", ['sport', 'date', 'participants', 'vainqueur']) == 0
assert cherche_indice("vainqueur", ['sport', 'date', 'participants', 'vainqueur']) == 3
#assert cherche_indice("deces", ['sport', 'date', 'participants', 'vainqueur']) == None

#Question 6
lignes_ex1 : List[List[str]] = lignes_propres(exemple1, ";")

def dictionnaire_compte(lis : List[List[str]], clef : str) -> Dict[str, int]:
    """Renvoie un dictionnaire dont les clofs sont les donnes de clef et les valeurs sont leurs nombre d'occurences"""
    d : Dict[str, int] = {}
    c : int 
    i : int; j : List[str]; z : List[str]
    key : str
    for i in range(0, len(lis[0])):
         c = cherche_indice(clef, lis[0])
    for j in lis[1:]:
        key = j[c]
        d[key] = 0
    for z in lis[1:]:
        key = z[c]
        d[key] = d[key] + 1
    return d

assert dictionnaire_compte(lignes_ex1, "vainqueur") == {'Alice': 4, 'Carole': 4, 'Bob': 3, 'Damien': 1}
assert dictionnaire_compte(lignes_ex1, "sport") == {'boxe': 5, 'karate': 3, 'tennis': 1, 'echecs': 3}

#Question 7
def dictionnaire_somme(lis : List[List[str]], clef : str, valeur : str) -> Dict[str,int]:
    """Renvoie un dictionnaire qui contiens les valeurs correspondents a la clef"""
    d : Dict[str, int] = {}
    c : int 
    i : int; j : List[str]; z : List[str]; v : int; va : int
    key : str
    for i in range(0, len(lis[0])):
         c = cherche_indice(clef, lis[0])
         v = cherche_indice(valeur, lis[0])
    for j in lis[1:]:
        key = j[c]
        d[key] = 0
    for z in lis[1:]:
        key = z[c]
        va = int(z[v])
        d[key] = d[key] + va
    return d

assert dictionnaire_somme(lignes_ex1, "sport", "participants") == {'boxe': 41, 'karate': 59, 'tennis': 3, 'echecs': 360}

print(lignes_ex1)
#2 Suggestion : Courbes temporelles.
def duree(date1 : str, date2 : str) -> int:
    li1 : List[str] = decompose_ligne(date1, '-')
    li2 : List[str] = decompose_ligne(date2, '-')
    d1 : List[int] = []; d2 : List[int] = []
    for i in range(0, len(li1)):
        d1.append(int(li1[i]))
        d2.append(int(li2[i]))
    jour1 : int = d1[2]
    jour2 : int = d2[2]

    mois : Dict[int, int] = {1:31, 2:28, 3:31, 4:30, 35:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    mois2 : int = d2[1]
    mois1 : int = d1[1]

    an1 : int = d1[0]
    an2 : int = d2[0]
    
    duree : int = (an1 - an2)*365 + (mois1 - mois2)*30 + (jour1- jour2)
    if duree <= 0:
        return -duree
    else:
        return duree

print(duree('2022-12-15','2023-12-8'))
