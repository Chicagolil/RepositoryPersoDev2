# TP07 : PROGRAMMATION PAR CONTRAT, PROGRAMATION DÉFENSIVE ET EXCEPTIONS
# 1. PROGRAMMATION PAR CONTRAT
# rappel de quesque c quoi ce que c :

#ChatGpt
"""
approche de développement logiciel -> met l'accent sur la spécification formelle des comportements
attendus des composants logiciels.

Repose sur trois principaux éléments :
* 1er -> Préconditions : Des conditions qui doivent être vraies avant qu'une méthode ou une fonction
         ne s'éxécute. Ces conditions définissent les attentes sur les valeurs des paramètres ou
         d'autres états avant l'éxécution de la routine.

* 2ème-> Postconditions : Des conditions qui doivent être vraies après que la méthode ou une fonction
         a été éxécutée. Elles décrivent les résultats attendus et l'état final du système.

* 3ème-> Invaritants : Des conditions qui doivent être toujours vraies avant et après l'éxécution d'une
         routine. Les invariants reflètent des propriétés constantes du système.

idée : chaque composant(méthode, fonction, classe) établit un contrat aves ses utilisateurs. Les
utilisateur doivent respecter les préconditions avant d'appeler la routine, et la routine doit garantir
les postconditions après son éxécution. Pareil pour les invariants.

avantage -> rend les attentes et garanties du code explicites, ce qui facilite la comphréension, vérification
et maintenance du logiciel. On repère facilement les violations des contrats pendant le développement
ou l'éxécution, on peut donc les corriger avec aisance
"""

#Cours

"""
fait la distintion entre l'interface publique d'un code (utilisée par le développeur utilisateur) et
son implémentation (gérée par le(s) développeur(s) auteur(s)): l'utilisation d'une classe, méthode ou 
fonction n'a pas à savoir comment cette dernière est implémentée pourvu que son 'mode d'emploi' soit
correctement rédigé.

ce mode d'emploi ou spécification, se décline en deux informations: Les préconditions, et les 
postconditions. Les préconditions sont toutes les conditions à respecter dans le cadre d'une utilisation 
correcte de la méthode/fonction. Si ces préconditions sont remplies,alors il est garanti à l'utilisateur 
qu'après appel de cette méthode/fonction, les postconditions son réalisées.

Les préconditions concernent : 
    *  Les paramètres(événtuellement des objets) de la fonction ou de la méthode. On s'intéresse plus 
       particulièrement à leur type éventuel(en python: via les annotations ), et aux conditions 
       s'appliquant sur leurs valeurs, et notamment les valeurs limites acceptées (entier/positif/None/listeVide/etc) 
       
    *  En programmation orientée-objet : l'état de l'objet courant (self en python ) 
    
Les postconditions concernent : 
    *  La valeur de retour de la fonction/méthode 
    *  Les effets de bords (=effets autres que la valeur envoyée):
        ** En programation orientée-objet : l'état de l'objet courant
        ** Les modifications de ressources utilisées en paramètres
            *** fichiers, communication réseau,...
            *** En POO : l'état des objets passés en paramètres
    * La gestion des erreurs (les éventuelles exceptions lancées)
    
    
Convetion Pydoc -> PRE/POST/RAISE 
annotation python -> les trucs bizarres que louis mettait à côté des ses paramètres -> ex après 
"""

# exemple d'une fonction avec annotations :
def add_numbers(a: int, b: int) -> int:
    """Cette fonction additionne deux nombres entiers."""
    return a + b

# QUE LE TP COMMENCE !!!!! bon moi je vais dodo, il est déjà 4h du zbar

# TP
def factorielle(n: int)  -> int :
    """calcule la factorielle de n
    PRE : n est un entier positif
    POST : Renvoie n!
    """
    if n==0 or n==1 :
        return 1
    else :
        return n * factorielle(n-1)
factorielle(3)

# comment moi je le fais

def factorielle(n: int)  -> int :
    """calcule la factorielle de n
    PRE : n est un entier positif
    POST : Renvoie n!
    """
    resultat = n
    while n > 1 :
        n-=1
        resultat *= n
    return resultat

print(factorielle(4))

# 2 PROGRAMMATION DÉFENSIVE__________________________________________________________________________________________________________________________

