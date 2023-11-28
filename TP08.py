# TP08 - GUI(graphical user interface)
# on va commencer à jouer un peu avec des interfaces graphiques
# on va utiliser la librairie Kivy.
# Jvais lire un peu de doc dessus mais jvais pas prendre de notes, donc le toi du futur -> démerdes-toi
#Préambule
# Hello World
from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='Le zizi de noah il est tout petit', font_size='100sp')


HelloApp().run()

# Fenêtre

from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config


class HelloApp(App):
    def build(self):
        self.title = 'Agrouu !'
        self.icon = 'hello.png' # jsp cque ca fait
        return Label(text='Hello World')

Config.set('graphics','width','300')
Config.set('graphics','height','150')


HelloApp().run()

# Composant Graphiques ( bouttons,liste,cases,etc) :
#   * Widget -> Label, zone de texte, bouton

from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '50')


class LoginApp(App):
    def build(self):
        self.title = 'se Connecter'
        box = BoxLayout(orientation='horizontal')
        box.add_widget((Label(text='PinCode')))
        box.add_widget(TextInput())
        box.add_widget(Button(text='Entrer'))

        return box


LoginApp().run()
#Problème avec la taille de la fenêtre : le programe IGNORE les lignes Config.set hmmmmmmmmmmmmmmmmmmmmmm WAHY??

# Plus gros programme mais qui contient case à cocher, bouton radio, liste déroulante (tjrs des widgets/composants)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class SignalApp(App):
    def build(self):
        self.title='Les feux du monde'
        city = BoxLayout(orientation='horizontal')
        city.add_widget(Label(text='Feu'))
        cities = ('Viville','Liège','Arlon')
        city.add_widget(Spinner(values=cities))

        activation = BoxLayout(orientation='horizontal')
        activation.add_widget(CheckBox())
        activation.add_widget(Label(text='Activer le Feu'))

        state = BoxLayout(orientation='horizontal')
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Rouge'))
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Orange'))
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Vert'))

        box = BoxLayout(orientation='vertical')
        box.add_widget(city)
        box.add_widget(activation)
        box.add_widget(state)
        return box

SignalApp().run()


# Gestionnaire de la mise en page -> grille

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

class GridGame(App):
    def build(self):
        self.title = 'Jeu avec les cases'
        grid = GridLayout(rows=3,cols=4)
        for i in range(12):
            grid.add_widget(Button(text=str(i+1)))
        return grid

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '150')

GridGame().run()

# Gestionnaire de la mise en page -> nimporteNawak

from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class FreePos(App):
    def build(self):
        self.title='on est ou là'
        float = FloatLayout(size=(200,150))
        x=0
        y=0
        for i in range(4):
            float.add_widget(Button(text='Ici',size_hint=(0.3,0.2),pos=(x,y)))
            x+=50
            y+=50
        return float
Config.set('graphics', 'width', '225')
Config.set('graphics', 'height', '200')

FreePos().run()


# Fichier KV

from kivy.app import App
from kivy.config import Config

class LoginApp(App):
    pass

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '50')

LoginApp().run()

# et dans le fichier login.kv on met :
"""
BoxLayout:
    orientation: 'horizontal'
    Label:
        text: 'Pin code'
    TextInput
    Button:
        text: 'Entrer'  
"""
# je n'ai aucune idée de comment le programme va chercher ce fichier
# il est bcp trop smart


# C'est bon j'ai les armes pour ce tp, jvais pouvoir concevoir une interface ou on voit thomas avaler des énormes chibrax
# Comment ça me hype de fou, c'est clairement mon fantasme le plus énorme


#EXERCISE n°1__________________________________________________________________________________________________________________________________

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class calculatrice(App):
    def build(self):
        self.title='Prout'
        box = BoxLayout(orientation='vertical',spacing=10,padding=10)

        self.premier = TextInput(hint_text='Entrez le premier nombre', multiline=False)
        self.deuxième = TextInput(hint_text='Entrez le deuxième nombre', multiline=False)
        box.add_widget(self.premier)
        box.add_widget(self.deuxième)
        box.add_widget(Button(text='Calculer', on_press=self.calculerSomme))
        self.resultat = Label(text='Résulat')
        box.add_widget(self.resultat)
        return box


    def calculerSomme(self):
        try:
            num1 = float(self.premier.text)
            num2 = float(self.deuxième.text)
            resultat = num1+num2

            self.resultat.text = f'Résultat de {num1} + {num2}: {resultat}'
        except ValueError :
            self.premier.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'
            self.deuxième.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'


if __name__ == '__main__':
    calculatrice().run()


