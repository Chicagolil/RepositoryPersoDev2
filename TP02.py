# Salut les gros Loosers
# TP2 : Les Containers Python
# J'ai pas encore fini le tp1 hihi
# C'est bon j'ai fini hihi
# 1: LES LISTES
# 1.1

liste1 = []
for i in range(1, 101):
    liste1.append(i)
print(liste1)

# OU

liste1 = list(range(1, 101))
print(liste1)

# 1.2
liste2 = []
for i in range(50, 201, 5):
    liste2.append(i)
print(liste2)

# OU

liste2 = list(range(50, 201, 5))
print(liste2)

# 1.3

liste3 = []
for i in range(15, 21):
    liste3.append(liste2[i])
print(liste3)

# OU avec slicing

liste3 = liste2[15:21]
print(liste3)

# 1.4
liste3 = ['jambon', 'sel', 'miel', 'confiture', 'beurre']
del liste3[1:3]
liste4 = liste3
print(liste4)

# OU

liste3 = ['jambon', 'sel', 'miel', 'confiture', 'beurre']
nouvelle_liste = liste3[:1] + liste3[3:]

# 1.5 tests

listeT1 = ['jambon', 'sel', 'miel', 'confiture', 'beurre']

listeT2 = [1, 47, 65, 20, 41, 78, 49, 35, 26, 85, 59, 2, 4, 7]

listeT1.sort()              # Modifie la liste => croissante
listeT2.sort()              # Modifie la liste croissante
listeT1.sort(reverse=True)  # Modifie la liste liste décroissante
nouvelle_liste = sorted(listeT1) # Crée une nouvelle liste croissante : marche aussi sur les cahines de caractères
triLongeur = sorted(listeT1, key=len)    # Crée une nouvelle liste et tri les mots en fonction de leur longeur
triLongeur = sorted(listeT2, key=len)         # ERREUR, les chiffres n'ont pas de "len"


mixte = [10, "orange", 5, "pomme", 8, "banane"]
mixte.sort()                                # ERREUR, .sort() tente de comparer des éléments de types différents
nveauMixte= sorted(mixte)                       # ici, ça ne marche pas non plus

nombres = [3, 1, 4, 1, 5, 9, 2, 6, 16]
resultat = sorted(nombres, key=lambda x: x % 2) # on crée une petite fonction lambda qui va trier en fonction de la parité de la liste

# 1.6
def sommeListe(liste):
    somme = 0
    for i in range(0,len(liste)):
        somme += liste[i]
    return somme


nombres = [3, 1, 4, 1, 5, 9, 2, 6, 16]
resultat = sommeListe(nombres)
print(f"La somme de tous les index de la liste {nombres} est : {resultat}")
# Ici , on ne peut pas rentrer une liste de strings en tant que paramètre à cause du "somme = 0" pcq on ne peut pas add des strings avec des int


# 1.7

liste3 = ['jambon', 'sel', 'miel', 'confiture', 'beurre']

phrase = ' le gros séparateur aussi gros que mon zizi '.join(liste3)
print(phrase)

#OU
separateur = '\n'
phrase = separateur.join(liste3)
print(phrase)

# 2.LES TUPLES________________________________________________________________________________________________________________________________________________

# 2.1
def creerTuplue(chaine):
    nouveauTuple = tuple(chaine)
    return nouveauTuple

maPhrase = "C'est pas non plus la honte d'avoir un ptit zizi "
monTuple = creerTuplue(maPhrase)
print(monTuple)

# 2.2

mon_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
monElement = mon_tuple[1][1]
print(monElement)

# 2.3

mon_tuple = (1,2,3,4,5,6)
a, b, c, d = mon_tuple
print(f"{a}\n{b}\n{c}\n{d}")

# 2.4

def compteurDeTout(chaine):
    compteurM = 1
    compteurL = 0
    for i in range(0, len(maPhrase)):
        if maPhrase[i] == " ":
            compteurM += 1
        else:
            compteurL += 1
    monResultat = (compteurM,compteurL)
    return monResultat

maPhrase = "J'ai un q.i pas mal beaucoup mais je pense que c'est quand même faux ce que j'ai fait"
monTuple = compteurDeTout(maPhrase)
print(f"La Phrase que tu a rentrée contient {monTuple[0]} mots et {monTuple[1]} lettres")

# OU

def compteurDeTout(chaine):
    mots = len(chaine.split())
    lettres = sum(caractere.isalnum() for caractere in chaine)
    monResultat = (mots,lettres)
    return monResultat

maPhrase = "J'ai un q.i pas mal beaucoup mais je pense que c'est quand même faux ce que j'ai fait"
monTuple = compteurDeTout(maPhrase)
print(f"La Phrase que tu a rentrée contient {monTuple[0]} mots et {monTuple[1]} lettres")

# OU

def compteurDeTout(chaine):
    mots = len(chaine.split())
    maListe = []
    for i in chaine:
        if i.isalnum():
            maListe.append(i)
    resultat = len(tuple(maListe))
    final = (resultat,mots)
    return final

maPhrase = "J'ai un q.i pas mal beaucoup mais je pense que c'est quand même faux ce que j'ai fait"
monTuple = compteurDeTout(maPhrase)
print(f"La Phrase que tu a rentrée contient {monTuple[0]} mots et {monTuple[1]} lettres")

# 2.5

from operator import itemgetter

monTuple = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
resultat = tuple(sorted(monTuple, key=itemgetter(1), reverse=True))
print(resultat)

