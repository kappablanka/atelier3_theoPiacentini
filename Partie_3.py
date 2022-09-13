def mot_correspond(mot: str, motif: str) -> bool:
    """

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


def testeur_de_fonction_sur_str_2_arg(funct, jeu_de_tests):
    """
    Fonction permettant de tester la fonction message_imc()
    :return: void
    """
    for e in jeu_de_tests:
        print(f"{funct.__name__}({e[0]}, {e[1]}) = {funct(e[0], e[1])}")
    print("\n")


JDT6 = [("tarte", "t..t."),
        ("cheval", "c..v..l"),
        ("cheval", "c..v.l")]

testeur_de_fonction_sur_str_2_arg(mot_correspond, JDT6)
