#Classes et Objets______________________________________________________________________________________________________________________
#1.Création de la Classe
class FirstPerson :
    pass

pers1 = FirstPerson()

print(pers1)
# Résultat (exemple): <__main__.FirstPerson object at 0x000002115AD66D30>
### C'est qwa ? -> La sortie indique que 'pers1' est une instance de la classe 'FirstPerson' située à une certaine adresse mémoire.
### La représentation par défault d'un objet en python affiche le type de l'objet et son emplacement mémoire
## FirstPerson == Classe || pers1 == instance de cette classe

#2. Notion de constructeur et d'attributs________________________________________________________________________________________________
#2.1
class Person :
    """
    Une Classe représentant une personne

    Attributs :
        gender (str) : le sexe de la personne
        height (init) : la taille de la personne
        weight (init) : le poids de la personne
    """
    pass
#2.2 (j'enlève la doc pcq ça prend de la place)

class Person :
   def __init__(self, gender="Inconnu", height=0, weight=0): # j'attribue des valeurs par défault
       #2.3 commence ici
       self.gender = gender
       self.height = height
       self.weight = weight
    #plus de pass car mtn la class n'est plus vide

person1= Person()
print(person1.weight)
print(person1.height)
print(person1.gender)

    #affiche les valeurs par défault

#2.4 / 2.5

pers2_0 = Person()
print(f"pers2_0: {pers2_0.gender}, {pers2_0.height}, {pers2_0.weight}")

pers2_1 = Person(gender="Femme")
print(f"pers2_1: {pers2_1.gender}, {pers2_1.height}, {pers2_1.weight}")

pers2_2 = Person(gender="Homme", height=175)
print(f"pers2_2: {pers2_2.gender}, {pers2_2.height}, {pers2_2.weight}")

pers2_3 = Person(gender="Non-binaire", height=160, weight=60)
print(f"pers2_3: {pers2_3.gender}, {pers2_3.height}, {pers2_3.weight}")

#BONUS ( définir une méthode dans la classe )

class Person :
   def __init__(self, gender="Inconnu", height=0, weight=0): # j'attribue des valeurs par défault
       #2.3 commence ici
       self.gender = gender
       self.height = height
       self.weight = weight
   def presentationRapide (abc):
       print(f"Bonjour je suis du sexe {abc.gender}, je mesure {abc.height}cm, et je pèse {abc.weight}kg")

pers2_0 = Person()
pers2_0.presentationRapide()

# ATTRIBUT PRIVÉ ET GETTER
# 2.6
# La différence entre un ou deux underscore est que
# un underscore rend l'attribut "protégé"(convention de nommage, python n'empêche pas réellement l'accès à cet attribut)
# tandis que deux rend l'attribut "privé" (on ne peut plus réelement y accéder de l'éxtérieur par erreur, mais avec un peu d'effort, on y arrive quand même)
class Person :
   def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height  # PRIVÉ grâce au deux ptits __
       self.weight = weight

pers1 = Person()
print(pers1.height) # ne fonctionne pas, erreur car le nom est manglé

# 2.7

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def getter(self):
        return self.__height

# 2.8

pers1 = Person(gender="homme", height=120, weight=70)
print(pers1.getter)

# BONUS : sans décorateur

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    def getter(self):
        return self.__height



pers1 = Person(gender="homme", height=120, weight=70)
print(pers1.getter())



# SETTER
# 2.9
pers1 = Person(gender="homme", height=120, weight=70)
pers1.height = 40
    #Pas d'erreur,mais ça n'a aucun impact, ça ne marche pas, il faut que je crée un setter

#2.10 sans décorateur
class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def monGetter(self):
        return self.__height
    def monSetter(self,nouvGrd):
        self.__height = nouvGrd

pers1 = Person(gender="homme", height=120, weight=70)
pers1.monSetter(40)
print(pers1.monGetter)

# 2.11

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def monGetter(self):
        return self.__height
    @monGetter.setter
    def monSetter(self,nouvGrd):
        self.__height = nouvGrd



