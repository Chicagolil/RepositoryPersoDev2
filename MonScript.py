import qrcode
import fitz
import tkinter as tk
from tkinter import filedialog
import time
import os


def genererCodeQr(donnees, nomFichier, dossierSortie="codesQr"):
    cheminComplet = os.path.join(dossierSortie, nomFichier)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(donnees)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")


    os.makedirs(dossierSortie, exist_ok=True)

    img.save(cheminComplet)

    return cheminComplet


def creerCodesQrDePdf(pdfPath, tailleMaxParQr=1000, nomBaseFichier="codeQr"):
    try:
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
            cheminQr = genererCodeQr(morceau, nomFichierQr)
            tailleQr = os.path.getsize(cheminQr)
            tailleTotale += tailleQr


        print("Le fichier d'informations a été généré avec succès dans informationsProcessus.txt.")
        print( f"Les codes QR ont été générés avec succès. Accédez aux codes QR dans le dossier 'codesQr' crée dans le répértoire courant ")
        return len(morceauxTexte), tailleTotale
    except Exception as e:
        print(f"Erreur lors du traitement du fichier PDF : {e}")
        return 0, 0


def creerCodeQrDeTexte(texte, tailleMaxParQr=1000, nomBaseFichier="codeQr"):
    try:
        morceauxTexte = []
        for i in range(0, len(texte), tailleMaxParQr):
            morceau = texte[i:i + tailleMaxParQr]
            morceauxTexte.append(morceau)

        tailleTotale = 0
        i=0
        for morceau in morceauxTexte:
            i+=1
            nomFichierQr = f"{nomBaseFichier}{i }.png"
            cheminQr = genererCodeQr(morceau, nomFichierQr)
            tailleQr = os.path.getsize(cheminQr)
            tailleTotale += tailleQr


        print("Le fichier d'informations a été généré avec succès dans informationsProcessus.txt.")
        print( f"Les codes QR ont été générés avec succès. Accédez aux codes QR dans le dossier 'codesQr' crée dans le répértoire courant ")

        return len(morceauxTexte), tailleTotale
    except Exception as e:
        print(f"Erreur lors du traitement du fichier texte : {e}")
        return 0, 0



def traiterFichier(fichierEntree):
    nomBaseFichier = os.path.splitext(os.path.basename(fichierEntree))[0]
    debut = time.time()


    if fichierEntree.lower().endswith(".pdf"):
        nbCodesQr, tailleTotale = creerCodesQrDePdf(fichierEntree,nomBaseFichier=nomBaseFichier)

    elif fichierEntree.lower().endswith((".txt", ".text")):
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


def choisirFichier():
    fichierEntree = filedialog.askopenfilename(title="Choisir un fichier PDF ou Txt", filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])

    if fichierEntree:
        traiterFichier(fichierEntree)



class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Générateur de Codes QR")

        self.label = tk.Label(master, text="Choisir un fichier PDF ou texte:")
        self.label.pack()

        self.boutonChoisirFichier = tk.Button(master, text="Choisir un fichier", command=self.choisirFichier)
        self.boutonChoisirFichier.pack()

        self.boutonQuitter = tk.Button(master, text="Quitter", command=self.quitter)
        self.boutonQuitter.pack()

    def choisirFichier(self):
        choisirFichier()

    def quitter(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
