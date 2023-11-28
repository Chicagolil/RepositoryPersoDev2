#4 SCRIPTING - MANIPULATION DE FICHIERS
#1 LECTURE DE FICHIERS____________________________________________________________________________________________________________________________

file = open('data')     #ouverture du fichier 'data.txt' du répertoire courant

file.close()            #ça le ferme le fichier je pense que tu t'en doutes bien

# gestion des erreurs, genre imagine on pointe  vers un fichier qui n'existe pas enft hihi
# exemple

try :
    file = open('data.txt')
    print(file)
    file.close()
except FileNotFoundError:
    print("Fichier Introuvable")
except IOError :
    print('Erreur IO.')

#comment on lit dans un fichier dis moi

try:
    file = open('data.txt')
    print(file.read())   #ICIIII
    file.close()
except FileNotFoundError :
    print("Aie Aie Aie, t'inventes ton nom de fichier, regarde un peu mieux mon petit chat en sucre")
except IOError :
    print("Je sais pas ce que c'est mais t'as une erreur IO., ça veut ptêt dire INTERNATIONAL ORGANISATION ou encore INFLAMMATION ORBITALE")

# le code n'est pas efficace -> il lit tout le contenu d'un seul coup <- solution : lire ligne par ligne

try :
    file = open('data.txt')
    for line in file :
        print(line)
    file.close()
except FileNotFoundError:
    print("Fichier Introuvable")
except IOError :
    print('Erreur IO.')

# Problème encooore, l'affichage des lignes n'est pas optimal, vient du fait que le fichier contient en vérité des caractères de retoure à la ligne etc
# Solution

try :
    file = open ('data.txt', encoding='utf-8')
    for line in file :
        print(line.rstrip())
    file.close()
except FileNotFoundError :
    print('FileNotFoundError')
except IOError :
    print("IoError")

# autres méthodes bonus

# -> .readlines()
file = open('data.txt')
tab =file.readlines()
print(tab[2])
file.close()
# -> .readline
file = open('data.txt')
print(file.readline())
file.close()
# -> .seek(position)
# -> .read(nbBytes)

# Dernier Problème cependant -> dans le cas d'une erreur IO, le fichier ne se ferme pas correctement
# Car il ne lit pas el famoso ligne file.close()
# 2 solutions existent

#1ère -> la pas jolie -> on rajoute la ligne à la mano

try :
    file = open ('data.txt',encoding='utf-8')
    for line in file :
        print(line.rstrip())
    file.close()
except FileNotFoundError :
    print('FileNotFoundError')
except IOError :
    print("IoError")
    file.close()        # BEURK


#2ème -> oh belle belle belle, oh belle -> synthaxe spéciale python qui garantit que les ressources sont correctement gérés

try :
    with open('data.txt') as file :
        for line in file :
            print(line.rstrip())
except FileNotFoundError:
    print("Fichier Introuvable")
except IOError:
    print("Erreur IO.")

# test/curiosité personel avec le module

import time
try :
    with open('data.txt') as file :
        for line in file :
            print(line.rstrip())
            time.sleep(0.5)
except FileNotFoundError:
    print("Fichier Introuvable")
except IOError:
    print("Erreur IO.")

# EXERCISES
#1.1 students.txt

def calculerMoyenne(points):
    return sum(points)/len(points)

try  :
    with open('data-files/students.txt') as fichier :
        lignes = fichier.readlines()
    pointsEtudiants = {}
    for ligne in lignes  :
        elements = ligne.strip().split()
        print(elements)
        if len(elements) != 3 :
            print(f'Erreur dans le format de la ligne : {ligne}')
            continue
        prenom, nom, pointStr = elements
        try :
            points = float(pointStr)
        except ValueError :
            print(f"Erreur de conversion du résultat en nombre pour l'étudiant {nom} {prenom}")
        cleEtu = (prenom,nom)
        if cleEtu not in pointsEtudiants :
            pointsEtudiants[cleEtu] = []
        pointsEtudiants[cleEtu].append(points)

    for cle,points in pointsEtudiants.items() :
        prenom,nom = cle
        moyenne = calculerMoyenne(points)
        print(f"Moyenne de {prenom} {nom} : {moyenne:.2f}")


except FileNotFoundError :
    print("Fichier Introuvable")
except Exception as e :
    print(f"Une erreur s'est produite : {e}")

# 1.2 temp.csv

def calculerMoyenne(temp):
    return sum(temp)/len(temp)