pers1 = Person(gender="homme", height=120, weight=70)

print(pers1.monGetter)

pers1.monSetter= 45

print(pers1.monGetter)

# SYNTHÈSE de tout ça
# Une classe est un constructeur d'objet, comme un 'blueprint'
# Un objet est une instance d'une classe
# objectif de l'encapsulation: restreindre l'accès direct aux données d'un objet -> accès via des méthodes spécifiques
# 1 : Utiliser des attributs privés -> self.__attribut <- rend l'attribut plus difficilement accessible et modifiable
# 2 : Fournir Des méthodes de getter et setter -> fournissent un moyen contôlé d'accéder/modifier la valeur de l'attribut
# 3 : Utiliser Des décorateurs :
# - @property -> permet d'accéder à la méthode comme si c'était un attribut direct (sans utiliser les paranthèses)
# - @[nomDuGetter].setter -> permet de modifier la valeur de l'attribut comme si c'était une affectation directe sans utiliser de méthode explicite


#3. MÉTHODES___________________________________________________________________________________________________________________________________________________________________________________________

#3.1

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def monGetter(self):
        return self.__height
    @monGetter.setter
    def monSetter(self,nouvGrd):
        self.__height = nouvGrd


# 3.2

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def monGetter(self):
        return self.__height
    @monGetter.setter
    def monSetter(self, nouvGrd):
        self.__height = nouvGrd

    def description(self):
        return f"I am a {self.gender}, I measure {self.__height} centimeters, and I weight {self.weight} kilograms"

#3.3
pers3 = Person(gender="MAN", height=120, weight=70)

#3.4
print(pers3.description())

#3.5 methode __str__

class Person :
    def __init__(self, gender="Inconnu", height=0, weight=0):
       self.gender = gender
       self.__height = height
       self.weight = weight
    @property
    def monGetter(self):
        return self.__height
    @monGetter.setter
    def monSetter(self, nouvGrd):
        self.__height = nouvGrd

    def __str__(self):
        return f"I am a {self.gender}, I measure {self.__height} centimeters, and I weight {self.weight} kilograms"


# 3.6

pers4 = Person(gender="MAN", height=120, weight=70)
print(pers4)
#OU
print(str(pers4))

# 3.7
# plus facile d'appeler la méthode pusique __str__ est implicitement appélée quand on emploie les fonctions print() ou str()


# 4 NOTIONS D'HÉRITAGE
#4.1
class SuperHero(Person):
    pass
#4.2

class SuperHero(Person):
    def __init__ (self, super_power="Super Raciste"):
        self.superPOUVOIR = super_power

#4.3

class SuperHero(Person):
    def __init__(self, super_power, gender, height, weight):
        super().__init__(gender, height, weight)
        self.superPOUVOIR = super_power

    def __str__(self):
        parent_str = super().__str__()
        return f"{self.superPOUVOIR} : {parent_str}"


superR = SuperHero(super_power="SuperRaciste", gender="On sait pas", height=190, weight=200)
print(superR)


# EXERCISES DE DRILL

#1
class Calculatrice :
    def __init__(self,valInitiale):
        self.valAff = valInitiale
    def ajoute(self,val):
        self.valAff += val
        return self.valAff
    def soustrait(self,val):
        self.valAff -= val
        return self.valAff
    def carre(self):
        self.valAff **= 2
        return self.valAff
    def __str__(self):
        return f"La Valeur en entrée est : {self.valAff}"


calc1 = Calculatrice(valInitiale=16)
print(calc1)
calc1.ajoute(3)
print("+3")
print(calc1)
calc1.soustrait(10)
print("-10")
print(calc1)
calc1.carre()
print("²")
print(calc1)

