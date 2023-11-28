from Fraction import Fraction
import unittest
import coverage


class onVaLaTesterCteFraction(unittest.TestCase):

    def testCreationFraction(self):
        fraction = Fraction(3, 4)
        self.assertEqual(fraction.numerateur, 3)
        self.assertEqual(fraction.denominateur, 4)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def testRepresentationTextuelle(self):
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(3, 4)
        # __str__
        self.assertEqual(str(fraction1), '5/2')
        self.assertEqual(str(fraction2), '3/4')
        # as_mixed_number
        self.assertEqual(fraction1.as_mixed_number(), '2 + 1/2')
        self.assertEqual(fraction2.as_mixed_number(), '3/4')

    def testOperationsMathematiques(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(2, 3)
        # __add__
        resultatAddition = fraction1 + fraction2
        self.assertEqual(resultatAddition.numerateur, 17)
        self.assertEqual(resultatAddition.denominateur, 12)

        # __sub__
        resultatSoustraction = fraction1 - fraction2
        self.assertEqual(resultatSoustraction.numerateur, 1)
        self.assertEqual(resultatSoustraction.denominateur, 12)

        # __mul__
        resultatMultiplication = fraction1 * fraction2
        self.assertEqual(resultatMultiplication.numerateur, 1)
        self.assertEqual(resultatMultiplication.denominateur, 2)

        # __truediv__
        resultatDivision = fraction1 / fraction2
        self.assertEqual(resultatDivision.numerateur, 9)
        self.assertEqual(resultatDivision.denominateur, 8)

        # __pow__
        resultatPuissance = fraction1 ** 2
        self.assertEqual(resultatPuissance.numerateur, 9)
        self.assertEqual(resultatPuissance.denominateur, 16)

    def testProprietesFraction(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(4, 3)
        fraction3 = Fraction(5, 1)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(1, 1)

        # is_zero
        self.assertFalse(fraction1.is_zero())
        self.assertTrue(fraction4.is_zero())

        # is_integer
        self.assertFalse(fraction1.is_integer())
        self.assertTrue(fraction3.is_integer())

        # is_proper
        self.assertTrue(fraction1.is_proper())
        self.assertFalse(fraction2.is_proper())

        # is_unit
        self.assertFalse(fraction1.is_unit())
        self.assertTrue(fraction5.is_unit())

        # is_adjacent_to
        self.assertFalse(fraction1.is_adjacent_to(Fraction(7, 4)))
        self.assertTrue(fraction1.is_adjacent_to(Fraction(2, 3)))

    def testConversionEnDecimal(self):
        fraction = Fraction(3, 4)
        self.assertEqual(float(fraction), 0.75)


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    cov.stop()
    cov.report()





"""commentaires : 

____________________________________________________________________________________________________________________________________________________________________________________________________________________
erreur trouvée et corrigé dans as_mixed_number (gère désormais le cas ou la fraction est plus petite que 1)  :


          partieEntier = self.__num // self.__den
                reste = self.__num % self.__den
                if reste == 0:
                    return str(partieEntier)

                return f'{partieEntier} + {reste}/{self.__den}'

    remplacé par


          partieEntier = self.__num // self.__den
                reste = self.__num % self.__den
                if reste == 0:
                    return str(partieEntier)
                elif abs(self.__num / self.__den) < 1:
                    return f'{reste}/{self.__den}'

                return f'{partieEntier} + {reste}/{self.__den}'

___________________________________________________________________________________________________________________________________________________________________________________________________________                
erreur trouvée et corrgée dans __add__ (erreur entre paranthèses) :
        nveauNum = self.__num * other.__den + self.__den * (self.__num)
                nveauDen = self.__den * other.__den
                return Fraction(nveauNum,nveauDen)

    remplacé par :

        nveauNum = self.__num * other.__den + self.__den * (other.__num)
                nveauDen = self.__den * other.__den
                return Fraction(nveauNum,nveauDen)

_____________________________________________________________________________________________________________________________________________________________________________________________________________
erreur trouvée et corrigée dans __sub__ : exactement la même qu'au dessus -> un self.num au lieu d'un other.num
_____________________________________________________________________________________________________________________________________________________________________________________________________________

différentes fautes de frappes dans l'écriture des tests -> un True au lieu d'un False, etc...
"""
