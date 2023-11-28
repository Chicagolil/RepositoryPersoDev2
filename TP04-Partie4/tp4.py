# copier collé de l'exo 3.3

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