# 2
#sans gestion d'erreur
class Etudiant:
    def __init__(self, nom, prenom, numMat):
        self.numMat = numMat
        self.nom = nom
        self.prenom = prenom
        self.nomComplet = f"{prenom} {nom}"

    def __str__(self):
        return f"Nom : {self.nom}\nPrenom : {self.prenom}\nNuméro de Matricule : {self.numMat}"


etu1 = Etudiant(nom="Devroye", prenom="Lilian", numMat=202305)
print(etu1)
print(etu1.nomComplet)

#OU

class Etudiant:
    def __init__(self, nom, prenom, numMat):
        self.numMat = numMat
        self.nom = nom
        self.prenom = prenom

    @property
    def nomComplet (self) :
            return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"Nom : {self.nom}\nPrenom : {self.prenom}\nNuméro de Matricule : {self.numMat}"


etu1 = Etudiant(nom="Devroye", prenom="Lilian", numMat=202305)
print(etu1)
print(etu1.nomComplet)

# avec gestion d'erreur

class Etudiant:
    def __init__(self, nom, prenom, numMat):
        if numMat < 0 :
            raise ValueError("Le Matricule entré doit être positif")
        self.numMat = numMat
        self.nom = nom
        self.prenom = prenom

    @property
    def nomComplet (self) :
            return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"Nom : {self.nom}\nPrenom : {self.prenom}\nNuméro de Matricule : {self.numMat}"


etu1 = Etudiant(nom="Devroye", prenom="Lilian", numMat= -202305)
print(etu1)
print(etu1.nomComplet)

#3


from datetime import datetime

class Etudiant:
    def __init__(self, nom, prenom, numMat, dateDeNaissance):
        if numMat < 0:
            raise ValueError("Le Matricule entré doit être positif")
        self.numMat = numMat
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance


    def age (self):
        aujourdHui = datetime.today()
        dateDeNaissance = datetime.strptime(self.dateDeNaissance, "%Y-%m-%d")
        age = aujourdHui.year - dateDeNaissance.year - ((aujourdHui.month, aujourdHui.day) < (dateDeNaissance.month,dateDeNaissance.day))
        return age

    @property
    def nomComplet(self):
        return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"Nom : {self.nom}\nPrenom : {self.prenom}\nNuméro de Matricule : {self.numMat}\nAge : {Etudiant.age(self)}"




etudiant1 = Etudiant(nom="Doe", prenom="John", numMat=12345, dateDeNaissance="1990-05-15")
print(etudiant1)


# 4

class Livre :
    def __init__(self,titre,nom,ISBN):
        self.titre = titre
        self.nom = nom
        self.ISBN = ISBN
    def __str__(self):
        return f"-----------------------\nAuteur : {self.nom}\nTitre : {self.titre}\nISBN : {self.ISBN}"

livre1 = Livre(titre="L'hyptohèse K.",nom="Aurelien Barreau",ISBN=70911)
livre2 = Livre(titre="Les choses humaines",nom="Karine Tuill",ISBN=15916)
livre3 = Livre(titre="La peste",nom="Albert Camus",ISBN=85039)
livre4 = Livre(titre="Le monde comme volonté et comme représentation",nom="Arthur Schopenhauer",ISBN=14467)
livre5 = Livre(titre="Critique de la raison pure ",nom="Emmanuel Kant",ISBN=83505)
livre6 = Livre(titre="1984",nom="George Orwell",ISBN=77184)
livre7 = Livre(titre="Le meilleur des mondes",nom="Aldous Huxley",ISBN=32500)
livre8 = Livre(titre="Le petit prince",nom="Antoine De St-Exupery",ISBN=68578)
livre9 = Livre(titre="L'écume des jours",nom="Boris Vian",ISBN=32588)
livre10= Livre(titre="L'interpretation des rêves",nom="Sigmund Freud",ISBN=96431)

listedelivres = [livre1,livre2,livre3,livre4,livre5,livre6,livre7,livre8,livre9,livre10]

listeTriée = sorted(listedelivres, key=lambda livre : (livre.nom , livre.ISBN))

for i in listeTriée :
    print(i)