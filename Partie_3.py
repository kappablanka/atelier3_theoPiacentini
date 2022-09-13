import Partie_1_et_2


def mot_correspond(mot: str, motif: str) -> bool:
    """
    Fonction testant la correspondance entre une chaine de caractère et un motif donné les "." du motif etant des
    jockers
    :param mot:
    :type mot: str
    :param motif:
    :type motif: str
    :return:
    :rtype: bool
    """
    flag_motif_correspond = True
    if len(motif) != len(mot):
        flag_motif_correspond = False
    else:
        for i in range(len(motif)):
            if mot[i] != motif[i] and motif[i] != ".":
                flag_motif_correspond = False
    return flag_motif_correspond


JDT6 = [("tarte", "t..t."),
        ("cheval", "c..v..l"),
        ("cheval", "c..v.l")]

Partie_1_et_2.testeur_de_fonction(mot_correspond, JDT6, arg_nb=2)


def presente(lettre: str, mot: str) -> int:
    """
    Fonction renvoyan un entier représentant l'indice de la lettre passée en paramètre dans le str mot. La foncction
    renvoie -1 si la lettre n'est pas trouveé
    :param lettre:
    :type lettre: str
    :param mot:
    :type mot: str
    :return:
    :rtype: int
    """
    emplacement_lettre = -1
    for i in range(len(mot)):
        if mot[i] == lettre:
            emplacement_lettre = i

    return emplacement_lettre


JDT7 = [("t", "tarte"),
        ("h", "cheval"),
        ("l", "cheval"),
        ("z", "cheval")]

Partie_1_et_2.testeur_de_fonction(presente, JDT7, arg_nb=2)


def mot_possible(mot: str, lettres: str) -> bool:
    """
    Renvoie True ou False suivant que le mot peut s'obtenire avec les lettres passées en param
    :param mot:
    :type mot: str
    :param lettres:
    :type lettres: str
    :return:
    :rtype: str
    """
    lettres_splite = [*lettres]
    flag_mot_possible = True
    for e in mot:
        if e not in lettres_splite:
            flag_mot_possible = False
        if e in lettres_splite:
            lettres_splite.remove(e)

    return flag_mot_possible


JDT7 = [("chapeau", "abcehpuv"),
        ("chapeau", "abcehpuva")]

Partie_1_et_2.testeur_de_fonction(mot_possible, JDT7, arg_nb=2)


def mot_optimaux(dico: list[str], lettres: str) -> list[str]:
    """
    Renvoie une liste des mots de longueur maximale présents dans la liste dico que l'on peut fire avec les lettres
    passées en paramètre
    :param dico:
    :type dico: list[str]
    :param lettres:
    :type lettres: str
    :return:
    :rtype: list[str]
    """
    l_mots = []
    i = len(lettres)
    while len(l_mots) == 0 and i > 0:
        dico_i_lettres = Partie_1_et_2.mots_n_lettres(dico, i)
        for e in dico_i_lettres:
            if mot_possible(e, lettres):
                l_mots.append(e)
        i -= 1

    return l_mots


listes_capitales = Partie_1_et_2.build_list("capitales.txt")
print(listes_capitales)

print(mot_optimaux(listes_capitales, "paris"))


def ouvrante(car: str) -> bool:
    """
    Renvoie un booléen indiquant si le paramettre est une parenthèse "("
    :param car:
    :type car: str
    :return:
    :rtype: bool
    """
    return car == "(" or car == "[" or car == "{"


def fermante(car: str) -> bool:
    """
    Renvoie un booléen indiquant si le paramettre est une parenthèse ")"
    :param car:
    :type car: str
    :return:
    :rtype: bool
    """
    return car == ")" or car == "]" or car == "}"


def reverse(car: str) -> str:
    """
    Renvoie un caractère fermant selon que le parametre soit une parenthèse ouvrante, un crochet, etc...
    :param car:
    :type car: str
    :return:
    :rtype: str
    """
    DICO_OUVRANTE_FERMANTE = {"(": ")", "[": "]", "{": "}"}
    if ouvrante(car):
        return DICO_OUVRANTE_FERMANTE[car]
    elif fermante(car):
        for k, v in DICO_OUVRANTE_FERMANTE.items():
            if v == car:
                return k
    else:
        return car


JDT8 = ["(", "]", "a"]

Partie_1_et_2.testeur_de_fonction(reverse, JDT8)


def operateur(car: str) -> bool:
    """
    Renvoie True si "car" est * ou + et False sinon
    :param car:
    :type car: str
    :return:
    :rtype: bool
    """
    return car == "*" or car == "+" or car == "-" or car == "\\"


def nombre(car: str) -> bool:
    """
    Renvoie un booléen indiquant si la chaine est un nombre
    :param car:
    :type car: str
    :return:
    :rtype: bool
    """
    flag_nombre = True
    CHIFFRES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for e in car:
        if e not in CHIFFRES:
            flag_nombre = False

    return flag_nombre


def caracter_valide(car: str) -> bool:
    """
    Renvoie True si le caractère est valide dans une expression arithmétique
    :param car:
    :type car: str
    :return:
    :rtype: bool
    """
    return ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or car == " "


def verif_parenthese(expression: str) -> bool:
    """
    Verifie si l'expression passée en paramètre contient des caractères valides et est correctement parenthésé ou non
    :param expression:
    :type expression: str
    :return:
    :rtype:
    """
    liste_p = []
    flag_validite = True
    for e in expression:
        if not caracter_valide(e):
            print("aaaa")
            flag_validite = False
        elif ouvrante(e):
            liste_p.append(e)
        elif fermante(e) and liste_p[-1] == reverse(e):
            liste_p.pop()
    if len(liste_p) > 0:
        flag_validite = False
    return flag_validite


JDT10 = ["(3+2)*6-1",
         "((3+2)*6-1",
         "(5+7]*12"]

Partie_1_et_2.testeur_de_fonction(verif_parenthese, JDT10)
