# TP06- SUBPROCESS
# QUESQUEC ?
# pouvoir utiliser des commandes de lignes de commandes directement depuis un script python
# librairie subprocess
# Le module subprocess vous permet de lancer de nouveaux processus,
# les connecter à des tubes d'entrée/sortie/erreur, et d'obtenir leurs codes de retour.
# fontion run ()
# Lorsque vous travaillez avec les subprocess sous Windows, il est nécessaire de définir
# l'attribut shell comme étant True lorsque vous utilisez les utilitaires 'built-in' de
# l'invite de commande (ex : dir).

# 1. Première éxecution_______________________________________________________________________________________________________________________________________

# 1.1

import subprocess
subprocess.run("dir", shell=True, )

# 2. AFFICHER LE RESULTAT DE LA COMMANDE __________________________________________________________________________________________________________________________

# 2.1
#Affichez l'attribut stdout de mySub en console
import subprocess
mySub = subprocess.run('dir', shell=True,stdout = subprocess.PIPE) # subprocess.PIPE -> capture_output
print(mySub.stdout)

# Test avec universal_newlines
# Moins le chaos que la commande juste au dessus

import subprocess
mySub = subprocess.run('dir', shell=True,stdout = subprocess.PIPE,text=True) #text =True -> universal_newlines
print(mySub.stdout)

import subprocess
mySub = subprocess.run('dir', shell=True,stdout = subprocess.PIPE,universal_newlines=True) #text =True -> universal_newlines
print(mySub.stdout)

# text et universal_newlines c'est la même chose enft

# ajout d'un paramètre supp à la commande

# 1ère
import subprocess
mySub= subprocess.run(['dir','/a'],shell=True,stdout=subprocess.PIPE,text=True)
print(mySub.stdout)

# 2ième
import subprocess
mySub = subprocess.run("dir /a",shell=True,text=True, stdout=subprocess.PIPE)
print(mySub.stdout)

# les deux fonctionnent pareil mais il faut obligatoirement un shell=True contrairement à ce
# qui est mis dans le tp -> concerne les systèmes UNIX

#lister un fichier qui n'existe pas

import subprocess
mySub = subprocess.run('dir lesdsfd',shell=True,stdout = subprocess.PIPE,stderr=subprocess.PIPE,text=True)

print("Sortie Standard (stdout) ")
print(mySub.stdout)

print("\nSortie D'erreur (stderr):")
print(mySub.stderr)

# 2.2
# oups depuis tout à l'heure je me trompais sur le capture_output
# on va faire les choses dans l'autre sens alors, flemme de tout recommencer
# avec capture_output

import subprocess
mySub = subprocess.run('dir lesdsfd',shell=True,capture_output=True,text=True)

print("Sortie Standard (stdout) ")
print(mySub.stdout)

print("\nSortie D'erreur (stderr):")
print(mySub.stderr)

# returncode -> attribut de l'objet mySub
# Comment le voir ? Soit:
print(mySub) #-> il traîne quelquepartdans les paranthèses
#SOIT
print(mySub.returncode) # -> directement affiché, plus simple quand même hein

# a quoi il correspond
# returncode = 0 -> pas d'erreur dans la commande
# returncode = 1 -> il y a une entrée sur stderr donc on a mal fait qqch

# commment rediriger sterr vers stdout pour se faciltier un peu la vie
# Solution :

import subprocess
mySub = subprocess.run('dir sdfs',shell=True,stdout = subprocess.PIPE, stderr=subprocess.STDOUT,text=True)
print(mySub.stdout) # -> stdout + stderr
print(mySub.stderr) # -> il n'y a plus rien ici vu qu'on a redirigé cette sortie vers stdout
    # -> affiche : None