import csv
try :
    with open('data-files/temp.csv', 'r') as fichier :
        lecteurCsv =  csv.reader(fichier)
        lignes = list(lecteurCsv)
    tabMax = []
    tabMin = []
    for i in lignes :
        tabMax.append(float(i[2]))
        tabMin.append(float(i[1]))
    moyMax = calculerMoyenne(tabMax)
    moyMin = calculerMoyenne(tabMin)
    print(f"La Température moyenne des températures maximales : {moyMax:.2f} °C")
    print(f"La Température moyenne des températures minimales : {moyMin:.2f} °C")
except FileNotFoundError :
    print("Fichier Introuvable")
except Exception as e :
    print(f"Une erreur s'est produite : {e}")

# 1.3 swapi.json

import json
import time
try:
    with open('data-files/swapi.json', 'r') as fichier:
        donnees = json.load(fichier)
    print(f"Nombre de personnages : {len(donnees['results'])}")
    for i in donnees['results']:
        print (i['name'])
        time.sleep(1)
except FileNotFoundError:
    print("Fichier Introuvable")


# 1.4 router.cfg
try :
    with open('data-files/router0.cfg','r',encoding='utf-8') as fichier :
        lignes = fichier.readlines()[1:]
    interfaces = {}
    for ligne in lignes :
        elements = ligne.rstrip().split()
        interfaces[elements[0]]=elements[1]

except FileNotFoundError:
    print('Fichier introuvable.')

except IOError:
    print('Erreur IO.')

for interface, ip in interfaces.items() :
    print(f"{interface} -> {ip}")


#2. ÉCRITURE DES FICHIERS_____________________________________________________________________________________
# similaire à la lecture
# juste 2 diff
# indiquer qu'on veut ouvrir le fichier en écriture
# décider si on écrase les donées existantes, ou si on écris par dessus

file = open('data.txt','w')  # 'w' -> write, écrase le contenu existant

file = open('data.txt','a')  # 'a' -> append ,nouveau contenu à la fin

# si un fichier n'existe pas et qu'on essaie de l'ouvrir en écriture, il se crée tout seul

# Exercises
#2.1 students.txt

import csv
from collections import defaultdict

