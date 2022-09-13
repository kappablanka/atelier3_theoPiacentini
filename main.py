import random


def full_name(str_arg: str) -> str:
    """
    Renvoie un nom prénom en ajoutant les majusculs
    :param str_arg: nom prenom
    :type str_arg: str
    :return: NOM Prenom
    :rtype: str
    """
    str_arg_splitter = str_arg.split(" ")
    print(str_arg_splitter)
    return f"{str_arg_splitter[0].upper()} {str_arg_splitter[1].capitalize()}"


def testeur_de_fonction_sur_str(funct, jeu_de_tests):
    """
    Fonction permettant de tester la fonction message_imc()
    :return: void
    """
    for e in jeu_de_tests:
        print(f"{funct.__name__}({e}) = {funct(e)}")
    print("\n")


def testeur_de_fonction_sur_str_2_arg(funct, jeu_de_tests):
    """
    Fonction permettant de tester la fonction message_imc()
    :return: void
    """
    for e in jeu_de_tests:
        print(f"{funct.__name__}({e[0]}, {e[1]}) = {funct(e[0], e[1])}")
    print("\n")


JDT_1 = ["Piacentini Théo"]
testeur_de_fonction_sur_str(full_name, JDT_1)

print(full_name("theo Piacentini"))


def is_mail(str_arg: str) -> (int, int):
    """
    Fonction testant la validité d'un mail
    :param str_arg: mail passé en paramètre
    :type str_arg: str
    :return: (validité, code erreur)
    :rtype: (int, int)
    """
    validite, erreur = 1, -1

    mail_split = str_arg.split("@")
    if len(mail_split) == 1:
        print(str_arg)
        return 0, 2
    elif mail_split[0] == "" or len(mail_split) == 1:
        print(str_arg)
        return 0, 2
    elif mail_split[1] == "":
        print(str_arg)
        return 0, 3

    corps = mail_split[0]
    domaine = mail_split[1]

    corps_deux_points_a_la_suite = False
    corps_seulement_alphanum_tiret_et_underscore = True
    for i in range(len(corps)):
        if i < len(corps) - 1:
            if corps[i] == "." and corps[i + 1] == ".":
                corps_deux_points_a_la_suite = True

        if not corps[i].isalnum() and not corps[i] == "_" and not corps[i] == "-" and not corps[i] == ".":
            corps_seulement_alphanum_tiret_et_underscore = False

    if corps[0] == "." or corps[-1] == "." or corps_deux_points_a_la_suite or not \
            corps_seulement_alphanum_tiret_et_underscore:
        validite, erreur = 0, 1

    domaine_deux_points_a_la_suite = False
    domaine_seulement_alphanum_et_tiret = True
    domaine_presence_point = False
    for i in range(len(domaine)):

        if i < len(domaine) - 1:
            if domaine[i] == "." and domaine[i + 1] == ".":
                domaine_deux_points_a_la_suite = True

        if domaine[i] == ".":
            domaine_presence_point = True

        if not domaine[i].isalnum() and not domaine[i] == "-" and not domaine[i] == ".":
            print(f"ce domaine pose prolème {domaine}")
            domaine_seulement_alphanum_et_tiret = False

    if not domaine_presence_point or domaine_deux_points_a_la_suite or not domaine_seulement_alphanum_et_tiret:
        validite, erreur = 0, 3

    return validite, erreur


# A refactorer


JDT_2 = ["Piacentini Théo",
         "bisambigllia_paul@univ-corse.fr",
         "bisambigllia_paulOuniv-corse.fr",
         "bisambigllia_paul@univ-corsePOINTfr",
         "@univ-corse.fr",
         "bisambigllia.paul@univ-corse.fr",
         "bisambigllia_paul@univ-corse.fr",
         "bisambigllia_paul@univ_corse.fr",
         "bisambigllia..paul@univ-corse.fr"]
testeur_de_fonction_sur_str(is_mail, JDT_2)


def mots_n_lettres(lst_mot: list[str], n: int) -> list[str]:
    """
    Fonction renvoyant une liste de tous les mots de n lettre(s) dans une liste passée en paramètre
    :param lst_mot: liste de str passé en paramètre
    :type lst_mot: list[str]
    :param n: nombre de lettres des mots à récupérer
    :type n: int
    :return: liste des mots de n lettres
    :rtype: list[str]
    """
    tab_resultat = []
    for e in lst_mot:
        if len(e) == n:
            tab_resultat.append(e)
    return tab_resultat


JDT_3 = [(["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"],
          4),
         (["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"],
          5), (
             ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir",
              "aimer"],
             6)]
testeur_de_fonction_sur_str_2_arg(mots_n_lettres, JDT_3)


def commence_par(mot: str, prefix: str) -> bool:
    """

    :param mot:
    :type mot:
    :param prefix:
    :type prefix:
    :return:
    :rtype:
    """
    flag_prefix_present = True
    for i in range(len(prefix)):
        if mot[i] != prefix[i]:
            flag_prefix_present = False
    return flag_prefix_present


JDT_4 = [("aaaaaaa", "aaa"),
         ("aaaaaaa", "baa")]
testeur_de_fonction_sur_str_2_arg(commence_par, JDT_4)


def finit_par(mot: str, suffix: str) -> bool:
    """

    :param mot:
    :type mot:
    :param suffix:
    :type suffix:
    :return:
    :rtype:
    """
    flag_suffix_present = True
    for i in range(len(suffix)):
        if mot[-i - 1] != suffix[i]:
            flag_suffix_present = False
    return flag_suffix_present


