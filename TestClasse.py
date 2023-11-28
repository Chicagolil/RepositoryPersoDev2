from TP07_MiseEnPratique import Fraction

fraction1 = Fraction(3, 6)
fraction2 = Fraction(4, 3)
fraction3 = Fraction(5)
fraction4 = Fraction(1,2)
# fractionErr = Fraction(5, 0) -> erreur Direct, bloque tout

print(f"Fraction1 : {fraction1}")
print(f"Fraction2 : {fraction2}")
print(f"Fraction3 : {fraction3}")

# les deux sont pareilles, puisque l'opérateur + appelle implicitement la méthode/fonction __add__ qui est built in python
print(fraction1.__add__(fraction2))
print(fraction1+fraction2)

#__sub__
print(fraction1-fraction2)
print(fraction1.__sub__(fraction2))

#__mul__
print(fraction1*fraction2)

#__trueDiv__
print(fraction1/fraction2)

#__pow__
print(fraction1**2)

#__eq__
print(fraction1==fraction2)
print(fraction1==fraction4)

#__float__
print(float(fraction1))

# is_zero
print(fraction1.is_zero())

# is_integer
print(fraction3.is_integer())

# as_mixed_number
print(fraction2.as_mixed_number())

# is_proper
print(fraction2.is_proper())

# is_unit
print(fraction3.is_unit())
print(fraction1.is_unit())



# FINIIIIIIIIIIIIIIIIII