# Exercise N°2____________________________________________________________________________________________________________________________________________________________

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class calculatrice(App):
    def build(self):
        self.title = 'Prout'
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.premier = TextInput(hint_text='Entrez le premier nombre', multiline=False)
        self.deuxième = TextInput(hint_text='Entrez le deuxième nombre', multiline=False)
        box.add_widget(self.premier)
        box.add_widget(self.deuxième)

        operations = BoxLayout(orientation='horizontal')
        self.somme = Button(text='Somme', on_press=self.calculerSomme)
        self.Diff = Button(text='Différence', on_press=self.calculerDiff)
        self.Mult = Button(text='Multiplication', on_press=self.calculerMult)
        self.Div = Button(text='Division', on_press=self.calculerDiv)
        operations.add_widget(self.somme)
        operations.add_widget(self.Diff)
        operations.add_widget(self.Mult)
        operations.add_widget(self.Div)
        box.add_widget(operations)
        self.resultat = Label(text='Résulat')
        box.add_widget(self.resultat)
        return box

    def calculerSomme(self,instance):
        try:
            num1 = float(self.premier.text)
            num2 = float(self.deuxième.text)
            resultat = num1 + num2

            self.resultat.text = f'Résultat de {num1} + {num2} : {resultat}'
        except ValueError:
            self.premier.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'
            self.deuxième.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'


    def calculerMult(self,instance):
        try:
            num1 = float(self.premier.text)
            num2 = float(self.deuxième.text)
            resultat = num1 * num2

            self.resultat.text = f'Résultat de {num1} * {num2} : {resultat: .2f}'
        except ValueError:
            self.premier.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'
            self.deuxième.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'


    def calculerDiff(self,instance):
        try:
            num1 = float(self.premier.text)
            num2 = float(self.deuxième.text)
            resultat = num1 - num2

            self.resultat.text = f'Résultat de {num1} - {num2} : {resultat: .2f}'
        except ValueError:
            self.premier.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'
            self.deuxième.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'

    def calculerDiv(self,instance):
        try:
            num1 = float(self.premier.text)
            num2 = float(self.deuxième.text)
            resultat = num1 / num2

            self.resultat.text = f'Résultat de {num1} / {num2} : {resultat :.2f}'
        except ValueError:
            self.premier.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'
            self.deuxième.text = 'VEUILLEZ ENTRER UN CHIFFRE VALIDE MAGGLE'




if __name__ == '__main__':
    calculatrice().run()

# j'ai un peu triché, le cours veut qu'on utilise une checkbox -> boriiiing mais jle fait quand même allez


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class CalculatriceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Zone de texte pour le premier nombre
        self.num1_input = TextInput()
        layout.add_widget(self.num1_input)

        # Zone de texte pour le deuxième nombre
        self.num2_input = TextInput()
        layout.add_widget(self.num2_input)

        # Ajouter des CheckBoxes pour choisir l'opération
        operations_layout = BoxLayout(orientation='horizontal')
        self.addition_checkbox = CheckBox(group='operation', active=True)
        self.subtraction_checkbox = CheckBox(group='operation')
        self.multiplication_checkbox = CheckBox(group='operation')
        self.division_checkbox = CheckBox(group='operation')

        operations_layout.add_widget(Label(text='Addition'))
        operations_layout.add_widget(self.addition_checkbox)
        operations_layout.add_widget(Label(text='Subtraction'))
        operations_layout.add_widget(self.subtraction_checkbox)
        operations_layout.add_widget(Label(text='Multiplication'))
        operations_layout.add_widget(self.multiplication_checkbox)
        operations_layout.add_widget(Label(text='Division'))
        operations_layout.add_widget(self.division_checkbox)

        layout.add_widget(operations_layout)

        # Bouton pour effectuer le calcul
        self.calculate_button = Button(text='Calculer', on_press=self.calculer)
        layout.add_widget(self.calculate_button)

        # Zone de texte pour afficher le résultat
        self.result_label = Label()
        layout.add_widget(self.result_label)

        return layout

    def calculer(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)

            if self.addition_checkbox.active:
                result = num1 + num2
            elif self.subtraction_checkbox.active:
                result = num1 - num2
            elif self.multiplication_checkbox.active:
                result = num1 * num2
            elif self.division_checkbox.active:
                result = num1 / num2

            self.result_label.text = f"Résultat : {result}"
        except ValueError:
            self.result_label.text = "Veuillez entrer des nombres valides."

if __name__ == '__main__':
    CalculatriceApp().run()


# EXERCISE n°3___________________________________________________________________________________________________________________________

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Rectangle
import random

tab=['Ouf','Boom']
couleurs=[[0,1,0,1],[1,0,0,1],[0,0,1,1],[1,1,0,1],[1,0,1,1],[0,1,1,1],[0.5,0.5,0.5,0.5]]

class grilleApp(App):
    def build(self):
        self.title='Jeu Des Couleurs'
        grille = GridLayout(rows=5,cols=5)
        for i in range (25):
            button = Button(text=str(random.choice(tab)), background_normal='', background_color=(1,1,1,1))
            button.bind(on_press=self.changeColor)
            grille.add_widget(button)
        return grille
    def changeColor(self,button):
        if button.background_color == [1,1,1,1]:
            button.background_color = random.choice(couleurs)
        else:
            button.background_color = [1, 1, 1, 1]
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '150')

if __name__ =='__main__':
    grilleApp().run()



#FINIIIIIIII , il était plutôt agréable ce tp

