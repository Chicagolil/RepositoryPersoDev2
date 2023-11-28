import os

def nomFichierData(dossier):
    try:
        tabfich = []
        for i in os.listdir(dossier):
            if not i.startswith('.'):
                tabfich.append(i)
        return tabfich
    except FileNotFoundError :
        print('Le Dossier que vous avez sélectionné ou le chemin entré n\'existe pas')
    except OSError :
        print(f"La syntaxe du nom de fichier, de répertoire ou de volume est incorrecte :\n{dossier}")


def ouvertureFichier(fichier):
    dictionnaireLivres = {}
    with open(fichier, 'r', encoding='utf-8') as fichier:
        o = fichier.readlines()
        for i in o[1:] :
            elements = i.rstrip().split(';')
            nomBd = elements[1]
            prixBd = float(elements[2].replace(',','.'))
            qteVendue = int(elements[3])
            if nomBd not in dictionnaireLivres:
                dictionnaireLivres[nomBd] = {'qteTotale' : 0, 'prixUnitaire' : prixBd}
            dictionnaireLivres[nomBd]['qteTotale'] += qteVendue
        return dictionnaireLivres


def concatTout(donnees):
    tout = {}
    for i in donnees :
        for o in i :
            nomDonnees = i[o]
            if o not in tout :
                tout[o]={'qteTotale':0 ,'prixUnitaire':nomDonnees['prixUnitaire']}
            tout[o]['qteTotale'] += nomDonnees['qteTotale']
    return tout


def recevoirLesDonnees(dossier):
    liste=[]
    for fichier in nomFichierData(dossier):
        liste.append(ouvertureFichier(f'{dossier}\\{fichier}'))
    return concatTout(liste)


if __name__ == '__main__':
    print('****TEST****')
    cheminDoss = 'D:\#5_LILIAN\#2_EPHEC\\2ième\Dev2\Tp5\data'
    print(recevoirLesDonnees(cheminDoss))