import Partie_1_et_2


def mot_correspond(mot: str, motif: str) -> bool:
    """
    Fonction testant la correspondance entre une chaine de caractère et un motif donné les "." du motif etant des
    jockers
    :param mot:
    :type mot:
    :param motif:
    :type motif:
    :return:
    :rtype:
    """
    flag_motif_correspond = True
    if len(motif) != len(mot):
        flag_motif_correspond = False
    else:
        for i in range(len(motif)):
            if mot[i] != motif[i] and motif[i] != ".":
                flag_motif_correspond = False
    return flag_motif_correspond


def testeur_de_fonction_2_arg(funct, jeu_de_tests):
    """
    Fonction permettant de tester les fonctions à deux arguments
    :return: void
    """
    for e in jeu_de_tests:
        print(f"{funct.__name__}({e[0]}, {e[1]}) = {funct(e[0], e[1])}")
    print("\n")


JDT6 = [("tarte", "t..t."),
        ("cheval", "c..v..l"),
        ("cheval", "c..v.l")]

testeur_de_fonction_2_arg(mot_correspond, JDT6)


def presente(lettre: str, mot: str) -> int:
    """
    Fonction renvoyan un entier représentant l'indice de la lettre passée en paramètre dans le str mot. La foncction
    renvoie -1 si la lettre n'est pas trouveé
    :param lettre:
    :type lettre:
    :param mot:
    :type mot:
    :return:
    :rtype:
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

testeur_de_fonction_2_arg(presente, JDT7)


def mot_possible(mot: str, lettres: str) -> bool:
    """
    Renvoie True ou False suivant que le mot peut s'obtenire avec les lettres passées en param
    :param mot:
    :type mot:
    :param lettres:
    :type lettres:
    :return:
    :rtype:
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

testeur_de_fonction_2_arg(mot_possible, JDT7)


def mot_optimaux(dico: list[str], lettres: str) -> list[str]:
    """
    Renvoie une liste des mots de longueur maximale présents dans la liste dico que l'on peut fire avec les lettres
    passées en paramètre
    :param dico:
    :type dico:
    :param lettres:
    :type lettres:
    :return:
    :rtype:
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