#3 FOURNIR UN INPUT A UN PROCÉSSUS
# Cette fonctionnalité est un peu limité sur windows
# on va pas faire comme dit dans le cours, puisqui'il est rédigé par une UNIXgirl
#3.1
import subprocess
texteRecherche = """
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
        options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
        inet 127.0.0.1 netmask 0xff000000 
        inet6 ::1 prefixlen 128 
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
        nd6 options=201<PERFORMNUD,DAD>
    gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
    stf0: flags=0<> mtu 1280
    ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3e:22:fb:60:4a:5f 
        media: autoselect
        status: inactive
    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3c:22:fb:60:4a:5f 
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect (<unknown type>)
        status: inactive
    en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
        options=460<TSO4,TSO6,CHANNEL_IO>
        ether d2:c0:77:f9:9c:00 
        media: autoselect <full-duplex>
        status: inactive"""

process = subprocess.Popen('findstr flag', stdin=subprocess.PIPE,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                text=True)



output, errors = process.communicate(input=texteRecherche)

print("Resultat De la recherche :")
print(output)

# mais on peut aussi faire autrement parce j'ai pas tout capté de la commande .Popen()
# on va faire avec ce bon vieux .run()

import subprocess

texteRecherche = """
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
        options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
        inet 127.0.0.1 netmask 0xff000000 
        inet6 ::1 prefixlen 128 
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
        nd6 options=201<PERFORMNUD,DAD>
    gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
    stf0: flags=0<> mtu 1280
    ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3e:22:fb:60:4a:5f 
        media: autoselect
        status: inactive
    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3c:22:fb:60:4a:5f 
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect (<unknown type>)
        status: inactive
    en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
        options=460<TSO4,TSO6,CHANNEL_IO>
        ether d2:c0:77:f9:9c:00 
        media: autoselect <full-duplex>
        status: inactive"""

result  = subprocess.run('findstr flag',text=True, stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE,
                                                        input=texteRecherche)

print("Resultat de la recherche: ")
print(result.stdout)

# PIPE ENTRE PROCESSUS(e(s)) -> écriture inclusive maggle
# on peut evidemment connecter plusieurs processus entre eux
# De la magie ??
# NON
# De l'INFORMATIQUE -> explosion , gens choqués , super ordinateur Xpro 3000 superBoostSuperMax

# 4.1

