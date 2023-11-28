# Salut les loosers
# Manipulation de variables
# 1

import math
n = float(input("Veuillez entrer un nombre positif : \n "))

if n <= 0:
    print("Le nombre entré n'est pas positif")
else:
    surface = math.pi * n**2  # Vient de la librairie qu'on a importé
    print(f"La surface du cercle de rayon {n} est : {surface}")


# 2
l = float(input("Veuillez entrer un nombre positif"))
L = float(input("Veuillez entrer un nombre positif"))

if l <= 0 or L <= 0:
    print("Le nombre entré n'est pas positif")
else:
    perimetre= 2*l + 2*L
    print(f"Le périmètre du Rectangle de Largeur {L} et de Longeure {l} est de {perimetre}")

# 3
demande = input("Veuillez entre Soit True Soit False : \n")

if demande.lower() == "true":
    print("False")
elif demande.lower == "False":
    print("True")
else:
    print("La demande est invalide Fdp")

# 4

egaux1 = float(input("Entrez un premier chiffre"))
egaux2 = float(input("Entrez un deuxième chiffre"))

if egaux1 == egaux2:
    print("True")
else:
    print("False")

# 5

entier1 = int(input("Entrez un premier entier"))
entier2 = int(input("Entrez un deuxième entier"))

print(entier1>=entier2)

# 6

test1 = (1.121515 + 3)   # C
test2 = "B"+"I"+"T"+"E"    # C
test3 = "B"+ 3    # Erreur

# STRUCTURES DE CONTROLE _____________________________________________________________________

# 1

ageUti = int(input("Veuillez entrer votre âge svp"))

if ageUti >= 18:
    print("Majeur")
else:
    print("Mineur")

# 2

entierUti = int(input("Veuillez rentrer un entier svp : \n"))

if (entierUti % 2) == 0:
    print("Pair")
else:
    print("Impair")

# 3

valeur = int(input("Veuillez rentrer un premier Entier positif : \n"))
increment = valeur
if valeur >= 0:
    while True :
        valeur = int(input(
            "Veuillez rentrer un autre entier pour l'additioner ou un Zéro pour afficher la somme et arrêter le programme \n"))

        if valeur > 0:
            increment += valeur

        elif valeur == 0:
            print(f"La somme de toutes les valeurs que vous avez entrées est de : {increment}\n")
            break

        else:
            print("Nombre Négatif entré : invalide \n")
            break
else:
    print("Bon Frangin fais un effort j'ai dis Positif")

print("Progamme Terminé")

# 4

entierDiv2 = int(input("Entre un chiffre et je te dis combien de fois ton chiffre peut-être divisée par deux \n"))
compteur = 0

while entierDiv2 % 2 == 0:
    entierDiv2 /= 2
    compteur += 1

print(f"Ton chiffre peut être divisé par deux {compteur} fois ")

# 5

racine = float(input("Veuillez Entrer un nombre entier : \n"))

if racine == int(racine):
    if racine >= 0 and int(racine**(1/2)) == (racine**(1/2)):
        resultat=int(racine**(1/2))
        print(f"Le racine carré est égale à : {resultat}")
    elif racine < 0:
        print("T'as du rentrer un nombre négatif mon copain")
    else:
        flotant = float(racine**(1/2))
        print(f"Le résultat ne donne pas un entier mais un flotant qui est en l'occurence : {flotant}")
else:
    print(f"Jtai demandé Un entier et toi tu me mets {racine} t'es con ou quoi? ")

# 6 (un peu compliqué l'avant dernière ligne : a revoir )

pyramide = int(input("Rentre un entier Positif et jte fais une pyramide avec \n"))
if pyramide < 0:
    print("Le chiffre est négatif : FAUX")
else:
   for i in range(1, pyramide+1):
        ligne = ' '.join(str(i) for _ in range(i))
        print(ligne)

# TP1 Partie 2 __________________________________________________________________________________________________________________________
# Exercises sur les chaînes de caractères
# 1
chaineUti = input("Veuillez Entrer Une Chaîne svp\n")
if "toto" in chaineUti.lower():
    print("OK")
else:
    print("Toto est perdu alors")

# 2

chaine = input("Entrez votre phrase préférée de toutes les phrases du monde\n")

occur = chaine.lower().count("a")

print(f"Le nombre de 'a' dans \n '{chaine}' \nest au nombre de {occur}")

# 3

majChaine = input("Attention votre phrase va vous crier dessus \n").upper()
print(f"{majChaine}!!!!")

# 4

chaine1 = input("Veuillez entrer une Phrase\n")
chaine2 = input("Veuillez entrer une autre phrase, t'auras peut-être un cadeau si tu écrit l'exacte inverse de ta première phrase\n")
if chaine1.lower() == chaine2[::-1].lower():
    print(f"""Bien joué beaugoss \n{chaine1} \net \n{chaine2}\nsont parfaitement inversées : \nTiens t'as le droit à un bonbon""")
else:
    print(f"Tu m'étonnes que t'es le mal aimé de la famille petit merde pleine de caca")

# 5 Je ne Comprends Pas Vraiment L'ex
#1ère manière
nom = "Devroye"
prénom = "Lilian"
cours = "Devéloppement informatique"
iteCours = 2

print(f"Je me nomme {prénom} {nom} Et je participe au cours de {cours}{iteCours}")

#2ième manière
mots = ["Je","me","nomme","Devroye","Lilian","Et","Je","Particpe","au","cours","de","Développement","Informatique","II"]
phrase = ' '.join(mots)

#EXERCISES SUR LES FONCTIONS
# 1
#FRANCHEMENT FLEMME JLE FERAI PEUT ETRE PLUS TARD

#2

def carre(nombre):
    resultat=nombre**2
    return resultat

nombre = 5
end = carre(nombre)
print(f"Le carré de {nombre} est : {end}")

# 3
def max(a, b, c):
    max = 0
    if a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    else:
        max = c

    return max
a=int(input("Entrer un premier nombre\n"))
b=int(input("Entrer un 2ième nombre\n"))
c=int(input("Entrer un 3ième nombre\n"))
maxi= max(a,b,c)

print(f"Le plus grand nombre entre {a}, {b} et {c} est : {maxi}")

# 4
def factorielle(nombre):
    fact=1
    for i in range(1,nombre+1):
        fact *= i
    return fact

jtagresse = factorielle(int(input("Tiens je sais que tu t'en fous mais Donne moi un nombre et je te fais sa factorielle")))
print(f"La factorielle Du chiffre que tu m'as donné est {jtagresse}")

#5
def apprecitation(resultat,total):
    rapport = resultat/total
    if rapport >= 0.8:
        return "A"
    elif rapport >= 0.7:
        return "B"
    elif rapport >= 0.6:
        return "C"
    elif rapport >= 0.5:
        return "D"
    elif rapport >= 0.3:
        return "E"
    else:
        return "F"

note = int(input("Donne moi ta note !!\n"))
total = int(input("Il était sur combien ce test ?\n"))

final=apprecitation(note,total)

print(f"Ton année est résumée à une seule lettre qui est : {final}")