# 2.6

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
# Ca Marche, Pourquoi ?
# Parce on ne change pas le tuple en tant que tel mais la liste qui est contenue dans le tuple

# 3 : LES DICTIONNAIRES


# 3.1

mon_dict = {
   "classe":{
      "etudiant":{
         "nom":"Arthur",
         "resultats":{
            "admin":70,
            "python":80
         }
      }
   }
}

resultat = mon_dict["classe"]["etudiant"]["resultats"]["python"]
print(f"Le résultat d'arthur dans son cours sur python est de {resultat}\net c'est côté sur 1000 donc arthur est une grosse merde\nboo le gros nullos")


# 3.2

def contains_value(dict, val):
   for valeur in dict.values():
      if valeur == val:
         return True
      else:
         return False

# ne marche pas sur tout les dictionnaires
mon_dict = {"a": 1, "b": 2, "c": 3}
# sur celui là oui
mon_dict = {
   "classe":{
      "etudiant":{
         "nom":"Arthur",
         "resultats":{
            "admin":70,
            "python":80
         }
      }
   }
}
# mais sur celui là non


# 3.3

cles = ['Dix', 'Vingt', 'Trente']
valeurs = [10, 20, 30]

dictNveau = dict(zip(cles,valeurs))
print(dictNveau)

# 3.4

resultats = {
    'Arthur' : 80,
    'Xavier' : 50,
    'Gérard' : 38,
    'Clémentine' : 20,
    'Emilie' : 75,
    'Gaston' : 83,
    'Capucine' : 87
}

tri = dict(sorted(resultats.items() , key = lambda item : item[1]))

# 4 LES ENSEMBLES

# 4.1

ensemble = {"Jaune", "Orange", "Noir"}
liste = ["Bleu", "Vert", "Rouge"]
ensemble.update(liste)
print(ensemble)

# 4.2

ensemble1 = {1, 2, 3}
ensemble2 = {1, 2, 3, 4, 5}

print(ensemble1.issubset(ensemble2))
print(ensemble2.issuperset(ensemble1))
print(ensemble2.issubset(ensemble1))

# 4.3
# MA SOLUTION, CA MARCHE
ma_liste = [1, 2, 3, 7, 4, 5, 8, 4]

def doublons(list):
    listetriee = sorted(list)
    compteur = 0
    for i in range(0, len(listetriee)):
        if listetriee[i] == listetriee[i - 1]:
            compteur += 1
        else:
            compteur = compteur
    if compteur > 0:
        return True
    else:
        return False

print(doublons(ma_liste))

# UNE SOLUTION MOINS GALERIENNE

ma_liste = [1, 2, 3, 7, 4, 5, 8]

def doublonsV2(list):
    ensemble = set()
    for element in list :
        if element in ensemble:
            return True
        ensemble.add(element)
    return False

# 5 FONCTIONS NOTIONS AVANCEES
# PARAMETRES PAR DEFAUT
def print_list(ma_liste, nb_elem_par_ligne=1):
    ligne = ""
    for i in range(len(ma_liste)):
        ligne = ligne + " " + ma_liste[i]
        if ((i + 1) % nb_elem_par_ligne) == 0:
            print(ligne)
            ligne = ""


def printListe(liste, elem = 1):                #Celle là est fausse et j'ai enfin capté pq
    phrase = ""
    for i in range(0, len(liste)):
        phrase = phrase + " " + liste[i]
        if i+1 == elem:                         #L'erreur est ici , la condition ne va être vraie qu'une seule fois, car i continue d'être incrémenté
            print(phrase)
            phrase = ""


ma_liste = ["elem_1", "elem_2", "elem_3", "elem_4"]

print("Un élément par ligne")
print_list(ma_liste)

print("Deux éléments par ligne")
print_list(ma_liste,2)

#ARGUMENTS NOMMéS

def print_list(ma_liste, nb_elem_par_ligne=1, bullet=""):
    ligne = ""
    for i in range(len(ma_liste)):
        ligne = ligne + " " + ma_liste[i]
        if ((i + 1) % nb_elem_par_ligne) == 0:
            print(bullet + " " + ligne)
            ligne = ""
    print(bullet + " " + ligne)  # J'ai l'impression que cette ligne ne sert à rien

print_list(ma_liste, "-") # ERREUR, je crois
print_list(ma_liste, bullet="-")

# LISTE D'ARGUMENTS DE TAILLE ARBITRAIRE


def concat(*args):              #Crée un tuple
    return ", ".join(args)

print(concat("2TL1", "2TL2", "2TM1"))


mes_arguments = (2, 10, 2)
print(*mes_arguments)
for i in range(*mes_arguments):
    print(i)

# UTILISER UN DICTIONNAIRE POUR LES ARGUMENTS NOMMéS

ma_liste = ["elem_1", "elem_2", "elem_3", "elem_4", "elem5"]
mon_dict = {'nb_elem_par_ligne':2, 'bullet':'*'}
print_list(ma_liste, **mon_dict)

#SYNTHESE FONCTION 2.0

def ma_fonction(parametre_normal,
                parametre_avec_default="valeur par défaut",
                *args,
                **kwargs):
    pass

    #CETTE FONCTION EST UN EXEMPLE ET NE FAIS RIEN CONCRETEMENT

#5.1

def somme(*args):
    total = sum(args)
    return total

print(somme(1, 2, 3, 4, 5))


#5.2

def num_args(*args):
    return len(args)

nombreArguments = num_args(1, 2, 3, "quatre", "cinq")
print(f"Nombre d'arguments : {nombreArguments}")


#FINIIIII ENFIN MASHALLAH
