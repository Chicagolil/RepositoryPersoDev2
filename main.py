import argparse
from libs.file_mgmt import csvOpener
from libs.bd import BandeDessinee
import time

if __name__ == '__main__':
    ligne ="______________________________________________________________________________"
    parser = argparse.ArgumentParser()
    parser.add_argument('dossier',help='Il me faut un nom de dossier avec tes fichiers excel de vente de BD par mois')
    args=parser.parse_args()

    donnees = csvOpener.recevoirLesDonnees(args.dossier)
    #'D:\#5_LILIAN\#2_EPHEC\\2ième\Dev2\Tp5\data'

    tab = []
    for nomBd in donnees :
        dataBD = donnees[nomBd]
        bd = BandeDessinee(dataBD['prixUnitaire'],nomBd,dataBD['qteTotale'])

        for details in dataBD:
            continue
        tab.append(bd)

    for bd in tab :
        time.sleep(0.4)
        print(f'{ligne}\n{bd}')
    print(ligne)
    maxBD = max(tab, key=lambda bd : bd.total )
    print(f"\nLE GRAND GAGNANT EST : {maxBD.nomBD} AVEC {maxBD.total:.2f} € DE CHIFFRE D'AFFAIRE")