import subprocess
ipConfig = subprocess.run('ipconfig',shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
mySub2 = subprocess.run('findstr Ethernet',shell=True,text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,input=mySub.stdout)
print(mySub2.stdout)

fin = "voila maintenant on va passer aux exercises mais avant ça, je vais aller manger"

# 5 EXERCISES____________________________________________________________________________________________________________________________________
# 5.1

import subprocess
cheminJeu='C:\Program Files\Epic Games\\rocketleague\Binaries\Win64\\RocketLeague.exe'
subprocess.run([cheminJeu])

#5.2
#compte le nombre de lignes
# une seule commande
import subprocess
fichier= 'D:\#5_LILIAN\#2_EPHEC\\2ième\Dev2\\loremIpsum.txt'
mySub = subprocess.run(f'type {fichier} | find /c /v ""',shell=True, stdout=subprocess.PIPE ,text=True, stderr =subprocess.STDOUT)
print(mySub.stdout)

# deux commandes

import subprocess
fichier= 'D:\#5_LILIAN\#2_EPHEC\\2ième\Dev2\\loremIpsum.txt'
texte = subprocess.run(f'type {fichier}' ,shell=True, text=True , stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
nbredelignes = subprocess.run('find /c /v ""', input=texte.stdout, text=True, shell=True, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
resultat =  nbredelignes.stdout.rstrip()
print(f'{resultat} lignes ')


# on refait appel aux compétences du tp04 pour avoir le nombre de mots

fichier = 'D:\#5_LILIAN\#2_EPHEC\\2ième\Dev2\\loremIpsum.txt'
with open(fichier) as fichier:
    elements = fichier.readlines()
    tab=[]
    for i in elements:
        o = i.rstrip().split()
        for e in o :
            tab.append(e)

    print(len(tab))

# 5.3

import subprocess
def trouverLesIpDuTraceRt(destination):
    listeIp =[]
    liste2 = []
    traceRoute = subprocess.run(f'tracert {destination}',shell=True, stdout = subprocess.PIPE,text=True)
    jsp = traceRoute.stdout.rstrip().split()
    print(jsp)
    print(traceRoute.stdout)
    for i in jsp :
        if len(i) > 15 :
            listeIp.append(i.replace('[', ''))
    for i in listeIp:
        liste2.append(i.replace(']',''))

    return(liste2)

#ça marche mais c'est hyper bancal
#on refait mtn mais en mode hyper propre avec gestion d'erreurs et tout



import subprocess
import ipaddress
def trouverlesAddressesIp(destination):
    tracert = subprocess.run(f'tracert {destination}',shell=True, stdout = subprocess.PIPE,text=True)
    if tracert.returncode == 0 :
        lignes=tracert.stdout.splitlines()
        hop = lignes[4:]

        ipadd=[]
        for o in hop:
            elements = o.split()
            for element in elements :
                try :
                    ip = ipaddress.IPv6Address(element)
                    ipadd.append(str(ip))
                    break
                except ipaddress.AddressValueError:
                    pass

        return ipadd


    else :
        print("Erreur lors de l'exécution de tracert.")
        return None

print(trouverlesAddressesIp("google.com"))


# 5.4  BOnus j'ai fait aucun effort
# j'ai pas les addresses ip mais toute la ligne

import subprocess
import ipaddress

def traceroute(target):
    process = subprocess.Popen(["tracert", target], stdout=subprocess.PIPE, text=True)

    while True:
        line = process.stdout.readline()
        if not line:
            break
        else:
            line = line.strip()
            print(line)


            elements = line.split()
            for element in elements:
                try:
                    ip = ipaddress.IPv4Address(element)
                    print(f"Adresse IP du saut : {ip}")
                    break
                except ipaddress.AddressValueError:
                    pass

    process.wait()

target_address = "google.com"
traceroute(target_address)

#FINIIIIIIIIIIIIIIIIIIIII_________________________________________________________________________________________________________________________

# ah bah nn enft j'ai envie de crever, -> TP06 Partie 2 : UML

#1.MODÉLISATION____________________________________________________________________________________________________________________________________
# j'ai griffoné mes réponses dans un ptit cahier tout mimi
# 2.DE L'UML AU PYTHON
# rappel :
"""
*   Une relation d'utilisation se traduit par l'utilisation d'un classe 
    par une autre comme variable locale ou comme paramètre de méthode 

*   Une relation d'association implique qu'une classe est utilisée comme 
    variable d'instance d'une autre classe. Cette relation peut éventuellement être 
    bidirectionnel 

*   Une relation d'aggrégation implique qu'une classe est utilisée comme variable 
    d'instance d'une autre classe, et en est un composant fort. Cependant, le cycle
    de vie de l'aggrégat n'est pas lié au cycle de vie de la classe aggrégeante. Cela 
    se traduit par le fait que l'aggrégat est instancié avant d'être assigné comme variable 
    d'instance. Il est passé en paramètre du constructeur

*   Une relation de composition implique qu'une classe est utilisée comme variable 
    d'instance d'une autre classe, et en est un composant fort, lié à son cycle de 
    vie. Cela se traduit par la création de l'instance du composant dans le constructeur 
    de la classe composite.

*   Une relation d'héritage se traduit tout simplement par le mécanisme d'héritage en Python.

"""

#2.1 Animaux
# Les Animaux sont des herbivores, soit des carnivores.
# On trouve par exemple des lapins, des moutons, des lions,...
# Un animal est composé d'une tête d'un corps et de membres
# Chaque animal possède un habitat.
class Animal :
    def __init__ (self,tete,corps,membres,habitat):
        self.tete = tete
        self.corps = corps
        self.membres = membres
        self.habitat = habitat

    def __str__(self):
        return f"Cet animal a une tête {self.tete}, un corps {self.corps}, {self.membres} membres, et vit dans un habitat {self.habitat}"

class Herbivores(Animal):
    def __init__(self,tete,corps,membres,habitat,diet='Herbivore'):
        super().__init__(tete,corps,membres,habitat)
        self.diet = diet

    def __str__(self):
        return super().__str__() + f". Il est un {self.diet}."

class Carnivores(Animal):
    def __init__(self,tete,corps,membres,habitat,diet='Carnivore'):
        super().__init__(tete, corps, membres, habitat)
        self.diet =diet
    def __str__(self):
        return super().__str__()+f'. Il est un {self.diet}'


lapin = Herbivores("petite", "pelucheux", 4, "prairie")
lion = Carnivores("majestueuse", "musclé", 4, "savane")


print(lapin)
print(lion)

# 2.2 Clasee
# Une classe est définie par un professeur et ses élèves (max30). Le professeur
# et ses élèves ont tous un dossier personel dans l'école reprenant leur état civil
# et leurs coordonnées.

class Personne :
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
    def afficherDossier(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Âge: {self.age}, Adresse: {self.adresse}"

class eleve(Personne):
    def __init__(self,nom,prenom,age,adresse,niveau):
        super().__init__(nom,prenom,age,adresse)
        self.niveau = niveau
    def __str__(self):
        super().afficherDossier()+f'. Il est en {self.niveau}'

class professeur(Personne):
    def __init__(self,nom,prenom,age,adresse,matiere):
        super().__init__(nom,prenom,age,adresse)
        self.matiere = matiere

    def __str__ (self):
        super().afficherDossier() + f' Il enseigne {self.matiere}'


class classe():
    def __init__(self,professeur, eleves = None):
        self.professeur = professeur
        self.eleves = eleves or []

    def ajouterEleve(self,eleve):
        if len(self.eleves) < 30 :
            self.eleves.append(eleve)
            return True
        else :
            print("Il y a déjà trop d'élèves dans cte classe HASSOUL")
            return False

    def afficherClasse(self):
        infoProf = self.professeur.afficherDossier()
        infoEleve = [eleve.afficherDossier() for eleve in self.eleves]
        return f'Professeur :\n{infoProf}\nÉlèves:\n{", ".join(infoEleve)}'


prof = professeur("Dupont", "Jean", 35, "123 Rue de l'École", "Mathématiques")
eleve1 = eleve("Durand", "Alice", 14, "456 Rue de l'École", "9ème année")
eleve2 = eleve("Martin", "Bob", 15, "789 Rue de l'École", "10ème année")

classe1 = classe(prof, [eleve1, eleve2])

print(classe1.afficherClasse())


# 2.3 Email
# Un email est composé d'un titre (facultatif), d'un texte (facultatif),
# d'un expéditeur (adresse email), d'une destination (adresse email) ,
# d'un ou plusieurs fichiers joints.

class FichierJoint:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille

    def afficher_info(self):
        return f"Nom du fichier joint: {self.nom}, Taille: {self.taille} Ko"


class Email:
    def __init__(self, expediteur, destination, titre=None, texte=None, fichiers_joints=None):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = fichiers_joints or []

    def ajouter_fichier_joint(self, fichier_joint):
        self.fichiers_joints.append(fichier_joint)

    def afficher_email(self):
        info = f"Expéditeur: {self.expediteur}, Destinataire: {self.destination}"
        if self.titre:
            info += f"\nTitre: {self.titre}"
        if self.texte:
            info += f"\nTexte: {self.texte}"

        info += "\nFichiers joints:\n"
        info += "\n".join([fj.afficher_info() for fj in self.fichiers_joints])

        return info

fichier1 = FichierJoint("document.pdf", 120)
fichier2 = FichierJoint("image.jpg", 80)

email1 = Email(
    expediteur="expediteur@email.com",
    destination="destinataire@email.com",
    titre="Réunion",
    texte="Bonjour, voici les documents pour la réunion.",
    fichiers_joints=[fichier1, fichier2]
)

print(email1.afficher_email())


# FINIINININININI Pour de vrai cette fois ci
