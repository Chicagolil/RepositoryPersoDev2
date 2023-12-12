import qrcode
import fitz
import argparse
import time
import os


def genererCodeQr(donnees, nomFichier, couleurRemplissage, couleurFond, dossierSortie="codesQr"):

    cheminComplet = os.path.join(dossierSortie, nomFichier)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(donnees)
    qr.make(fit=True)
    img = qr.make_image(fill_color=couleurRemplissage, back_color=couleurFond)

    os.makedirs(dossierSortie, exist_ok=True)

    img.save(cheminComplet)

    return cheminComplet


def creerCodesQrDePdf(pdfPath, tailleMaxParQr=1000, nomBaseFichier="codeQr"):
    try:
        couleurFond = input("Choisissez la couleur de fond du code QR, vous avez le choix entre :\n-black \n-white \n-red \n-blue \n-green \n-yellow \n-purple \n-orange \n-pink\n")
        couleurRemplissage = input("Choisissez la couleur du code QR, vous avez le choix entre :\n-black \n-white \n-red \n-blue \n-green \n-yellow \n-purple \n-orange \n-pink\n")
        dossierSortie = input('Quel nom voulez vous donner au dossier de sortie des Codes Qr : ')
        doc = fitz.open(pdfPath)
        texteTotal = ""
        for pageNum in range(doc.page_count):
            page = doc[pageNum]
            textePage = page.get_text()
            texteTotal += textePage

        morceauxTexte = []
        for i in range(0, len(texteTotal), tailleMaxParQr):
            morceau = texteTotal[i:i + tailleMaxParQr]
            morceauxTexte.append(morceau)

        tailleTotale = 0

        i = 0
        for morceau in morceauxTexte:
            i += 1
            nomFichierQr = f"{nomBaseFichier}{i} .png"
            cheminQr = genererCodeQr(morceau, nomFichierQr, couleurFond, couleurRemplissage, dossierSortie=dossierSortie)
            tailleQr = os.path.getsize(cheminQr)
            tailleTotale += tailleQr

        print("Le fichier d'informations a été généré avec succès dans informationsProcessus.txt.")
        print(
            f"Les codes QR ont été générés avec succès. Accédez aux codes QR dans le dossier {dossierSortie} crée dans le répértoire courant ")
        return len(morceauxTexte), tailleTotale
    except Exception as e:
        print(f"Erreur lors du traitement du fichier PDF : {e}")
        return 0, 0, []


def creerCodeQrDeTexte(texte, tailleMaxParQr=1000, nomBaseFichier="codeQr"):
    try:
        couleurFond = input("Choisissez la couleur de fond du code QR, vous avez le choix entre :\n-black \n-white \n-red \n-blue \n-green \n-yellow \n-purple \n-orange \n-pink\n")
        couleurRemplissage = input("Choisissez la couleur du code QR, vous avez le choix entre :\n-black \n-white \n-red \n-blue \n-green \n-yellow \n-purple \n-orange \n-pink\n")
        dossierSortie = input('Quel nom voulez vous donner au dossier de sortie des Codes Qr : ')
        morceauxTexte = []
        for i in range(0, len(texte), tailleMaxParQr):
            morceau = texte[i:i + tailleMaxParQr]
            morceauxTexte.append(morceau)

        tailleTotale = 0
        i = 0
        for morceau in morceauxTexte:
            i += 1
            nomFichierQr = f"{nomBaseFichier}{i}.png"
            cheminQr = genererCodeQr(morceau, nomFichierQr, couleurFond, couleurRemplissage, dossierSortie=dossierSortie)
            tailleQr = os.path.getsize(cheminQr)
            tailleTotale += tailleQr

        print("Le fichier d'informations a été généré avec succès dans informationsProcessus.txt. disponible dans le répertoire courant")

        print(
            f"Les codes QR ont été générés avec succès. Accédez aux codes QR dans le dossier {dossierSortie} crée dans le répértoire courant ")
        return len(morceauxTexte), tailleTotale
    except Exception as e:
        print(f"Erreur lors du traitement du fichier texte : {e}")
        return 0, 0, []


def traiterFichier(fichierEntree):

    debut = time.time()

    if fichierEntree.lower().endswith(".pdf"):
        nomBaseFichier = input("Entrez le nom de base pour les fichiers de sortie des codes QR (sans extension) : ")
        nbCodesQr, tailleTotale = creerCodesQrDePdf(fichierEntree, nomBaseFichier=nomBaseFichier)

    elif fichierEntree.lower().endswith((".txt", ".text")):
        nomBaseFichier = input("Entrez le nom de base pour les fichiers de sortie des codes QR (sans extension) : ")
        with open(fichierEntree, "r", encoding="utf-8") as fichier_texte:
            texte = fichier_texte.read()
        nbCodesQr, tailleTotale = creerCodeQrDeTexte(texte, nomBaseFichier=nomBaseFichier)

    else:
        print("Format de fichier non pris en charge. Le script accepte uniquement les fichiers PDF et texte.")
        return
    fin = time.time()
    dureeExecution = fin - debut

    informations = f"Informations sur le processus:\n \
                     - Nombre de codes QR générés: {nbCodesQr}\n \
                     - Taille totale des codes QR générés: {tailleTotale} octets\n \
                     - Nom du fichier d'origine: {nomBaseFichier}\n \
                     - Taille du fichier d'origine: {os.path.getsize(fichierEntree)} octets\n \
                     - Durée d'exécution: {dureeExecution:.2f} secondes"

    with open("informationsProcessus.txt", "w") as fichierInfos:
        fichierInfos.write(informations)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Générateur de Codes QR pour fichiers PDF et texte")
    parser.add_argument("fichier", help="Chemin vers le fichier PDF ou texte à traiter", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    traiterFichier(args.fichier)
