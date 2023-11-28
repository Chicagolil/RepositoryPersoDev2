

from math import gcd

class Fraction:
    """Classe qui représente une fraction et des opérations qu'on peut lui opérationner

    Auteur : Lilian Devroye
    Date : Novembre 2023
    Cette classe permet des manipulations et opérations sur les fractions
    """

    def __init__(self,num: int =0 , den: int=1 ) -> int:
        """Construit la fraction avec un numérateur et dénominateur

        PRE : 'num' entier, 'den' est un entier 
        POST : crée une fraction représentée sous forme réduiteles, attributs privés
        RAISES : ZeroDivisionError si 'den' est nul -> on arrête tout
        """
        if den == 0 :
            raise  ZeroDivisionError("\nLe dénominateur est zéro, t'as cassé tout l'univers ")

        PGDC = gcd(abs(num),abs(den))
        self.__num = num // PGDC # // division entière -> précaution pour ne pas obtenir de flottant , même si c'est le PGDC
        self.__den = den // PGDC


    @property
    def numerateur(self):
        """
        Getter pour le numérateur
        PRE:/
        POST : Renvoie le numérateur de la fraction

        """
        return self.__num

    @property
    def denominateur(self):
        """
        Getter pour le dénominateur
        PRE : /
        POST : Renvoie le dénominateur de la fraction

        """
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Renvoie une répresentation textuelle  de la fraction simplifiée

        PRE : /
        POST : Renvoie une représentation textuelle réduite de la fraction
        et renvoie le num si den==1
        """
        if self.__den == 1:
            return str(self.__num)
        return f'{self.__num}/{self.__den}'

    def as_mixed_number(self):
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte

        Un nombre mixe est une somme d'un entier et d'une fraction
        PRE : /
        POST : Renvoie la représentation textuelle sous forme de nombre mixte de la fraction réduite
                si par hasard il n'y a pas de reste, tqt on gère
        """
        partieEntier= self.__num // self.__den
        reste = self.__num % self.__den
        if reste == 0 :
            return str(partieEntier)

        return f'{partieEntier} + {reste}/{self.__den}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """surcharge l'opérateur + pour les fractions

         PRE : 'other' est une instance de Fraction
         POST : Renvoie une nouvelle fraction représentant la somme des deux fractions
         """
        nveauNum = self.__num * other.__den + self.__den * self.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum,nveauDen)


    def __sub__(self, other):
        """surcharge l'opérateur - pour les fractions
        PRE : 'other' est une instance de Fraction
        POST : Renvoie une nouvelle fraction représentant la différence des deux fractions
        """
        nveauNum = self.__num * other.__den - self.__den * self.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum, nveauDen)


    def __mul__(self, other):
        """surcharge l'opérateur *  pour les fractions

               PRE : 'other' est une instance de Fraction
               POST : Renvoie une nouvelle fraction représentant la multiplication des deux fractions
               """

        nveauNum = self.__num * other.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum, nveauDen)

    def __truediv__(self, other):
        """Surcharge l'opérateur / pour les frations

        PRE : 'other' est une instance de Fraction et 'other' n'est pas une fraction nulle
        POST : Renvoie une nouvelle fraction représentant la division des deux fractions
        RAISES : ZeroDivisionError si 'den' est nul
        """
        if other.__num == 0:
            raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
        nveauNum = self.__num * other.__den
        nveauDen = self.__den * other.__num
        return Fraction(nveauNum, nveauDen)

    def __pow__(self, power):
        """Surcharge l'opérateur ** pour les fractions

        PRE : 'other ' est un entier
        POST : Renvoie une nouvelle fraction représentant la puissance de la fraction
        """
        nveauNum = self.__num ** power
        nveauDen = self.__den ** power
        return Fraction(nveauNum, nveauDen)


    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions

        PRE : 'other' est une instance de Fraction
        POST : Renvoie True si les deux fractions sont équivalentes , False sinon

        """
        return self.__num == other.__num and self.__den == other.__den

    def __float__(self):
        """Retourne la valeur décimale de la fraction

        PRE : /
        POST : Renvoie la valeur décimale de la fraction
        """
        return self.__num/self.__den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Vérifie si valeur de la fraction est 0

        POST : Renvoie True si la fraction est nulle, False sinon
        """
        return self.__num == 0


    def is_integer(self):
        """Vérifie si la fraction est un entier entier


        POST : Renvoie True si la fraction est un entier, False sinon
        """
        return self.__num/self.__den == int(self.__num/self.__den)

    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1

        POST : Renvoie True si la fraction est propre, False sinon
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Vérifie si le numérateur de la fraction est 1 dans sa forme simplfiée


        POST : Renvoie True si le numérateur est 1, False sinon
        """
        return self.__num == 1

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent d'une fraction unitaire

        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

        POST : Renvoie True si les deux fractions sont adjacentes, False sinon
        """
        diff = abs(self.__num * other.__den - other.__num * self.__den)
        return diff == 1



# FINIIIIIIIIIIIIIIIIII