testeur_de_fonction_sur_str_2_arg(finit_par, JDT_4)


def finissent_par(lst_mot: list[str], suffix: str) -> list[str]:
    tab_resultat = []
    for e in lst_mot:
        if finit_par(e, suffix):
            tab_resultat.append(e)
    return tab_resultat


def commencent_par(lst_mot: list[str], prefix: str) -> list[str]:
    tab_resultat = []
    for e in lst_mot:
        if commence_par(e, prefix):
            tab_resultat.append(e)
    return tab_resultat


def liste_mots(lst_mot: list[str], prefix: str, suffix: str, n: int) -> list[str]:
    """
    :param lst_mot:
    :type lst_mot:
    :param prefix:
    :type prefix:
    :param suffix:
    :type suffix:
    :param n:
    :type n:
    :return:
    :rtype:
    """
    tab_resultat = []
    for e in lst_mot:
        if commence_par(e, prefix) and finit_par(e, suffix) and len(e) == n:
            tab_resultat.append(e)
    return tab_resultat


def dictionnaire(fichier: str) -> list[str]:
    """
    Fonction retournant la liste des mots d'un dictionnaire en txt
    :param fichier: de l'amplacement d'un fichier txt représentant un dictionnaire
    :type fichier: str
    :return: liste des mots du dictionnaire
    :rtype: list[str]
    """
    f = open(fichier, "r")
    lis_mots = []
    c = f.readline()
    while c != "":
        for e in c.split(" "):
            lis_mots.append(e)
        c = f.readline()

    return lis_mots


dico = dictionnaire("littre.txt")


# Partie 2


def places_lettre(ch: str, mot: str) -> list:
    """
    Recherche si le caractère est présent.
    :param ch: car d'une lettre
    :type ch: str
    :param mot: str d'un mot
    :type mot: str
    :return:
    :rtype: list
    """
    liste_emplacements = []
    for i in range(len(mot)):
        if ch == mot[i]:
            liste_emplacements.append(i)
    return liste_emplacements


JDT_5 = [('b', 'bonjour'),
         ('a', 'bonjour'),
         ('m', 'maman')]

testeur_de_fonction_sur_str_2_arg(places_lettre, JDT_5)


def output_str(mot: str, lpos: list) -> str:
    """
    Renvoie un mot un cachant les car present dans les indices d'une list d'int
    :param mot: mot
    :type mot: str
    :param lpos: liste des entiers représentants les indices des caractères de la chaine de mot à afficher
    :type lpos: list
    :return:
    :rtype: str
    """
    mot_cache = ""
    for i in range(len(mot)):
        if i in lpos:
            mot_cache += mot[i]
        else:
            mot_cache += "_"

    return mot_cache


JDT_6 = [('bonjour', []),
         ('bonjour', [0]),
         ('bonjour', [0, 1, 4]),
         ('maman', [1, 3]),
         ('bon', [0, 1, 2])]

testeur_de_fonction_sur_str_2_arg(output_str, JDT_6)

C5 = "|---] "
C4 = "| O "
C3 = "| T "
C2 = "|/ \ "
C1 = "|______"
pendu = [C1, C2, C3, C4, C5]


def run_game():
    """
    Programme principal devant:
    Déclarer une liste de mots
    Tirer aléatoirement un mot de la liste
    Afficher la chaine de tirets représentant le nb de car du mot sous la forme :
    paris = _____
    jusqu'à ce que le mmot soit trouvé ou le pendu dessiné (5 erreurs)
    Demander à l'utilisateur une lettre
    Rechercher la place de la lettre dans le mot
    afficher l'etat actuel du mot
    afficher le dessin du pendu correspondant complété en cas d'erreur
    afficher le nombre de coups restant
    :return:
    :rtype:
    """
    l_mots = ['paris', 'londres', 'madrid', 'berlin', 'new york']

    mot_tire = random.choice(l_mots)
    print(f"mot tiré  = {mot_tire}")
    nb_erreurs = 0
    flag_mot_trouve = False
    empl_lettres_trouve = []
    while nb_erreurs < 5 and not flag_mot_trouve:
        print(output_str(mot_tire, empl_lettres_trouve))
        lettre_choisie = input("donnez une lettre : ")
        l_emplacement_lettres = places_lettre(lettre_choisie, mot_tire)
        if len(l_emplacement_lettres) != 0:
            for e in l_emplacement_lettres:
                empl_lettres_trouve.append(e)
        else:
            nb_erreurs += 1

        if nb_erreurs > 0:
            for i in range(nb_erreurs, 0, -1):
                print(pendu[i])
            print(f"nombre de coups restant : {5 - nb_erreurs}")

        if len(empl_lettres_trouve) == len(mot_tire):
            print("bravo")
            flag_mot_trouve = True


def build_list(file_name: str) -> list:
    """
    Prend en paramètre un nom de fichier et construit automatiquement la liste des mots
    :param file_name:
    :type file_name:
    :return:
    :rtype:
    """
    f = open(file_name, "r")
    lis_mots = []
    c = f.readline()
    while c != "":
        c = f.readline()
        lis_mots.append(c[:-1].lower())
    return lis_mots


liste_capitales = build_list("capitales.txt")
print(liste_capitales)