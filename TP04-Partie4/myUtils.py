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