"""
Technique qui anticipe les mauvaises utilisations d'une fonction ou d'une méthoode mise à disposition
En Progrmaion par contrat, si l'utilisateur ne respecte pas la précondition, rien est garantit 
ex avec la factorielle : on met un entier négatif 
"""
def factorielle(n: int)  -> int :
    """calcule la factorielle de n
    PRE : n est un entier positif
    POST : Renvoie n!
    """
    resultat = n
    while n > 1 :
        n-=1
        resultat *= n
    return resultat

print(factorielle(-4))  #-> ça fait nimp

""" on peut prévenir l'utilisateur qu'il fait pas bien en renvoyant une valeur spéciale """

def factorielle(n: int)  -> int :
    """calcule la factorielle de n
    PRE : n est un entier
    POST : Renvoie n! si n>= 0 , sinon retourne -1
    """
    if n >= 0 :
        resultat = n
        while n > 1 :
            n-=1
            resultat *= n
        return resultat
    else :
        return -1

print(factorielle(-4))  #-> affiche -1 ce qui dit a l'uti qu'il a commis une erreur 

# rem : on a changé la précondition -> tous les entiers sont acceptés mtn
# contre intuitif, mais il apparaît pcq on peut mtn traiter correctement tous les entier
# même si tous ne renvoie pas la factorielle
# c'est ça la programmation défensive : -> accepte spécification la plus large possible tout en
# traitant les cas d'erreurs
# Danger de cette technique -> les uti ne regardent pas tout le temps les valeurs de retours d'une fonction
# donc ils peuvent passer à côté de l'erreur
# ex:

x = 3
result = 45 + factorielle(x)
print(result)

# Quand x est positif tout est ok, MS qd x est négatif, le résultat est faux pcq la fonction aura
# envoyée la valeur de retour, l'uti est pas prévenu que problème il y a eu
# donc on va mtn eviter de faire des retours de valeurs négatives
# tout est question de ctxt, ici ça me paraît evident que le fait d'envoyer une valeur numérique
# négative dans une fonction ou on joue avec des chiffres est une mauvaise idée
# mais si dans une autre fonction, ce retour bloque la suite des opérations, bah on peut alors l'utiliser

# existe-il un autre système qui va empêcher ce genre de confusion ?
# OUIIIII

# 3 EXCEPTIONS_________________________________________________________________________________________________________________________________

# on en à déjà utilisés un peu dans la manipulation de fichiers
# exception-> signal lancé par le programme en cours d'éxécution lorsqu'un cas particulier se présente
# comme par exemple : un erreur
# Si rien est prévu dans le programme, il s'arrête. Mais on peut anticiper ces erreurs et faire du cas
# par cas : un traitement spécial pour chaque

# on reprend la factorielle et on lance une exception

class exceptionParamNegatif(Exception):
    pass
def factorielle(n: int) -> int:
    """calcule la factorielle de n
    PRE : n est un entier
    POST : Renvoie n! si n>= 0
    RAISES : exceptionParamNegatif si n<0
    """
    if n >= 0:
        resultat = n
        while n > 1:
            n -= 1
            resultat *= n
        return resultat
    else:
        raise exceptionParamNegatif("\nUn paramètre négatif n'est pas accepté -> TU CONNAIS PAS TES MATH \nNan mais une factorielle d'un nombre négatif on est ou là")

factorielle(-4)

# ça marche, c'est rouge de partt quand on mets un enetier négatif
# mais on devrait quand éviter de faire "planter" le programme
# on peut faire ça mieux et plus gentillement
# encore une fois du cas par caca : des fois on fait un popup, des fois un message dans les logs
# -> mieux d'arrêter ou de faire continuer le programme malgré l'erreur

# on va afficher un message d'erreur de manière plus douce plutôt que de foutre du rouge partt sur stderr

class exceptionParamNegatif(Exception):
    pass

def factorielle(n: int) -> int:
    """calcule la factorielle de n
    PRE : n est un entier
    POST : Renvoie n! si n>= 0
    RAISES :
    """
    if n >= 0:
        resultat = n
        while n > 1:
            n -= 1
            resultat *= n
        return resultat
    else:
        raise exceptionParamNegatif("\nUn paramètre négatif n'est pas accepté -> TU CONNAIS PAS TES MATH  \nNan mais une factorielle d'un nombre négatif on est ou là")

def test_factorielle(x) :
    try :
        print(factorielle(x))
    except exceptionParamNegatif as e:
        print(e)

test_factorielle(3)
test_factorielle(-1)
test_factorielle(5)

# MISE EN PRATIQUE
# Jvais avoir besoin d'un nveau fichier -> TP07_MiseEnPratique