def generer_csv(input_file, output_file):
    # Dictionnaire pour stocker les résultats par étudiant
    resultats_etudiants = defaultdict(list)

    try:
        with open(input_file, 'r') as file:
            lignes = file.readlines()

        # Remplir le dictionnaire des résultats
        for ligne in lignes:
            elements = ligne.strip().split()
            if len(elements) != 3:
                print(f"Erreur dans le format de la ligne : {ligne}")
                continue

            prenom, nom, resultat_str = elements
            try:
                resultat = float(resultat_str)
            except ValueError:
                print(f"Erreur de conversion du résultat en nombre pour l'étudiant {prenom} {nom}")
                continue

            cle_etudiant = (prenom, nom)
            resultats_etudiants[cle_etudiant].append(resultat)

        # Créer et écrire le fichier CSV
        with open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['nom', 'prenom', 'resultat', 'nb_tentatives'])

            for cle, resultats in resultats_etudiants.items():
                prenom, nom = cle
                moyenne = sum(resultats) / len(resultats)
                nb_tentatives = len(resultats)
                csv_writer.writerow([prenom, nom, moyenne, nb_tentatives])

        print(f"Le fichier CSV {output_file} a été créé avec succès.")

    except FileNotFoundError:
        print(f"Le fichier {input_file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
generer_csv('students.txt', 'resultat.csv')


# 2.2

import json
charactèresParGenre= {}
try:
    with open('data-files/swapi.json', 'r') as fichier:
        donnees = json.load(fichier)
    personnages = donnees['results']
    for i in personnages :

        genre = i['gender']
        if genre not in charactèresParGenre :
            charactèresParGenre[genre] = []
        charactèresParGenre[genre].append(i)
except FileNotFoundError:
    print("Le fichier swapi.json n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

try :
    with open('data-files/genderSw.json','w',encoding='utf-8') as fichier:
        fichier.write(json.dumps(charactèresParGenre))
except Exception as e:
    print(f"Une erreur s'est produite : {e}")


#3 SYSTÈME DE FICHIERS ET CHEMINS D'ACCÈS___________________________________________________________________________________________________
# Facile de travailler avec des fichiers ou il faut seulement tendre la main pour les avoir
# Mais Qu'en est il lorsque les fichiers sont à pétaouschnok HEIN
# Solution -> module os

# 3.1

import os

print(f'Répértoire courant de la mtn ou on est la tout de suite :\n{os.getcwd()}\n')
print("Fichier dans ce répertoire : ")
tabFich = os.listdir(os.getcwd())
for i in tabFich :
    print (f'- {i}')

# 3.2

import os
tabFich = os.listdir(os.getcwd())
print(f"tartempion.txt présent dans ce fichier : {'tartempion' in tabFich}")
print(f"swapi.json présent dans ce fichier : {'swapi.json' in tabFich}")

# 3.3

import os
tabfich = os.listdir(os.getcwd())

for i in tabfich :
    cheminComplet = os.path.join(os.getcwd(),i)

    if os.path.isdir(cheminComplet) :
        print(f'{cheminComplet} est un répertoire ')
    else :
        print(f'{cheminComplet} est un fichier ')


# 4 UN PREMIER EXECUTABLE_____________________________________________________________________________________________________
# On passe à pycharm dans les tps wouhooou
# archi méga ultra trop content
# programme de plus grande échelle
# je suis obligé de partir d'ici mais je vais prendre des notes que me paraissent utiles
# à commencer paaaaaaar :


#4.1
# c'est quoi venv :
# c'est un environment virtuel -> créer un espace isolé pour un projet python
## Avantages :
# - Isolation des dépendances : évite les conflits entre différentes versions des bibliothèques et garantit que le projet fonctionnera de manière cohérente sur différentes machines
# - Gestion des versions de Python
# - Nettoyage facile
# - Compatibilité avec d'autres outils

#4.2 création du fichier tp4.py + copier coller

#4.3 executer ce fichier via le terminal

#4.4 créer tp4Bis
# le fait d'importer le tp4 dans tp4Bis fonctionne
# MAIS en éxecutant tp4Bis.py on se rend compte que le script de tp4 est aussi éxecuté
# et ça nananana on en veut pas
# Solution -> if __name__ == '__main__': <code à exécuter lors d'un appel direct du script>
# Directement dans le fion de tp4
# Ca fait qwa ?
# mtn quand jappel tp4Bis.py, le script qui vient de tp4.py HASSOUL, il n'est pas éxécuté merlish
# hamdoulilah on est sauvé

#dans l'autre tp4.py
import os
def euuuhCdesFichiersOuuu():
    tabfich = os.listdir(os.getcwd())

    for i in tabfich :
        cheminComplet = os.path.join(os.getcwd(),i)

        if os.path.isdir(cheminComplet) :
            print(f'{cheminComplet} est un répertoire ')
        else :
            print(f'{cheminComplet} est un fichier ')


if __name__ == '__main__':
    euuuhCdesFichiersOuuu()


# 5 SCRIPT AVEC OPTIONS___________________________________________________________________________________________________________________________________
# arguments positionels -> là ou la position compte
# WALLAH SHERLOCK
# ex(unix): ls -lh *.txt
# on va faire tout pareil pour les scripts python
# genre en arguments tu pourras mettre la taille de ton zigounet
# en tu recevra en fonction une médaille qui aura une immense valeur dans ton ptit coeur
# à part si t'as la médaille en chocolat, ce qui veut dire que t'as vraiment une ptite bite
# ds ce cas, brûle tout de suite ton ordinateur en éspérant que personne ne t'ai vu
# mais tu devras vivre le reste de ta vie avec ce poids sur la conscience
# et si t'es une meuf bah tu peux pas jouer parce que t'as une zezette BEUUURK
# en plus t'as déjà assez à faire dans ta cuisine grosse conne

# on peut utiliser sys.arg maggle
# Bah non enft
# on va utiliser Argparse mais plutôt de nous faire une ptite intro comme elle a fait avec sys.arg
# on va juste aller lire touuuute la doc -> super moyen d'apprendre
# top top, j'ai pas du tout la haine naaaaan
# j'en ai juste marre de lire des docs qui me prennent une heure à lire sur un tp de 2 heures hihi


# 5.1 décidemment elle aime vraiment bcp le 3.3 hein, quoi elle est amoureuse la crâneuse ?
#pas facile facile mais j'ai réussi
# dans myUtils.py

import os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('directory', help='indique moi le chemin de ton repertoire mon ami',default = os.getcwd(),nargs='?')
parser.add_argument('-f','--files',help='si tu veux afficher uniqument les fichier sans les répertoire my amigo', action="store_true")
parser.add_argument('-l','--long',help="tu veux le chemin complet peut-être, alors utilise MOI",action="store_true")
args = parser.parse_args()


tabfich = os.listdir(args.directory)

for i in tabfich :
    if args.long:
        i = os.path.join(args.directory, i)

    if args.files and os.path.isdir(i):
        continue
    else:
        print(i)


# TP 04 Dans la poquette FINII ________________________________________________________________________________________________________________________________________________________________