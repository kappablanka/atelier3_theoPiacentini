

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
        if i < len(corps)-1:
            if corps[i] == "." and corps[i+1] == ".":
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


